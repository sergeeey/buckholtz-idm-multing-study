# Literature Bridge Map — Support for Hamiltonian H²(a) Derivation

**Date:** 2026-05-29  
**Purpose:** Map existing cosmology literature to MULTING Hamiltonian bridge derivation  
**Status:** BACKGROUND_SUPPORT (not direct proof)

---

## Executive Summary

**Claim under review:** Can pairwise MULTING potentials V(D) → cosmological H²(a)?

**Literature support strength:**

| Framework | Support | Strength | Caveat |
|-----------|---------|----------|--------|
| **Layzer-Irvine equation** | Energy conservation in expanding universe | STRONG | Applies to N-body, not single pair |
| **Lattice universe models** | Discrete → continuum averaging | PARTIAL | Requires homogeneity assumption |
| **Wigner-Seitz cell** | Pair → cell → background | PARTIAL | Valid only for periodic lattices |
| **Buchert averaging** | Inhomogeneity ↔ effective H² | BACKGROUND_ONLY | Does not endorse arbitrary potentials |

**Overall verdict:** PARTIAL_SUPPORT — frameworks exist for pair → background mapping, but MULTING-specific potentials NOT directly proven.

---

## 1. Layzer-Irvine Equation

### What It Says

**Original context:** Energy conservation in Newtonian cosmology for N-body system

**Equation:**
```
dE/dt = ∑ᵢⱼ F_ij · v_ij

where E = K + U (kinetic + potential)
```

**For expanding universe:**
```
d/dt (K + U) = −3H(K + ⅓U)
```

**Virial form:**
```
2K + U = constant × a³
```

### Connection to MULTING

**MULTING uses:**
```
E = (1/2) μ Ḋ² + V_MULT(D)

where V_MULT = V_m + V_d + V_q
```

**Layzer-Irvine supports:**
- ✅ Energy conservation framework valid
- ✅ Kinetic + potential decomposition standard
- ✅ Expansion → energy redistribution

**Layzer-Irvine does NOT support:**
- ❌ Arbitrary potential V(D) → H²(a) without averaging
- ❌ Single pair generalization to background
- ❌ Specific MULTING multipole terms (dipole, quadrupole)

**Strength:** STRONG for framework, WEAK for specific potentials

---

## 2. Lattice Universe Models

### What They Say

**Historical context:** Zel'dovich, Irvine, Shandarin (1970s-1980s)

**Core idea:** Approximate real cluster distribution as periodic lattice → derive effective H²(a)

**Method:**
1. Place masses on lattice (cubic, BCC, FCC)
2. Compute pairwise forces
3. Average over Wigner-Seitz cell
4. Derive effective Friedmann equation

**Result:**
```
H²_eff(a) = H²_FLRW + correction terms

where corrections depend on lattice geometry
```

### Connection to MULTING

**MULTING assumes:**
- Inter-cluster interactions follow V_MULT(D)
- D = a(t) D₀ (comoving)
- Averaging over pairs → H²(a)

**Lattice models support:**
- ✅ Discrete → continuum averaging framework exists
- ✅ Pair interactions → effective H² possible
- ✅ Corrections to FLRW from structure

**Lattice models do NOT support:**
- ❌ Real clusters are NOT on periodic lattice
- ❌ Dipole and quadrupole terms (standard models use monopole only)
- ❌ Specific β_d, β_q parameter choices

**Strength:** PARTIAL — framework applicable, specific potentials unverified

---

## 3. Wigner-Seitz Cell Approximation

### What It Says

**Solid-state physics analog:** Approximate crystal by Wigner-Seitz cell around one atom

**Cosmology adaptation:**
1. Choose representative cluster pair
2. Define cell boundary (Voronoi tessellation)
3. Assume cell dynamics → background dynamics

**Key assumption:** Periodic boundary conditions + homogeneity

### Connection to MULTING

**MULTING single-pair approach:**
```
E = (1/2) μ Ḋ² + V_MULT(D) → H²(a)
```

**Wigner-Seitz supports:**
- ✅ Pair interaction → cell dynamics → background
- ✅ Comoving distance D = a(t) D₀ natural in cell picture
- ✅ Energy conservation per cell

**Wigner-Seitz does NOT support:**
- ❌ Cells must be PERIODIC (real universe not periodic)
- ❌ Edge effects neglected (boundary conditions matter)
- ❌ Homogeneity required (real distribution lumpy)

**Strength:** PARTIAL — valid for idealized periodic lattice, questionable for real universe

---

## 4. Buchert Averaging Framework

### What It Says

**Modern context:** Thomas Buchert (2000s), inhomogeneity and backreaction

**Core idea:** Averaging Einstein equations ≠ Einstein equations of averaged quantities

