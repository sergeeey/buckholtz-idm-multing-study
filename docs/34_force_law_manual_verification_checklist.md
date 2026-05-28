# Force-Law Manual Verification Checklist

**Date:** 2026-05-28  
**Status:** PENDING — manual verification NOT YET performed  
**Purpose:** Character-by-character verification of extracted MULTING force-law equations against manuscript PDF

**Source document:** `preprints202511.0598.v6.pdf`  
**Target equations:** Equations 14–20 (force-law section)  
**Extracted records:** `src/multing_force_law_records.py`  
**Report:** `docs/33_public_formula_stripping_report.md`

---

## Verification Protocol

**DO NOT upgrade any formula to SOURCE_CONFIRMED until ALL checks pass.**

For each equation:
1. Open `preprints202511.0598.v6.pdf` in PDF reader
2. Navigate to equation number (Eq.14, Eq.15, etc.)
3. Compare character-by-character with extracted formula
4. Check: coefficients, signs, powers, absolute value bars, object labels
5. Mark ✅ PASS or ❌ FAIL for each component
6. If ANY component fails → ENTIRE formula is SOURCE_INCORRECT

**After verification:**
- If ALL checks pass → upgrade status `SOURCE_CANDIDATE` → `SOURCE_CONFIRMED`
- If ANY check fails → downgrade to `SOURCE_INCORRECT`, re-extract manually
- Update `code_permission` if status changes
- Re-run tests: `pytest tests/test_multing_force_law_dimensionality.py -v`

---

## Checklist — Monopole Force (F_m)

**Extracted formula:**
```
F_m = G m_A m_P / r²
```

**Source location:** Equation _____ (fill in after finding)  
**Page number:** _____ (fill in)

| Component | Extracted | Manuscript | Match? | Notes |
|-----------|-----------|------------|--------|-------|
| Coefficient | G | | ☐ | Gravitational constant |
| Numerator mass 1 | m_A | | ☐ | Object A mass |
| Numerator mass 2 | m_P | | ☐ | Probe mass |
| Denominator | r² | | ☐ | Separation distance squared |
| Sign | (none, attractive) | | ☐ | Standard Newtonian attraction |
| Object labels | A, P | | ☐ | Check subscripts match |

**Overall verdict:** ☐ PASS ☐ FAIL  
**If FAIL, reason:** ___________________________________

---

## Checklist — Dipole Force (F_d)

**Extracted formula:**
```
F_d = G c⁻² (k_A m_P |r_dA| + k_P m_A |r_dP|) / r³
```

**Source location:** Equation _____ (fill in after finding)  
**Page number:** _____ (fill in)

| Component | Extracted | Manuscript | Match? | Notes |
|-----------|-----------|------------|--------|-------|
| Coefficient | G c⁻² | | ☐ | G times c to the minus two |
| Speed of light power | c⁻² | | ☐ | Check sign of exponent (−2 not +2) |
| First term k | k_A | | ☐ | Kinetic energy scale of A |
| First term m | m_P | | ☐ | Probe mass (not m_A) |
| First term r_d | \|r_dA\| | | ☐ | Absolute value bars present? |
| Second term k | k_P | | ☐ | Kinetic energy scale of P |
| Second term m | m_A | | ☐ | Object A mass (not m_P) |
| Second term r_d | \|r_dP\| | | ☐ | Absolute value bars present? |
| Operator between terms | + | | ☐ | Addition (not subtraction) |
| Denominator | r³ | | ☐ | Separation distance cubed (not squared) |
| Object labels | A, P, dA, dP | | ☐ | All subscripts match |

**Overall verdict:** ☐ PASS ☐ FAIL  
**If FAIL, reason:** ___________________________________

---

## Checklist — Quadrupole Force (F_q)

**Extracted formula:**
```
F_q = G k_A k_P c⁻⁴ |r_qAB|² / r⁴
```

**Source location:** Equation _____ (fill in after finding)  
**Page number:** _____ (fill in)

