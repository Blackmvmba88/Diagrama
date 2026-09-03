# Loss Validation

## Conservation of Meaning Across Representation Transforms

`Loss Validation` is the semantic safety layer of Diagrama.

Its job is not to decide whether a representation is visually attractive. Its job is to determine whether the representation preserves the information that matters for the observer's intent.

---

# 1. Problem

Any projection may collapse information.

Examples:

```text
3D → 2D              may remove depth
network → histogram  removes identity and topology
continuous → bins    removes local variation
sequence → set       removes order
probability → label  removes uncertainty
causal graph → table may hide direction
```

Diagrama must never perform this collapse silently.

Every representation transform must therefore produce:

```text
representation
+
loss report
```

---

# 2. Formal model

Let:

```text
S = semantic source (SIR)
T = representation transform
R = resulting representation
V = validator
```

Then:

```text
T(S) → R
V(S, R, intent, constraints) → LossReport
```

Validation always compares the **final representation against the original semantic source**.

It must not rely only on the previous graphical state, because an earlier lossy projection may already have destroyed information.

---

# 3. Semantic invariants

An invariant is a property whose meaning may need to survive the transform.

Typical invariant classes:

```text
entity_identity
entity_count
category_membership
relation_identity
topology
causal_direction
order
hierarchy
metric_distance
relative_distance
magnitude
sign
orientation
temporal_order
temporal_resolution
frequency
phase
uncertainty
confidence
context
```

Each invariant receives:

```text
importance weight
minimum preservation threshold
protected / non-protected status
```

Example:

```yaml
invariants:
  causal_direction:
    weight: 1.0
    protected: true
    min_preservation: 1.0

  metric_distance:
    weight: 0.4
    protected: false
    min_preservation: 0.6
```

---

# 4. Preservation score

For invariant `i`, define:

```text
p_i ∈ [0,1]
```

where:

```text
1.0 = fully preserved
0.0 = completely absent
```

A weighted semantic fidelity score can be expressed as:

```text
F_sem = Σ(w_i · p_i) / Σ(w_i)
```

and semantic loss as:

```text
L_sem = 1 - F_sem
```

This global score is useful for ranking, but it must never override protected invariants.

A candidate with:

```text
F_sem = 0.97
```

is still invalid if it destroys a protected causal direction.

---

# 5. Hard constraints

For every protected invariant:

```text
p_i >= min_preservation_i
```

If the condition fails:

```text
candidate.status = REJECTED
```

Example:

```text
Candidate: Pie Chart

REJECTED
✗ causal_direction = 0.0 < 1.0
✗ relation_topology = 0.0 < 0.9
```

This prevents aesthetics or simplicity from corrupting meaning.

---

# 6. Transformation classes

## LOSSLESS

All required semantic invariants survive within tolerance.

```text
∀ protected i: p_i >= threshold_i
and
L_sem <= ε
```

## LOSSY

One or more non-protected dimensions are compressed, aggregated or removed, but the transform remains within the intent-specific loss budget.

## COMPENSATED

An original perceptual or geometric channel disappears, but its semantic value is re-encoded elsewhere.

Example:

```text
Z position
    ↓ lost geometrically
color saturation
    ↓ compensation channel
```

## INVALID

At least one protected invariant is destroyed or falls below its preservation threshold.

---

# 7. Compensation

A lost channel is not necessarily a lost meaning.

Suppose:

```text
x = longitude
y = latitude
z = altitude
```

When projecting into 2D:

```text
z geometry disappears
```

Possible compensation:

```text
altitude → color
altitude → point size
altitude → contour lines
altitude → opacity
altitude → animation
altitude → sonification
```

Compensation is valid only if the replacement channel remains perceptually distinguishable enough for the task.

Therefore a compensation record should include:

```yaml
source_dimension: altitude
source_channel: z_position
replacement_channel: color_luminance
semantic_preservation: 0.91
perceptual_confidence: 0.84
reason: 2D display constraint
```

