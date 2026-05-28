# MULTING Solar System Limit — Open Questions

**Purpose:** Track unanswered questions about MULTING behavior at Solar System scales.

**Status:** BLOCKED — awaiting author clarification (2026-05-28)

**Context:** MULTING includes dipole and quadrupole terms beyond Schwarzschild monopole. To assess compatibility with Solar System PPN constraints (Cassini light deflection, Mercury perihelion), we need explicit formulation of local weak-field limit.

---

## Question 1: Does MULTING Have a Metric?

**Question:** Is MULTING formulated as a metric theory (modifying g_μν), or as a Newtonian force correction?

**Why it matters:**
- **If metric theory:** PPN formalism applies directly → extract γ, β parameters
- **If Newtonian force:** Need alternative comparison (observed vs predicted accelerations)

**What we know:**
- Manuscript describes "monopole, dipole, quadrupole terms" (verbal description)
- No explicit metric or field equations provided
- H-MULT(z) is phenomenological fit (cosmological scale), not local metric

**What we need:**
- Weak-field metric: `g_μν = η_μν + h_μν` to O(GM/rc², v²/c²)
- OR: Statement that MULTING is Newtonian-level approximation (no metric modification)

**Status:** UNKNOWN — author clarification required

---

## Question 2: Do Dipole/Quadrupole Apply Locally?

**Question:** Are dipole and quadrupole terms active for ordinary Solar System matter (Sun, planets), or only for dark matter clusters?

**Why it matters:**
- **If local:** PPN constraints apply → must recover γ = 1, β = 1 within observational bounds
- **If cluster-only:** Solar System sees monopole (Schwarzschild) → no PPN conflict

**What we know:**
- r_d = beta_d × r_A where r_A = cluster radius ~ 1-10 Mpc
- r_d ~ 4.5-45 Mpc (cosmological scale)
- Solar System scale: R_sun ~ 7×10⁻¹⁴ Mpc (10¹⁴ times smaller than r_d)
- Manuscript does not discuss Solar System limit

**What we need:**
- Explicit statement: "Dipole term is negligible for r << r_d"
- OR: "Dipole applies to all matter (ordinary + dark)"
- OR: Scale-dependent coupling formula

**Status:** UNKNOWN — author clarification required

---

## Question 3: What is k_A for Ordinary Matter?

**Question:** Manuscript mentions "sub-object kinetic energy" k_A in dipole term description. What is k_A for the Sun? For Earth?

**Why it matters:**
- If dipole ~ k_A, need k_A values to compute local dipole contribution
- k_A = kinetic energy relative to WHAT frame? (Solar System COM? Galaxy COM? Cosmic rest frame?)
- Preferred frame (cosmic rest) would violate Local Lorentz Invariance → tight constraints

**What we know:**
- k_A appears in verbal description of dipole term
- No formula or values provided
- No COM frame specified

**What we need:**
- k_A(Sun), k_A(Earth) values OR formula
- COM frame definition
- Clarification: is k_A = (1/2) M v² (classical kinetic energy)?

**Status:** UNKNOWN — author clarification required

---

## Question 4: Does Dipole Vanish in COM Frame?

**Question:** Does the MULTING dipole term vanish when computed in the center-of-mass frame of the system?

**Why it matters:**
- **If vanishes in COM:** Dipole is frame-dependent artifact (similar to tidal effects) → may not affect local measurements
- **If nonzero in COM:** Physical dipole moment → contributes to PPN parameters

**What we know:**
- Dipole described as "related to sub-object COM motion"
- No explicit statement about COM frame behavior

**What we need:**
- Mathematical derivation showing dipole term in COM frame
- OR: Statement "dipole term is zero in system COM frame"

**Status:** UNKNOWN — author clarification required

---

## Question 5: Preferred Frame Effects?

**Question:** Does MULTING introduce velocity-dependent terms relative to a preferred cosmic rest frame?

**Why it matters:**
- Preferred frame violates Local Lorentz Invariance (LLI)
- PPN parameters α₁, α₂, α₃ measure preferred-frame effects
- Constraints VERY tight: α₁ < 10⁻⁴ (lunar laser ranging), |α₂| < 4×10⁻⁷ (CMB dipole)
- Typical alternative gravity theories with preferred frame are ruled out

**What we know:**
- Dipole term possibly velocity-dependent (if k_A ~ v²)
- No discussion of Lorentz invariance or preferred frame in manuscript

