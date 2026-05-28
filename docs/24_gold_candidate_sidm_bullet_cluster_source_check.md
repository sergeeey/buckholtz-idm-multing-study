# Gold Candidate Source Check — SIDM / Bullet Cluster Constraint

**Date:** 2026-05-28  
**Status:** SOURCE_MISSING  
**Relevance classification:** cannot_assess_without_interaction_definition

---

## Purpose

Determine whether Self-Interacting Dark Matter (SIDM) and Bullet Cluster constraints are relevant to Buckholtz's "six isomers / five dark sectors" Isomeric Dark Matter (IDM) claim.

**Critical:** This is NOT a confirmation that Bullet Cluster refutes or validates IDM. This is a source check to determine IF the constraint is applicable.

---

## Background

### SIDM / Bullet Cluster Constraint (Standard Astrophysics)

**What it is:**
- Bullet Cluster (1E 0657-56) = two galaxy clusters post-collision
- X-ray observations (Chandra) show hot gas displaced from dark matter
- Weak lensing observations show dark matter peaks centered on galaxies (not gas)
- **Key result:** Dark matter is effectively collisionless (passed through itself without slowing)
- Constraint on self-interaction cross-section: σ/m < 1–2 cm²/g (68% CL, Randall+ 2008)

**Why it matters for dark sectors:**
- If dark sectors have self-interactions (dark photons, dark nuclear forces, etc.) → DM particles scatter off each other
- Strong self-interactions → dark matter would lag behind galaxies (like gas does)
- Bullet Cluster: dark matter did NOT lag → constrains σ/m
- Standard ΛCDM: σ/m ~ 0 (collisionless CDM) → consistent with Bullet Cluster
- SIDM models: σ/m ~ 0.1–1 cm²/g (velocity-dependent) → can be consistent if σ/m drops at high velocities

**Bullet Cluster velocity:** v_rel ~ 3000–4000 km/s (high-velocity collision)

**Key question:**
Does Buckholtz's IDM claim **six isomers with interactions between isomers** that would produce self-scattering?

If YES → Bullet Cluster constrains σ/m (potentially falsifying or requiring velocity dependence).  
If NO → Bullet Cluster is **not applicable** (dark isomers are effectively collisionless, like ΛCDM).

---

## Source Search Results

### Search Terms Used

Searched local `docs/` directory for:
- `SIDM`, `self-interacting`, `self interaction`
- `Bullet Cluster`, `cluster collision`, `1E 0657-56`
- `dark atom`, `dark photon`, `dark nuclear force`
- `SEA-DM` (Strongly Electromagnetically Active), `MEA-DM` (Marginally Electromagnetically Active)
- `cross-section`, `sigma/m`, `collisional`, `dissipative`
- `dark sector`, `isomer`, `multipole`, `dipole`, `quadrupole`

### Search Findings

| Term | Matches in Buckholtz materials? | Location | Context |
|------|-------------------------------|----------|---------|
| SIDM | ❌ NO | — | Only in 22_discovery_ledger.md where WE listed it as candidate |
| self-interacting / self interaction | ❌ NO | — | Not mentioned in Buckholtz materials |
| Bullet Cluster | ✅ YES | docs/05_data_anchoring_map.md | Listed as "Constraint" with "Low" leakage risk. Note: "Tests collisionless nature, not beta values" |
| 1E 0657-56 | ❌ NO | — | Specific cluster name not mentioned |
| dark atom | ❌ NO | — | Not mentioned |
| dark photon | ✅ YES | docs/23_gold_candidate_bbn_neff_source_check.md | Only in OUR question template ("do isomers contain dark photons?") — NOT in Buckholtz materials |
| SEA-DM / MEA-DM | ❌ NO | — | Not mentioned |
| cross-section / sigma/m | ❌ NO | — | Only in 22_discovery_ledger.md where WE mentioned it |
| collisional / dissipative | ❌ NO | — | Not discussed |
| dark sector | ✅ YES | docs/06_rosetta_stone.md | "Isomeric Dark Matter" → "Hidden sector / mirror-matter-like dark sector" (Medium match 5/10) |
| isomer | ✅ YES | Multiple docs | "6 isomers (5 dark, 1 ordinary)" mentioned as hypothesis |
| multipole / dipole / quadrupole | ✅ YES | Multiple docs | MULTING terms: monopole/dipole/quadrupole contributions to H(z) |

