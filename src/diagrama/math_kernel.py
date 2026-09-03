"""Core mathematical operators for Diagrama.

This module intentionally contains renderer-independent operations.  It turns
semantic quantities into mathematical structures that later representation
layers can encode visually, spatially, temporally, or sonically.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import networkx as nx
import numpy as np

ArrayLike = Iterable[float] | np.ndarray


@dataclass(frozen=True)
class LossVector:
    """Structured semantic loss for a representation transform."""

    identity: float = 0.0
    topology: float = 0.0
    metric: float = 0.0
    order: float = 0.0
    magnitude: float = 0.0
    direction: float = 0.0
    uncertainty: float = 0.0
    temporal_resolution: float = 0.0
    hierarchy: float = 0.0
    context: float = 0.0

    def as_array(self) -> np.ndarray:
        return np.asarray(
            [
                self.identity,
                self.topology,
                self.metric,
                self.order,
                self.magnitude,
                self.direction,
                self.uncertainty,
                self.temporal_resolution,
                self.hierarchy,
                self.context,
            ],
            dtype=float,
        )

    def weighted_loss(self, weights: ArrayLike | None = None) -> float:
        values = self.as_array()
        if weights is None:
            weights_arr = np.ones_like(values)
        else:
            weights_arr = np.asarray(weights, dtype=float)
            if weights_arr.shape != values.shape:
                raise ValueError("weights must contain 10 values")
        denom = weights_arr.sum()
        if denom <= 0:
            raise ValueError("weights must have a positive sum")
        return float(np.dot(values, weights_arr) / denom)

    def fidelity(self, weights: ArrayLike | None = None) -> float:
        return float(np.clip(1.0 - self.weighted_loss(weights), 0.0, 1.0))


def normalize(values: ArrayLike, *, eps: float = 1e-12) -> np.ndarray:
    """Min-max normalize a numeric vector to [0, 1]."""

    x = np.asarray(values, dtype=float)
    if x.size == 0:
        return x.copy()
    lo = np.nanmin(x)
    hi = np.nanmax(x)
    span = hi - lo
    if not np.isfinite(span) or abs(span) <= eps:
        return np.zeros_like(x)
    return (x - lo) / span


def derivative(values: ArrayLike, time: ArrayLike | None = None) -> np.ndarray:
    """Estimate the first derivative using NumPy's gradient operator."""

    x = np.asarray(values, dtype=float)
    if x.ndim != 1:
        raise ValueError("values must be one-dimensional")
    if x.size < 2:
        return np.zeros_like(x)
    if time is None:
        return np.gradient(x)
    t = np.asarray(time, dtype=float)
    if t.shape != x.shape:
        raise ValueError("time and values must have the same shape")
    return np.gradient(x, t)


def second_derivative(values: ArrayLike, time: ArrayLike | None = None) -> np.ndarray:
    """Estimate acceleration: d²x/dt²."""

    first = derivative(values, time)
    return derivative(first, time)


def cartesian_to_polar(x: ArrayLike, y: ArrayLike) -> tuple[np.ndarray, np.ndarray]:
    """Transform Cartesian coordinates into radius and angle."""

    x_arr = np.asarray(x, dtype=float)
    y_arr = np.asarray(y, dtype=float)
    if x_arr.shape != y_arr.shape:
        raise ValueError("x and y must have the same shape")
    radius = np.hypot(x_arr, y_arr)
    theta = np.arctan2(y_arr, x_arr)
    return radius, theta


def polar_to_cartesian(radius: ArrayLike, theta: ArrayLike) -> tuple[np.ndarray, np.ndarray]:
    """Transform polar coordinates into Cartesian coordinates."""

    r = np.asarray(radius, dtype=float)
    t = np.asarray(theta, dtype=float)
    if r.shape != t.shape:
        raise ValueError("radius and theta must have the same shape")
    return r * np.cos(t), r * np.sin(t)


def helical_embedding(
    time: ArrayLike,
    *,
    radius: ArrayLike | float = 1.0,
    angular_frequency: float = 1.0,
    pitch: float = 1.0,
) -> np.ndarray:
    """Embed a temporal sequence into a 3D helix.

    This representation preserves cyclic phase in x/y while preserving
    progression in z.
    """

    t = np.asarray(time, dtype=float)
    r = np.asarray(radius, dtype=float)
    if r.ndim == 0:
        r = np.full_like(t, float(r))
    if r.shape != t.shape:
        raise ValueError("radius must be scalar or have the same shape as time")

    theta = angular_frequency * t
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = pitch * t
    return np.column_stack((x, y, z))