**What we need:**
- Statement: "MULTING is Lorentz-invariant" OR "There is a preferred cosmic rest frame"
- If preferred frame: derivation showing how α₁, α₂, α₃ constraints are satisfied

**Status:** UNKNOWN — author clarification required

---

## Question 6: Solar System PPN Recovery?

**Question:** Does MULTING recover γ = 1 and β = 1 (GR values) in the Solar System?

**Why it matters:**
- **Current constraints:**
  - γ - 1 = (2.1 ± 2.3) × 10⁻⁵ (Cassini)
  - β - 1 = (-4.1 ± 7.8) × 10⁻⁵ (Mercury)
- **If MULTING predicts different values:** Must fall within error bars OR be excluded

**What we know:**
- No Solar System analysis in manuscript
- No derivation of γ, β parameters

**What we need:**
- Explicit calculation: γ_MULTING, β_MULTING at Solar System scales
- OR: Statement "MULTING reduces to GR locally (γ = 1, β = 1)"
- OR: Section addressing Solar System constraints

**Status:** UNKNOWN — author clarification required

---

## Question 7: Scale Cutoff Mechanism?

**Question:** Does r_d = beta_d × r_A create a physical cutoff (dipole vanishes for r < r_d), or just a characteristic scale (dipole smoothly decreases)?

**Why it matters:**
- **If hard cutoff:** Solar System (r << r_d) unaffected → no PPN conflict
- **If smooth scaling:** Need functional form f(r/r_d) to compute local dipole strength

**What we know:**
- r_d ~ 4.5-45 Mpc (cosmological)
- Solar System r ~ 10⁻⁸ Mpc (much smaller)
- No cutoff function provided

**What we need:**
- Functional form: dipole(r) = f(r/r_d) × [monopole contribution]
- OR: Statement "dipole is zero for r < r_d"

**Status:** UNKNOWN — author clarification required

---

## Summary of Blockers

| Question | Blocker | Impact on PPN Check |
|----------|---------|---------------------|
| 1. Metric formulation | No weak-field metric provided | Cannot extract γ, β parameters |
| 2. Local applicability | Unclear if dipole applies to Solar System | Cannot determine if PPN constraints relevant |
| 3. k_A definition | No values or formula for ordinary matter | Cannot compute dipole contribution |
| 4. COM frame behavior | No statement about dipole in COM | Cannot assess frame-dependence |
| 5. Preferred frame | No Lorentz invariance discussion | Cannot rule out α₁, α₂, α₃ violations |
| 6. PPN recovery | No Solar System analysis | Cannot compare with Cassini/Mercury data |
| 7. Scale cutoff | No cutoff function provided | Cannot determine local dipole strength |

**All 7 questions BLOCK PPN assessment.**

---

## Interpretation Risk Matrix

| Interpretation | PPN Risk | Likelihood | Testability |
|----------------|----------|------------|-------------|
| Local mass dipole (Sun + planets) | HIGH (γ, β ≠ 1) | LOW (dipole of Solar System mass is small) | BLOCKED (no metric) |
| Kinetic energy dipole (galaxy frame) | HIGH (preferred frame → α₁ ≠ 0) | MEDIUM (matches "sub-object motion" description) | BLOCKED (no k_A, no frame) |
| Velocity-dependent term | HIGH (LLI violation → tight α constraints) | MEDIUM (if k_A ~ v²) | BLOCKED (no Lagrangian) |
| Metric modification (covariant) | MEDIUM (depends on coupling) | UNKNOWN (no metric) | BLOCKED (no metric) |
| Cluster-scale only (r < r_d cutoff) | NONE (PPN not applicable) | MEDIUM (matches r_d ~ Mpc scale) | BLOCKED (no cutoff function) |
| Phenomenological H(z) only | NONE (no local predictions) | LOW (manuscript discusses dipole physically) | N/A |

**Conclusion:** ALL interpretations either HIGH risk OR BLOCKED by missing information.

---

## Next Actions

**Priority 1:** Send author questions (docs/26) to obtain:
1. Weak-field metric OR statement of formulation type (metric vs Newtonian)
2. Solar System limit OR explicit scale cutoff
3. k_A definition for ordinary matter

**Priority 2:** After author response:
- If metric provided → extract γ, β → compare with Cassini/Mercury
- If cluster-only confirmed → mark PPN as NOT APPLICABLE
- If preferred frame confirmed → check α₁, α₂, α₃ constraints

**Priority 3:** Update discovery ledger with Finding 11 (PPN status)

---

**Status:** BLOCKED — all questions unanswered, no PPN check possible

**Last updated:** 2026-05-28