### Key Finding: Data Anchoring Map

From `docs/05_data_anchoring_map.md` (line 27):

```
| **Bullet Cluster** | Dark matter distribution | Chandra X-ray + optical | Constraint | Low | Tests collisionless nature, not beta values |
```

**Interpretation:**
- Bullet Cluster IS mentioned in repository materials
- Categorized as "Constraint" (external observational constraint)
- Leakage risk: **Low** (not used to fit beta values, safe to use as independent test)
- Purpose: "Tests collisionless nature, not beta values"

**Critical gap:** NO discussion of:
- Whether 6 isomers are collisionless or self-interacting
- What σ/m is predicted for IDM
- Whether dipole/quadrupole interactions are BETWEEN isomers (self-interaction) or WITH ordinary matter (cross-interaction)

---

### Key Finding: Rosetta Stone — Isomer Structure

From `docs/06_rosetta_stone.md`:

```
| **Six isomers (5 dark + 1 ordinary)** | Multiple dark sectors or flavors | Low | "Isomer" in particle physics usually means nuclear isomers. Here may mean: (1) multiple dark species, (2) different interaction channels, or (3) something novel. |
```

**Interpretation:**
- "Isomer" meaning is UNCLEAR
- Three possible interpretations:
  1. Multiple dark species (e.g., dark proton, dark electron — would have dark electromagnetic interactions)
  2. Different interaction channels (different forces, different couplings)
  3. Something novel (not standard particle physics)

**Critical gap:** Interpretation (1) → dark atoms with dark photons → SIDM. Interpretation (2) → depends on channels. Interpretation (3) → unknown.

---

### Key Finding: Multipole Interactions (Dipole/Quadrupole)

From `docs/22_discovery_ledger.md` (Finding 8):

```
MULTING's multipole interactions (dipole/quadrupole) may predict SIDM signature.
```

**From our own discovery ledger:**
- Dipole/quadrupole terms mentioned in H_MULT(z) formula
- Question: Do these terms represent interactions BETWEEN dark isomers (self-interaction) or contributions to cosmological expansion (modified gravity)?

**From `docs/09_meeting_brief.md`:**

```
**Issue:** Monopole, dipole, quadrupole terms mentioned but exact formulas unclear.

Questions:
2. How do dipole and quadrupole terms enter the Friedmann equations?
```

**Critical gap:**
- Dipole/quadrupole interpretation UNKNOWN
- IF dipole = repulsion between dark isomers → self-interaction → Bullet Cluster applies
- IF dipole = modified gravity term (like f(R), TeVeS) → NOT self-interaction → Bullet Cluster does NOT constrain dipole

**Analogy:**
- TeVeS (Bekenstein 2004) has "vector field" contributing to gravity (called "dipole-like" by some)
- BUT: TeVeS vector field is NOT dark matter self-interaction, it's modification of spacetime curvature
- Bullet Cluster does NOT constrain TeVeS dipole directly (though it constrains other TeVeS predictions)

**Resolution needed:** Ask Buckholtz: "Are dipole/quadrupole interactions BETWEEN dark matter particles (self-scattering) or contributions to the metric (modified gravity)?"

---

## Question-by-Question Assessment

| Question | Evidence from Buckholtz? | Source location | Status | Notes |
|----------|-------------------------|-----------------|--------|-------|
| Does Buckholtz define whether dark isomers self-interact? | ❌ NO discussion | — | **source_missing** | Interaction type not specified. |
| Does he distinguish SEA-DM and MEA-DM? | ❌ NO | — | **source_missing** | SEA-DM/MEA-DM terminology not used. |
| Does he claim only ~20% of dark matter is strongly/electromagnetically active? | ❌ NO | — | **source_missing** | Fraction breakdown not discussed. |
| Does he discuss Bullet Cluster or cluster collision constraints? | ⚠️ PARTIAL | docs/05_data_anchoring_map.md | **acknowledged_but_not_analyzed** | Bullet Cluster listed as constraint ("tests collisionless nature") but NO analysis of whether IDM passes this test. |
| Does he provide cross-section per mass σ/m? | ❌ NO | — | **source_missing** | σ/m not calculated or mentioned. |
| Does he explain why most dark matter remains effectively collisionless? | ❌ NO | — | **source_missing** | Collisionless vs collisional not discussed. |
| Does he discuss dark atoms, dark photons, or dissipative cooling? | ❌ NO | — | **source_missing** | Dark particle content not specified (same issue as BBN/N_eff check). |
| Does he compare with standard SIDM constraints? | ❌ NO | — | **source_missing** | SIDM literature not referenced. |
| Are dipole/quadrupole interactions BETWEEN isomers (self-scattering) or modified gravity? | ❌ NO clarification | docs/04_assumption_dependency_graph.md, 09_meeting_brief.md | **critical_ambiguity** | Dipole/quadrupole mentioned but physical interpretation unclear. |

