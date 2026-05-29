# Multi-Hypothesis Kill-Test Protocol (Chamberlin-Platt Method)

**Date:** 2026-05-29  
**Status:** REUSABLE_METHOD_PROTOCOL  
**Scope:** META_METHODOLOGY  
**Author-facing:** NO  
**Current project action:** DO_NOT_EXPAND_SCOPE  
**Buckholtz physics status:** UNCHANGED  
**MCMC status:** BLOCKED  
**Prediction status:** BLOCKED

---

## ⚠️ Important Context

**This is a methodology document, not Buckholtz physics content.**

This protocol provides a reusable method for evaluating competing explanations in research audits where:
- Source documentation is incomplete
- Multiple interpretations are plausible
- Premature commitment to one explanation is risky
- Author clarification is pending or unavailable

**This is a method for organizing uncertainty, not a method for proving a preferred hypothesis.**

**Do NOT:**
- Import Pais/Pauli/Yang-Mills/Higgs historical physics content into Buckholtz analysis
- Expand Buckholtz physics model scope
- Start new historical physics research track
- Use this protocol as evidence for or against any specific Buckholtz hypothesis

**DO:**
- Use this protocol to organize multiple bridge candidates
- Apply to future research reproducibility audits
- Prevent tunnel vision and premature convergence
- Structure uncertainty explicitly

---

## 1. Purpose

### The Problem

When auditing under-specified or under-tested scientific frameworks, researchers face a common trap:

**Tunnel Vision:** Commit to the first plausible explanation, then seek confirming evidence while ignoring alternatives.

**Example failure modes:**
- "This must be the bridge method because it's mathematically elegant"
- "Author probably meant X because that's standard in the field"
- "This interpretation works, so let's implement it without checking alternatives"

**Consequences:**
- Wasted implementation effort on wrong interpretation
- Missed better explanations
- False confidence in reconstruction
- Adversarial tone when single interpretation conflicts with source

### The Solution

**Chamberlin-Platt Multi-Hypothesis Protocol** combines:

1. **Chamberlin's Multiple Working Hypotheses (1890):**
   - Generate ≥3 competing explanations
   - Treat each hypothesis as working tool, not belief
   - Avoid emotional attachment to favored hypothesis

2. **Platt's Strong Inference (1964):**
   - Design experiments/tests that kill hypotheses
   - Prefer tests that eliminate multiple candidates
   - Iterate: surviving hypotheses face stricter tests

3. **Modern additions:**
   - Red-team surviving hypotheses (adversarial critique)
   - Confidence calibration (explicit uncertainty)
   - Author-dependency tracking (what requires confirmation)
   - Combined hypotheses (when no single explanation suffices)

**Goal:** Maintain multiple plausible explanations until evidence definitively separates them.

---

## 2. Protocol Steps (7 Steps)

### Step 1: Generate Multiple Competing Hypotheses

**Rule:** Do NOT start with one favored explanation.

**Minimum:** 3 competing hypotheses  
**Recommended:** 4-6 hypotheses covering broad interpretation space

**How to generate:**
- Parse source material for ambiguous statements
- Identify missing links (e.g., "Step 6: AI service" without formula)
- Consider standard approaches in the field
- Consider non-standard but algebraically valid approaches
- Include null hypothesis (e.g., "retrodiction only, no predictive model")

**Quality check:**
- Hypotheses should be **mutually distinguishable** (different predictions or requirements)
- Avoid pseudo-alternatives (minor variations of same core idea)
- Include at least one hypothesis that challenges your initial assumptions

---

### Step 2: Define Kill-Test for Each Hypothesis

**For each hypothesis, design a test that would weaken or eliminate it.**

**Kill-test characteristics:**
- **Falsifiable:** Clear pass/fail criterion
- **Minimal:** Smallest test that provides diagnostic signal
- **Diagnostic:** Result tells you something even if hypothesis survives

**Questions to ask:**
- What observation would **disprove** this hypothesis?
- What would we expect if the hypothesis is **wrong**?
- What is the **cheapest** test (time/data/computation)?
- If hypothesis survives, what **alternative explanation** remains?

**Example (generic):**

