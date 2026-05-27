# Assumption Dependency Graph

## Purpose

Document which claims depend on which assumptions, to identify:
1. Hidden degrees of freedom
2. Circular dependencies
3. Bottleneck assumptions (many claims depend on one assumption)
4. Risk propagation (if assumption X is wrong, what breaks?)

---

## Dependency Structure

```
H(z) fit
  ├── beta_d
  │     ├── beta_d normalization choice
  │     └── r_A definition (if beta_d = r_dA / r_A)
  ├── beta_q
  │     ├── beta_q normalization choice
  │     └── length scale L_ref (if beta_q relates to L_q^2)
  ├── cluster radius definition
  ├── sub-object kinetic energy definition
  └── dataset choice (Pantheon vs cosmic chronometers vs both)

Eq.15 relation
  ├── exponent 6 mechanism
  └── prefactor 4/3 mechanism

6 isomers claim
  ├── isomer definition
  └── 5 dark / 1 ordinary ratio
        └── (derived or assumed?)

MULTING dipole term
  ├── PPN constraints (must not violate Solar System tests)
  └── beta_d definition

MULTING quadrupole term
  ├── PPN constraints (must not violate Solar System tests)
  └── beta_q definition
```

---

## Full Dependency Table

| Parent claim | Depends on | Why it matters | Hidden degree-of-freedom risk |
|---|---|---|---|
| **H(z) fit** | beta_d | H(z) formula requires beta_d value | High — if beta_d is free parameter, fit depends on it |
| **H(z) fit** | beta_q | H(z) formula requires beta_q value | High — if beta_q is free parameter, fit depends on it |
| **H(z) fit** | cluster radius definition | Scale interpretation needs radius | Medium — different definitions → different beta interpretations |
| **H(z) fit** | sub-object kinetic energy definition | Multipole terms may depend on kinetic energy | Medium — unclear how this enters |
| **H(z) fit** | dataset choice | Different datasets may prefer different betas | Medium — dataset-dependent fit |
| **beta_d** | r_A definition | If beta_d = r_dA / r_A, need to define r_A | High — normalization ambiguity |
| **beta_d** | beta_d normalization choice | Different normalizations → different numerical values | High — explains conflicting candidate values? |
| **beta_q** | length scale L_ref | If beta_q relates to L_q^2, need reference length | High — normalization ambiguity |
| **beta_q** | beta_q normalization choice | Different normalizations → different numerical values | High — explains conflicting candidate values? |
| **Eq.15 relation** | exponent 6 mechanism | Physical reason for (m_tau/m_e)^12 term unclear | High — without mechanism, could be numerology |
| **Eq.15 relation** | prefactor 4/3 mechanism | Physical reason for 4/3 unclear | Medium — prefactor choice affects result |
| **6 isomers claim** | isomer definition | Need to define what "isomer" means in this context | High — foundational definition |
| **6 isomers claim** | 5 dark / 1 ordinary ratio | Ratio stated but not derived | High — is this fundamental or phenomenological? |
| **MULTING dipole term** | PPN constraints | Dipole terms may violate Solar System tests | **Critical** — could falsify model |
| **MULTING quadrupole term** | PPN constraints | Quadrupole terms may violate Solar System tests | **Critical** — could falsify model |

---

## High-Risk Dependency Chains

### Chain 1: H(z) → beta_d → r_A → cluster radius
**Risk:** Each step introduces ambiguity.

**Impact:** If cluster radius definition changes, beta_d interpretation changes, H(z) fit changes.

**Mitigation:** Request explicit definitions at each level.

### Chain 2: H(z) → beta_q → L_ref → ???
**Risk:** L_ref not defined.

**Impact:** Cannot interpret beta_q numerically without reference length.

**Mitigation:** Request L_ref definition.

### Chain 3: MULTING dipole/quadrupole → PPN → Solar System tests
**Risk:** If MULTING violates PPN constraints, model is falsified in Solar System.

**Impact:** Model may work cosmologically but fail locally.

**Mitigation:** Perform PPN mapping before claiming model is viable.