---

## Relevance Classification

**Classification:** `cannot_assess_without_interaction_definition`

**Reasoning:**
- Bullet Cluster constraint applies to **self-interacting dark matter** (scattering between DM particles)
- Buckholtz materials do NOT specify:
  - Whether 6 isomers are collisionless (like ΛCDM) or self-interacting (like SIDM)
  - What "isomer" means in particle physics terms (dark atoms? different force carriers? flavor-like structure?)
  - Whether dipole/quadrupole are self-interactions or modified gravity contributions
  - What σ/m is predicted for IDM
- Bullet Cluster IS acknowledged in data anchoring map ("tests collisionless nature") but NO analysis of whether IDM is consistent

**Three possible interpretations:**

| Interpretation | Bullet Cluster relevance | Status |
|----------------|-------------------------|--------|
| **Isomers = dark atoms with dark EM** | HIGH (predicts σ/m > 0, testable) | Requires: dark photon coupling strength, dark fine structure constant |
| **Isomers = collisionless species with different masses** | LOW (σ/m ~ 0, like ΛCDM) | Bullet Cluster automatically satisfied, not a constraint |
| **Dipole = modified gravity (not self-interaction)** | MEDIUM (affects cluster dynamics differently) | Requires: functional form of dipole term at cluster scales |

**Cannot determine which interpretation without author clarification.**

---

## Partial Applicability Scenario

**IF Buckholtz confirms a TWO-COMPONENT structure:**

Some authors propose dark matter is MOSTLY collisionless (~80%) + small fraction self-interacting (~20%):
- Majority component: passes through Bullet Cluster (consistent with observations)
- Minority component: self-interacts, could explain small-scale structure anomalies (too-big-to-fail, core-cusp)

**Example:** Kaplan+ (2009, 2011) "Atomic Dark Matter" — dark protons + dark electrons bound by dark photons, but only small fraction of total DM

**Question for Buckholtz:**
> "Do all 6 isomers contribute equally to dark matter density, or is there a dominant collisionless component + subdominant self-interacting component?"

IF answer = "5 dark isomers are collisionless, only 1 is self-interacting" → Bullet Cluster constrains that 1 component, not all 5.

**Classification in this case:** `partially_applicable`

---

## Safe vs Unsafe Wording

### Safe Wording ✅

**When discussing with Buckholtz:**

> "Dr. Buckholtz, I am reviewing external constraints that may be relevant to IDM. Bullet Cluster observations (1E 0657-56) show that dark matter is effectively collisionless (self-interaction cross-section σ/m < 1–2 cm²/g at cluster collision velocities ~3000 km/s).  
>  
> Could you clarify:  
> (1) Are the 6 isomers collisionless (like standard CDM) or self-interacting (like SIDM)?  
> (2) If self-interacting: what is the predicted σ/m?  
> (3) Are the MULTING dipole/quadrupole terms interactions BETWEEN dark matter particles (self-scattering) or contributions to the gravitational potential (modified gravity)?  
>  
> This determines whether Bullet Cluster constraints apply to IDM."

**In technical write-ups:**

> "SIDM/Bullet Cluster constraints are potentially relevant if IDM's 6 isomers have self-interactions (dark photons, dark nuclear forces, or multipole scattering between isomers). Buckholtz does not specify whether isomers are collisionless or self-interacting in available materials. Dipole/quadrupole terms mentioned in MULTING may represent either (a) self-interactions between DM particles or (b) modified gravity contributions. Applicability cannot be determined without explicit interaction definition."

**In discovery ledger:**

> "Status: source_missing. Bullet Cluster constraint (σ/m < 1–2 cm²/g) applies to self-interacting dark matter. IDM mentions 6 isomers and dipole/quadrupole interactions, but does NOT specify: (1) whether isomers self-interact, (2) what σ/m is predicted, (3) whether dipole/quadrupole are DM-DM scattering or modified gravity. Bullet Cluster acknowledged in data anchoring map but not analyzed for IDM consistency. Cannot classify as applicable or not applicable without interaction definition from author."