| Hypothesis | Kill-Test |
|-----------|-----------|
| H1: Parameter X derived from theory | Find contradiction with source equations |
| H2: Parameter X fitted to data | Find independent source stating X is theoretical |
| H3: Parameter X assumed for simplicity | Author confirms X was measured/derived, not assumed |

---

### Step 3: Test Against Available Evidence

**Priority order:**
1. **Source-confirmed evidence** (manuscript, supplement, author communication)
2. **Internal consistency** (does hypothesis contradict itself?)
3. **Dimensional analysis** (do units match?)
4. **Limiting cases** (does hypothesis reduce to known result in special case?)
5. **Algebraic stress tests** (sign analysis, monopole limit, etc.)

**Rules:**
- Use ONLY available evidence first (do not fabricate data to test hypothesis)
- Mark evidence with provenance: [SOURCE], [DERIVED], [ASSUMED], [UNKNOWN]
- If kill-test requires unavailable data → mark hypothesis as **DATA_DEPENDENT**
- If kill-test requires author input → mark hypothesis as **AUTHOR_DEPENDENT**

**Output:** For each hypothesis, record:
- Which tests were run
- Which tests passed / failed / blocked
- What evidence was used
- Confidence in test result

---

### Step 4: Red-Team Surviving Hypotheses

**For each hypothesis that survived Step 3, apply adversarial critique:**

**Red-team questions:**
1. **Confounders:** What alternative explanation produces same observations?
2. **Overfitting:** Is hypothesis flexible enough to fit anything?
3. **Hidden assumptions:** What unstated assumptions does hypothesis require?
4. **Evidence gaps:** What key evidence is missing?
5. **Falsifiability:** Can this hypothesis be tested, or is it unfalsifiable?
6. **Author intent:** Does hypothesis match likely author intent, or is it our projection?

**Process:**
- For each surviving hypothesis, write 3-5 critical objections
- Rate objection severity: MINOR / MODERATE / SEVERE / FATAL
- If FATAL objection found → downgrade hypothesis status
- If objection requires data → mark DATA_DEPENDENT
- If objection requires clarification → mark AUTHOR_DEPENDENT

**Example:**

> **Hypothesis:** Hamiltonian bridge H²(a) = H₀²[Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]
>
> **Red-team objections:**
> 1. **MODERATE:** Monopole limit works, but mean-field averaging from discrete clusters to continuous H(a) is not justified
> 2. **MODERATE:** Cluster variables (m_A, r_A, D_AB) missing → cannot compute Ω coefficients from physics
> 3. **SEVERE:** Not source-confirmed → may not match author's intended bridge
> 4. **MINOR:** 11 data points / 4 parameters = underdetermined (but diagnostic fit acceptable if labeled correctly)

---

### Step 5: Assign Confidence and Status

**After Steps 1-4, classify each hypothesis:**

| Status Label | Meaning |
|--------------|---------|
| **SURVIVED** | Passed all available tests, no fatal red-team objections |
| **PARTIAL** | Passed some tests, failed others, or has MODERATE objections |
| **QUESTIONABLE** | Survived but has SEVERE objections or major evidence gaps |
| **FAILED** | Kill-test definitively eliminated hypothesis |
| **AUTHOR_DEPENDENT** | Requires author confirmation to proceed |
| **DATA_DEPENDENT** | Requires external data not yet available |
| **NOT_TESTABLE** | Hypothesis is unfalsifiable or lacks clear predictions |

**Confidence scoring (optional):**

Assign confidence 0.0–1.0 based on:
- Evidence strength (source-confirmed > algebraic > phenomenological)
- Test coverage (all tests run vs. blocked tests)
- Red-team severity (no SEVERE objections > multiple SEVERE)
- Author alignment (likely intent > speculative reconstruction)

**Example:**

| Hypothesis | Status | Confidence | Reasoning |
|-----------|--------|------------|-----------|
| H1: Table-fit / AI-output | PARTIAL | 0.6 | Consistent with "AI service" wording, but no explicit confirmation |
| H2: Hidden bridge in source | AUTHOR_DEPENDENT | 0.3 | Possible but not found after exhaustive search |
| H3: Hamiltonian bridge | SURVIVED / NOT_SOURCE_CONFIRMED | 0.7 | Algebraically valid, but reconstruction not confirmed |
| H4: Discrete lattice / N-body | AUTHOR_DEPENDENT | 0.4 | Interesting but data-heavy, no source confirmation |
| H5: Operational H(z) ambiguity | CONCEPTUAL | 0.5 | Clarification needed on H_MULT meaning |
| H6: Phenomenological retrodiction | SURVIVED | 0.8 | Conservative interpretation, consistent with available evidence |

