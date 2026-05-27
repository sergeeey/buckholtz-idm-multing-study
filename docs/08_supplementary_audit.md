# Supplementary Material Audit

## Purpose

Audit claims made in supplementary materials (AI-generated summaries, chatbot outputs, informal communications) to separate them from peer-reviewed or formally published work.

**Important:** Supplementary materials may contain preliminary explorations that require reproduction before being treated as verified.

---

## Supplementary Sources Inventory

| Claim | AI service / source | Claimed value | Source code available? | Data available? | Reproduced? | Verdict |
|---|---|---:|---|---|---|---|
| *Placeholder* | *TBD* | *TBD* | *TBD* | *TBD* | *TBD* | *TBD* |

**Note:** This section will be populated as supplementary materials are identified.

---

## Treatment Guidelines

### If claim appears in AI-generated summary:

**DO:**
- Mark as `status="requires_source_verification"`
- Request original source (paper, calculation, dataset)
- Reproduce independently before upgrading to `status="calculation"`
- Note: "Originally from AI summary, reproduced on [date]"

**DO NOT:**
- Treat AI summary as verified source
- Assume numerical values are correct without reproduction
- Cite "ChatGPT conversation" as source in formal documents

### If claim appears in informal communication:

**DO:**
- Mark as `status="hypothesis"` or `status="unclear"`
- Request formal write-up or publication reference
- Ask clarifying questions for ambiguous points
- Note: "From informal communication [date], pending formal source"

**DO NOT:**
- Treat as peer-reviewed claim
- Build critical dependencies on unverified informal claims
- Assume context is complete

### If claim appears in preprint (arXiv, etc.):

**DO:**
- Cite with preprint ID and date
- Mark as `status="hypothesis"` until peer-reviewed
- Track publication status (submitted? under review? published?)
- Upgrade to `status="fact"` only after peer review + publication

**DO NOT:**
- Treat preprint as equivalent to published paper
- Ignore "v2", "v3" version updates (claim may have changed)

---

## Reproduction Protocol

**For any supplementary claim:**

1. **Extract claim**
   - Write down exact claim text
   - Note source (AI service, email date, preprint ID)
   - Classify initial status

2. **Identify required inputs**
   - Constants used
   - Datasets used
   - Formulas used

3. **Reproduce independently**
   - Write reproduction script/notebook
   - Use same inputs
   - Compare outputs

4. **Document result**
   - If match: upgrade status to `status="calculation"`
   - If mismatch: mark as `status="requires_clarification"`
   - If cannot reproduce: mark as `status="unknown"`

5. **Seek formal source**
   - Request paper reference
   - Request calculation details
   - Request dataset access

---

## Wording Recommendations

### For AI-generated content:

**Instead of:**
> "ChatGPT confirmed that beta_d = 4.25"

**Say:**
> "A preliminary AI-assisted exploration suggested beta_d ~ 4.25. This requires formal derivation and verification."

### For informal communications:

**Instead of:**
> "Dr. Buckholtz stated that MULTING predicts cosmic reversal at z = 0.5"

**Say:**
> "Dr. Buckholtz mentioned in informal communication (date) that MULTING may predict cosmic reversal around z ~ 0.5. Formal publication pending."

### For preprints:

**Instead of:**
> "Buckholtz (2023) proves 6 isomers"

**Say:**
> "Buckholtz (2023, arXiv:XXXX.XXXXX) proposes 6-isomer structure. Peer review status: [submitted/under review/accepted]."

---

## Red Flags for Supplementary Claims

| Red flag | What to check | Action if present |
|---|---|---|
| **"AI confirmed"** | Was human expert consulted? | Request human verification |
| **"Preliminary result"** | Is this finalized? | Mark as `status="hypothesis"` |
| **"To be published"** | Where? When? | Track publication status |
| **Round numbers (100%, 1.0, etc.)** | Suspiciously perfect? | Check if synthetic data |
| **No error bars** | Uncertainty unknown? | Request uncertainty estimate |
| **"Trust me" / "Obviously"** | Argument from authority? | Request derivation or citation |

---

## Current Status

**Supplementary materials identified:** 0

**Supplementary materials reproduced:** 0

**Supplementary materials upgraded to verified:** 0

**Action required:** Identify and catalog any supplementary materials referenced in Buckholtz communications.

---

## Integration with Main Registry

When supplementary claim is verified:

1. Move from supplementary audit to main `epistemic_registry.py`
2. Update status from `requires_source_verification` to appropriate verified status
3. Update source from "informal communication" to formal publication reference
4. Add reproduction test to test suite

**Example workflow:**

```
Supplementary claim (AI-generated): "beta_d = 4.25"
  ↓
Reproduction attempt: Write test
  ↓
Result: Matches / Mismatches / Cannot reproduce
  ↓
If matches: Add to beta_definitions.py with status="calculation"
If mismatches: Request clarification
If cannot reproduce: Mark as status="unknown"
```

---

## Responsible Use of AI-Assisted Research

**AI tools (ChatGPT, Claude, etc.) can be useful for:**
- Literature search
- Dimensional analysis checks
- Code generation
- Brainstorming alternative hypotheses

**AI tools should NOT be used as:**
- Primary sources for numerical values
- Verification of complex physics claims
- Replacement for peer review
- Substitute for formal derivations

**Protocol:** AI-assisted work is preliminary exploration. Always verify independently.

---

## Next Steps

1. Request list of all supplementary materials (AI summaries, informal notes, unpublished drafts)
2. Catalog each supplementary claim in this document
3. Prioritize reproduction efforts (high-impact claims first)
4. Update status as reproduction proceeds
5. Integrate verified claims into main registry

---

**Supplementary audit principle:**  
> Preliminary exploration ≠ verified claim. Reproduce before you rely.
