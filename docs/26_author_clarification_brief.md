# Author Clarification Brief — Dr. Thomas J. Buckholtz

**Date:** 2026-05-28  
**Status:** Ready for review before sending  
**Purpose:** Source-grounding questions for reproducibility audit

---

## 1. Purpose

Dr. Buckholtz,

I am building a small reproducibility and epistemic-audit layer for selected parts of your IDM/MULTING work. My goal is **not** to validate or challenge the model, but to **separate definitions from predictions** and ensure I am representing your work accurately.

I have reached a stage where further progress requires clarification from you on several points. I am trying to make my audit **source-grounded** before doing any modeling or numerical calculations.

---

## 2. What I Have Already Verified

From manual verification of manuscript `preprints202511.0598.v6.pdf`, Appendix A.3, Table A1:

✅ **Beta values:**
- beta_d = 4.5
- beta_q = 18.0

✅ **Context:**
- These values were selected by an AI-assisted online service to minimize standard deviations from observed H(z)
- They are **fitted phenomenological parameters**, not derived theoretical constants
- I am treating them as **fit-reproduction parameters** (I can reproduce the Table A1 fit after receiving the formula), **not** as theoretical predictions (I will not claim they "predict" H(z) since they were fitted to it)

This distinction is important to avoid circular reasoning in my audit.

---

## 3. Questions — H-MULT Fit Reproduction

To reproduce the Table A1 H-MULT column and compare with H-FLRW, I need:

### Q1: H-MULT Functional Form

**Question:**
> Could you provide the explicit functional form for H_MULT(z; beta_d, beta_q)?

**Context:**
- The manuscript mentions monopole, dipole, and quadrupole terms
- I have not found the exact combination formula (e.g., H_MULT = H_monopole + beta_d × H_dipole(z) + beta_q × H_quadrupole(z), or a different form)
- I need this to implement a solver and reproduce Table A1

**Example of what would help:**
- Explicit equation with z-dependence
- OR reference to equation number in a prior publication
- OR explicit statement if the formula is proprietary or still being finalized

---

### Q2: H(z) Dataset

**Question:**
> Which observed H(z) dataset was used in Table A1?

**Options:**
- Cosmic chronometers (galaxy ages) — which compilation? (Moresco+ 2012? 2016? 2022?)
- Pantheon+ SNIa H(z) measurements
- BAO measurements
- Combination of datasets
- Custom dataset

**Why this matters:**
- To reproduce the fit, I need the same input data
- To avoid circular reasoning, I need to document: "beta values fitted to dataset X → cannot claim to predict dataset X"

---

### Q3: sigma_MULT Definition

**Question:**
> How is sigma_MULT (the fit quality metric in Table A1) defined?

**Possibilities:**
- Number of standard deviations: |H_MULT(z) - H_obs(z)| / σ_obs
- Chi-squared contribution: ((H_MULT - H_obs) / σ_obs)²
- Cumulative metric across all redshift bins
- Something else

**Why this matters:**
- To verify fit quality claims
- To compare H-MULT fit quality with H-FLRW (ΛCDM) fit quality on the same dataset

---

### Q4: AI-Estimated vs Fixed Quantities

**Question:**
> In Appendix A.3, the manuscript mentions that the online AI service estimated m_A, r_A, k_A, D_C:AB, and selected beta_d and beta_q.
> 
> Which of these quantities were:
> (A) Estimated by the AI (free parameters in the fit)?
> (B) Fixed by you (input constraints to the AI)?

**Why this matters:**
- Counting free parameters (more free parameters = easier to fit any dataset → lower evidential value)
- Understanding which quantities are theoretically predicted vs phenomenologically fitted

---

## 4. Questions — IDM Microphysics (External Constraints)

I am reviewing three independent observational constraints that **may** be relevant to IDM:
1. Big Bang Nucleosynthesis (BBN) and effective neutrino species (N_eff)
2. Self-Interacting Dark Matter (SIDM) and Bullet Cluster observations
3. Gaia stellar kinematics and dark disk constraints

To determine whether these constraints apply, I need clarification on the **microphysical structure** of the 6 dark isomers.

**Important:** I am **not** claiming these constraints refute or validate IDM. I am trying to determine **whether they are applicable** to your model. If they are not applicable (e.g., because dark isomers do not have the relevant properties), I will document that and move on.

---

### Q5: Thermal History (BBN / N_eff)

