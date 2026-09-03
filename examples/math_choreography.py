"""Example: one temporal signal, three observational bases.

Run:
    python examples/math_choreography.py

The example demonstrates a central Diagrama idea:
The semantic source stays fixed while the observational basis changes.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from diagrama import derivative, helical_embedding


def build_signal(samples: int = 600) -> tuple[np.ndarray, np.ndarray]:
    t = np.linspace(0.0, 8.0 * np.pi, samples)
    signal = (1.0 + 0.025 * t) * np.sin(t) + 0.22 * np.sin(3.0 * t)
    return t, signal


def timeline(t: np.ndarray, signal: np.ndarray) -> None:
    fig, ax = plt.subplots()
    ax.plot(t, signal)
    ax.set_title("Timeline — progression")
    ax.set_xlabel("time")
    ax.set_ylabel("signal")
    fig.tight_layout()


def phase_view(t: np.ndarray, signal: np.ndarray) -> None:
    velocity = derivative(signal, t)
    fig, ax = plt.subplots()
    ax.plot(signal, velocity)
    ax.set_title("Phase portrait — state dynamics")
    ax.set_xlabel("signal")
    ax.set_ylabel("d(signal)/dt")
    fig.tight_layout()


def helix_view(t: np.ndarray, signal: np.ndarray) -> None:
    radius = 1.0 + 0.35 * np.abs(signal)
    xyz = helical_embedding(t, radius=radius, angular_frequency=1.0, pitch=0.08)

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot(xyz[:, 0], xyz[:, 1], xyz[:, 2])
    ax.set_title("Helical basis — recurrence + progression")
    ax.set_xlabel("phase X")
    ax.set_ylabel("phase Y")
    ax.set_zlabel("progression")
    fig.tight_layout()


def main() -> None:
    t, signal = build_signal()
    timeline(t, signal)
    phase_view(t, signal)
    helix_view(t, signal)
    plt.show()


if __name__ == "__main__":
    main()
