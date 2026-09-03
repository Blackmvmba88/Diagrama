# Pattern Language

## Diagrama — Universal Structural Pattern Vocabulary

`Diagrama` is not only a representation engine.

It can also become a **pattern-revelation system**.

The important distinction is this:

```text
Representation answers:
How should this information be expressed?

Pattern analysis asks:
What structure is present here, even if the observer has not named it yet?
```

In many real situations, the human observer feels that *something is there* before being able to describe it precisely.

Diagrama should support that stage.

It should help turn:

```text
intuition
   ↓
visible structure
   ↓
pattern hypothesis
   ↓
semantic description
   ↓
formal representation
```

---

# 1. Patterns are domain-independent

A bottleneck in a network, a bottleneck in a supply chain and a bottleneck in a biological pathway are not the same phenomenon physically.

But structurally, they may share the same pattern:

```text
many inputs
   ↓
small-capacity region
   ↓
many outputs
```

Likewise:

```text
resonance
feedback loop
cascade
cluster
symmetry
symmetry breaking
oscillation
phase transition
bifurcation
critical threshold
hub formation
fragmentation
convergence
divergence
saturation
decay
latency accumulation
burst
wave
spiral
hierarchical nesting
```

can appear in software, biology, finance, music, mechanics, social systems, telemetry or abstract knowledge.

Diagrama should reason about these structures **before domain vocabulary is applied**.

---

# 2. Pattern families

## A — Growth and Decay

```text
linear growth
exponential growth
logistic growth
saturation
plateau
decay
collapse
recovery
overshoot
undershoot
```

Best revealed through:

```text
temporal curves
log scales
phase portraits
derivative views
state transitions
```

---

## B — Oscillation and Rhythm

```text
periodicity
harmonic behavior
quasi-periodicity
beat pattern
resonance
damping
phase shift
phase locking
entrainment
cyclic recurrence
```

Best revealed through:

```text
radial plots
spectrograms
frequency-domain views
phase portraits
helix transforms
sonification
```

---

## C — Threshold and Transition

```text
critical threshold
breakout
phase transition
regime change
bifurcation
tipping point
hysteresis
state jump
activation threshold
```

Best revealed through:

```text
state-space plots
change-point markers
phase diagrams
before/after transforms
animated transitions
```

---

## D — Flow

```text
convergence
divergence
circulation
recirculation
leakage
accumulation
bottleneck
backpressure
feedback
feed-forward
cascade
```

Best revealed through:

```text
Sankey
vector fields
streamlines
flow networks
state diagrams
```

---

## E — Network Structure

```text
hub
bridge
cluster
community
island
chain
star
mesh
core-periphery
small-world structure
centralization
fragmentation
redundancy
single point of failure
```

Best revealed through:

```text
network graphs
adjacency matrices
centrality glyphs
community maps
hierarchical edge bundles
```

---

## F — Spatial Structure

```text
cluster
gradient
boundary
front
void
hotspot
coldspot
corridor
ring
shell
layer
territory
basin
ridge
```

Best revealed through:

```text
heatmaps
contours
hexbin
Voronoi
topography
3D surfaces
```

---

## G — Symmetry

```text
mirror symmetry
rotational symmetry
translational symmetry
self-similarity
scale symmetry
symmetry breaking
chirality
balanced opposition
```

Best revealed through:

```text
radial geometry
matrix layouts
paired views
fractal views
3D structure
```

Symmetry breaking is often more informative than symmetry itself.

A system may appear stable until one sector deviates.

---

## H — Hierarchy and Nesting

```text
parent-child structure
recursive nesting
layered containment
fractal hierarchy
branching
power-law hierarchy
core-shell organization
```

Best revealed through:

```text
trees
sunburst
treemap
nested circles
icicle
recursive geometry
```

---

## I — Distribution and Density

```text
normal concentration
long tail
heavy tail
multimodal distribution
skew
outlier field
sparse regime
dense regime
clustered density
uniformity
```

Best revealed through:

```text
histograms
violin plots
density fields
ridgelines
hexbin
probability surfaces
```

---

## J — Causality and Propagation

```text
chain reaction
cascade
feedback loop
causal fork
causal convergence
delayed effect
amplification
attenuation
propagation front
```

Best revealed through:

```text
causal graphs
time-lag plots
Sankey
sequence diagrams
animated propagation
```

---

## K — Anomaly

```text
single outlier
local anomaly
global anomaly
structural anomaly
contextual anomaly
temporal anomaly
novel cluster
unexpected transition
```

Best revealed through:

```text
contrast
isolation
glyph mutation
pulse
color inversion
topological displacement
sonification
```

---

## L — Competition and Balance

```text
equilibrium
unstable equilibrium
dominance
oscillating dominance
resource competition
trade-off
Pareto frontier
zero-sum interaction
coexistence
```

Best revealed through:

```text
phase space
radar
Pareto plots
balance glyphs
vector competition fields
```

---

## M — Emergence

```text
collective behavior
self-organization
spontaneous clustering
pattern formation
synchronization
emergent hierarchy
critical mass
order from local rules
```

Best revealed through:

```text
animated fields
agent maps
network evolution
multiscale views
entropy measures
```

---

## N — Transformation

```text
morphing
migration
splitting
merging
rotation of basis
compression
expansion
folding
unfolding
projection
reparameterization
```

Best revealed through:

```text
animated morphs
alluvial diagrams
before/after views
transform chains
3D-to-2D projections
```

---

# 3. Pattern descriptors

A pattern should not be represented only by a name.

It should carry measurable descriptors.

Example:

```yaml
pattern:
  type: oscillation
  confidence: 0.93
  scale: medium
  locality: global
  persistence: high
  periodicity: 12.4
  amplitude: 0.71
  phase_stability: 0.88
```

Generic descriptors may include:

```text
confidence
scale
locality
persistence
strength
direction
periodicity
symmetry
entropy
centrality
curvature
density
frequency
amplitude
duration
propagation_speed
```

---

# 4. Multi-scale pattern recognition

The same system may contain different patterns at different scales.

Example:

```text
GLOBAL
  stable equilibrium

REGIONAL
  two competing clusters

LOCAL
  one accelerating anomaly
```

Therefore Diagrama should support:

```text
micro
meso
macro
```

and potentially continuous scale-space analysis.

A pattern that is invisible globally may be obvious locally.

A local anomaly may disappear when aggregated.

A global trend may disappear when looking only at individual entities.

Representation must therefore be scale-aware.

---

# 5. Pattern superposition

Real structures rarely contain one pattern at a time.

Example:

```text
exponential growth
+
periodic oscillation
+
regional anomaly
+
network bottleneck
```

Diagrama should allow multiple pattern hypotheses to coexist.

```yaml
patterns:
  - type: growth
    confidence: 0.96

  - type: periodicity
    confidence: 0.88

  - type: bottleneck
    confidence: 0.72
```

A representation may then assign different perceptual channels to each pattern.

---

# 6. Pattern → Representation

Once a pattern hypothesis exists, representation selection can intentionally amplify it.

Example:

```text
pattern: periodicity
```

Candidate transformations:

```text
linear timeline
   ↓ radialize
circular phase view
   ↓ spectralize
frequency view
```

If periodicity becomes clearer after radialization, the transform has increased **pattern visibility** without changing the underlying semantics.

This suggests an additional objective function for Diagrama:

```text
PatternVisibility(R, P)
```

Where:

```text
R = representation
P = pattern hypothesis
```

Representation selection can then optimize not only semantic fidelity but also the observer's ability to perceive a suspected pattern.

---

# 7. Pattern visibility score

Conceptually:

```text
V_pattern = f(
  perceptual_separation,
  contrast,
  scale_match,
  dimensional_alignment,
  clutter,
  occlusion,
  temporal_resolution
)
```

Then candidate ranking may become:

```text
Score(R) =
    α · TaskUtility
  + β · SemanticFidelity
  + γ · PatternVisibility
  + δ · PerceptualClarity
  - λ · CognitiveCost
  - μ · SemanticLoss
```

This makes Diagrama capable of selecting a representation specifically because it exposes a latent structure better.

---

# 8. Pattern hypothesis loop

Diagrama can eventually operate iteratively:

```text
SIR
 ↓
initial representation
 ↓
pattern detector
 ↓
pattern hypothesis
 ↓
representation transform
 ↓
increased pattern visibility
 ↓
human inspection
 ↓
confirmed / rejected / refined pattern
```

This creates a human-machine discovery loop.

The system does not need to claim that every detected pattern is true.

It needs to make hypotheses **visible and inspectable**.

---

# 9. Cross-domain structural analogy

One of the most powerful future capabilities is structural analogy.

If two systems share a semantic topology, Diagrama may notice that they instantiate the same abstract pattern even though their domains differ.

Example:

```text
software dependency congestion
supply-chain bottleneck
vascular constriction
network queue saturation
```

Possible shared abstraction:

```text
many upstream paths
      ↓
limited-capacity intermediary
      ↓
downstream delay
```

The purpose is not to claim that the systems are physically equivalent.

The purpose is to recognize that the same **structural motif** can appear in different domains.

That makes pattern vocabulary reusable.

---

# 10. Pattern motifs

Reusable motifs may eventually live in a registry:

```text
motifs/
├── bottleneck.yaml
├── feedback_loop.yaml
├── cascade.yaml
├── hub.yaml
├── bifurcation.yaml
├── resonance.yaml
├── symmetry_break.yaml
├── convergence.yaml
├── divergence.yaml
├── saturation.yaml
├── spiral.yaml
└── hierarchy.yaml
```

Example:

```yaml
id: bottleneck
family: flow

signature:
  upstream_degree: high
  intermediary_capacity: low
  downstream_demand: high

preserve:
  - direction
  - capacity
  - topology

recommended_views:
  - sankey
  - flow_network
  - capacity_heatmap
```

---

# 11. Pattern discovery is not pattern hallucination

Diagrama must distinguish:

```text
observed structure
inferred pattern
speculative interpretation
```

Every pattern hypothesis should carry:

```text
confidence
evidence
scale
assumptions
counterexamples
```

A beautiful representation must never upgrade weak evidence into certainty.

This principle connects Pattern Language directly to `Loss Validation` and explainability.

---

# 12. The observer may begin without words

A critical design principle:

The user should not need to know the name of a visualization, transform or pattern in advance.

They may begin with:

```text
"something feels circular"
"there is a hidden layer"
"these things seem to pull each other"
"I think this repeats but not exactly"
"there is a shape here I cannot name"
"something changes after this threshold"
```

Diagrama's job is to progressively formalize that intuition.

```text
vague intuition
    ↓
semantic clues
    ↓
structural hypothesis
    ↓
representation candidates
    ↓
pattern visibility
    ↓
formal description
```

This is not a weakness in the interface.

It is one of the reasons the system exists.

---

# 13. Final principle

> **A pattern does not become important when we name it.**
>
> **Naming is what becomes possible after the pattern is made visible.**

Diagrama should help bridge that gap.

**BlackMamba Lab — Diagrama**  
*Make hidden structure perceptible.*
