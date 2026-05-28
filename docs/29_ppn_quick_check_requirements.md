# PPN Quick-Check Requirements

**Purpose:** Define what is needed to assess whether MULTING dipole/quadrupole terms survive Solar System PPN constraints.

**Status:** BLOCKED — insufficient source material to perform PPN check (2026-05-28)

**Conclusion:** PPN check is currently NOT POSSIBLE because MULTING framework lacks source-confirmed:
1. Weak-field metric or covariant field equations
2. Solar System / local weak-field limit
3. Explicit Lagrangian or action functional
4. Definition of k_A (kinetic energy scale) for ordinary matter

---

## What PPN Checks

**Parametrized Post-Newtonian (PPN) formalism** tests weak-field, slow-motion deviations from GR.

**PPN parameters (primary):**
- **γ** — space curvature from unit rest mass (light deflection)
- **β** — nonlinearity in superposition of gravitational potentials (perihelion precession)

**GR predictions:** γ = 1, β = 1

**Observational constraints (Solar System):**
- γ - 1 = (2.1 ± 2.3) × 10⁻⁵ (Cassini light deflection)
- β - 1 = (-4.1 ± 7.8) × 10⁻⁵ (Mercury perihelion shift)

**PPN applicability:** Theories with:
- Weak-field metric (g_μν = η_μν + h_μν, |h| << 1)
- Slow motion (v << c)
- Local measurement (not cosmological scales)
- Conservative field (no dissipation)

---

## What We Have From MULTING

### Available information
1. **H-MULT(z) parameterization** — phenomenological fit to cosmological H(z) observations
   - Beta_d = 4.5, beta_q = 18.0 (fitted, not derived)
   - Formula not provided (BLOCKED: Finding 3, Conflict 3)

2. **Verbal description** — "monopole, dipole, quadrupole terms"
   - No explicit metric or field equations
   - No Lagrangian or action
   - No stress-energy coupling specified

3. **Scale parameters** — r_d = beta_d × r_A, r_q = beta_q × r_A
   - r_A = cluster radius (typical value: 1-10 Mpc)
   - r_d ~ 4.5-45 Mpc, r_q ~ 18-180 Mpc
   - Cosmological scales, NOT Solar System scales (R_sun ~ 7×10⁻¹⁴ Mpc)

4. **Physical interpretation (from manuscript text, unclear):**
   - Dipole: "related to sub-object COM motion" OR "mass distribution asymmetry" OR "kinetic energy term"
   - Quadrupole: "quadrupole moment" OR "higher-order mass distribution"
   - No definition of "sub-object" for ordinary matter (Sun, Earth)

### Missing information (BLOCKERS)
1. **Weak-field metric** — g_μν(x) for MULTING
2. **Field equations** — how T_μν sources h_μν
3. **Solar System limit** — what happens when r << r_d?
4. **Lagrangian** — needed to derive equations of motion + PPN parameters
5. **k_A definition** — kinetic energy scale parameter (appears in dipole term description)
6. **Preferred frame** — is there a preferred cosmic rest frame for dipole term?
7. **Local cutoff** — does dipole vanish for r << r_d or scale down smoothly?

---

## Interpretation Branches (NOT CLAIMS — QUESTIONS)

### Branch 1: Local Mass Dipole → High PPN Risk
**If** dipole term = mass distribution dipole moment of local system (Sun + planets):
- **Then:** PPN γ and β likely deviate from GR significantly (multipole moments contribute to metric)
- **Expected:** γ - 1 ~ O(1), β - 1 ~ O(1) (NOT consistent with Cassini/Mercury data)
- **Block:** Dipole for Solar System mass distribution is SMALL (Sun dominates, planets ~ 0.1% mass, Jupiter dominates planets)
- **Counter:** If MULTING dipole is cluster-scale effect, may not apply locally
- **Author question:** Does MULTING dipole term activate for ordinary Solar System matter?

