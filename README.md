# DIAGRAMA

## BlackMamba Lab — Universal Representation Engine

> **Information does not have one shape.**  
> **Representation is part of reasoning.**  
> **Meaning must survive the projection.**

`Diagrama` is a domain-agnostic engine for translating **knowledge, relationships, dimensions, states, uncertainty and intent** into the representation that best exposes their structure to a human observer.

It is not a chart library.

It is not an infographic generator.

It is not a wrapper around D3.js, matplotlib, Three.js or any specific renderer.

Those systems answer questions such as:

```text
Draw this line.
Place this point here.
Render this mesh.
Color this region.
```

**Diagrama operates one level above them.**

It asks:

```text
What does this information mean?
What relationships must remain visible?
What is the observer trying to understand?
Which dimensions are essential?
Which may be compressed?
What geometry exposes the hidden structure?
What information would be lost by that projection?
Can that loss be compensated through another perceptual channel?
```

Then — and only then — does it decide how the information should be represented.

---

# The idea

Most visualization pipelines assume:

```text
DATA → CHART
```

Diagrama proposes:

```text
RAW INFORMATION
      ↓
SEMANTIC MODEL
      ↓
OBSERVER INTENT
      ↓
REPRESENTATION CANDIDATES
      ↓
LOSS VALIDATION
      ↓
PERCEPTUAL ENCODING
      ↓
GEOMETRY
      ↓
RENDERER
```

Or, in one line:

```text
Knowledge → Semantics → Intent → Geometry → Perception
```

The renderer is the final actuator.

The real intelligence happens before drawing anything.

---

# Why this matters

The same information can expose radically different truths depending on its representation.

A timeline emphasizes **order**.

A clock emphasizes **recurrence**.

A helix emphasizes **recurrence plus progression**.

A network emphasizes **connection**.

A matrix emphasizes **exact pairwise structure**.

A Sankey emphasizes **flow**.

A vector field emphasizes **direction and magnitude**.

A topographic surface turns intensity into **terrain**.

A glyph compresses many variables into **one perceptual object**.

Animation can expose **transition** that a static image hides.

Sound can expose **events, urgency or periodicity** without consuming visual bandwidth.

> **Changing representation can reveal knowledge that was already present in the data but invisible in the previous basis.**

That is the core thesis of Diagrama.

---

# A computational instrument for observation

A microscope changes the scale at which structure can be perceived.

A telescope changes the distance at which structure can be perceived.

A spectrometer separates properties that appear merged to ordinary perception.

**Diagrama changes the representational basis through which information is perceived.**

Its long-term objective is therefore larger than visualization:

> **Build computational instruments that expand the observer's ability to detect structure, relation, transformation, uncertainty and hidden context.**

---

# Semantic Intermediate Representation — SIR

The source of truth is never the chart.

The source of truth is a representation-independent semantic model.

```yaml
entities:
  - id: source
    type: system

  - id: target
    type: system

relations:
  - from: source
    to: target
    type: influence
    magnitude: 0.82
    confidence: 0.91

dimensions:
  magnitude:
    type: quantitative

  confidence:
    type: probability

  direction:
    type: vector

intent:
  primary: explain_relation
```

From that same SIR, Diagrama could produce:

```text
network
adjacency matrix
vector diagram
Sankey
radial relation map
3D spatial scene
symbolic glyph
animated transition
sonified state
```

The knowledge remains invariant.

The **basis of observation** changes.

---

# Information primitives

Diagrama does not begin with pixels. It begins with semantic primitives.

## Entities

```text
people
objects
systems
components
files
ideas
cities
cells
machines
states
processes
```

## Quantities

```text
magnitude
count
rate
probability
energy
cost
time
distance
frequency
confidence
```

## Relations

```text
dependency
causality
similarity
ownership
flow
containment
adjacency
influence
communication
competition
feedback
```

## States

```text
active
inactive
stable
unstable
growing
falling
critical
unknown
transitioning
```

## Structures