**Effective Friedmann equations:**
```
3H²_eff = 8πG⟨ρ⟩ − ½⟨R⟩ + Q

where Q = backreaction term (inhomogeneity)
```

**Key result:** Inhomogeneous structure → effective dark energy-like term

### Connection to MULTING

**MULTING effective H²:**
```
H²(a) = H₀² [Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]
```

**Buchert supports:**
- ✅ Inhomogeneity can modify effective H²
- ✅ Structure → effective acceleration possible
- ✅ Non-standard H²(a) forms allowed

**Buchert does NOT support:**
- ❌ Specific a⁻⁴, a⁻⁵ terms (Buchert uses different expansion)
- ❌ Pairwise potentials → effective H² (Buchert uses metric averaging)
- ❌ MULTING force law (Buchert uses GR, not modified gravity)

**Strength:** BACKGROUND_ONLY — framework for structure effects, not MULTING-specific

---

## 5. Virial Theorem Cosmology

### What It Says

**Classical mechanics:** For bound system under gravity

```
2⟨K⟩ + ⟨U⟩ = 0  (time-averaged)
```

**Cosmology extension:** Cluster dynamics in expanding universe

**Connection to H(z):**
```
⟨v²⟩ ∝ ⟨M/R⟩ → constraints on H(z) via cluster observations
```

### Connection to MULTING

**MULTING energy:**
```
E = (1/2) μ Ḋ² + V_MULT(D)
```

**Virial theorem supports:**
- ✅ Energy balance framework applicable
- ✅ Cluster velocity dispersion → H(z) connection exists
- ✅ Potential energy → expansion rate link

**Virial theorem does NOT support:**
- ❌ Specific MULTING potential forms (V_d, V_q)
- ❌ Single pair → virial (virial requires ensemble average)
- ❌ Dipole and quadrupole forces (standard virial uses monopole)

**Strength:** PARTIAL — framework applicable, specific forces unverified

---

## 6. N-Body Cosmology Simulations

### What They Say

**Standard practice:** Millennium, Illustris, EAGLE simulations

**Method:**
1. Place dark matter particles
2. Compute pairwise Newtonian forces
3. Evolve N-body system
4. Extract effective H(z) from expansion

**Result:** Effective H(z) ≈ H_ΛCDM + small corrections (<1%)

### Connection to MULTING

**MULTING claims:** Modified pairwise forces → different H(z)

**N-body simulations support:**
- ✅ Pairwise forces → effective H(z) (principle validated)
- ✅ Numerical method for pair → background
- ✅ Framework exists for testing MULTING

**N-body simulations do NOT support:**
- ❌ MULTING forces not implemented in standard codes
- ❌ Dipole and quadrupole forces not tested
- ❌ Would require custom simulation (NOT done yet)

**Strength:** BACKGROUND_ONLY — framework exists, MULTING implementation missing

---

## 7. Summary Table

| Claim | Literature Support | Strength | Caveat |
|-------|-------------------|----------|--------|
| "Pairwise forces → H²(a)" | Layzer-Irvine, N-body sims | STRONG | Framework validated, MULTING-specific NOT |
| "Single pair → background" | Wigner-Seitz cell, lattice models | PARTIAL | Requires periodic lattice, homogeneity |
| "Energy conservation E → H²" | Standard cosmology textbooks | STRONG | Uncontroversial principle |
| "V_MULT → H² derivation" | No direct precedent | WEAK | Analogy to Layzer-Irvine, not proven |
| "Dipole force → a⁻⁴ term" | No direct precedent | WEAK | Our derivation, not in literature |
| "Quadrupole force → a⁻⁵ term" | No direct precedent | WEAK | Our derivation, not in literature |
| "Multipole cosmology valid" | Some modified gravity models | BACKGROUND_ONLY | Not MULTING-specific |

---

## 8. Literature Gaps

### What IS in Literature
✅ Energy conservation in expanding universe (Layzer-Irvine)  
✅ Discrete → continuum averaging (lattice universe)  
✅ Pair → cell → background (Wigner-Seitz)  
✅ Inhomogeneity → effective H² (Buchert)  
✅ N-body → effective cosmology (simulations)  

### What is NOT in Literature
❌ MULTING-specific dipole force → a⁻⁴ term  
❌ MULTING-specific quadrupole force → a⁻⁵ term  
❌ Verification that V_MULT → H² averaging is valid  
❌ N-body simulation with MULTING forces  
❌ Mean-field theory for MULTING potentials  
❌ Field-theoretic derivation of MULTING Friedmann equations  

---

## 9. Verdict by Claim

### Claim 1: "Layzer-Irvine supports arbitrary MULTING pair potentials"

**Status:** ⚠️ **PARTIAL_SUPPORT**