---

### Step 6: Synthesize Combined Hypothesis (If Needed)

**Allow combined explanations when no single hypothesis is sufficient.**

**When to combine:**
- Multiple hypotheses each explain different aspects
- No single hypothesis passes all tests
- Evidence supports hybrid interpretation

**How to combine:**
1. Identify non-overlapping strengths of each hypothesis
2. Check for logical consistency (can both be true?)
3. Define boundary: where does H1 apply vs. H2?
4. Assign confidence to combined hypothesis

**Example (generic):**

> **Combined Hypothesis:** Mechanism X operates at high energy (H1), mechanism Y operates at low energy (H2), with crossover at energy E_c.
>
> **Evidence:** High-energy data fits H1, low-energy data fits H2, no data at E_c.
>
> **Confidence:** MODERATE (each regime supported, but transition not tested)

**Buckholtz example (hypothetical combined):**

> **Combined Hypothesis:** H_MULT in Table A1 is an AI-assisted fit (H1) that approximates a Hamiltonian-like energy bridge (H3), useful for retrodiction (H6) but not yet validated as predictive model.
>
> **Status:** PARTIAL / AUTHOR_CONFIRMATION_REQUIRED
>
> **Confidence:** 0.6 (consistent with available evidence, but speculative about author intent)

---

### Step 7: Define Crucial Next Experiment

**Find the smallest next test that separates surviving hypotheses.**

**Crucial experiment characteristics:**
- **Decisive:** Result clearly favors one hypothesis over others
- **Feasible:** Can be done with available resources or reasonable effort
- **Minimal:** Smallest test that provides separation
- **Informative:** Result tells you something regardless of outcome

**Process:**
1. List surviving hypotheses from Step 5
2. For each pair, identify what observation would separate them
3. Rank tests by: cost (low better) × decisiveness (high better)
4. Select top-ranked test

**Example (Buckholtz):**

| Test | Separates | Cost | Decisiveness | Rank |
|------|-----------|------|--------------|------|
| **Author clarifies bridge method** | H1 vs H2 vs H3 vs H4 | Low (1 email) | High | ⭐ #1 |
| **Diagnostic fit on Rows 2-12** | H3 algebraic validity | Low (code ready) | Medium | #2 |
| **Author provides cluster variables** | H4 feasibility | Medium (requires data) | High | #3 |
| **Out-of-sample test (Pantheon+)** | H6 (retrodiction vs prediction) | High (full MCMC) | High | #4 (blocked) |

**Recommendation:** #1 (author clarification) is crucial next step. Already prepared as Q14-Q19 in docs/26.

---

## 3. Buckholtz Application Template

**Current bridge candidate hypotheses (as of 2026-05-29):**

| ID | Hypothesis | Kill-Test | Evidence | Status | Confidence | Next Test |
|----|-----------|-----------|----------|--------|------------|-----------|
| **H1** | Table-fit / AI-output | Author provides explicit formula independent of AI | Appendix A1 "AI service" (Step 6) | PARTIAL / AUTHOR_DEPENDENT | 0.6 | Q15, Q16 |
| **H2** | Hidden bridge in source | Exhaustive search finds no formula; author confirms not published | None found in manuscript/supplement | AUTHOR_DEPENDENT | 0.3 | Q15 |
| **H3** | Hamiltonian bridge | Force signs fail, H² powers fail, monopole limit fails, or diagnostic fit unstable | Algebraic verification (docs/48), diagnostic fit code ready | SURVIVED_ALGEBRAIC / NOT_SOURCE_CONFIRMED | 0.7 | Diagnostic fit, Q15 |
| **H4** | Discrete lattice / N-body | Averaging cancels dipole, cluster variables unavailable, or author rejects | Literature precedent (docs/47), but cluster data missing | RESEARCH_PATH / AUTHOR_DEPENDENT | 0.4 | Q17 |
| **H5** | Operational H(z) ambiguity | Author confirms H_MULT is FLRW-like background H(z) | H_MULT may be kinematic/effective not metric (docs/55) | CONCEPTUAL_AMBIGUITY / AUTHOR_CLARIFICATION_REQUIRED | 0.5 | Q-operational |
| **H6** | Phenomenological retrodiction | Source-confirmed model predicts independent H(z) out-of-sample | Table A1 used for beta fit → circular validation | CURRENT_WORKING_CLASSIFICATION | 0.8 | Pantheon+ test (blocked) |

