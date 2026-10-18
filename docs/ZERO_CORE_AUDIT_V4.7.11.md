# Zero Theorem V4.7.11: zero-functionality audit

Audited 18 October 2026. Scope: the local V4.7.11 engine and the frozen Task 4 baseline. This is a computational behavior audit, not a mathematical proof assessment. The engine and baseline were unchanged, confirmed by SHA-256 before and after the probes.

## Outcome

The existing recovery/regeneration demonstrations remain valid within their tested scope. All five mathematical archive domains route their record creation and operation kernels through zero_core. However, passage through that dispatcher is not equivalent to independent mathematical verification, reconstruction coverage, or complete feedback scheduling. Zero functionality needs further work before proof-oriented testing.

## Coverage map

| Domain | Current zero passage | Independent checking | Missing-record reconstruction |
| --- | --- | --- | --- |
| Rational | Operations and records | Fraction-based tree replay; parent/order/index checks; additional construction replay for four supported pathways | Tested record 20 rebuilt from retained evidence; other pathway types have narrower support |
| Complex | Operations and records | Links, indexes, passage markers and retained content digests; full arithmetic replay is missing | Tested record 125 remained pending |
| Symbolic | Operations and records | Links and digests; numeric embeddings have additional symbolic lineage checks; no general replay of every standalone symbolic record | Tested record 87 remained pending |
| Calculus | Operations and records | Links, variable bindings and digests; full coefficient-operation replay is missing | Tested record 19 remained pending |
| Roles | Transformations and records | Explicit role-rule and variable-binding checks in the link audit | Tested record 23 remained pending |

These deletion probes each removed one record while retaining its original recovery metadata. They test the repair preflight directly, not whether adaptive regeneration can later produce a usable fresh branch.

## Confirmed issues and recommended order

### 1. Complete mathematical validation and fix the calculus-to-rational bridge

Two deliberately incorrect constructor outputs were accepted by the full adaptive candidate check:

- A complex addition whose actual result was 0+i was recorded as 123+0i. The new record had valid parent references, zero passage, indexing and a matching freshly generated digest. The link audit reported zero issues and _zg_check accepted it.
- Differentiating the constant 1 was recorded as the constant 1 rather than 0. The record likewise passed the link audit and _zg_check.

These are fault-injection probes at the constructor boundary. They do not show that the ordinary arithmetic kernels currently calculate these results incorrectly. They show that the validation layer cannot independently catch those wrong outputs when the record metadata agrees. Ordinary edits to previously manifested records still encounter digest checks.

A correct operation chain exposed the opposite failure:

7 → 7x → 7x² → 14x → 14.

The chain used the engine's exact polynomial kernel, valid archived variable references, and depths 1–4. Its constant result created a rational leaf for 14. That value was not already in the baseline rational archive. Although the link audit reported zero issues, independent verification rejected the rational bridge with unregistered_foundation_leaf and unsupported_parentless_construction.

Relevant functions: calculus_record, _calculus_apply_exact, _zv_observe, _za_verify_memory, _zg_check, complex_record, symbolic_record.

Required behavior: independently replay each supported domain's construction; validate cross-domain embeddings against their typed source rather than requiring the embedded value to be a foundation leaf. Preserve ordinary tamper and recipe-conflict detection. Add regressions for both deliberately wrong outputs and the valid new-constant chain.

### 2. Extend exact reconstruction across domains and pathways

The retained rational recipe contains tree, parents and pathway. The generic reconstruction routine supports four rational arithmetic pathways: reuse_v1, result_feedback_v42, consume_v1 and revisit_v1. Other domain manifest entries do not contain equivalent executable reconstruction recipes.

In the five deletion probes, rational record 20 was restored; the complex, symbolic, calculus and role records became explicit zero_recovery_pending slots. This is honest unresolved handling, but it is incomplete reconstruction functionality.

Required behavior: typed reconstruction recipes and deterministic replay for all supported archive construction types, including cross-domain sources, roles, calculus and the remaining rational representation/nexus pathways. Retain ambiguity and contradictions as unresolved evidence. Regeneration must continue to identify itself as a new lineage.