---

### Unsafe Wording ❌ (DO NOT USE)

**Forbidden claims:**

❌ "Bullet Cluster disproves IDM."  
→ We do not know if IDM predicts self-interactions. Collisionless IDM would pass Bullet Cluster automatically.

❌ "Bullet Cluster validates IDM."  
→ Absence of SIDM discussion ≠ consistency with Bullet. No validation without explicit σ/m calculation.

❌ "6 isomers ruled out by Bullet Cluster."  
→ Only rules out if isomers have σ/m > 2 cm²/g at cluster velocities. Unknown.

❌ "IDM predicts σ/m = X."  
→ Model does not provide σ/m calculation. Cannot compute without knowing: (a) dark photon coupling, (b) dark particle masses, (c) whether dipole is self-interaction.

❌ "Dipole repulsion = self-interaction."  
→ Dipole may be modified gravity (not DM-DM scattering). Ambiguous.

❌ "Most dark matter is collisionless in IDM."  
→ Not stated. May be 100% collisionless, 100% self-interacting, or mixed. Unknown.

---

## Next Steps

### Priority 1: Ask Buckholtz (Recommended)

**Question for author:**

> "Are the 6 dark isomers collisionless (like standard CDM) or self-interacting (like SIDM)?  
>  
> If collisionless:  
> - Bullet Cluster constraint automatically satisfied (σ/m ~ 0).  
> - No further analysis needed for this constraint.  
>  
> If self-interacting:  
> - What is the predicted self-interaction cross-section σ/m (in cm²/g)?  
> - Is σ/m velocity-dependent (different at cluster scales ~3000 km/s vs galactic scales ~200 km/s)?  
> - Do all 6 isomers have the same σ/m, or is there a dominant collisionless component + subdominant self-interacting component?  
>  
> Additionally:  
> - Are the MULTING dipole/quadrupole terms interactions BETWEEN dark matter particles (DM-DM scattering) or contributions to spacetime curvature (modified gravity)?  
> - If DM-DM scattering: what is the cross-section? If modified gravity: does dipole affect cluster-scale dynamics (could mimic or interfere with SIDM signatures)?"

### Priority 2: Conditional Analysis Path

**IF Buckholtz confirms collisionless:**
- Bullet Cluster: NOT APPLICABLE (constraint irrelevant)
- Update ledger: `not_applicable` (isomers are collisionless, σ/m ~ 0)
- Archive finding, focus on other constraints

**IF Buckholtz confirms self-interacting:**
- Bullet Cluster: APPLICABLE (high-priority constraint)
- Upgrade ledger: `gold_candidate` → `copper_result` (after σ/m calculation)
- Calculate or request σ/m prediction
- Compare with Bullet Cluster limit (σ/m < 1–2 cm²/g at v ~ 3500 km/s)
- If σ/m > 2 cm²/g → IDM **falsified** by Bullet Cluster
- If σ/m < 1 cm²/g → IDM **consistent** with Bullet Cluster
- If 0.1 < σ/m < 1 cm²/g → IDM in **SIDM regime** (interesting, testable on multiple scales)

**IF Buckholtz confirms mixed (collisionless + self-interacting):**
- Bullet Cluster: PARTIALLY APPLICABLE (constrains self-interacting fraction only)
- Classification: `partially_applicable`
- Require: fraction of DM in self-interacting component + σ/m for that component
- Bullet Cluster constrains: f_SIDM × σ/m < threshold (effective cross-section)

### Priority 3: Dipole/Quadrupole Disambiguation

**Critical fork:**
- IF dipole/quadrupole = modified gravity (spacetime contribution) → Bullet Cluster does NOT directly constrain dipole
- IF dipole/quadrupole = self-interaction (DM-DM scattering force) → Bullet Cluster DOES constrain dipole

**Test:**
- Modified gravity: dipole contributes to H(z) at cosmological scales, may or may not affect cluster dynamics
- Self-interaction: dipole produces drag force between DM particles → affects collision dynamics → Bullet Cluster sensitive

**Request from Buckholtz:**
> "In MULTING, do dipole/quadrupole terms represent:  
> (A) Modified gravitational potential (like f(R) or TeVeS vector field), OR  
> (B) Forces between dark matter particles (self-scattering)?  
> This determines whether Bullet Cluster observations constrain dipole/quadrupole amplitudes."