| Component | Extracted | Manuscript | Match? | Notes |
|-----------|-----------|------------|--------|-------|
| Coefficient | G | | ☐ | Gravitational constant |
| First k | k_A | | ☐ | Kinetic energy scale of A |
| Second k | k_P | | ☐ | Kinetic energy scale of P |
| Speed of light power | c⁻⁴ | | ☐ | Check sign of exponent (−4 not +4 or −2) |
| Quadrupole scale | \|r_qAB\|² | | ☐ | Absolute value bars? Squared outside bars? |
| Denominator | r⁴ | | ☐ | Separation distance to the fourth (not cubed) |
| Object labels | A, P, qAB | | ☐ | Subscript qAB (not qA or qP) |

**Overall verdict:** ☐ PASS ☐ FAIL  
**If FAIL, reason:** ___________________________________

---

## Checklist — Total Force (F_oP)

**Extracted formula:**
```
F_oP = F_m - F_d + F_q
```

**Source location:** Equation _____ (fill in after finding)  
**Page number:** _____ (fill in)

| Component | Extracted | Manuscript | Match? | Notes |
|-----------|-----------|------------|--------|-------|
| Monopole term | F_m | | ☐ | Appears first |
| Monopole sign | + (implicit) | | ☐ | Attractive (positive contribution) |
| Dipole term | F_d | | ☐ | Appears second |
| Dipole sign | − | | ☐ | SUBTRACTIVE (critical — why?) |
| Quadrupole term | F_q | | ☐ | Appears third |
| Quadrupole sign | + | | ☐ | Additive (enhances attraction) |
| Force subscript | oP | | ☐ | "on P" or similar notation |

**Sign structure check:**
- Monopole: + (attractive)
- Dipole: − (reduces attraction or repulsive)
- Quadrupole: + (enhances attraction)

**Overall verdict:** ☐ PASS ☐ FAIL  
**If FAIL, reason:** ___________________________________

**Critical question to ask author:** Why is dipole subtractive? Does this encode repulsion under certain kinematic conditions?

---

## Checklist — Dipole Length Scale (r_dA)

**Extracted formula:**
```
r_dA = beta_d × r_A
```

**Source location:** Equation _____ or inline definition (fill in after finding)  
**Page number:** _____ (fill in)

| Component | Extracted | Manuscript | Match? | Notes |
|-----------|-----------|------------|--------|-------|
| Left side | r_dA | | ☐ | Subscript "dA" (dipole, object A) |
| Coefficient | beta_d | | ☐ | Dipole strength parameter |
| Right side | r_A | | ☐ | Characteristic radius of A |
| Operator | × (multiplication) | | ☐ | Not division or addition |

**Overall verdict:** ☐ PASS ☐ FAIL  
**If FAIL, reason:** ___________________________________

---

## Checklist — Dipole Length Scale (r_dP)

**Extracted formula:**
```
r_dP = beta_d × r_P
```

**Source location:** Equation _____ or inline definition (fill in after finding)  
**Page number:** _____ (fill in)

| Component | Extracted | Manuscript | Match? | Notes |
|-----------|-----------|------------|--------|-------|
| Left side | r_dP | | ☐ | Subscript "dP" (dipole, object P) |
| Coefficient | beta_d | | ☐ | SAME beta_d as r_dA (symmetric) |
| Right side | r_P | | ☐ | Characteristic radius of P |
| Operator | × (multiplication) | | ☐ | Not division or addition |

**Overall verdict:** ☐ PASS ☐ FAIL  
**If FAIL, reason:** ___________________________________

---

## Checklist — Quadrupole Length Scale (|r_qAB|²)

**Extracted formula:**
```
|r_qAB|² = beta_q² × r_A × r_P
```

**Source location:** Equation _____ or inline definition (fill in after finding)  
**Page number:** _____ (fill in)

| Component | Extracted | Manuscript | Match? | Notes |
|-----------|-----------|------------|--------|-------|
| Left side | \|r_qAB\|² | | ☐ | Absolute value bars? Squared outside? |
| Coefficient | beta_q² | | ☐ | SQUARED (not beta_q or beta_q⁴) |
| First radius | r_A | | ☐ | Characteristic radius of A |
| Second radius | r_P | | ☐ | Characteristic radius of P |
| Operator | × (multiplication) | | ☐ | Product r_A × r_P (not sum or ratio) |
| Subscript | qAB | | ☐ | Quadrupole, objects A and B (or A and P?) |