```text
sequence
hierarchy
network
cycle
field
cluster
manifold
grid
layer
continuum
```

## Uncertainty

```text
confidence
error
variance
range
ambiguity
missing data
probability
prediction
```

These are the primitives the engine reasons about.

Domains are adapters at the edge.

---

# Intent Engine

The same information should not be represented identically for every purpose.

Diagrama explicitly models the observer's intention.

```text
compare
measure
explain
trace
discover
alert
monitor
diagnose
navigate
summarize
teach
predict
explore
remember
communicate
```

A first resolution matrix:

| Intent | Preferred geometry family | Dominant perceptual channels | Typical objective |
|---|---|---|---|
| **Discover / Alert** | topological, spatial, density | contrast, pulse, motion | expose anomalies or emergent structure |
| **Explain / Trace** | flow, network, state graph | width, direction, connectivity | explain how something propagates |
| **Monitor / Observe** | polar, radial, temporal | position, size, motion | preserve situational awareness |
| **Compare / Measure** | Cartesian, aligned matrix | position, length | maximize quantitative precision |
| **Navigate** | topology, hierarchy, spatial map | proximity, containment | move through complex structure |
| **Diagnose** | matrix, causal graph, layered view | contrast, relation, uncertainty | isolate causes and dependencies |
| **Teach** | progressive diagram, narrative layers | hierarchy, annotation, motion | control cognitive load |
| **Predict** | trajectory, probability field, phase space | direction, opacity, envelope | expose future state and uncertainty |

This matrix is not a hard-coded truth.

It is the beginning of the autonomous `Representation Selector`.

---

# Representation Selector

Conceptually:

```text
representation = f(
    semantics,
    intent,
    dimensionality,
    cardinality,
    topology,
    uncertainty,
    audience,
    medium,
    interaction,
    loss_budget
)
```

The selector generates candidate representations and scores them.

Example:

```text
Candidate              Utility   Fidelity   Complexity
─────────────────────────────────────────────────────
Adjacency Matrix        0.94      0.98       0.31
Network Graph           0.86      0.91       0.66
Chord Diagram           0.63      0.78       0.71
Sankey                  0.28      0.51       0.62
```

And it must be able to explain its decision:

```text
Selected: Adjacency Matrix

because:
+ 2,400 entities
+ dense pairwise relations
+ exact relation lookup is important
+ topology must be preserved
- node-link layout would create excessive edge crossings
```

A future Diagrama should not merely render.

**It should justify why a representation was chosen.**

---

# Visual and perceptual grammar

Representation is built from perceptual channels.

Each channel can carry semantic information.

| Channel | Possible semantic load |
|---|---|
| X / Y / Z position | quantity, chronology, space, category |
| distance | similarity, separation, dependency |
| angle | phase, orientation, class |
| radius | magnitude, reach, importance |
| length | quantitative value |
| area | magnitude |
| volume | density or magnitude |
| shape | category or semantic role |
| color | state, polarity, category, intensity |
| saturation | confidence or intensity |
| luminosity | energy, activity, relevance |
| opacity | uncertainty, confidence, relevance |
| line width | strength, capacity, flow |
| line style | relation type or uncertainty |
| border | alert, classification, confidence |
| texture | density, class, uncertainty |
| connectivity | relation structure |
| motion | change, urgency, direction |
| velocity | rate |
| acceleration | change of rate |
| rotation | phase, periodicity, energy |
| pulse | recurrence, activity, urgency |
| depth | hierarchy or latent dimension |
| sound | event, magnitude, anomaly, state |
| haptics | force, threshold, urgency |

A representation does not need one axis per dimension.

A single glyph may encode:

```text
position = context
size     = magnitude
color    = state
border   = uncertainty
rotation = direction
pulse    = acceleration
opacity  = confidence
```

Seven dimensions.

One object.

---

# Geometry families

Diagrama treats geometries as alternative observational spaces.

## Cartesian

Best for magnitude, correlation, alignment and temporal evolution.

