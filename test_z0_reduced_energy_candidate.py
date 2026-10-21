from fractions import Fraction
from tempfile import TemporaryDirectory
from pathlib import Path
from z0_reduced_energy_integrated_candidate import Z0ReducedEnergy

e=Z0ReducedEnergy()
cases=[(3,"+",4,"7"),(3,"-",4,"-1"),(3,"*",4,"12"),(12,"/",4,"3"),(Fraction(1,2),"+",Fraction(1,3),"5/6"),(-2,"*",3,"-6")]
for a,op,b,expected in cases:
    assert e.rational(a,op,b)["result"]==expected
assert e.rational(1,"/",0)["status"]=="blocked"
for branch,expected in [("+1",("5/3","0")),("-1",("-1/3","0")),("+i",("2/3","1")),("-i",("2/3","-1"))]:
    result=e.energy_through_zero(Fraction(2,3),branch)["formal_output"]
    assert (result["real"],result["imag"])==expected
assert e.verify()
with TemporaryDirectory() as folder:
    path=str(Path(folder)/"archive.json")
    e.save(path); loaded=Z0ReducedEnergy.load(path)
    assert loaded.verify() and len(loaded.energy)==4
    loaded.nodes["N1"]["value"]=900
    assert not loaded.verify()
    try:loaded.save(path);raise AssertionError("tamper accepted")
    except ValueError:pass
print("PASS: exact arithmetic, four Z0 energy branches, persistence and corruption rejection")