---

# 8. Loss budget

Not every task requires the same fidelity.

Define:

```text
LossBudget = f(intent, audience, medium, task, risk)
```

Examples:

## Scientific inspection

```text
metric loss        very low tolerance
uncertainty loss   forbidden
topology loss      forbidden if structurally relevant
```

## Monitoring dashboard

```text
fine detail        moderate tolerance
state loss         forbidden
anomaly visibility forbidden
```

## Teaching diagram

```text
low-priority detail may be intentionally collapsed
causal structure should remain intact
```

## Executive summary

```text
high aggregation allowed
major direction and magnitude must survive
```

Loss is therefore not automatically a defect.

**Unacknowledged or intent-incompatible loss is the defect.**

---

# 9. Loss vector

A transform should expose a structured loss vector rather than only one scalar.

```yaml
loss:
  identity: 0.00
  topology: 0.02
  metric: 0.35
  order: 0.00
  magnitude: 0.04
  direction: 0.00
  uncertainty: 0.10
  temporal_resolution: 0.20
  hierarchy: 0.00
  context: 0.08
```

This tells the selector **what kind of truth is being sacrificed**.

---

# 10. Cognitive cost

Semantic fidelity alone is not enough.

A representation that preserves everything but overwhelms the observer may fail its purpose.

Diagrama therefore treats cognitive cost as a separate quantity:

```text
C = f(
  mark_count,
  channel_count,
  overlap,
  occlusion,
  interaction_depth,
  label_density,
  animation_rate,
  visual_entropy
)
```

Selection becomes a constrained optimization problem:

```text
maximize:
  task utility
  semantic fidelity
  perceptual discriminability

minimize:
  cognitive cost
  irrelevant detail
  semantic loss
```

subject to:

```text
protected invariants
medium constraints
accessibility constraints
loss budget
```

---

# 11. Loss-aware candidate scoring

A first conceptual score:

```text
Score(R) =
    α · TaskUtility
  + β · SemanticFidelity
  + γ · PerceptualClarity
  + δ · Explainability
  - λ · CognitiveCost
  - μ · SemanticLoss
```

The coefficients are context-dependent.

This formula is not intended as a permanent universal metric. It is a starting contract for experimentation.

---

# 12. Transform chain validation

Example:

```text
SIR
 ↓ cluster
clustered semantic view
 ↓ radialize
radial representation
 ↓ animate
animated radial representation
```

Do not estimate final fidelity by simply multiplying local transform scores.

Instead:

```text
V(original_SIR, final_representation)
```

must remain the authoritative check.

Intermediate transform metadata is still retained for explainability and debugging.

---

# 13. Reversibility

Every transform should declare whether it is:

```text
reversible
partially reversible
irreversible
```

Example:

```yaml
transform: aggregate_by_category
reversibility: partial
requires_source_ir: true
```

Diagrama should retain enough lineage metadata to answer:

```text
Where did this visible mark come from?
Which semantic entities were merged into it?
Which dimensions were removed?
Can I recover them from the SIR?
```

---

# 14. Explainable loss report

A human-readable report might look like:

```text
Representation: 2D Topology Map
Status: COMPENSATED
Semantic Fidelity: 0.93

Preserved
✓ entity identity
✓ connectivity
✓ causal direction
✓ category membership

Compressed
△ exact metric distance
△ temporal resolution

Compensated
↻ confidence → opacity
↻ depth → color luminance

Rejected alternatives
✗ Pie chart — destroys topology
✗ Bar chart — destroys relation direction

Reason
The observer intent is navigation. Connectivity is protected;
exact metric distance is secondary.
```

The engine must eventually be capable of generating this explanation automatically.

---

# 15. Core axiom

> **A projection is allowed to simplify information. It is never allowed to silently falsify its meaning.**

That is the purpose of Loss Validation.