```text
line
bar
scatter
area
surface
candlestick
```

## Polar / Radial

Best for cycles, periodicity, multidimensional profiles and centrality.

```text
radar
polar plot
radial bars
concentric rings
sunburst
```

## Circular / Orbital

Best for closed cycles, ecosystems and center-periphery relations.

```text
chord diagrams
orbit maps
circular dependencies
concentric systems
```

## Matrix

Best for dense relationships and exact pairwise inspection.

```text
adjacency matrix
heatmap
correlation matrix
confusion matrix
```

## Network

Best for connectivity, communities, propagation and influence.

```text
node-link
force-directed
bipartite
knowledge graph
causal graph
```

## Hierarchical

Best for containment, ancestry and decomposition.

```text
tree
dendrogram
treemap
icicle
sunburst
```

## Flow

Best for transfer, conversion, process and state transition.

```text
Sankey
alluvial
funnel
swimlane
state machine
```

## Hexagonal

Best for tiling, density and neighborhood systems.

```text
hexbin
hex map
cellular field
```

## Vectorial

Best for magnitude plus direction.

```text
vector
quiver
vector field
streamline
phase portrait
```

## Topological

Best when connectivity matters more than metric distance.

```text
topology maps
adjacency systems
manifolds
persistent structures
```

## Volumetric / 3D

Best for layered structure, surfaces, internal density and spatial relationships.

```text
point cloud
mesh
voxel volume
isosurface
layered scene
```

## Symbolic

Best for immediate semantic recognition.

```text
icons
badges
glyphs
notation systems
semantic marks
```

## Temporal / Animated

Best when transition itself is information.

```text
animated state space
morphing representation
trails
pulse
motion field
```

## Multimodal

Best when visual bandwidth alone is insufficient.

```text
visual + motion
visual + sound
visual + haptics
3D + interaction
AR + spatial annotation
```

---

# Representation transforms

A critical capability of Diagrama is changing the representational basis **without changing the semantic source**.

```text
LINEAR
   ↓ radialize
RADIAL
   ↓ spatialize
3D
   ↓ relationalize
NETWORK
   ↓ aggregate
MATRIX
```

Candidate transforms:

```text
radialize
flatten
project
cluster
aggregate
explode
collapse
layer
normalize
rotate
rebase
spatialize
relationalize
symbolize
animate
sonify
```

Example — one semantic variable: **time**.

```text
TIMELINE
────────────────────────►

        ↓ radialize

CLOCK / CYCLE
       12
    9   ◉   3
        6

        ↓ spatialize

HELIX
      ╱╲
     ╱  ╲
     ╲  ╱
      ╲╱
```

Each basis reveals a different property:

```text
timeline → order
circle   → recurrence
helix    → recurrence + progression
```

Transformation is therefore not merely graphical.

It can be a **knowledge operation**.

---

# Loss Validation — Conservation of Meaning

Every projection risks destroying information.

A 4D state projected into 2D may lose depth.

A network converted into a histogram may lose identity and connectivity.

A continuous signal summarized as categories may lose local variation.

A 3D structure flattened into a map may preserve adjacency but destroy metric distance.

Diagrama must know this.

Every transform should produce both:

```text
Representation
+
Loss Report
```

Conceptually:

```text
T : SIR → R
```

and

```text
V(SIR, R) → LossVector
```

Where a loss vector may contain:

```text
L = {
  identity,
  topology,
  metric,
  order,
  magnitude,
  direction,
  uncertainty,
  temporal_resolution,
  hierarchy,
  context
}
```

Example:

```yaml
transform: project_3d_to_2d
classification: lossy

preserved:
  - identity
  - topology
  - x
  - y

lost:
  - z_depth

compensation:
  z_depth:
    channel: opacity
    confidence: 0.84
```

This introduces three fundamental transformation classes:

### Lossless

Protected semantic invariants survive the transform.

### Lossy

One or more semantically relevant dimensions are discarded or compressed.

### Compensated

A dimension disappears from its original channel but is re-encoded through another perceptual channel.