Relevant functions: _zr_manifest_entry, _zr_reconstruct, _zr_preflight.

### 3. Reconnect pending recovery to later evidence

Code inspection: the final run wrapper follows a valid adaptive-active pointer to the chosen branch and returns through the existing run function. It does not invoke the old recovery trial while that branch continues. Recovery evidence is retained, but retained work is not automatically serviced by this continuation path.

Required behavior: bounded, persistent rechecks of unresolved recovery when relevant evidence or supported rules change. Record what triggered a retry, what was checked, and why it remains unresolved. A regenerated equal value must not authenticate an old missing construction or replace its historical identity.

Relevant functions: final run wrapper, _zg_recover, _zg_advance, zero_verify_candidate.

### 4. Preserve alternative parent derivations

Probe: constructing 1+4 using rational parents [1,4] created record 296. Repeating the same tree and pathway with the distinct archived parent [149,4] returned None. Records 1 and 149 have the same leaf tree, but different recorded origins.

The rational deduplication key contains pathway and tree, excluding parent IDs and ancestry. It preserves different trees yielding the same value, but does not retain every distinct parent derivation for an identical tree. Its duplicate journal event records value and pathway, without the alternative parents.

Required behavior: decide whether construction identity includes typed parents, or retain separate derivation edges for every alternate lineage. Prevent unbounded duplicate loops without discarding meaningful provenance.

Relevant functions: add_expression, combine. Review the complex and symbolic-nexus identity policies at the same time.

### 5. Make resource-limited retries and proposal status consistent

Code inspection: role/calculus exploration retains deferred work, and symbolic source imports have explicit continuation cursors. Rational combine can return after a depth/bit limit without a persistent deferred construction, while its arithmetic worker advances the operation cursor. Complex depth limits also complete the current worker path. Increasing a limit therefore does not guarantee that all previously skipped constructions are retried.

Zero-assisted and observer proposals are recorded observations; the audit did not identify a general approval/execution worker for them. Replacing a zero denominator is a new expression proposal, not permission to evaluate division by zero.

Required behavior: distinguish blocked mathematics, resource-deferred work, recorded suggestions, and executable approved constructions. Persist resumable tasks and the conditions for retry.

Relevant functions: combine, work_arithmetic_pair, work_complex, zero_assist, work_roles, work_calculus.

### 6. Validate phone execution and clarify scope reporting

After the preceding changes, rerun restart/resume and interruption checks in a phone-friendly bundle using disposable fixtures. Preserve the original inputs and expose clear reports without requiring manual JSON edits.

Current scope is supplied exact arithmetic, specified symbolic operations, rational polynomials and an explicit role grammar. Role targets include A, a, x and registered numeric states; arbitrary letters, arbitrary functions and newly discovered executable rules are not implemented by that grammar.

The foundation seed and executable rules remain supplied by the program. Complex i and -i are declared seed roots; archive reachability includes those roots as well as rational zero. The zero-core coverage report checks passage bookkeeping, not mathematical completeness. Journaling also has a per-run suppression limit, so the journal is not a promise to retain every event indefinitely.

## What remains established

- The supplied baseline passes the current full adaptive candidate check.
- Existing Task 4 results demonstrate the tested recovery/regeneration branches, source preservation and saved continuation.
- Failed or ambiguous exact recovery can remain unresolved while a separately identified fresh branch continues.
- All probe changes were confined to disposable memory copies. No engine patch was applied during this audit.

## Recommended next task

Implement item 1 first: complete independent checking for the currently supported operations and repair typed calculus-to-rational validation. Then expand reconstruction, reconnect evidence retries, preserve alternative derivations, and standardize deferred work before broadening the operation vocabulary or starting proof studies.

## Reproducible probe evidence

The following output was produced by audit_zero_core_v4711.py against the frozen Task 4 baseline. Static inspection findings above are labeled separately from executed probes.

