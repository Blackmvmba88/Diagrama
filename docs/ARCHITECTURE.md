# Diagrama Architecture

## BlackMamba Lab — Semantic Representation Runtime

This document defines the first implementation architecture for Diagrama.

The system is intentionally split into two worlds:

```text
SEMANTIC WORLD                    REPRESENTATION WORLD
────────────────────────────────────────────────────────
entities                          marks
relations                         edges
states                            color / shape
quantities                        position / size
uncertainty                       opacity / texture
intent                            layout strategy
invariants                        transform constraints
```

The architecture exists to make the boundary explicit.

A renderer must never become the semantic source of truth.

---

# 1. Pipeline

```text
┌──────────────────────┐
│ Domain Input         │
│ logs / JSON / graph  │
│ telemetry / text     │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Domain Adapter       │
│ optional             │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Semantic IR (SIR)    │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Semantic Analyzer    │
│ structure            │
│ topology             │
│ dimensionality       │
│ uncertainty          │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Intent Engine        │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Candidate Generator  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Constraint Filter    │
│ protected invariants │
│ medium               │
│ accessibility        │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Transform Planner    │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Loss Validator       │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Candidate Scorer     │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Representation Plan  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Renderer             │
└──────────────────────┘
```

---

# 2. Semantic IR

The Semantic Intermediate Representation is the stable contract between domains and representations.

The SIR should describe **what exists and what it means**, not how it should be drawn.

Primary sections:

```text
entities
relations
dimensions
states
uncertainty
invariants
intent
constraints
metadata
```

A domain adapter may infer these from raw input.

Example:

```yaml
entities:
  - id: A
    type: subsystem
  - id: B
    type: subsystem

relations:
  - id: AB
    from: A
    to: B
    type: causal
    direction: forward
    strength: 0.73

intent:
  primary: trace

protected_invariants:
  - entity_identity
  - causal_direction
```

---

# 3. Semantic Analyzer

Responsibilities:

```text
infer cardinality
measure graph density
classify topology
detect hierarchy
detect cycles
detect temporal dimensions
detect vector quantities
detect uncertainty
identify high-dimensional structures
estimate relation complexity
```

Example output:

```yaml
analysis:
  entity_count: 2400
  relation_count: 58122
  relation_density: high
  topology: dense_graph
  hierarchy: false
  temporal: false
  uncertainty: true
  recommended_constraints:
    avoid_node_edge_clutter: true
```

---

# 4. Intent Engine

The Intent Engine translates an observer goal into representational priorities.

Example:

```yaml
intent: diagnose
priorities:
  causal_structure: 1.0
  anomaly_contrast: 0.9
  exact_magnitude: 0.6
  global_overview: 0.8
  aesthetic_symmetry: 0.1
```

Intent can be explicit or inferred.

Explicit intent always wins over inference.

---

# 5. Representation Registry

Every geometry family registers capabilities and limitations.

Example conceptual record:

```yaml
id: adjacency_matrix
family: matrix

supports:
  dense_relations: excellent
  pairwise_lookup: excellent
  topology: good
  direction: good
  hierarchy: weak
  flow: weak

costs:
  label_density: high
  global_path_tracing: medium

channels:
  - x_position
  - y_position
  - color
  - opacity
```

The registry allows selection to be data-driven rather than hard-coded into conditionals.

---

# 6. Candidate Generator

The generator queries the representation registry using:

```text
semantic structure
intent priorities
medium constraints
interaction availability
cardinality
uncertainty
```

It should return multiple candidates, not one immediate answer.

Example:

```text
adjacency_matrix
force_directed_network
hierarchical_edge_bundle
chord_diagram
```

---

# 7. Constraint Filter

Candidates are rejected before scoring if they violate hard constraints.

Constraint classes:

```text
protected semantic invariants
screen / output size
static vs interactive medium
2D vs 3D availability
color accessibility
latency budget
rendering budget
privacy rules
required precision
```

This prevents a high visual score from overriding semantic validity.

---

# 8. Transform Planner

A representation may require a chain of transformations.

Example:

```text
high-dimensional graph
   ↓ cluster
community graph
   ↓ project
2D topology
   ↓ compensate depth
color + opacity
   ↓ annotate
interactive representation
```

The planner records every step.