Example:

```text
Z position lost
      ↓
encoded as color saturation
```

The engine can therefore reason about a **loss budget**.

```text
loss_budget = f(intent, audience, medium, task)
```

A monitoring display may tolerate geometric simplification for speed.

A scientific inspection may forbid loss of metric relationships.

A teaching diagram may intentionally collapse detail to reduce cognitive load.

The question is not:

> Is information being lost?

The real question is:

> **Is the lost information irrelevant to the observer's current intent, or must it be preserved elsewhere?**

This is one of Diagrama's core contracts.

---

# Protected invariants

A transform may declare invariants that are not allowed to disappear.

```yaml
protected_invariants:
  - entity_identity
  - causal_direction
  - hierarchy
  - confidence
```

A representation candidate that violates one of those invariants can be rejected automatically.

```text
Candidate: Pie Chart
Rejected:
✗ causal direction destroyed
✗ entity relation topology destroyed
```

This moves Diagrama from visual recommendation toward **semantic validation**.

---

# Hidden dimensions

Not every meaningful dimension belongs on an axis.

Secondary dimensions can be expressed through:

```text
color
shape
opacity
texture
border
layer
motion
frequency
rotation
proximity
connectivity
depth
sound
interaction
```

A layered observation can therefore preserve context beyond visible geometry:

```text
LAYER 1  magnitude
LAYER 2  relation
LAYER 3  temporal behavior
LAYER 4  uncertainty
LAYER 5  context
LAYER 6  semantic state
LAYER 7  prediction
```

The goal is not maximum complexity.

The goal is **maximum relevant meaning per unit of cognitive load**.

---

# Symbol systems

Symbols are first-class semantic carriers.

Example generic vocabulary:

| Symbol | Generic semantic role |
|---|---|
| ▲ | increase / ascent |
| ▼ | decrease / descent |
| ⚖ | equilibrium |
| ⚡ | acceleration / sudden energy |
| 🔥 | threshold break |
| 🚀 | rapid propagation |
| ✦ | extraordinary event |
| ⚠ | anomaly / attention |
| 💎 | exceptional quality |
| ☠ | exhaustion / loss of momentum |

These are examples, not domain rules.

A domain may define its own notation:

```yaml
symbols:
  growth:
    glyph: "▲"
    color: green

  anomaly:
    glyph: "⚠"
    color: amber

  exceptional:
    glyph: "✦"
    color: purple
```

This allows Diagrama to host reusable **semantic alphabets**.

---

# Domain agnosticism

Diagrama should be capable of representing:

```text
financial markets
music analytics
molecular systems
software architecture
Git histories
transport networks
biological pathways
mechanical systems
knowledge graphs
social systems
telemetry
astronomical systems
supply chains
AI model behavior
education
urban systems
energy systems
human workflows
abstract ideas
```

Not because these domains are identical.

Because they all contain combinations of:

```text
entities
relations
states
quantities
uncertainty
space
time
structure
meaning
```

Those are Diagrama's real primitives.

---

# Proposed architecture

```text
Diagrama/
│
├── core/
│   ├── semantics/
│   ├── entities/
│   ├── relations/
│   ├── dimensions/
│   ├── uncertainty/
│   └── ir/
│
├── intent/
│   ├── compare/
│   ├── explain/
│   ├── discover/
│   ├── monitor/
│   ├── diagnose/
│   └── navigate/
│
├── grammar/
│   ├── position/
│   ├── color/
│   ├── shape/
│   ├── size/
│   ├── motion/
│   ├── texture/
│   ├── symbols/
│   ├── sound/
│   └── haptics/
│
├── geometries/
│   ├── cartesian/
│   ├── polar/
│   ├── radial/
│   ├── circular/
│   ├── matrix/
│   ├── network/
│   ├── hierarchy/
│   ├── flow/
│   ├── hexagonal/
│   ├── vector/
│   ├── topology/
│   └── spatial3d/
│
├── transforms/
│   ├── radialize/
│   ├── flatten/
│   ├── project/
│   ├── cluster/
│   ├── aggregate/
│   ├── layer/
│   ├── spatialize/
│   ├── symbolize/
│   ├── animate/
│   └── loss_validation/
│
├── selector/
│   ├── candidates/
│   ├── scoring/
│   ├── constraints/
│   └── explainability/
│
├── renderers/
│   ├── svg/
│   ├── canvas/
│   ├── terminal/
│   ├── webgl/
│   ├── threejs/
│   ├── audio/
│   └── multimodal/
│
├── domains/
│   └── adapters/
│
├── schemas/
├── examples/
├── docs/
└── README.md
```