```json
{
  "engine": "V4.7.11",
  "inputs_before": {
    "zero_theoremV4.7.11.py": "43a098ce73f051e48cbbd96f6b43ac295f13b003c234c218e1c44773435e9f7b",
    "task4_fixture/baseline.json": "5d105759ce2655437c6177ac779c70a9dae8dfffcade67eee54d2e0d107ec900"
  },
  "probes": {
    "baseline": {
      "accepted": true
    },
    "missing_record_reconstruction": {
      "rational": {
        "deleted_id": 20,
        "ready": true,
        "target_status": "intact"
      },
      "complex": {
        "deleted_id": 125,
        "ready": false,
        "target_status": "zero_recovery_pending"
      },
      "symbolic": {
        "deleted_id": 87,
        "ready": false,
        "target_status": "zero_recovery_pending"
      },
      "calculus": {
        "deleted_id": 19,
        "ready": false,
        "target_status": "zero_recovery_pending"
      },
      "roles": {
        "deleted_id": 23,
        "ready": false,
        "target_status": "zero_recovery_pending"
      }
    },
    "incorrect_complex_constructor": {
      "new_id": 126,
      "expected_real": "0",
      "expected_imaginary": "1",
      "stored_real": "123",
      "stored_imaginary": "0",
      "link_issues": 0,
      "validation": {
        "accepted": true
      }
    },
    "incorrect_calculus_constructor": {
      "new_id": 20,
      "expected_coefficients": [
        "0"
      ],
      "stored_coefficients": [
        "1"
      ],
      "link_issues": 0,
      "validation": {
        "accepted": true
      }
    },
    "correct_calculus_new_constant": {
      "steps": [
        {
          "operation": "multiply_x",
          "coefficients": [
            "0",
            "7"
          ],
          "id": 21
        },
        {
          "operation": "multiply_x",
          "coefficients": [
            "0",
            "0",
            "7"
          ],
          "id": 22
        },
        {
          "operation": "differentiate",
          "coefficients": [
            "0",
            "14"
          ],
          "id": 23
        },
        {
          "operation": "differentiate",
          "coefficients": [
            "14"
          ],
          "id": 24
        }
      ],
      "rational_bridge": "14",
      "link_issues": 0,
      "validation": {
        "accepted": false,
        "error": "Independent adaptive check failed: [{'id': 296, 'reasons': ['unregistered_foundation_leaf', 'unsupported_parentless_construction']}]"
      }
    },
    "alternate_parent_same_tree": {
      "first_parents": [
        1,
        4
      ],
      "alternate_parents": [
        149,
        4
      ],
      "same_parent_tree": true,
      "operation": "+",
      "first_id": 296,
      "alternate_id": null
    }
  },
  "inputs_after": {
    "zero_theoremV4.7.11.py": "43a098ce73f051e48cbbd96f6b43ac295f13b003c234c218e1c44773435e9f7b",
    "task4_fixture/baseline.json": "5d105759ce2655437c6177ac779c70a9dae8dfffcade67eee54d2e0d107ec900"
  },
  "inputs_unchanged": true
}
```

## Probe script

