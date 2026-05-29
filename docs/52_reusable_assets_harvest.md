# Reusable Assets Harvest — Buckholtz IDM/MULTING Project

**Date:** 2026-05-29  
**Purpose:** Identify assets from this project reusable beyond Buckholtz-specific context

---

## Scoring System

**Asset Score = Reuse + Pain + Proof + Uniqueness** (each 1-5, max 20)

| Parameter | Question | 1 | 5 |
|-----------|----------|---|---|
| **Reuse** | Переиспользуется в другом проекте? | Нет, специфично | Да, универсально |
| **Pain** | Решает реальную боль? | Никто не просил | Люди платят за это |
| **Proof** | Есть работающий код/пример? | Только идея | Работает в prod |
| **Uniqueness** | Это есть у других? | Банально, всё есть | Твой угол зрения |

**Interpretation:**
- 0–6: Архивировать как наблюдение
- 7–12: Сохранить как модуль / Obsidian заметка
- 13–16: Выделить в мини-проект
- 17–20: Проверить как продукт / API / услуга

---

## Asset 1: Epistemic Registry Framework

### Description

**Files:**
- `src/epistemic_registry.py`
- `src/beta_provenance.py`
- `src/conflict_resolver.py`
- `docs/03_derived_fitted_assumed_unknown.md`

**Core concepts:**
- Classify every parameter/number as: DERIVED / FITTED / ASSUMED / UNKNOWN
- Track provenance chain (where did this number come from?)
- Detect conflicts (two sources give different values)
- Build assumption dependency graph (if assumption X is wrong, what breaks?)

**Example usage (from this project):**
```python
registry = EpistemicRegistry()

# Register β_d from manuscript
registry.register("beta_d", value=4.5, status="SOURCE_CONFIRMED", 
                 source="Table A1 caption, page 38")

# Register H_MULT(z) as fitted
registry.register("H_MULT", status="FITTED", source="AI service (Step 6)",
                 dependencies=["beta_d", "beta_q", "F_oP"])

# Check conflicts
conflicts = registry.find_conflicts()
```

### Reuse Cases

1. **ML paper reproduction:**
   - Track which hyperparameters are from paper, which tuned, which assumed
   - Detect when two tables give different values for same metric
   - Build dependency graph: if learning rate was wrong, what else breaks?

2. **Economics models:**
   - Classify GDP/inflation numbers as observed / estimated / forecasted
   - Track which model parameters are fitted vs. theoretical
   - Detect conflicting data sources

3. **Theoretical physics:**
   - Track derived constants vs. measured constants
   - Detect when two experiments give conflicting values
   - Build assumption chains for falsification

4. **Medical evidence audits:**
   - Classify treatment effects as RCT-derived / observational / meta-analyzed
   - Track provenance of risk estimates
   - Detect conflicts between studies

5. **AI alignment claim tracking:**
   - Classify safety claims as proven / assumed / unknown
   - Track dependency chains (if assumption A fails, claims B,C,D collapse)
   - Detect conflicting safety proofs

### Score

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| **Reuse** | 5/5 | Universal across any domain with parameters |
| **Pain** | 5/5 | Reproducibility crisis is real, people pay for audit |
| **Proof** | 4/5 | Working code in this project, but not PyPI package yet |
| **Uniqueness** | 5/5 | No existing tool tracks provenance + conflicts + dependency graph together |
| **TOTAL** | **19/20** | |

**Action:** Extract as standalone package

---

## Asset 2: Scientific Table Reverse Engineering Framework

### Description

**Files:**
- `src/table_a1_reverse_engineering.py`
- `tests/test_table_a1_reverse_engineering.py`
- `docs/42_table_a1_reverse_engineering_results.md`

**Core concepts:**
- Load table from CSV/PDF
- Compute expected values from formulas
- Check residuals (reported vs. calculated)
- Check sigma consistency (standardized deviations)
- Adaptive tolerance by value precision
- Generate markdown audit report

**Example usage:**
```python
from src.table_a1_reverse_engineering import audit_table

results = audit_table(
    table_df=df,
    target_col="H_MULT",
    reference_col="H_obs",
    sigma_col="sigma_MULT",
    tolerance=0.11  # adaptive by row
)

# Output: residual report, sigma consistency, outlier detection
```

### Reuse Cases

1. **DESI BAO tables:**
   - Verify reported D_A/r_d vs. computed from models
   - Check chi-square values match data
   - Detect transcription errors

2. **Pantheon+ supernova tables:**
   - Verify distance modulus vs. redshift formula
   - Check sigma consistency across rows
   - Detect outliers