**Overall verdict:** ☐ PASS ☐ FAIL  
**If FAIL, reason:** ___________________________________

**Note:** Check whether manuscript uses "B" or "P" for probe object. If "B" → update all records.

---

## Checklist — Beta Parameter Values

**Extracted values (from Table A1):**
- beta_d = 4.5
- beta_q = 18.0

**Source location:** Table A1, Appendix A.3  
**Already verified:** ✅ YES (manual verification 2026-05-27, Finding 1 in discovery ledger)

| Component | Extracted | Manuscript | Match? | Notes |
|-----------|-----------|------------|--------|-------|
| beta_d value | 4.5 | ✅ 4.5 | ✅ PASS | Confirmed 2026-05-27 |
| beta_q value | 18.0 | ✅ 18.0 | ✅ PASS | Confirmed 2026-05-27 |
| Context | AI-assisted fit | ✅ AI fit | ✅ PASS | "online service reported choosing" |
| Status | Fitted (not derived) | ✅ Fitted | ✅ PASS | Phenomenological parameters |

**Overall verdict:** ✅ ALREADY VERIFIED (2026-05-27)

---

## Checklist — COSM Constants (if present)

**Check if manuscript defines any COSM-related constants for force-law context.**

| Constant | Description | Extracted? | Manuscript Eq. | Match? |
|----------|-------------|------------|----------------|--------|
| r_A definition | Characteristic radius of A | ☐ NOT FOUND | _____ | ☐ |
| r_P definition | Characteristic radius of P | ☐ NOT FOUND | _____ | ☐ |
| k_A definition | Kinetic energy scale of A | ☐ NOT FOUND | _____ | ☐ |
| k_P definition | Kinetic energy scale of P | ☐ NOT FOUND | _____ | ☐ |
| G definition | Gravitational constant | Standard (PDG) | _____ | ☐ |
| c definition | Speed of light | Standard (PDG) | _____ | ☐ |

**If r_A, r_P, k_A, k_P definitions NOT found in manuscript:**
- Mark as `interpretation_unknown` in records
- Add to author clarification questions (docs/26)
- Document as blocker for force-law application

---

## Post-Verification Actions

### If ALL checks PASS:

1. **Update status in `src/multing_force_law_records.py`:**
   ```python
   status=ProvenanceStatus.SOURCE_CONFIRMED  # was SOURCE_CANDIDATE
   source_note="Manually verified 2026-05-28 against preprints202511.0598.v6.pdf, Equations [fill in numbers]"
   ```

2. **Update code permission:**
   ```python
   code_permission=CodePermission.ALLOWED_FOR_DIMENSIONAL_CHECK  # unchanged
   # Still NO H(z) modeling (closure missing)
   ```

3. **Update docs/33_public_formula_stripping_report.md:**
   - Change all instances of `SOURCE_CANDIDATE` → `SOURCE_CONFIRMED`
   - Add verification date and equation numbers
   - Keep "awaiting manual PDF verification" → "manually verified 2026-05-28"

4. **Update docs/22_discovery_ledger.md (Finding 12):**
   - Change `Source status: SOURCE_CANDIDATE` → `SOURCE_CONFIRMED`
   - Change `Verification status: ⏸️ PENDING` → `✅ VERIFIED (2026-05-28)`
   - Add equation numbers from manuscript

5. **Re-run tests:**
   ```bash
   pytest tests/test_multing_force_law_dimensionality.py -v
   ```
   - All 18 tests should still pass
   - Tests check status field existence, not specific value

6. **Commit changes:**
   ```bash
   git checkout -b update/force-law-source-confirmed
   git add src/multing_force_law_records.py docs/33* docs/22* docs/34*
   git commit -m "Upgrade force-law status: SOURCE_CANDIDATE → SOURCE_CONFIRMED (manual verification 2026-05-28)"
   ```