```python
"""Diagnostic probes on disposable copies; never edits the engine or fixture."""
import copy, hashlib, importlib.util, json, tempfile
from pathlib import Path
from fractions import Fraction
ROOT=Path(__file__).resolve().parent
source=ROOT/'zero_theoremV4.7.11.py'; fixture=ROOT/'task4_fixture/baseline.json'
spec=importlib.util.spec_from_file_location('audit_engine',source)
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
baseline=json.loads(fixture.read_text())
hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (source,fixture)}
results={'engine':'V4.7.11','inputs_before':hashes,'probes':{}}
def check(m):
    with tempfile.TemporaryDirectory() as directory:
        path=Path(directory)/'memory.json'
        m={k:v for k,v in m.items() if not k.startswith('_')}
        path.write_text(json.dumps(m,default=lambda obj:sorted(obj) if isinstance(obj,set) else str(obj)))
        try:
            e._zg_check(str(path)); return {'accepted':True}
        except Exception as error:return {'accepted':False,'error':str(error)[:1800]}
results['probes']['baseline']=check(copy.deepcopy(baseline))
# Missing typed slots: original manifests are retained.
missing={}
for domain in e._ZR_DOMAINS:
    m=copy.deepcopy(baseline); e.upgrade_v45(m); records=e._zr_records(m,domain)
    target=20 if domain=='rational' else len(records)-1
    del records[target]
    candidate,ready=e._zr_preflight(m,vars(e))
    missing[domain]={'deleted_id':target,'ready':ready,'target_status':e._zr_records(candidate,domain)[target].get('status','intact')}
results['probes']['missing_record_reconstruction']=missing
# Constructor injects a deliberately incorrect complex result with valid links.
m=copy.deepcopy(baseline); e.upgrade_v45(m)
parents=[len(m['complex_archive']['expressions'])-1,0]
left,right=[m['complex_archive']['expressions'][p] for p in parents]
expr='('+left['expr']+' + '+right['expr']+')'
idx=e.complex_record(m,(Fraction(123),Fraction(0)),expr,parents,'+','complex_arithmetic_v44')
results['probes']['incorrect_complex_constructor']={'new_id':idx,'expected_real':str(Fraction(left['real'])+Fraction(right['real'])),'expected_imaginary':str(Fraction(left['imaginary'])+Fraction(right['imaginary'])),'stored_real':'123','stored_imaginary':'0','link_issues':e.archive_link_audit(m)['issues'],'validation':check(m)}
# Deliberately incorrect calculus derivative of a constant; all references valid.
m=copy.deepcopy(baseline); e.upgrade_v45(m); ca=m['calculus_archive']['expressions']
parent=next(r['id'] for r in ca if r['coefficients']==['1'] and r['operation']=='constant_import')
variable=m['roles_archive']['variable_refs'][0]
idx=e.calculus_record(m,['1'],'differentiate',parents=[parent],sources=[{'archive':'roles','id':variable}],depth=1)
results['probes']['incorrect_calculus_constructor']={'new_id':idx,'expected_coefficients':['0'],'stored_coefficients':['1'],'link_issues':e.archive_link_audit(m)['issues'],'validation':check(m)}
# Correct polynomial route: 7 -> 7x -> 7x^2 -> 14x -> 14.
m=copy.deepcopy(baseline); e.upgrade_v45(m)
seven=next(r['id'] for r in m['expressions'] if r['value']=='7')
idx=e.calculus_record(m,['7'],'constant_import',sources=[{'archive':'rational','id':seven}])
steps=[]
for depth,op in enumerate(['multiply_x','multiply_x','differentiate','differentiate'],1):
    previous=idx; coeff=m['calculus_archive']['expressions'][idx]['coefficients']
    coeff,reason=e.zero_core(m,'calculus',operation=op,operands=(coeff,variable))
    idx=e.calculus_record(m,coeff,op,parents=[previous],sources=[{'archive':'roles','id':variable}],depth=depth)
    steps.append({'operation':op,'coefficients':coeff,'id':idx})
results['probes']['correct_calculus_new_constant']={'steps':steps,'rational_bridge':m['expressions'][-1]['value'],'link_issues':e.archive_link_audit(m)['issues'],'validation':check(m)}
# Same tree from different archived parents: find a genuinely new first expression.
m=copy.deepcopy(baseline); e.upgrade_v45(m); stats={'new':0,'observer_added':0}
found=None
for other in range(1,7):
    for op in ['+','-','*','/']:
        tree={'op':op,'left':m['expressions'][1]['tree'],'right':m['expressions'][other]['tree']}
        key=json.dumps(['reuse_v1',tree],sort_keys=True,separators=(',',':'))
        if key not in m['known_expression_keys']:
            found=(other,op);break
    if found:break
if found:
    other,op=found; first=e.combine(m,1,other,op,'reuse_v1',stats)
    second=e.combine(m,149,other,op,'reuse_v1',stats)
    results['probes']['alternate_parent_same_tree']={'first_parents':[1,other],'alternate_parents':[149,other],'same_parent_tree':m['expressions'][1]['tree']==m['expressions'][149]['tree'],'operation':op,'first_id':first,'alternate_id':second}
else: results['probes']['alternate_parent_same_tree']={'probe':'no unused fixture pair found'}
results['inputs_after']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (source,fixture)}
results['inputs_unchanged']=results['inputs_before']==results['inputs_after']
(ROOT/'zero_core_audit_v4711.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
```