**Question:**
> Do the 5 dark isomers contain thermally populated relativistic particles (e.g., dark photons, dark neutrinos) at early times (temperature T ~ MeV, BBN epoch)?

**If yes:**
- What is the dark-sector temperature ratio T_dark / T_visible?
- Does the model predict the effective number of neutrino species (N_eff)?
- Current observational constraint: Planck 2018 + BBN gives N_eff = 2.99 ± 0.17

**If no (dark sectors are cold or decoupled at BBN):**
- BBN/N_eff constraints do not apply → I will document this and archive that constraint

**Why this matters:**
- BBN is the gold-standard early-universe constraint
- IF dark isomers are thermally populated → BBN constrains their particle content
- IF dark isomers are cold/non-relativistic → BBN is irrelevant

---

### Q6: Self-Interactions (SIDM / Bullet Cluster)

**Question:**
> Are the 6 dark isomers collisionless (self-interaction cross-section σ/m ~ 0, like standard CDM) or self-interacting (σ/m > 0, like SIDM)?

**If self-interacting:**
- What is the predicted self-interaction cross-section σ/m (in cm²/g)?
- Is σ/m velocity-dependent?
- Current observational constraint: Bullet Cluster (1E 0657-56) gives σ/m < 1–2 cm²/g at cluster collision velocities (~3500 km/s)

**If collisionless:**
- Bullet Cluster constraint automatically satisfied → I will document this

**Additional question:**
> Are the MULTING dipole/quadrupole terms interactions **between dark matter particles** (DM-DM scattering forces) or contributions to **spacetime curvature** (modified gravity, like f(R) or TeVeS vector fields)?

**Why this matters:**
- IF dipole = DM-DM scattering → Bullet Cluster constrains dipole amplitude
- IF dipole = modified gravity → Bullet Cluster does not directly constrain dipole (different physics)

---

### Q7: Scale Range and Dissipative Processes (Gaia / Dark Disk)

**Question:**
> At what physical scales do the MULTING dipole/quadrupole terms operate?

**Options:**
- (A) Cosmological scales only (Mpc–Gpc, affects H(z) expansion but not local dark matter distribution)
- (B) All scales including galactic (kpc, affects local dark matter density and vertical profile)
- (C) Scale-dependent with a cutoff (strong at Mpc, weak or zero at kpc)

**If (A) — cosmological only:**
- Gaia constraints (local dark matter, r ~ 8 kpc) do not apply → I will document this

**If (B) or (C) — also galactic:**
- Gaia stellar kinematics constrain local dark matter: ρ_DM(z=0) ~ 0.3–0.6 GeV/cm³
- Need prediction for ρ_DM(z) vertical profile to compare

**Additional question:**
> Are the 6 dark isomers dissipative (dark photons, radiative cooling, dark atom formation)?

**If dissipative:**
- Dark isomers can cool and collapse into disk-like structures (dark disk)
- Gaia constrains dark disk mass: M_disk / M_halo < 0.3–0.5

**If non-dissipative:**
- Dark isomers remain halo-like (spherical/ellipsoidal distribution, like standard ΛCDM)
- No dark disk formation → dark disk constraint does not apply

**Why this matters:**
- Dimensional analysis from beta_d ~ 4.25 (if dimensionless) suggests a characteristic scale L ~ 2.3–2.6 Mpc (galaxy group / cluster scale, **240× larger** than Milky Way disk ~ 10 kpc)
- This suggests dipole may **not** operate at galactic scales, but I want to confirm this interpretation is correct

---

## 5. Safe Wording Examples

When I write about your model in my audit documentation, I am using phrasing like:

✅ **Safe:**
- "Buckholtz's model proposes 6 isomers (5 dark, 1 ordinary). The microphysical structure is not specified in available materials."
- "Beta values are fitted to H(z) observations and can be used to reproduce the manuscript fit, but cannot be used to predict H(z) on new data (circular reasoning)."
- "BBN/N_eff constraints may be relevant **if** dark isomers are thermally populated. Applicability cannot be determined without clarification."
- "I may be misunderstanding the scale range of dipole terms. Could you clarify whether they operate at cosmological (Mpc) or galactic (kpc) scales?"

❌ **Avoiding:**
- "BBN disproves IDM"
- "This is numerology"
- "Your model violates X"
- "MULTING predicts Y" (when Y was not explicitly predicted by you)

I want to ensure I am representing your work accurately and not putting words in your mouth.

---

## 6. Summary of What I Am Asking For

