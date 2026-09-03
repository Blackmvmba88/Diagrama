import numpy as np

from diagrama import (
    LossVector,
    cartesian_to_polar,
    derivative,
    graph_laplacian,
    helical_embedding,
    polar_to_cartesian,
    second_derivative,
    spectral_embedding,
    weighted_semantic_fidelity,
)


def test_polar_round_trip():
    x = np.array([1.0, 0.0, -1.0])
    y = np.array([0.0, 1.0, 0.0])
    r, theta = cartesian_to_polar(x, y)
    x2, y2 = polar_to_cartesian(r, theta)
    assert np.allclose(x, x2)
    assert np.allclose(y, y2)


def test_derivatives_of_quadratic():
    t = np.linspace(0.0, 10.0, 101)
    x = t**2
    v = derivative(x, t)
    a = second_derivative(x, t)
    assert np.allclose(v[2:-2], 2 * t[2:-2], atol=1e-2)
    assert np.allclose(a[2:-2], 2.0, atol=1e-2)


def test_helix_has_three_dimensions():
    t = np.linspace(0.0, 2 * np.pi, 100)
    xyz = helical_embedding(t, angular_frequency=1.0, pitch=0.25)
    assert xyz.shape == (100, 3)
    assert np.allclose(xyz[:, 2], 0.25 * t)


def test_graph_laplacian_rows_sum_to_zero():
    adjacency = np.array(
        [
            [0.0, 1.0, 0.0],
            [1.0, 0.0, 1.0],
            [0.0, 1.0, 0.0],
        ]
    )
    lap = graph_laplacian(adjacency)
    assert np.allclose(lap.sum(axis=1), 0.0)


def test_spectral_embedding_shape():
    adjacency = np.array(
        [
            [0.0, 1.0, 0.0, 0.0],
            [1.0, 0.0, 1.0, 0.0],
            [0.0, 1.0, 0.0, 1.0],
            [0.0, 0.0, 1.0, 0.0],
        ]
    )
    embedding = spectral_embedding(adjacency, dimensions=2)
    assert embedding.shape == (4, 2)


def test_semantic_fidelity():
    fidelity = weighted_semantic_fidelity([1.0, 0.5], [3.0, 1.0])
    assert np.isclose(fidelity, 0.875)


def test_loss_vector_fidelity():
    loss = LossVector(identity=0.0, topology=0.2)
    assert 0.0 <= loss.fidelity() <= 1.0