### Hypothesis Details

#### H1: Table-Fit / AI-Output Hypothesis

**Statement:**
H_MULT in Table A1 is primarily an AI-assisted fitted output designed to track H_obs data. Explicit computational formula may not exist or may not have been published.

**Supporting evidence:**
- Appendix A1 Step 6: "AI service generates candidate formulas" (manuscript p.38)
- No explicit H_MULT(z) formula in manuscript or supplement
- Beta parameters (β_d=4.5, β_q=18.0) reported alongside Table A1 → fitted/reported, not purely derived

**Kill-test:**
Author provides explicit, reproducible formula or algorithm that generates Table A1 H_MULT values independently of AI fitting process.

**Current status:** PARTIAL / AUTHOR_DEPENDENT

**Confidence:** 0.6

**Red-team objections:**
- MINOR: "AI service" may refer to candidate generation, not final H_MULT calculation
- MODERATE: Does not explain why H_MULT fits H_obs so well (6× better than H_FLRW)

**Next action:** Q15, Q16 (author clarification)

---

#### H2: Hidden Bridge in Source Hypothesis

**Statement:**
The source-confirmed F_oP → H_MULT computational bridge exists in materials not yet extracted, not yet understood, or referenced obliquely in manuscript.

**Supporting evidence:**
- Manuscript presents H_MULT in Table A1 → some method must exist
- Possible we missed subtle reference in text

**Kill-test:**
Exhaustive source search (manuscript + supplement + references) finds no formula; author explicitly confirms bridge method not published in detail.

**Current status:** AUTHOR_DEPENDENT

**Confidence:** 0.3 (exhaustive search already conducted, nothing found)

**Red-team objections:**
- SEVERE: Exhaustive extraction (docs/07) found no explicit formula
- MODERATE: Appendix A1 Step 6 says "AI service" → suggests method not fully specified

**Next action:** Q15 (author clarification whether bridge published)

---

#### H3: Hamiltonian Energy Bridge Hypothesis

**Statement:**
A valid computational bridge from F_oP to H_MULT can be constructed via classical mechanics: force → potential → energy equation → H²(a).

**Formula:**
```
F_oP(r) = -G m_A m_P [α_m r⁻² + α_d r⁻³ + α_q r⁻⁴]

V(a) = ∫ F dr  (with appropriate limits and signs)

E_total = ½μḊ² + V(D)

H²(a) ≡ (Ḋ/D)² = 2V(D)/μD² = H₀²[Ω_k a⁻² + Ω_m a⁻³ + Ω_d a⁻⁴ + Ω_q a⁻⁵]
```

**Supporting evidence:**
- Algebraic verification (docs/48): dimensional analysis ✅, force-to-potential integration ✅, monopole limit ✅, sign analysis ✅
- Acceleration condition: a⁻⁴ term can accelerate if Ω_d < 0 (dipole repulsive) ✅
- Literature support: PARTIAL (framework exists, MULTING-specific not proven)

**Kill-test:**
1. Force-to-potential signs fail (check integration bounds/conventions)
2. H² power scaling does not match force scaling
3. Monopole-only limit does not reduce to Friedmann
4. Diagnostic fit shows instability (leave-one-out CV high)
5. Author explicitly rejects this bridge

**Current status:** SURVIVED_ALGEBRAIC_CHECK / NOT_SOURCE_CONFIRMED

**Confidence:** 0.7 (strongest internal reconstruction, but not confirmed)

**Red-team objections:**
- MODERATE: Mean-field averaging (discrete clusters → continuous H) not rigorously justified
- MODERATE: Cluster variables missing → cannot compute Ω coefficients from first principles
- SEVERE: Not source-confirmed → may not match author intent
- MINOR: 11 data points / 4 params = underdetermined (acceptable for diagnostic fit, not for validation)

**Next action:**
1. Run diagnostic fit (code ready, not executed)
2. Q15, Q16 (author clarification)

