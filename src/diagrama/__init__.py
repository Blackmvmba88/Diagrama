"""Diagrama — BlackMamba Lab universal representation engine."""

from .math_kernel import (
    LossVector,
    cartesian_to_polar,
    derivative,
    graph_from_adjacency,
    graph_laplacian,
    helical_embedding,
    normalize,
    polar_to_cartesian,
    second_derivative,
    spectral_embedding,
    spring_layout_energy,
    weighted_semantic_fidelity,
)

__all__ = [
    "LossVector",
    "cartesian_to_polar",
    "derivative",
    "graph_from_adjacency",
    "graph_laplacian",
    "helical_embedding",
    "normalize",
    "polar_to_cartesian",
    "second_derivative",
    "spectral_embedding",
    "spring_layout_energy",
    "weighted_semantic_fidelity",
]

__version__ = "0.1.0"