The domain belongs at the boundary.

**The core must never become dependent on the domain.**

---

# First engine contract

```text
INPUT
  Semantic IR
  + observer intent
  + medium constraints
  + protected invariants

PROCESS
  analyze semantics
  infer dimensionality
  identify topology
  generate representation candidates
  estimate cognitive cost
  evaluate semantic loss
  compensate recoverable dimensions
  rank candidates

OUTPUT
  selected representation
  + perceptual encoding
  + transform chain
  + loss report
  + selection explanation
```

That is the minimum viable intelligence of Diagrama.

---

# Principles

### 1. Meaning before rendering

Never choose geometry before understanding semantics.

### 2. Semantic source of truth

Visual state must remain traceable to the SIR.

### 3. Representation is a hypothesis

Every visualization claims that certain properties matter more than others.

Make that claim explicit.

### 4. Transformation must declare loss

No projection is allowed to silently destroy relevant meaning.

### 5. Preserve invariants before aesthetics

Beauty cannot justify semantic corruption.

### 6. Use the perceptual channel that matches the question

Position for precision. Motion for change. Connectivity for relation. Sound for events. Depth only when depth adds meaning.

### 7. Complexity must earn its place

A dimension is added only when it carries useful information.

### 8. Multiple representations may coexist

One view may explain. Another may reveal. Another may measure.

### 9. Domains are adapters

The engine reasons about semantics, not industries.

### 10. The representation should be explainable

Diagrama must eventually answer:

> Why am I showing you this information this way?

---

# Roadmap

## Phase 0 — Foundation

- define Semantic IR
- define semantic primitive vocabulary
- define geometry registry
- define perceptual channel registry
- define intent taxonomy
- define protected invariants
- define Loss Validation contract

## Phase 1 — Representation intelligence

- candidate generation
- intent-to-geometry matrix
- dimensionality analysis
- cardinality heuristics
- topology detection
- semantic loss scoring
- cognitive-cost scoring

## Phase 2 — Transform engine

- project
- radialize
- flatten
- cluster
- aggregate
- layer
- compensate lost dimensions
- reversible transform metadata

## Phase 3 — Renderers

- SVG
- terminal
- Canvas
- WebGL / Three.js
- animation

## Phase 4 — Multimodal representation

- sonification
- motion grammar
- interaction grammar
- haptic mappings
- spatial / AR representations

## Phase 5 — Autonomous representation

```text
raw information
      ↓
semantic extraction
      ↓
intent inference
      ↓
representation synthesis
      ↓
loss validation
      ↓
explainable rendering
```

At that point, Diagrama stops being a visualization toolkit.

It becomes a **general-purpose semantic representation runtime**.

---

# BlackMamba Lab

Diagrama was not created because another graph library was needed.

It emerged from a recurring engineering problem:

> Information changes character when its representation changes.

Once that is recognized, the logical next step is not to collect more chart types.

The logical next step is to build a system that understands **why one representation reveals what another hides**.

That is what Diagrama is for.

---

## Final axiom

```text
The data is not the diagram.
The diagram is not the truth.
The diagram is a projection of truth optimized for an observer and an intent.

Diagrama exists to choose that projection consciously,
measure what it sacrifices,
and preserve the meaning that matters.
```

**BlackMamba Lab — Diagrama**  
*Compile meaning into perception.*