---

## Comparison with BBN/N_eff Check

**Similar pattern:**

| Constraint | Applicability depends on | Status in Buckholtz materials | Classification |
|------------|-------------------------|------------------------------|----------------|
| BBN / N_eff | Whether isomers are thermally populated relativistic sectors | NO discussion of thermal history, particle content, T_dark/T_visible | `source_missing_constraint` |
| SIDM / Bullet Cluster | Whether isomers are self-interacting (σ/m > 0) | NO discussion of collisionless vs SIDM, no σ/m, dipole interpretation unclear | `source_missing_constraint` |

**Common issue:** Buckholtz defines IDM at HIGH LEVEL ("6 isomers", "multipole terms") but does NOT specify MICROPHYSICS (particle content, interactions, cross-sections, thermal history).

**Without microphysics:**
- Cannot compute N_eff (need: dark photons? dark neutrinos? temperature ratio?)
- Cannot compute σ/m (need: dark force strength? dark particle masses? interaction range?)
- Cannot determine constraint applicability

**Resolution:** Request microphysical specification from author.

---

## References

### SIDM Literature (for context, NOT for Buckholtz critique)

- Randall+ (2008), "Constraints on the Self-Interaction Cross-Section of Dark Matter from Numerical Simulations of the Merging Galaxy Cluster 1E 0657-56", ApJ 679, 1173
  - Bullet Cluster: σ/m < 1.25 cm²/g (68% CL, velocity-independent)
- Kaplan+ (2009), "Atomic Dark Matter", JCAP 05, 021
  - Dark atoms with dark photons → SIDM with σ/m ~ 0.1–1 cm²/g (velocity-dependent)
- Tulin & Yu (2018), "Dark Matter Self-interactions and Small Scale Structure", Phys. Rep. 730, 1
  - Review: SIDM can resolve small-scale CDM problems if 0.1 < σ/m < 10 cm²/g (velocity-dependent)
- Foot & Vagnozzi (2015), "Dissipative hidden sector dark matter", Phys. Rev. D 91, 023512
  - Mirror matter with dark EM → self-interactions + dissipative cooling

### Buckholtz Materials Searched

- `docs/05_data_anchoring_map.md` (Bullet Cluster mentioned, not analyzed)
- `docs/06_rosetta_stone.md` (isomer meaning unclear)
- `docs/09_meeting_brief.md` (dipole/quadrupole formulas missing)
- `docs/22_discovery_ledger.md` (Finding 8 = our speculation, not Buckholtz statement)
- `docs/23_gold_candidate_bbn_neff_source_check.md` (dark photon question template, not in Buckholtz materials)

**Result:** NO discussion of self-interactions, σ/m, SIDM, dark atoms, dark photons, collisionless vs collisional, or Bullet Cluster analysis.

---

## Summary

**SIDM/Bullet Cluster relevance to IDM: UNKNOWN**

**Reason:** Buckholtz does not specify whether 6 isomers are collisionless or self-interacting, does not provide σ/m, does not clarify whether dipole/quadrupole are DM-DM scattering or modified gravity.

**Bullet Cluster acknowledged:** Yes (listed in data anchoring map as constraint on "collisionless nature") but NO analysis of whether IDM passes this test.

**Action:** Mark as `source_missing_constraint` in discovery ledger (downgrade from `gold_candidate`, same as BBN/N_eff). Ask Buckholtz before investing time in σ/m calculations.

**Safe next step:** "Dr. Buckholtz, are the 6 dark isomers collisionless or self-interacting? If self-interacting, what is predicted σ/m? This determines whether Bullet Cluster constraints apply."

**Unsafe next step:** Calculating σ/m from "dipole/quadrupole" without knowing whether these are self-interactions or modified gravity → unjustified assumption.

---

**Classification:** `cannot_assess_without_interaction_definition`  
**Recommended ledger status:** Downgrade from `gold_candidate` to `source_missing_constraint`  
**Blocking question:** Are dark isomers collisionless or self-interacting? What is σ/m?  
**Critical ambiguity:** Are dipole/quadrupole DM-DM scattering (SIDM) or modified gravity (not SIDM)?  
**Unblocking answer:** Requires explicit interaction definition from Buckholtz or primary source citing σ/m or dark photon couplings.