3. **Benchmark leaderboards (ML):**
   - Verify accuracy/F1 vs. confusion matrix
   - Check reported metrics match paper
   - Detect fake submissions

4. **Financial tables:**
   - Verify sum/average rows in reports
   - Check percentage calculations
   - Detect errors in balance sheets

5. **Scientific PDF table extraction:**
   - Auto-extract → auto-verify → flag anomalies
   - Compare multiple papers' tables for same quantity
   - Detect systematic errors

### Score

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| **Reuse** | 5/5 | Any field with numerical tables |
| **Pain** | 5/5 | Table errors cause paper retractions, people need this |
| **Proof** | 4/5 | Working code, tested on Table A1 |
| **Uniqueness** | 4/5 | Some tools exist (tabula-py) but not with formula verification |
| **TOTAL** | **18/20** | |

**Action:** Extract as `table-auditor` package

---

## Asset 3: Bridge Candidate Math Audit Framework

### Description

**Files:**
- `src/bridge_candidate_math_audit.py`
- `src/deep_bridge_verification.py`
- `docs/43_bridge_candidate_math_stress_test.md`
- `docs/48_deep_bridge_independent_verification.md`

**Core concepts:**
- Evaluate multiple bridge candidates (6 families)
- Dimensional analysis (units must match)
- Force-to-potential integration verification
- Monopole-only limit check (reduce to known case)
- Sign and acceleration analysis
- Source-confirmed vs. reconstruction separation
- MCMC/prediction blocking until confirmed

**Example usage:**
```python
from src.bridge_candidate_math_audit import stress_test_bridge

result = stress_test_bridge(
    force_law="F = -G m1 m2 / r^2",
    proposed_h2="H^2 = H0^2 * Omega_m * (1+z)^3",
    checks=["dimensional", "monopole_limit", "sign_analysis"]
)

# Output: PASS / FAIL for each check, classification
```

### Reuse Cases

1. **Modified gravity models:**
   - Verify f(R) → H(z) bridge is dimensionally correct
   - Check monopole limit → GR
   - Verify sign constraints

2. **Physical model audits:**
   - Check proposed formula matches claimed derivation
   - Verify limiting cases
   - Detect dimensional errors

3. **Engineering simulations:**
   - Verify simplified model → full model bridge
   - Check boundary conditions
   - Validate approximations

4. **Theoretical derivation QA:**
   - Audit PhD thesis derivations
   - Check textbook examples
   - Verify paper supplementary math

### Score

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| **Reuse** | 4/5 | Physics/engineering specific, but broad within that |
| **Pain** | 5/5 | Derivation errors cause retracted papers |
| **Proof** | 5/5 | Complete implementation, 41 tests passing |
| **Uniqueness** | 5/5 | No existing tool does bridge candidate stress test |
| **TOTAL** | **19/20** | |

**Action:** Extract as `bridge-auditor` library

---

## Asset 4: Respectful Clarification Brief Template

### Description

**File:**
- `docs/26_author_clarification_brief.md`

**Core concepts:**
- How to ask difficult questions without sounding adversarial
- Safe vs. unsafe wording
- "I may be misunderstanding..." framing
- Context → Question → Why it matters structure
- Non-goals section (NOT validation, NOT refutation)

**Template structure:**
```markdown
## Question N: [Topic]

### Context
[What I observed in manuscript/code]

### My understanding
[My interpretation, explicitly marked as "my interpretation"]

### Question
> "I may be misunderstanding [X]. Could you clarify whether [specific question]?"

### Why this matters
[How answer affects reproducibility / my implementation]

### Non-goal
[Explicitly state: NOT claiming error, NOT validation, NOT refutation]
```

### Reuse Cases

1. **Academic reproducibility:**
   - Clarify computational methods without implying critique
   - Ask about missing details respectfully
   - Request data access politely

2. **Patent clarification:**
   - Query ambiguous claims
   - Request implementation details
   - Avoid adversarial tone

3. **Expert interviews:**
   - Clarify domain knowledge gaps
   - Ask about seemingly contradictory statements
   - Frame as learning, not challenging

4. **Historical research:**
   - Query archival inconsistencies
   - Ask about missing context
   - Avoid accusatory language

5. **Clinical trial clarification:**
   - Ask about statistical methods
   - Query missing data handling
   - Request protocol details

### Score

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| **Reuse** | 5/5 | Any field requiring respectful expert communication |
| **Pain** | 5/5 | Bad communication burns bridges, people pay for this skill |
| **Proof** | 4/5 | Working Q14–Q18 examples, but not a software tool |
| **Uniqueness** | 4/5 | Communication guides exist, but not for technical reproducibility |
| **TOTAL** | **18/20** | |

