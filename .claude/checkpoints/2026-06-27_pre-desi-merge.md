# Checkpoint: pre-DESI merge — 2026-06-27

## Branch state
- **master**: 2c0bd8e (merge: Koide null test + 77-paper survey → C9 context paragraph)
- **feature/desi2024-fsig8-verified**: d8554be (fix: exp_d_fsig8_observed — DESI 2024 values corrected)
- **feature/koide-null-test-paper**: 4b87cec (merged to master ✅)

## What was just done (session 7)
- Academic research: 77 papers searched, zero existing derivation of Eq.32 found
- Koide null test: K^p × (m_τ/m_e)^n scan → no combination within 10% (VERIFIED-BASH)
- Paper updated: Koide null test + 77-paper survey sentence added to C9 context paragraph
- Committed 4b87cec → merged to master as 2c0bd8e

## What's being merged next
- `feature/desi2024-fsig8-verified` — corrects DESI 2024 fσ8 values in exp_d_fsig8_observed.py
  from wrong source to arXiv:2411.12021 Appendix A [VERIFIED-REAL]

## Rollback
```
git checkout master
git reset --hard 2c0bd8e
```

## Tests before merge
853 passed, 12 skipped — all green