def graph_laplacian(
    adjacency: np.ndarray,
    *,
    normalized: bool = False,
) -> np.ndarray:
    """Compute the combinatorial or symmetric normalized graph Laplacian."""

    a = np.asarray(adjacency, dtype=float)
    if a.ndim != 2 or a.shape[0] != a.shape[1]:
        raise ValueError("adjacency must be a square matrix")

    degrees = a.sum(axis=1)
    if not normalized:
        return np.diag(degrees) - a

    inv_sqrt = np.zeros_like(degrees)
    nonzero = degrees > 0
    inv_sqrt[nonzero] = 1.0 / np.sqrt(degrees[nonzero])
    d_inv_sqrt = np.diag(inv_sqrt)
    return np.eye(a.shape[0]) - d_inv_sqrt @ a @ d_inv_sqrt


def spectral_embedding(adjacency: np.ndarray, dimensions: int = 2) -> np.ndarray:
    """Embed graph nodes using low-frequency eigenvectors of the normalized Laplacian."""

    if dimensions < 1:
        raise ValueError("dimensions must be >= 1")
    lap = graph_laplacian(adjacency, normalized=True)
    eigenvalues, eigenvectors = np.linalg.eigh(lap)
    order = np.argsort(eigenvalues)
    # Skip the first near-constant eigenvector when possible.
    start = 1 if lap.shape[0] > 1 else 0
    stop = min(start + dimensions, lap.shape[0])
    embedding = eigenvectors[:, order[start:stop]]
    if embedding.shape[1] < dimensions:
        embedding = np.pad(embedding, ((0, 0), (0, dimensions - embedding.shape[1])))
    return embedding


def spring_layout_energy(
    positions: np.ndarray,
    adjacency: np.ndarray,
    *,
    spring_constant: float = 1.0,
    rest_length: float = 1.0,
    repulsion_constant: float = 1.0,
    repulsion_power: float = 2.0,
    eps: float = 1e-9,
) -> float:
    """Evaluate a simple spring + pairwise repulsion layout energy."""

    p = np.asarray(positions, dtype=float)
    a = np.asarray(adjacency, dtype=float)
    if p.ndim != 2:
        raise ValueError("positions must have shape (n_nodes, n_dimensions)")
    if a.shape != (p.shape[0], p.shape[0]):
        raise ValueError("adjacency shape must match number of positions")

    energy = 0.0
    n = p.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            distance = float(np.linalg.norm(p[i] - p[j])) + eps
            weight = max(a[i, j], a[j, i])
            if weight > 0:
                stretch = distance - rest_length
                energy += 0.5 * spring_constant * weight * stretch * stretch
            energy += repulsion_constant / (distance**repulsion_power)
    return float(energy)


def graph_from_adjacency(adjacency: np.ndarray) -> nx.Graph:
    """Create a NetworkX graph while preserving numeric edge weights."""

    a = np.asarray(adjacency, dtype=float)
    if a.ndim != 2 or a.shape[0] != a.shape[1]:
        raise ValueError("adjacency must be a square matrix")
    return nx.from_numpy_array(a)


def weighted_semantic_fidelity(
    preservation: ArrayLike,
    weights: ArrayLike | None = None,
) -> float:
    """Compute weighted semantic fidelity from invariant preservation scores.

    preservation values are expected in [0, 1], where 1 means fully preserved.
    """

    p = np.asarray(preservation, dtype=float)
    if p.ndim != 1 or p.size == 0:
        raise ValueError("preservation must be a non-empty one-dimensional vector")
    if np.any((p < 0) | (p > 1)):
        raise ValueError("preservation scores must lie in [0, 1]")

    if weights is None:
        w = np.ones_like(p)
    else:
        w = np.asarray(weights, dtype=float)
        if w.shape != p.shape:
            raise ValueError("weights and preservation must have the same shape")
        if np.any(w < 0):
            raise ValueError("weights must be non-negative")

    denom = w.sum()
    if denom <= 0:
        raise ValueError("weights must have a positive sum")
    return float(np.dot(p, w) / denom)