**Action:** Write blog post / Medium article with template

---

## Asset 5: Discovery Ledger Pattern

### Description

**File:**
- `docs/22_discovery_ledger.md`

**Core concepts:**
- Finding status taxonomy:
  - GOLD: critical finding, high impact
  - COPPER: useful finding, medium impact
  - FOOLS_GOLD: seemed important, actually not
  - SOURCE_MISSING: needs author confirmation
  - SOURCE_CONFIRMED: manuscript supports this
  - SOURCE_TABLE_OUTLIER: data anomaly
- Prevents circular rediscovery (did we already check this?)
- Records why findings matter
- Tracks resolution status

**Example entries:**
```markdown
## Finding 18: Row 1 z=0 Sigma Anomaly

**Status:** SOURCE_TABLE_OUTLIER  
**Date:** 2026-05-XX  
**Impact:** HIGH  
**Classification:** COPPER (useful, but localized)

**What:** sigma_MULT reported 1.30, calculated -1.727 (diff 3.027)

**Why it matters:** Determines Row 1 inclusion in fits

**Resolution:** Excluded from fits, Q14 prepared for author

**Related findings:** None
```

### Reuse Cases

1. **Research projects:**
   - Track hypotheses tested
   - Record why each failed/succeeded
   - Prevent re-testing same idea

2. **Bug investigations:**
   - Track root cause hypotheses
   - Record why each was ruled out
   - Prevent circular debugging

3. **Startup hypothesis tracking:**
   - Track product ideas
   - Record why each was/wasn't pursued
   - Build institutional memory

4. **Exploratory data analysis:**
   - Track interesting patterns
   - Record which were spurious
   - Prevent re-discovering same patterns

### Score

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| **Reuse** | 5/5 | Any investigative work |
| **Pain** | 4/5 | Wastes time without it, but not critical |
| **Proof** | 5/5 | Used throughout project, 19 findings |
| **Uniqueness** | 3/5 | Lab notebooks exist, but not with status taxonomy |
| **TOTAL** | **17/20** | |

**Action:** Extract as mini-guide + template

---

## Top 3 to Extract (Priority Order)

### 1. Epistemic Registry Framework (Score: 19/20)

**Why extract first:**
- Highest impact (reproducibility crisis)
- Universal applicability
- No existing tool does this
- PyPI package potential

**Extraction plan:**
1. Create `epistemic-registry` GitHub repo
2. Refactor out Buckholtz-specific code
3. Add examples from 3 domains (ML, physics, economics)
4. Write tutorial + API docs
5. Publish to PyPI
6. Write blog post announcing

**Estimated effort:** 3-4 days

### 2. Scientific Table Auditor (Score: 18/20)

**Why extract second:**
- High pain point (table errors common)
- Clear use cases (DESI, Pantheon+, benchmarks)
- Existing code works well

**Extraction plan:**
1. Create `table-auditor` repo
2. Generalize beyond Table A1
3. Add PDF extraction integration
4. CLI tool + Python API
5. Publish to PyPI
6. Submit to JOSS (Journal of Open Source Software)

**Estimated effort:** 2-3 days

### 3. Respectful Clarification Brief Template (Score: 18/20)

**Why extract third:**
- High reuse (any expert communication)
- Low effort (already written)
- Medium/blog post format

**Extraction plan:**
1. Write Medium article: "How to Ask Difficult Scientific Questions Without Sounding Adversarial"
2. Include Q14–Q18 as examples (anonymized)
3. Provide template + dos/don'ts
4. Link to GitHub gist with markdown template

**Estimated effort:** 1 day

---

## Do NOT Extract Yet (Context-Sensitive)

### Buckholtz-Specific Physics

**Files:**
- Hamiltonian bridge derivation
- H_MULT diagnostic fit
- F_oP force law details
- Beta parameter analysis

**Why not extract:**
- Author-sensitive
- Not source-confirmed
- Context-specific
- May be wrong

**When to extract:**
- After author confirms bridge method
- If general multipole force → H(z) framework emerges
- If other physicists need similar tools

### Project-Specific Documentation

**Files:**
- docs/07 (Appendix A1 extraction)
- docs/22 (discovery ledger — project-specific)
- docs/26 (author clarification brief — contains Buckholtz-specific context)
- docs/42 (Table A1 reverse engineering — results specific to Table A1)

**Why not extract:**
- Contains author-identifying information
- Results not generalizable
- Part of reproducibility audit, not tool

---

## Extraction Timeline (Proposed)

