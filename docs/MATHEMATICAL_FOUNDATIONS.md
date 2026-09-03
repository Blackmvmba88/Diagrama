# Mathematical Foundations

## Diagrama — Mathematics as Choreography of Meaning

A Diagrama representation is not a decorative drawing.

It is the visible result of a mathematical choreography.

```text
semantic structure
      ↓
mathematical operators
      ↓
geometric transformation
      ↓
perceptual encoding
      ↓
visible / audible / interactive form
```

The renderer paints the final state.

The mathematics determines how the state is organized.

---

# 1. Core principle

For a semantic object `S`, a representation is modeled as a composition of transforms:

```text
R = ρ ∘ E ∘ G ∘ T (S)
```

where:

```text
S = Semantic IR
T = semantic / mathematical transform
G = geometric embedding
E = perceptual encoding
ρ = renderer
R = final representation
```

The renderer `ρ` may be matplotlib, SVG, Canvas, Three.js, WebGL, Blender, audio, AR or another backend.

It is intentionally the last term.

---

# 2. Coordinate systems as observational bases

A representation often begins by choosing a basis.

## Cartesian

```math
p = (x, y)
```

or

```math
p = (x, y, z)
```

Useful for alignment, metric comparison and correlation.

## Polar

```math
x = r cos(θ)
y = r sin(θ)
```

Useful for cycles, phase and radial relationships.

## Cylindrical

```math
x = r cos(θ)
y = r sin(θ)
z = z
```

Useful when recurrence and progression coexist.

## Helical time

A periodic process that also evolves can be embedded as:

```math
x(t) = r(t) cos(ωt)
y(t) = r(t) sin(ωt)
z(t) = kt
```

This preserves cyclic phase while making long-term progression visible.

A timeline may hide recurrence.
A circle may hide progression.
A helix can expose both.

---

# 3. Differential structure

For time-varying quantity `x(t)`:

```math
v(t) = dx/dt
```

represents rate of change.

```math
a(t) = d²x/dt²
```

represents change of rate.

```math
j(t) = d³x/dt³
```

represents jerk: change of acceleration.

These derivatives can become perceptual variables:

```text
x(t)  → position
v(t)  → orientation / motion
|v|   → speed / brightness
a(t)  → pulse / curvature
j(t)  → event emphasis
```

This makes the representation dynamic rather than merely descriptive.

---

# 4. Vector fields

A vector field is:

```math
F : Rⁿ → Rⁿ
```

For 2D:

```math
F(x,y) = (u(x,y), v(x,y))
```

It can represent:

```text
direction of change
flow
force
migration
optimization gradient
information movement
state tendency
```

Important operators:

## Divergence

```math
∇ · F
```

Detects local sources and sinks.

Conceptually:

```text
positive divergence → spreading / source
egative divergence → convergence / sink
```

## Curl

```math
∇ × F
```

Detects rotational structure.

Useful for spotting circulation, vortices or cyclic influence.

## Gradient

For scalar field `φ`:

```math
∇φ
```

points toward greatest local increase.

This supports semantic landscapes where a scalar property becomes terrain.

---

# 5. Scalar fields and topography

A scalar field:

```math
φ : Rⁿ → R
```

maps position to magnitude.

Possible encodings:

```text
φ → height
φ → color
φ → opacity
φ → density
φ → sound frequency
```

Contours satisfy:

```math
φ(x,y) = c
```

and reveal equal-value regions.

This is the mathematical foundation for semantic topography, heat fields and potential landscapes.

---

# 6. Dynamical systems

A state-space system can be expressed as:

```math
ẋ = f(x, u, t)
```

or discretely:

```math
xₜ₊₁ = f(xₜ, uₜ)
```

The representation can expose:

```text
attractors
repellers
limit cycles
fixed points
bifurcations
state transitions
stability regions
```

A phase portrait represents trajectories in state space rather than plotting each variable independently against time.

This is often a better observational basis for systems whose behavior emerges from interaction among variables.

---

# 7. Graph mathematics

A graph:

```math
G = (V, E)
```

with adjacency matrix `A`.

Degree matrix:

```math
Dᵢᵢ = Σⱼ Aᵢⱼ
```

Graph Laplacian:

```math
L = D - A
```

The Laplacian is fundamental for:

```text
connectivity
diffusion
community structure
spectral embeddings
smoothness over networks
propagation
```

The normalized form may be written:

```math
L_norm = I - D⁻¹ᐟ² A D⁻¹ᐟ²
```

Its eigenvectors provide alternative coordinate systems for graph structure.

A network can therefore be represented not only by force-directed positions, but by a mathematically derived spectral basis.

---

# 8. Physics-inspired graph layouts

A force-directed layout can treat nodes as particles.

One simplified energy model:

```math
E = Σ_(i,j)∈E ½ kᵢⱼ (||xᵢ-xⱼ|| - ℓᵢⱼ)²
  + Σ_i<j c / ||xᵢ-xⱼ||ᵖ
```

The first term behaves like springs.

The second behaves like repulsion.

The layout seeks approximately:

```math
x* = argmin E(x)
```

This does **not** imply the semantic system is physically governed by those forces.

Physics is being used as a computational metaphor to obtain a useful spatial organization.

That distinction is mandatory.

---

# 9. Diffusion and propagation

Diffusion on a graph can be modeled through:

```math
dx/dt = -Lx
```

with solution:

```math
x(t) = e^(-tL) x(0)
```

This can expose how a signal, influence or activation spreads across relational structure.

Related representations include:

```text
animated propagation
heat diffusion
infection-like spread
information flow
activation fronts
```

Again, the mathematics describes structural propagation; domain interpretation belongs to adapters.

---

# 10. Harmonic and spectral analysis

A temporal signal may be decomposed using Fourier analysis:

```math
X(f) = ∫ x(t)e^(-i2πft) dt
```

This changes the observational basis from:

```text
time → amplitude
```

to:

```text
frequency → energy / amplitude
```

Useful structures:

```text
periodicity
harmonics
resonance
rhythm
repeated events
cyclic anomalies
```

For nonstationary signals, time-frequency methods such as STFT or wavelets preserve locality.

The goal is not to make everything spectral.

The goal is to know when the frequency basis reveals structure the time basis hides.

---

# 11. Wavelets and multiscale observation

Wavelets analyze localized structure across scale.

Conceptually:

```math
W(a,b) = ∫ x(t) ψ*((t-b)/a) dt / √|a|
```

where:

```text
a = scale
b = position / time
ψ = analyzing wavelet
```

This is useful for:

```text
bursts
transients
local periodicity
multi-scale anomalies
structures that appear only at certain resolutions
```

Diagrama should eventually treat **scale** as a first-class dimension of observation.

---

# 12. Dimensionality reduction

High-dimensional information often requires projection.

## PCA

Given centered data matrix `X`, covariance:

```math
C = XᵀX / (n-1)
```

Principal directions are eigenvectors of `C`.

Projection:

```math
Z = XWₖ
```

where `Wₖ` contains selected eigenvectors.

PCA preserves variance optimally under a linear least-squares criterion, but does not preserve every semantic relationship.

Therefore any dimensionality reduction must feed `Loss Validation`.

Other possible projection backends:

```text
MDS
Isomap
UMAP
t-SNE
spectral embedding
autoencoder latent spaces
```

Each preserves different structures and sacrifices others.

---

# 13. Distances and similarity

Representation depends strongly on the metric.

Examples:

Euclidean:

```math
d(x,y) = ||x-y||₂
```

Manhattan:

```math
d(x,y) = Σ |xᵢ-yᵢ|
```

Cosine distance:

```math
d_cos = 1 - (x·y)/(||x||||y||)
```

Mahalanobis:

```math
d_M(x,y) = √((x-y)ᵀΣ⁻¹(x-y))
```

Choosing a metric is itself a semantic decision.

Two objects can be “close” under one definition and distant under another.

Diagrama must therefore make metric selection explicit.

---

# 14. Information theory

Visual compression can be reasoned about using information-theoretic ideas.

Entropy:

```math
H(X) = -Σ p(x) log p(x)
```

Mutual information:

```math
I(X;Y) = Σ p(x,y) log[p(x,y)/(p(x)p(y))]
```

Potential uses:

```text
measure redundancy
identify informative dimensions
select channels
estimate compression impact
rank explanatory variables
```

A future loss validator may use information preservation alongside semantic invariants.

---

# 15. Topology

Geometry asks about distance and shape.