**What Layzer-Irvine provides:**
- Energy conservation framework (K + U) for N-body cosmology
- Connection between virial theorem and H(t)

**What Layzer-Irvine does NOT provide:**
- Authorization for arbitrary V(D) forms
- Single pair → background generalization
- Dipole and quadrupole force treatment

**Correct statement:** "Layzer-Irvine provides the energy conservation framework used in MULTING derivation, but does not directly validate MULTING-specific potentials."

---

### Claim 2: "Lattice universe models support MULTING bridge"

**Status:** ⚠️ **PARTIAL_SUPPORT**

**What lattice models provide:**
- Proof-of-concept for discrete → continuum averaging
- Pair interaction → effective H²(a) framework

**What lattice models do NOT provide:**
- Real clusters are NOT on periodic lattice
- Standard lattice models use monopole only (no dipole/quadrupole)
- Homogeneity assumption questionable

**Correct statement:** "Lattice universe models provide a framework for pair → background averaging, but MULTING requires non-standard multipole forces and real cluster distribution is not lattice-like."

---

### Claim 3: "Wigner-Seitz cell justifies single-pair approach"

**Status:** ⚠️ **PARTIAL_SUPPORT**

**What Wigner-Seitz provides:**
- Representative cell → background connection
- Periodic boundary conditions eliminate edge effects

**What Wigner-Seitz does NOT provide:**
- Real universe is NOT periodic
- Cell boundaries in real universe arbitrary (not Voronoi)
- Homogeneity required (violated by large-scale structure)

**Correct statement:** "Wigner-Seitz cell approximation provides a conceptual bridge for pair → background, but requires periodic lattice and homogeneity, both violated in real universe."

---

### Claim 4: "Buchert backreaction supports a⁻⁴, a⁻⁵ terms"

**Status:** ❌ **OVERSTATED**

**What Buchert provides:**
- Framework for inhomogeneity effects on H²
- Effective dark energy from structure

**What Buchert does NOT provide:**
- Specific a⁻⁴, a⁻⁵ terms (Buchert uses different expansion)
- Pairwise potential approach (Buchert uses metric averaging)
- MULTING force law validation

**Correct statement:** "Buchert framework shows that inhomogeneity can modify effective H², but does not specifically support MULTING's a⁻⁴, a⁻⁵ terms."

---

## 10. Recommended Wording

### ✅ Safe Claims

"The Hamiltonian bridge uses energy conservation (Layzer-Irvine framework) and discrete-to-continuum averaging (lattice universe analogy) to map pairwise MULTING potentials to an effective H²(a). This approach has conceptual support in cosmology literature, but MULTING-specific multipole terms (dipole → a⁻⁴, quadrupole → a⁻⁵) have not been independently validated."

### ⚠️ Cautious Claims

"Lattice universe models and Wigner-Seitz cell approximation provide partial support for the pair → background leap, but require periodic lattice and homogeneity assumptions that may not hold in the real universe."

### ❌ Avoid

- "Layzer-Irvine directly proves MULTING is correct"
- "Lattice models confirm the Hamiltonian bridge"
- "Buchert framework validates a⁻⁴ and a⁻⁵ terms"
- "Literature fully supports MULTING bridge"

---

## References

**Key papers (conceptual support, not MULTING-specific):**

1. **Layzer, D. (1963)** — "On the energy equation for cosmological models"  
   *Astrophysical Journal* — Energy conservation in Newtonian cosmology

2. **Irvine, W.M. (1961)** — "Local irregularities in a universe satisfying the cosmological principle"  
   *Annals of Physics* — Virial theorem in expanding universe

3. **Zel'dovich, Y.B. (1970)** — "Gravitational instability: An approximate theory for large density perturbations"  
   *Astronomy & Astrophysics* — Lattice universe approximation

4. **Buchert, T. (2000)** — "On average properties of inhomogeneous fluids in general relativity"  
   *General Relativity and Gravitation* — Backreaction framework

5. **Wiegand, A. & Buchert, T. (2010)** — "Multiscale cosmology and structure-emerging Dark Energy"  
   *Physical Review D* — Effective dark energy from structure

**Note:** None of these papers discuss MULTING or validate MULTING-specific potentials.

---

**Status:** LITERATURE MAP COMPLETE

**Verdict:** Literature provides PARTIAL_SUPPORT for framework (energy conservation, discrete → continuum averaging), but MULTING-specific dipole/quadrupole terms NOT validated in existing literature.

**Recommendation:** Present Hamiltonian bridge as "conceptually supported by Layzer-Irvine and lattice universe frameworks" but NOT as "proven by literature."

**Next step:** Independent verification (docs/48) must check if framework application to MULTING is algebraically valid, even if not literature-proven.