### Immediate (After Author Response)

**If author confirms bridge:**
- Extract epistemic registry (universal tool)
- Keep bridge code in Buckholtz project

**If author declines detail:**
- Extract all 3 top assets
- Archive Buckholtz project
- Focus on reusable tools

### Month 1 (Weeks 1-4)

- Week 1: Epistemic Registry repo + PyPI
- Week 2: Table Auditor repo + PyPI
- Week 3: Clarification template Medium post
- Week 4: Blog posts announcing all 3

### Month 2 (Promotion)

- Submit Table Auditor to JOSS
- Tweet about epistemic registry
- Write case study: "3 Tools from a Failed Reproducibility Audit"
- Reach out to reproducibility researchers

---

## Asset Repository Structure (Proposed)

```
epistemic-registry/
├── src/epistemic_registry/
│   ├── __init__.py
│   ├── registry.py (core)
│   ├── provenance.py
│   ├── conflict_detector.py
│   └── dependency_graph.py
├── tests/
├── examples/
│   ├── ml_paper_reproduction.py
│   ├── physics_constants.py
│   └── economics_model.py
├── docs/
└── README.md

table-auditor/
├── src/table_auditor/
│   ├── __init__.py
│   ├── audit.py
│   ├── residual_check.py
│   ├── sigma_check.py
│   └── report_generator.py
├── tests/
├── examples/
│   ├── cosmology_table.py
│   ├── ml_benchmark.py
│   └── financial_report.py
├── docs/
└── README.md

respectful-clarification-template/
├── template.md
├── examples/
│   ├── computational_method.md
│   ├── data_access_request.md
│   └── statistical_clarification.md
├── dos_and_donts.md
└── README.md
```

---

## Success Metrics (3 Months Post-Extraction)

| Asset | Metric | Target |
|-------|--------|--------|
| **Epistemic Registry** | GitHub stars | 100+ |
| | PyPI downloads/month | 500+ |
| | Issues opened (engagement) | 10+ |
| **Table Auditor** | GitHub stars | 50+ |
| | PyPI downloads/month | 200+ |
| | Papers citing it | 1+ |
| **Clarification Template** | Medium claps | 200+ |
| | GitHub gist forks | 20+ |
| | Twitter mentions | 10+ |

---

## Lessons Applied to Extraction

### From Buckholtz Project

**What worked well:**
- Modular code structure (easy to extract)
- Clear separation of concerns
- Test coverage (confidence in extraction)
- Markdown docs (easy to adapt)

**What to avoid:**
- Hardcoded project-specific paths
- Buckholtz terminology in generic code
- Tight coupling to specific data format
- Missing examples beyond one use case

### Design Principles for Extracted Assets

1. **Universal > Specific:** Generalize from Buckholtz case
2. **Examples > Docs:** Show 3 examples, not just API
3. **CLI + API:** Both interfaces, choose based on user
4. **Fail gracefully:** Missing data → warning, not crash
5. **Extensible:** Users can add checks/reports easily

---

---

## Hypothesis Revival Engine Relevance

**Document:** `docs/meta/60_hypothesis_revival_engine_relevance.md`

**Summary:** Buckholtz IDM/MULTING project can later serve as a **case study** for computational reactivation of under-tested scientific hypotheses.

**Key concepts preserved:**
- Testability scoring (generalization of MCMC blocker chain)
- Human-in-the-loop principle (AI assists, cannot replace scientific judgment)
- Mapping between Hypothesis Revival labels and Buckholtz statuses
- 5 reusable assets created during this project

**Status labels:**
- FUTURE_META_PROJECT (not active)
- NOT_CURRENT_BUCKHOLTZ_TASK
- DO_NOT_EXPAND_NOW
- NO_PUBLIC_CLAIMS
- WAITING_FOR_AUTHOR_RESPONSE

**Current priority remains:** Repository closure, waiting for author response, GeoScan Gold blind test (27 days).

**Revisit timing:** After Buckholtz closure OR Q4 2026 (whichever later).

**Explicitly excluded from meta document:**
- Market sizing
- SaaS plans
- Product roadmap
- Autonomous lab roadmap
- New active research sprint

**Why preserved:** Useful for future generalization, but **not expanding current scope**.

---

**Status:** ASSET IDENTIFICATION COMPLETE  
**Next step:** Extract epistemic registry after author response  
**Total high-value assets identified:** 5 (3 extraction-ready, 2 context-sensitive)

---

**Last updated:** 2026-05-29  
**Related:** `/harvest` skill, session summary in Obsidian, `docs/meta/60` (Hypothesis Revival)