### Branch 2: Kinetic Energy Dipole → Requires k_A + COM Frame
**If** dipole term = kinetic energy relative to COM:
- **Then:** Need k_A (kinetic energy scale) for Sun + Earth
- **Expected:** k_A ~ (1/2) M v² where v = orbital velocity ~ 30 km/s (Earth), ~220 km/s (Sun around galaxy)
- **COM frame:** Whose COM? Solar System COM? Galaxy COM? Cosmic rest frame?
- **PPN risk:** If galaxy COM, introduces preferred frame (violates weak equivalence principle → PPN α₁, α₂ ≠ 0)
- **Author questions:**
  - What is k_A for the Sun?
  - Does dipole vanish in COM frame of the system?
  - Is there a preferred cosmic rest frame?

### Branch 3: Velocity-Dependent Term → Preferred Frame Risk
**If** dipole term depends on velocity relative to cosmic rest frame:
- **Then:** Violates Local Lorentz Invariance (LLI)
- **PPN parameters:** α₁, α₂, α₃ ≠ 0 (preferred-frame effects)
- **Constraints:** Very tight (e.g., α₁ < 10⁻⁴ from lunar laser ranging)
- **Expected:** MULTING likely excluded if this interpretation correct
- **Counter:** If dipole is covariant (scalar built from T_μν), may avoid preferred frame
- **Author question:** Is MULTING dipole term Lorentz-invariant or frame-dependent?

### Branch 4: Metric Modification → Need Weak-Field Expansion
**If** MULTING modifies metric (g_μν ≠ Schwarzschild at Solar System scales):
- **Then:** Need explicit h_μν(x) to extract PPN parameters
- **Standard procedure:** Expand metric to O(v²/c², GM/rc²), match to PPN form
- **BLOCKED:** No metric provided in manuscript
- **Author question:** Does MULTING have a weak-field metric, or is it a Newtonian-style force correction?

### Branch 5: Cluster/Cosmological Scale Only → PPN May Not Apply
**If** dipole/quadrupole activate only at r ~ r_d ~ Mpc scales:
- **Then:** Solar System (r ~ AU ~ 10⁻⁸ Mpc) may see monopole (Schwarzschild) only
- **Expected:** γ = 1, β = 1 locally (GR recovered)
- **Requires:** Explicit cutoff mechanism or scale-dependent coupling
- **Author question:** Does r_d = beta_d × r_A create a physical cutoff below which dipole vanishes?

### Branch 6: Phenomenological H(z) Correction → Not Enough for PPN
**If** MULTING is purely a phenomenological H(z) fit (no local metric modification):
- **Then:** PPN check does not apply (different physical regime)
- **Expected:** No conflict with Solar System tests (no local predictions)
- **But:** Cannot claim to be modified gravity theory (just parameterized expansion history)
- **Author question:** Is MULTING a metric theory or a phenomenological H(z) parameterization?

---

## Prerequisites for PPN Check

**Before performing PPN analysis, need AT LEAST ONE of:**

1. **Weak-field metric:**
   ```
   ds² = -(1 + 2Φ/c²) c²dt² + (1 - 2γΦ/c²) dx²
   ```
   where Φ = monopole + dipole + quadrupole contributions.
   - Extract γ, β from metric coefficients.

2. **Lagrangian + field equations:**
   ```
   L = L_GR + L_dipole + L_quadrupole
   ```
   - Derive equations of motion → extract PPN parameters.

3. **Solar System limit explicitly worked out:**
   - Paper section: "When applied to Solar System, MULTING reduces to..."
   - Comparison with Cassini γ and Mercury β constraints.

4. **Definition of k_A for ordinary matter:**
   - k_A(Sun), k_A(Earth), k_A(Mercury) values or formula.
   - COM frame specification.

5. **Explicit statement about local applicability:**
   - "Dipole/quadrupole terms are negligible for r << r_d."
   - OR: "MULTING applies only at cluster/cosmological scales."

**Current status:** NONE of the above are available in manuscript. **PPN check BLOCKED.**

---