---

## Circular Dependency Check

**Method:** Check if A depends on B AND B depends on A.

**Results:** No circular dependencies detected in current registry.

**Note:** This assumes current understanding is correct. If beta_d is fitted to H(z) and H(z) is then "predicted" using beta_d, that would be circular reasoning (not a graph cycle, but logical circularity).

---

## Bottleneck Assumptions

**Definition:** Assumptions on which many claims depend.

| Assumption | Dependent claims (count) | Risk if wrong |
|---|---:|---|
| **beta_d definition** | 3+ (H(z) fit, dipole term, beta_d scale relation) | High — core parameter |
| **beta_q definition** | 3+ (H(z) fit, quadrupole term, beta_q scale relation) | High — core parameter |
| **PPN constraints** | 2 (dipole term, quadrupole term) | **Critical** — falsifies model if violated |
| **6 isomers structure** | 1 (isomer ratio) | Medium — foundational but fewer dependencies |

**Interpretation:** Beta definitions are bottlenecks. Clarifying them unblocks multiple claims.

---

## Risk Propagation Map

**If beta_d is wrong (e.g., units misunderstood), what breaks?**

1. H(z) fit → incorrect
2. Dipole repulsion term → dimensionally inconsistent
3. Beta_d scale relation → meaningless
4. Any prediction based on beta_d → wrong

**If PPN constraints are violated, what happens?**

1. MULTING dipole term → falsified in Solar System
2. MULTING quadrupole term → falsified in Solar System
3. Model must be restricted to cosmological scales only (not a universal theory)

**If 5 dark / 1 ordinary ratio is assumed (not derived), what changes?**

1. Ratio becomes a free parameter
2. Different ratios may fit data equally well
3. Claim becomes less predictive

---

## Dependency Chain Depth

**Definition:** Longest chain from root claim to terminal assumption.

| Root claim | Max depth | Terminal assumptions |
|---|---:|---|
| H(z) fit | 3 | beta_d normalization, beta_q normalization, dataset choice |
| Eq.15 relation | 2 | exponent 6 mechanism, prefactor 4/3 mechanism |
| 6 isomers | 2 | isomer definition, ratio (derived or assumed?) |
| MULTING terms | 2 | PPN constraints, beta definitions |

**Interpretation:** Most chains are shallow (depth 2-3), which is good for tractability. But each link in the chain introduces ambiguity.

---

## Action Items by Dependency

| Dependency | Action | Priority | Who |
|---|---|---|---|
| beta_d definition | Request explicit formula with units | **Critical** | Dr. Buckholtz |
| beta_q definition | Request explicit formula with units | **Critical** | Dr. Buckholtz |
| PPN constraints | Literature review + mapping MULTING to PPN | **Critical** | Research team |
| r_A definition | Request definition if beta_d uses it | High | Dr. Buckholtz |
| L_ref definition | Request definition if beta_q uses it | High | Dr. Buckholtz |
| exponent 6 mechanism | Request physical derivation or mark as empirical | Medium | Dr. Buckholtz |
| isomer definition | Request definition + observational signatures | Medium | Dr. Buckholtz |
| 5/1 ratio | Clarify if derived or assumed | Medium | Dr. Buckholtz |

---

## Summary Statistics

| Metric | Value |
|---|---:|
| Total dependencies documented | 13 |
| High-risk dependencies | 10 |
| Critical dependencies (PPN) | 2 |
| Circular dependencies detected | 0 |
| Bottleneck assumptions | 2 (beta_d, beta_q) |
| Max dependency chain depth | 3 |

---

## Next Steps

1. **Immediate:** Request beta_d and beta_q definitions to unblock H(z) fit
2. **Critical:** Perform PPN mapping for MULTING dipole/quadrupole terms
3. **Important:** Request explicit functional forms for all MULTING terms
4. **Medium-priority:** Clarify all "unclear" dependencies in the table

---

**Dependency discipline principle:**  
> Every claim depends on something. Make dependencies explicit to avoid hidden assumptions.