```yaml
transform_chain:
  - cluster
  - project_2d
  - encode_depth_as_luminance
  - annotate_outliers
```

---

# 9. Loss Validator

The validator compares each candidate plan against the **original SIR**, not merely against intermediate outputs.

Outputs:

```text
semantic fidelity
loss vector
protected-invariant violations
compensation map
reversibility
loss classification
```

See `docs/LOSS_VALIDATION.md`.

---

# 10. Candidate Scorer

After invalid representations are removed, valid candidates can be ranked.

First conceptual dimensions:

```text
task utility
semantic fidelity
perceptual clarity
cognitive cost
interaction cost
rendering cost
explainability
accessibility
```

Possible conceptual function:

```text
Score =
  α TaskUtility
+ β SemanticFidelity
+ γ PerceptualClarity
+ δ Explainability
+ η Accessibility
- λ CognitiveCost
- μ SemanticLoss
- ν RenderCost
```

Weights come from intent and medium.

---

# 11. Representation Plan

The selector does not return pixels.

It returns a renderer-independent plan.

Example:

```yaml
representation:
  geometry: adjacency_matrix

encodings:
  relation_strength:
    channel: color_luminance
  confidence:
    channel: opacity
  anomaly:
    channel: border

interaction:
  hover: entity_details
  click: isolate_neighbors
  zoom: enabled

transform_chain:
  - order_by_cluster

loss_report:
  classification: lossy
  semantic_fidelity: 0.96

explanation:
  summary: Dense pairwise relations favor a matrix over a node-link layout.
```

This plan can then be consumed by different renderers.

---

# 12. Renderer Layer

Renderers are replaceable backends.

Potential targets:

```text
SVG
Canvas
terminal
D3.js
matplotlib
Plotly
Three.js
WebGL
Blender
audio
AR / XR
haptic devices
```

Diagrama does not compete with these systems.

**It decides what they should render and why.**

---

# 13. Explainability

Every autonomous representation decision should be inspectable.

Minimum explanation:

```text
what was selected
why it was selected
what alternatives were considered
what semantics were preserved
what semantics were compressed
what compensation was applied
what constraints caused rejection
```

Example:

```text
Selected: Heatmap

Why:
- observer intent: discover anomalies
- 40 × 24 categorical-temporal grid
- color contrast exposes local deviations efficiently

Preserved:
- time slot
- category identity
- intensity

Compressed:
- exact event sequence inside each slot
```

---

# 14. Domain Adapters

A domain adapter converts domain vocabulary into semantic primitives.

```text
Domain                    Semantic primitive
────────────────────────────────────────────
software dependency       directed relation
motor RPM                 temporal quantitative dimension
molecular bond            relation + strength
financial transfer        directed weighted flow
musical listener          entity
city                      spatial entity
uncertain forecast        state + probability
```

Adapters may contain domain knowledge.

The core may not.

---

# 15. Core interfaces

Conceptual interfaces:

```python
class SemanticAdapter:
    def to_sir(raw_input) -> SIR: ...

class SemanticAnalyzer:
    def analyze(sir: SIR) -> SemanticAnalysis: ...

class IntentEngine:
    def resolve(sir: SIR, requested_intent=None) -> IntentProfile: ...

class CandidateGenerator:
    def generate(analysis, intent, constraints) -> list[Candidate]: ...

class TransformPlanner:
    def plan(sir, candidate, constraints) -> RepresentationPlan: ...

class LossValidator:
    def validate(sir, plan, intent) -> LossReport: ...

class RepresentationSelector:
    def select(sir, intent, constraints) -> RankedPlans: ...

class Renderer:
    def render(plan: RepresentationPlan): ...
```

---

# 16. Critical separation

Never collapse these layers:

```text
semantic meaning ≠ geometry
geometry ≠ perceptual encoding
perceptual encoding ≠ renderer
renderer ≠ domain
```

That separation is what makes Diagrama universal.

---

# 17. The runtime loop

The long-term runtime can become interactive:

```text
observer asks question
        ↓
intent changes
        ↓
representation selector reruns
        ↓
representation changes basis
        ↓
observer discovers structure
        ↓
new question
```

Diagrama then becomes more than a static compiler.

It becomes an **interactive epistemic runtime**: a system for repeatedly changing the basis of observation as the human question evolves.