## Safe vs Unsafe Wordings

### ✅ Safe (honest about blockers)
- "PPN check is currently not possible because MULTING lacks a weak-field metric."
- "Without knowing k_A or the Solar System limit, we cannot assess PPN compatibility."
- "If dipole term is a local mass distribution effect, PPN constraints likely apply; if cluster-scale only, may not."
- "Author clarification needed on: weak-field metric, k_A definition, Solar System limit, preferred frame."

### ❌ Unsafe (overclaiming or premature refutation)
- "MULTING is ruled out by PPN constraints." (NO — no local predictions available to test)
- "PPN parameters show MULTING is inconsistent with GR." (NO — no PPN parameters derived)
- "Solar System tests falsify MULTING." (NO — no Solar System predictions made)
- "MULTING passes PPN checks." (NO — no checks performed)
- "Dipole term creates preferred frame." (MAYBE — depends on k_A + COM frame definition, not confirmed)

---

## Author Questions (Priority 2 — after H-MULT formula)

**To Dr. Buckholtz:**

> Dr. Buckholtz,
>
> We are attempting to understand whether MULTING dipole/quadrupole terms are consistent with Solar System tests (PPN constraints on γ and β parameters). To assess this, we need clarification on several points:
>
> **1. Metric formulation:**
> - Does MULTING have a weak-field metric (g_μν = η_μν + h_μν), or is it formulated as a Newtonian-style force correction?
> - If metric: could you provide the weak-field expansion to O(GM/rc², v²/c²)?
>
> **2. Local applicability:**
> - Do dipole/quadrupole terms apply to ordinary matter (Sun, planets) or only to dark matter clusters?
> - Is there a scale cutoff (e.g., dipole vanishes for r << r_d)?
>
> **3. Kinetic energy parameter k_A:**
> - What is k_A for the Sun? For Earth?
> - Is k_A = (1/2) M v² where v is orbital velocity, or something else?
>
> **4. Center-of-mass frame:**
> - Does the dipole term vanish in the center-of-mass frame of the system?
> - Is there a preferred cosmic rest frame, or is MULTING Lorentz-invariant?
>
> **5. Solar System limit:**
> - Does MULTING recover γ = 1 and β_PPN = 1 (GR values) in the Solar System?
> - Is there a section in your work addressing Solar System constraints (Cassini, Mercury perihelion)?
>
> **6. Preferred frame effects:**
> - Does MULTING introduce velocity-dependent terms relative to a cosmic rest frame?
> - If so, how does it avoid conflict with Local Lorentz Invariance tests (α₁, α₂, α₃ constraints)?
>
> Any guidance on where to find this information (manuscript section, supplementary notes, or other references) would be greatly helpful for our reproducibility audit.
>
> Thank you,
> [Your name]

---

## Next Steps (After Author Response)

**If metric + Solar System limit provided:**
1. Extract PPN parameters γ, β from metric
2. Compare with observational bounds
3. Document in docs/30_multing_solar_system_limit_questions.md
4. Update discovery ledger (Finding 11)

**If cluster-scale-only confirmed:**
1. Mark PPN check as NOT APPLICABLE
2. Document scope limitation (cosmological scales only)
3. No conflict with Solar System tests (different regime)

**If preferred frame confirmed:**
1. Check α₁, α₂, α₃ constraints (much tighter than γ, β)
2. Likely BLOCKED by lunar laser ranging / CMB dipole tests

**If Newtonian force correction (no metric):**
1. PPN formalism may not apply directly
2. Alternative: compare with observed Solar System accelerations
3. Requires explicit force law F(r) for dipole/quadrupole

---

**Summary:** PPN check is on hold until author provides:
- Weak-field metric OR explicit Solar System limit
- k_A definition for ordinary matter
- COM frame / preferred frame clarification

**No claims of refutation or validation can be made without this information.**

**Status:** docs/26_author_clarification_brief.md updated with PPN questions (Priority 2).

**Last updated:** 2026-05-28