**Fit reproduction (needed to proceed):**
1. H_MULT(z; beta_d, beta_q) functional form
2. H(z) dataset used in Table A1
3. sigma_MULT definition
4. Which quantities were AI-estimated vs fixed

**Microphysics (determines applicability of external constraints):**
5. Thermal history: thermally populated at BBN? T_dark/T_visible?
6. Self-interactions: collisionless or SIDM? σ/m? Dipole = DM-DM scattering or modified gravity?
7. Scale range: dipole operates at Mpc or kpc? Dissipative or halo-like?

If any of these are still being worked out or are proprietary, I will document that as "not yet specified in published materials" and move on. I am **not** expecting you to derive new results for my audit — I am just trying to avoid misrepresenting what you have already published or communicated.

---

## 7. Email Version (Concise)

**Subject:** Reproducibility Audit — Clarification Questions on IDM/MULTING

Dear Dr. Buckholtz,

I am building a small reproducibility audit for selected parts of your IDM/MULTING work. My goal is not to validate or challenge the model, but to separate definitions from predictions and avoid misrepresenting your work.

I have verified that beta_d = 4.5 and beta_q = 18.0 appear in Table A1 (Appendix A.3) as fitted values. I am treating them as fit-reproduction parameters (not theoretical predictions) to avoid circular reasoning.

To proceed, I need clarification on four points:

**H-MULT fit reproduction:**
1. Could you provide the explicit H_MULT(z; beta_d, beta_q) functional form (monopole + dipole + quadrupole combination)?
2. Which H(z) dataset was used in Table A1 (cosmic chronometers? Pantheon+? BAO?)?
3. How is sigma_MULT (fit quality metric) defined?
4. Which quantities (m_A, r_A, k_A, D_C:AB) were AI-estimated vs fixed?

**IDM microphysics (determines applicability of BBN, SIDM, Gaia constraints):**
5. Do dark isomers contain thermally populated relativistic particles at BBN (T ~ MeV)? If yes, what is T_dark/T_visible?
6. Are dark isomers collisionless (σ/m ~ 0) or self-interacting? Are dipole/quadrupole DM-DM scattering or modified gravity?
7. At what scales does dipole operate (cosmological Mpc or galactic kpc)? Are isomers dissipative (dark atoms, radiative cooling)?

If any are still being finalized, I will document "not yet specified" and move on. I am not asking for new derivations — just trying to source-ground my audit before doing further modeling.

Full details: [link to docs/26 if sending repo]

Best regards,  
[Your name]

---

## 8. PPN Questions (Priority 2 — After H-MULT Formula)

**Purpose:** Assess whether MULTING dipole/quadrupole terms are consistent with Solar System tests (Cassini light deflection γ parameter, Mercury perihelion β parameter).

**Current status:** PPN check is BLOCKED — MULTING lacks weak-field metric, Solar System limit, k_A definition, and COM frame specification.

**Questions:**

### Q5: Metric Formulation
> Does MULTING have a weak-field metric (g_μν = η_μν + h_μν), or is it formulated as a Newtonian-style force correction?

**If metric:** Could you provide the weak-field expansion to O(GM/rc², v²/c²)? This would allow extracting PPN parameters γ and β.

### Q6: Local Applicability
> Do dipole/quadrupole terms apply to ordinary matter (Sun, planets) or only to dark matter clusters?

**Context:** r_d = beta_d × r_A ~ 4.5-45 Mpc (cosmological scale), Solar System r ~ 10⁻⁸ Mpc. Is there a scale cutoff (e.g., dipole vanishes for r << r_d)?

### Q7: Kinetic Energy Parameter k_A
> What is k_A for the Sun? For Earth?

**Context:** Manuscript mentions "sub-object kinetic energy" k_A in dipole term description. Is k_A = (1/2) M v² (classical kinetic energy)? Relative to what frame (Solar System COM? Galaxy COM? Cosmic rest frame)?

### Q8: COM Frame Behavior
> Does the MULTING dipole term vanish when computed in the center-of-mass frame of the system?

**Why this matters:** If dipole vanishes in COM, it may be frame-dependent artifact rather than physical dipole moment.

### Q9: Preferred Frame Effects
> Is MULTING Lorentz-invariant, or does it introduce a preferred cosmic rest frame?

**Context:** If dipole is velocity-dependent relative to cosmic rest frame, PPN parameters α₁, α₂ would deviate from zero. Constraints are very tight: α₁ < 10⁻⁴ (lunar laser ranging), |α₂| < 4×10⁻⁷ (CMB dipole).