---

#### H4: Discrete Lattice / N-Body Hypothesis

**Statement:**
MULTING should be interpreted as large-scale discrete cluster dynamics, where H_MULT is an effective observable from N-body simulation or lattice averaging.

**Formula:**
```
ä/a = N_eff F_oP / (μ D_AB)

where:
  N_eff = effective number of interacting clusters
  μ = reduced mass
  D_AB = typical cluster separation
```

**Supporting evidence:**
- Literature precedent: lattice cosmology (Zel'dovich, Irvine, Wigner-Seitz) (docs/47)
- MULTING focuses on pairwise cluster forces → discrete starting point
- Wigner-Seitz cell approach: pair → cell → background observable

**Kill-test:**
1. Dipole term (r⁻³) averages to zero in lattice (symmetry cancellation)
2. Cluster variable evolution (m_A(z), r_A(z), D_AB(z)) unavailable or unmeasurable
3. Author explicitly rejects N-body interpretation

**Current status:** RESEARCH_PATH / AUTHOR_DEPENDENT

**Confidence:** 0.4 (interesting but data-heavy, no source confirmation)

**Red-team objections:**
- MODERATE: Requires full cluster evolution functions (not available)
- MODERATE: Averaging prescription unclear (mean-field? Monte Carlo?)
- MODERATE: Dipole term may cancel in symmetric lattice
- SEVERE: No source confirmation this is intended interpretation

**Next action:** Q17 (cluster variables), wait for author response

---

#### H5: Operational H(z) Ambiguity Hypothesis

**Statement:**
H_MULT(z) may not be operationally identical to FLRW H(z). It may represent:
- (a) FLRW-like metric expansion rate (modified Friedmann)
- (b) Kinematic effective separation rate of large structures (emergent observable)
- (c) Phenomenological comparison quantity (not physical observable)

**Supporting evidence:**
- MULTING starts from pairwise forces, not metric/field theory
- Appendix A1 does not specify operational meaning
- H_MULT operational interpretation affects MCMC design (which observables apply)

**Kill-test:**
Author explicitly confirms H_MULT is intended as standard FLRW-like background H(z), operationally equivalent for all observables (d_L, d_A, H_obs).

**Current status:** CONCEPTUAL_AMBIGUITY / AUTHOR_CLARIFICATION_REQUIRED

**Confidence:** 0.5 (ambiguity real, but resolution unknown)

**Red-team objections:**
- MINOR: May be overthinking — author may intend standard H(z)
- MODERATE: Affects MCMC design (d_L computable? BAO applicable?)
- SEVERE: Cannot resolve without author input

**Next action:** Q-operational (docs/55), wait for author response

---

#### H6: Phenomenological Retrodiction Hypothesis

**Statement:**
Table A1 is useful as a retrodictive comparison table demonstrating that MULTING-inspired parameters can track H_obs better than ΛCDM, but it is not (yet) a predictive model suitable for out-of-sample testing.

**Supporting evidence:**
- Beta parameters (β_d, β_q) fitted/reported using data that includes Table A1
- No independent out-of-sample test (Pantheon+, BAO, Cosmic Chronometers)
- Circular validation: data used for fit cannot validate the fit
- Conservative interpretation consistent with all available evidence

**Kill-test:**
Source-confirmed computational model (explicit formula + cluster variables) predicts H(z) on independent dataset (Pantheon+, BAO) with statistically significant improvement over ΛCDM.

**Current status:** CURRENT_WORKING_CLASSIFICATION

**Confidence:** 0.8 (most conservative, least speculative)

**Red-team objections:**
- MINOR: May underestimate MULTING potential (if bridge exists and works)
- MINOR: Table A1 is still useful evidence (retrodiction better than nothing)

**Next action:** Pantheon+ test (blocked until bridge confirmed + cluster variables provided)

---

### Combined Hypothesis (Synthesis)

**Current best synthesis:**

> **MULTING Table A1 represents a retrodictive AI-assisted fit (H1 + H6) that may approximate a Hamiltonian-like energy bridge (H3), potentially interpretable as kinematic effective observable (H2, H5) rather than pure metric expansion. Out-of-sample prediction requires author clarification of bridge method (H1, H2), operational meaning (H5), and cluster variables (H4).**

**Status:** PARTIAL / AUTHOR_DEPENDENT / MCMC_BLOCKED

**Confidence:** 0.6 (consistent with available evidence, but highly speculative about author intent)

**Action required:** Author response to Q14-Q19, then re-evaluate

---

## 4. Safety Rules

### Do NOT

❌ **Promote any candidate to SOURCE_CONFIRMED without evidence**
- Hamiltonian bridge is OUR_COMPUTATIONAL_RECONSTRUCTION, not "Buckholtz formula"
- Do not say "confirmed" unless author confirms

❌ **Treat internal reconstruction as author's formula**
- Label: OUR_RECONSTRUCTION, not "Buckholtz bridge"
- Always note: AUTHOR_CONFIRMATION_REQUIRED

❌ **Run MCMC as validation without blockers resolved**
- MCMC requires: source-confirmed bridge + cluster variables + out-of-sample data
- Current status: 0/5 blockers resolved (docs/54)

❌ **Use Table A1 as both training and validation**
- Beta fitted using data including Table A1
- Same data cannot validate fit (circular)
- Label: RETRODICTION_EVIDENCE, not PREDICTION

❌ **Ignore author-dependence**
- Multiple hypotheses require author input (H1, H2, H4, H5)
- Cannot resolve without clarification
- Status: WAITING_FOR_AUTHOR_RESPONSE

❌ **Collapse multiple hypotheses prematurely**
- Keep ≥3 candidates alive until crucial experiment
- Premature commitment risks wasted implementation
- Current recommendation: wait for author response

---

### DO Use These Labels

✅ **Evidence classification:**
- SOURCE_CONFIRMED — manuscript/supplement explicitly states this
- TABLE_REPORTED — value appears in Table A1
- OUR_COMPUTATIONAL_RECONSTRUCTION — we derived this, not confirmed
- AUTHOR_CONFIRMATION_REQUIRED — cannot proceed without clarification
- LITERATURE_PRECEDENT — similar approaches exist in literature

✅ **Status labels:**
- SURVIVED — passed all available tests
- PARTIAL — passed some, failed others
- AUTHOR_DEPENDENT — requires author input
- DATA_DEPENDENT — requires external data
- MCMC_BLOCKED — cannot run MCMC yet
- PREDICTION_BLOCKED — cannot predict out-of-sample

✅ **Confidence:**
- HIGH (0.7–1.0) — strong evidence, few objections
- MEDIUM (0.4–0.69) — some evidence, moderate objections
- LOW (0.0–0.39) — weak evidence, severe objections

---

## 5. Relation to Existing Project Docs

**This protocol supports and organizes findings from:**

### docs/40_hmult_algorithm_recovery_and_brainstorm.md
- Bridge candidate generation
- Organized as H1-H6 in this protocol

### docs/48_deep_bridge_independent_verification.md
- Hamiltonian bridge algebraic verification (H3 kill-tests)
- Dimensional analysis, monopole limit, sign analysis

### docs/53_three_path_hmult_roadmap_safe_memo.md
- Three bridge paths: Phi-scaling (H1), Hamiltonian (H3), Lattice (H4)
- Safe vs unsafe wording for each path

### docs/54_mcmc_blocker_chain.md
- MCMC blocked until hypotheses resolved
- 5 sub-blockers map to H1, H2, H4, H5
- 0/5 resolved → MCMC remains BLOCKED

### docs/55_conceptual_status_of_hz_in_multing.md
- Operational meaning ambiguity (H5)
- FLRW-like vs kinematic vs phenomenological

### docs/57_final_waiting_state_summary.md (if exists)
- Summary of waiting state
- This protocol prevents premature commitment during wait

**This protocol does NOT duplicate those documents.**

Instead, it provides:
- Unified framework for evaluating all candidates
- Kill-test methodology
- Red-team adversarial critique
- Confidence calibration
- Explicit author-dependency tracking

---

## 6. Current Recommendation (Buckholtz Project)

**For the Buckholtz IDM/MULTING project, this protocol currently recommends:**

### 1. Keep Multiple Bridge Hypotheses Alive

**Active candidates:** H1, H2, H3, H4, H5, H6

**Do NOT collapse prematurely** to single bridge (e.g., Hamiltonian) until crucial experiment (author clarification) separates candidates.

**Why:** Author intent may differ from our reconstruction. Premature commitment risks wasted MCMC implementation.

---

### 2. Do Not Collapse Prematurely onto Hamiltonian Bridge

**Hamiltonian bridge (H3) status:**
- ✅ SURVIVED algebraic stress tests
- ✅ Best internal reconstruction candidate
- ❌ NOT source-confirmed
- ⚠️ May not match author intent

**Use case:** INTERNAL_DIAGNOSTIC_FIT_ONLY

**Do NOT use for:**
- Validation claims
- MCMC without author confirmation
- Public claims about MULTING
- "Buckholtz formula" (it's OUR_RECONSTRUCTION)

---

### 3. Keep Hamiltonian Bridge as Best Internal Reconstruction Candidate

**Despite not being source-confirmed, H3 remains strongest candidate because:**
- Algebraically valid (dimensional, monopole limit, sign analysis all pass)
- Physically interpretable (force → potential → energy)
- Testable (diagnostic fit code ready)
- Literature-supported framework (classical mechanics → H²)

**Label:** BEST_INTERNAL_RECONSTRUCTION_CANDIDATE / NOT_SOURCE_CONFIRMED

**Use:** Diagnostic fits, sensitivity analysis, internal exploration

**Do NOT use:** Validation, MCMC, prediction, public claims

---

### 4. Wait for Author Clarification Before Upgrading Any Bridge

**Critical questions prepared (docs/26):**
- Q14: Row 1 z=0 sigma convention
- Q15: Which bridge method (Phi-scaling / Hamiltonian / Lattice / other)
- Q16: F_oP → H_MULT explicit formula or reference
- Q17: Cluster variable evolution functions
- Q18: Beta parameter derivation vs fitting
- Q-operational: H_MULT operational meaning (docs/55)

**Status:** Email sent 2026-05-29, WAITING_FOR_AUTHOR_RESPONSE

**Action:** Wait for response before:
- Upgrading any bridge to SOURCE_CONFIRMED
- Implementing MCMC
- Making prediction claims
- Collapsing onto single hypothesis

---

### 5. Use Diagnostic Fits Only as INTERNAL_DIAGNOSTIC_FIT_ONLY

**Diagnostic fit code:** src/deep_bridge_diagnostic_fit.py

**Purpose:**
- Test Hamiltonian bridge algebraic flexibility
- Assess overfitting risk (11 points / 4 params = underdetermined)
- Leave-one-out stability check
- Baseline comparisons (polynomial, H_FLRW)

**Safety labels:**
- INTERNAL_DIAGNOSTIC_FIT_ONLY
- NOT_VALIDATION
- NOT_PREDICTION
- AUTHOR_CONFIRMATION_REQUIRED

**Forbidden wording:** "validated", "proved", "solved", "confirmed bridge"

**Allowed wording:** "internal diagnostic fit", "algebraic form flexibility", "candidate bridge", "source-unconfirmed"

---

### Decision Tree

```
Buckholtz Multi-Hypothesis Decision Tree (2026-05-29)

Current state: 6 hypotheses (H1-H6), all AUTHOR_DEPENDENT or PARTIAL

Next crucial experiment: Author clarification (Q14-Q19)

IF author responds:
  ├─ Confirms Hamiltonian (H3):
  │    → Upgrade H3 to SOURCE_CONFIRMED
  │    → Implement MCMC (1 week)
  │    → Test on Pantheon+ / BAO
  │    └─ Report: CONFIRMED / FALSIFIED / NEEDS_COMPLEXITY_PENALTY
  │
  ├─ Confirms Phi-scaling (H1):
  │    → Upgrade H1 to SOURCE_CONFIRMED
  │    → Label as PHENOMENOLOGICAL_FIT
  │    → MCMC not applicable (no physical model)
  │    └─ Archive as retrodiction evidence
  │
  ├─ Confirms Lattice N-body (H4):
  │    → Upgrade H4 to SOURCE_CONFIRMED
  │    → Request cluster variables (Q17)
  │    └─ IF variables provided: implement N-body MCMC
  │       ELSE: archive (insufficient data)
  │
  ├─ Confirms other bridge (H2):
  │    → Request explicit formula
  │    └─ Implement as specified
  │
  └─ Declines to clarify:
       → Archive all as INSUFFICIENT_INFORMATION
       → Preserve H3 as independent reconstruction (optional)
       → Extract reusable assets (epistemic registry, table auditor, etc.)

IF author unresponsive (90 days):
  → Same as "declines to clarify"
  → Archive with: "Author unavailable"

Current status: WAITING (day 0 of 90)
```

---

## 7. Lessons for Future Audits

### What Worked Well (Buckholtz Project)

1. ✅ **Generated 6 bridge candidates** instead of locking onto one
2. ✅ **Defined kill-tests** for each (algebraic, source search, author confirmation)
3. ✅ **Red-teamed Hamiltonian bridge** despite it being strongest candidate
4. ✅ **Tracked author-dependence** explicitly (H1, H2, H4, H5 require input)
5. ✅ **Assigned confidence** (H6: 0.8, H3: 0.7, H1: 0.6, etc.)
6. ✅ **Prepared crucial experiment** (Q14-Q19) before proceeding
7. ✅ **Avoided premature MCMC** implementation

### What to Avoid (Anti-Patterns)

1. ❌ **Single-hypothesis tunnel vision** — "This must be the bridge because it's elegant"
2. ❌ **Confirmation bias** — seeking evidence for favored hypothesis while ignoring alternatives
3. ❌ **Premature implementation** — building MCMC before crucial experiment
4. ❌ **False confidence** — claiming "validated" when only internal diagnostic run
5. ❌ **Ignoring author-dependence** — assuming our reconstruction matches intent
6. ❌ **Collapsing too early** — picking winner before decisive test
7. ❌ **Unfalsifiable hypotheses** — keeping hypotheses that cannot be tested

### Protocol Checklist (Future Audits)

**Before starting audit:**
- [ ] Generate ≥3 competing hypotheses
- [ ] Define kill-test for each
- [ ] Identify crucial next experiment

**During audit:**
- [ ] Test against available evidence (source first, then algebraic)
- [ ] Red-team surviving hypotheses
- [ ] Assign confidence and status labels
- [ ] Track author-dependence explicitly
- [ ] Update hypothesis table after each test

**Before implementation:**
- [ ] Run crucial experiment (if feasible)
- [ ] Wait for author clarification (if needed)
- [ ] Verify ≥2 hypotheses eliminated before proceeding
- [ ] Document which hypothesis won and why

**After audit:**
- [ ] Archive all hypotheses (including failed ones)
- [ ] Preserve kill-tests and red-team critiques
- [ ] Record lessons for next audit

---

## 8. References

**Methodology sources:**
- Chamberlin, T.C. (1890). "The Method of Multiple Working Hypotheses." *Science*.
- Platt, J.R. (1964). "Strong Inference." *Science* 146(3642): 347–353.
- Lakatos, I. (1970). "Falsification and the Methodology of Scientific Research Programmes."
- Tetlock, P.E. (2005). *Expert Political Judgment: How Good Is It? How Can We Know?* (confidence calibration)

**Buckholtz project documents:**
- `docs/07_appendix_a1_extraction.md` — Source extraction
- `docs/26_author_clarification_brief.md` — Q14-Q19 prepared
- `docs/40_hmult_algorithm_recovery_and_brainstorm.md` — Bridge candidates
- `docs/42_table_a1_reverse_engineering_results.md` — Table audit
- `docs/43_bridge_candidate_math_stress_test.md` — Kill-tests
- `docs/47_literature_bridge_map.md` — Lattice cosmology precedents
- `docs/48_deep_bridge_independent_verification.md` — Hamiltonian verification
- `docs/53_three_path_hmult_roadmap_safe_memo.md` — Three-path decision memo
- `docs/54_mcmc_blocker_chain.md` — MCMC blockers
- `docs/55_conceptual_status_of_hz_in_multing.md` — Operational meaning ambiguity

**Status:**
- REUSABLE_METHOD_PROTOCOL
- META_METHODOLOGY
- NOT_BUCKHOLTZ_PHYSICS_CONTENT
- USEFUL_FOR_FUTURE_AUDITS

---

**Last updated:** 2026-05-29  
**Classification:** REUSABLE_METHOD_ASSET  
**Action required:** NONE (apply protocol during waiting period)  
**Revisit:** After author response OR during next research audit