---

### If ANY check FAILS:

1. **Downgrade status in `src/multing_force_law_records.py`:**
   ```python
   status=ProvenanceStatus.SOURCE_INCORRECT  # was SOURCE_CANDIDATE
   source_note="Formula-stripping error detected 2026-05-28. Manual re-extraction required. Error: [describe mismatch]"
   ```

2. **Document error in this checklist:**
   - Which equation failed?
   - What was the mismatch? (wrong sign, wrong power, wrong subscript, etc.)
   - What is the correct formula from manuscript?

3. **Re-extract manually:**
   - Open PDF
   - Copy equation character-by-character
   - Create corrected record
   - Re-run dimensional analysis

4. **Re-run verification checklist on corrected formula.**

---

### If equations NOT FOUND in manuscript:

1. **Mark status:**
   ```python
   status=ProvenanceStatus.SOURCE_MISSING  # was SOURCE_CANDIDATE
   source_note="Force-law equations not found in preprints202511.0598.v6.pdf after manual search. May be in different manuscript or unpublished."
   ```

2. **Add to author clarification questions:**
   - "Where are the explicit force-law equations (F_m, F_d, F_q) published?"
   - "Are they in a different manuscript or preprint?"
   - "If unpublished, can you provide them for reproducibility?"

3. **Update discovery ledger:**
   - Finding 12 type: `copper_result` → `dead_end` (source missing)

---

## Equation Number Map (fill in during verification)

| Formula | Expected in manuscript | Actual equation number | Page |
|---------|----------------------|------------------------|------|
| F_m (monopole) | Eq.14–20 range | _____ | _____ |
| F_d (dipole) | Eq.14–20 range | _____ | _____ |
| F_q (quadrupole) | Eq.14–20 range | _____ | _____ |
| F_oP (total) | Eq.14–20 range | _____ | _____ |
| r_dA definition | Eq.14–20 or inline | _____ | _____ |
| r_dP definition | Eq.14–20 or inline | _____ | _____ |
| \|r_qAB\|² definition | Eq.14–20 or inline | _____ | _____ |

---

## Additional Checks

### Sign consistency check:
- [ ] F_oP sign structure matches extracted: `+ monopole - dipole + quadrupole`
- [ ] If different, document actual structure: _____________________

### Object label consistency check:
- [ ] Manuscript uses "A" and "P" for objects (not "1" and "2" or other labels)
- [ ] If different labels used, document: _____________________

### Absolute value bars check:
- [ ] Dipole: `|r_dA|` and `|r_dP|` have absolute value bars in manuscript
- [ ] Quadrupole: `|r_qAB|²` has absolute value bars INSIDE the square in manuscript
- [ ] If missing or different placement, document: _____________________

### Power notation check:
- [ ] c⁻² in dipole (not c^(-2) or 1/c² unless equivalent)
- [ ] c⁻⁴ in quadrupole (not c^(-4) or 1/c⁴ unless equivalent)
- [ ] r², r³, r⁴ in denominators (not r^2, r^3, r^4 unless equivalent)

---

## Manual Verification Performed By:

**Name:** _____________________  
**Date:** _____________________  
**Time spent:** _____ minutes  
**PDF reader used:** _____________________  
**Verification method:** ☐ Character-by-character ☐ Formula comparison ☐ OCR + diff

---

## Overall Verification Verdict:

☐ **ALL PASS** → Upgrade to SOURCE_CONFIRMED  
☐ **ANY FAIL** → Downgrade to SOURCE_INCORRECT, re-extract  
☐ **NOT FOUND** → Mark SOURCE_MISSING, ask author  

**If PASS, next step:** Update status in codebase, re-run tests, commit changes  
**If FAIL, next step:** Document error, manual re-extraction, re-verify  
**If NOT FOUND, next step:** Add to docs/26 author questions, mark as blocker  

---

**Last updated:** 2026-05-28  
**Status:** CHECKLIST READY — manual verification NOT YET performed  
**Next action:** Open `preprints202511.0598.v6.pdf`, navigate to force-law equations, fill in this checklist