### Q10: Solar System PPN Recovery
> Does MULTING recover γ = 1 and β = 1 (GR values) in the Solar System?

**Context:** Current constraints are γ - 1 = (2.1 ± 2.3) × 10⁻⁵ (Cassini), β - 1 = (-4.1 ± 7.8) × 10⁻⁵ (Mercury). Is there a section in your work addressing Solar System constraints?

**If cluster-scale only:** If dipole/quadrupole activate only at r ~ r_d ~ Mpc scales, Solar System PPN checks may not apply.

**Interpretation branches (NOT claims — questions for clarification):**
1. If dipole = local mass distribution → PPN γ, β likely ≠ 1
2. If dipole = kinetic energy (galaxy frame) → preferred frame risk (α₁ constraints)
3. If dipole = velocity-dependent → Local Lorentz Invariance violation (α₁, α₂ constraints)
4. If dipole = metric modification → need weak-field expansion
5. If dipole = cluster-scale only (r < r_d cutoff) → PPN not applicable
6. If dipole = phenomenological H(z) only → no local predictions

**Safe vs unsafe wording:**

✅ **Safe:**
- "PPN check is currently not possible because MULTING lacks a weak-field metric. Author clarification required."
- "If dipole is cluster-scale only (r ~ Mpc), Solar System PPN checks may not apply."

❌ **Avoiding:**
- "MULTING is ruled out by PPN constraints" (no checks performed)
- "MULTING violates Solar System tests" (no local predictions available)
- "PPN parameters show MULTING is inconsistent with GR" (no PPN parameters derived)

**Detailed analysis:** See docs/29_ppn_quick_check_requirements.md (7 PPN checks, all BLOCKED) and docs/30_multing_solar_system_limit_questions.md (7 open questions).

---

## 9. Next Steps After Receiving Response

**If H-MULT formula received:**
- Implement H_MULT(z; beta_d, beta_q) solver
- Reproduce Table A1 fit
- Compare H-MULT vs H-FLRW fit quality on same dataset
- Document results in `docs/18_fit_reproduction_requirements.md`

**If microphysics clarified:**

| Answer | Action |
|--------|--------|
| Isomers thermally populated at BBN | Upgrade Finding 7 (BBN/N_eff) to `gold_candidate`, compute or request N_eff prediction |
| Isomers cold at BBN | Mark Finding 7 as `not_applicable`, archive |
| Isomers self-interacting | Upgrade Finding 8 (SIDM/Bullet Cluster) to `gold_candidate`, request σ/m |
| Isomers collisionless | Mark Finding 8 as `not_applicable` |
| Dipole operates at kpc scales | Upgrade Finding 9 (Gaia/dark disk) to `gold_candidate` (if dissipative) or `partially_applicable` (if non-dissipative) |
| Dipole only Mpc scales | Mark Finding 9 as `not_applicable` |

**If no response or "still being finalized":**
- Document blocker explicitly in README.md
- Publish repository as incomplete but transparent
- Note: "Further work requires author clarification on [X, Y, Z]"
- Move on to other projects

---

## 9. Acknowledgment

I want to emphasize:
- I am **not** claiming to validate or refute IDM/MULTING
- I am **not** using this audit to "disprove" your model
- I **am** trying to build a transparent, source-grounded reproducibility layer
- I **am** separating what is clearly defined (beta values from Table A1) from what requires clarification (H-MULT formula, microphysics)

Your work proposes interesting ideas (6 isomers, multipole cosmology, Eq.15 relation), and I want to represent them accurately. If I have misunderstood anything in this brief, please let me know.

Thank you for your time.

---

**Attachments (if sending full repo):**
- `docs/18_fit_reproduction_requirements.md` — full list of what's needed for fit reproduction
- `docs/23_gold_candidate_bbn_neff_source_check.md` — BBN/N_eff applicability analysis
- `docs/24_gold_candidate_sidm_bullet_cluster_source_check.md` — SIDM/Bullet Cluster applicability analysis
- `docs/25_gold_candidate_dark_disk_gaia_source_check.md` — Gaia/dark disk applicability analysis
- `docs/22_discovery_ledger.md` — summary of all 11 findings from audit

**Note:** These documents are internal audit materials. They contain technical details and safe/unsafe wording templates. The questions above are the core items I need clarification on.