Topology asks which structures survive continuous deformation.

Important concepts:

```text
connected components
cycles
holes
boundaries
neighborhoods
containment
```

Persistent homology can track topological features across scales.

This gives Diagrama a way to distinguish:

```text
noise that disappears quickly
```

from:

```text
structure that persists across scale
```

This can become extremely valuable for latent-pattern discovery.

---

# 16. Optimization

Choosing a representation is itself an optimization problem.

Let candidate representation `R` have:

```text
U(R) = task utility
F(R) = semantic fidelity
P(R) = pattern visibility
Q(R) = perceptual clarity
C(R) = cognitive cost
L(R) = semantic loss
K(R) = computational cost
```

Then a conceptual objective is:

```math
R* = argmax_R [
  αU(R)
+ βF(R)
+ γP(R)
+ δQ(R)
- λC(R)
- μL(R)
- νK(R)
]
```

subject to protected invariants:

```math
p_i(R) ≥ τ_i
```

for every protected semantic invariant `i`.

This makes representation selection mathematically inspectable rather than arbitrary.

---

# 17. Perceptual channel capacity

Not all channels have equal precision.

For many quantitative tasks, aligned position and length are easier to compare precisely than area, volume, color saturation or perspective depth.

Therefore Diagrama should model each perceptual channel with properties such as:

```text
precision
ordinal_capacity
category_capacity
attention_cost
occlusion_risk
accessibility_risk
temporal_bandwidth
```

Channel selection can then become a constrained assignment problem.

Example:

```text
high-priority exact magnitude → aligned position
secondary magnitude           → size
state category                → shape
uncertainty                   → opacity
urgent transition             → pulse
```

---

# 18. Physical operators as representation primitives

Physics provides useful mathematical operators for organizing information.

Potential operators:

```text
spring attraction
repulsive potential
gravitational-style attraction
diffusion
wave propagation
damping
oscillation
phase locking
potential fields
flow conservation
pressure-like gradients
energy minimization
```

These should be implemented as **representation operators**, not as claims that arbitrary data literally follows physical law.

Example:

A semantic cluster may be spatialized by attractive forces proportional to similarity:

```math
F_attr(i,j) = k sᵢⱼ (xⱼ - xᵢ)
```

while unrelated entities repel:

```math
F_rep(i,j) ∝ (xᵢ - xⱼ) / ||xᵢ-xⱼ||ᵖ
```

The resulting equilibrium becomes a readable topology.

The equations choreograph the representation.

---

# 19. Conservation laws for visualization

Some representations should preserve quantities analogous to conserved values.

Possible semantic conservation constraints:

```text
sum of flow in = sum of flow out
entity identity remains traceable
probability mass sums to 1
hierarchical containment remains valid
causal direction remains oriented
ordering remains monotonic
```

These are not necessarily physical conservation laws.

They are **semantic conservation laws**.

They belong beside `Loss Validation`.

---

# 20. Computational stack

Initial scientific stack:

```text
NumPy        vectorized numerical kernel
SciPy        optimization, interpolation, signal processing, spatial methods
NetworkX     graph algorithms and topology
Matplotlib   reference 2D scientific renderer
```

Future optional backends:

```text
Pandas       tabular adapters
scikit-learn dimensional transforms
UMAP         manifold projection
Plotly       interactive 2D/3D
D3.js        web-native graphical grammar
Three.js     interactive spatial rendering
PyVista      scientific 3D meshes / fields
Blender      high-fidelity spatial output
```

The dependency hierarchy should remain:

```text
SEMANTICS
   ↓
MATH KERNEL
   ↓
REPRESENTATION PLAN
   ↓
RENDERER ADAPTER
```

Never:

```text
matplotlib object → source of semantic truth
```

---

# 21. The choreography

A future representation could literally be constructed as:

```text
1. embed semantic entities in Rⁿ
2. compute similarity metric
3. construct graph Laplacian
4. project dominant structural modes
5. minimize layout energy
6. detect persistent clusters
7. map uncertainty to opacity
8. map temporal derivative to motion
9. map anomaly to pulse
10. validate semantic conservation
11. render
```

What the observer experiences as a beautiful moving form is therefore the visible trace of a chain of mathematical decisions.

**That is the intended identity of Diagrama:**

> mathematics choreographing meaning into perception.
