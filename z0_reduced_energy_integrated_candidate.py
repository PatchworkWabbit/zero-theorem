"""Zero Theorem experimental two-core mathematical/energy bridge.
Independent candidate: does not replace or mutate the V4.9.2 main archive.
Every integer movement is S or P; derived rational arithmetic and four
formal energy branches share the same Z0 provenance ledger.
"""
from fractions import Fraction
import json, os

class Z0ReducedEnergy:
    def __init__(self, budget=200000):
        self.budget = budget
        self.nodes = {"Z0":{"parent":None,"value":0,"step":"origin"}}
        self.paths = []
        self.energy = []
        self.shortcuts = {}
    def walk(self, start, delta, role):
        if type(start) is not int or type(delta) is not int: raise TypeError("integer required")
        if abs(start)+abs(delta)>self.budget: raise ArithmeticError("movement budget exceeded")
        parent="Z0"; chain=["Z0"]
        for n in (start,delta):
            for _ in range(abs(n)):
                step="S" if n>0 else "P"
                node="N"+str(len(self.nodes))
                self.nodes[node]={"parent":parent,"value":self.nodes[parent]["value"]+(1 if step=="S" else -1),"step":step}
                parent=node;chain.append(node)
        result=self.nodes[parent]["value"]
        path={"id":"P"+str(len(self.paths)+1),"root":"Z0","role":role,"chain":chain,"result":result}
        self.paths.append(path)
        return result
    def add(self,a,b):return self.walk(a,b,"addition")
    def negate(self,a):return self.walk(0,-a,"negation")
    def mul(self,a,b):
        value=0
        term=a if b>=0 else self.negate(a)
        for _ in range(abs(b)):value=self.add(value,term)
        return value
    def rational(self,a,op,b):
        a,b=Fraction(a),Fraction(b)
        if op not in ("+","-","*","/"):raise ValueError(op)
        if op=="/" and b==0:return {"status":"blocked","reason":"division_by_zero","root":"Z0"}
        first=len(self.paths)
        an,ad,bn,bd=a.numerator,a.denominator,b.numerator,b.denominator
        if op in ("+","-"):
            x,y=self.mul(an,bd),self.mul(bn,ad)
            num=self.add(x,y if op=="+" else self.negate(y))
            den=self.mul(ad,bd)
        elif op=="*":num,den=self.mul(an,bn),self.mul(ad,bd)
        else:num,den=self.mul(an,bd),self.mul(ad,bn)
        return {"status":"constructed","root":"Z0","result":str(Fraction(num,den)),
                "operation":op,"source":[str(a),str(b)],
                "paths":[p["id"] for p in self.paths[first:]]}
    def energy_through_zero(self,source,branch):
        if branch not in ("+1","-1","+i","-i"):raise ValueError(branch)
        source=Fraction(source); first=len(self.paths)
        real_delta=1 if branch=="+1" else -1 if branch=="-1" else 0
        imag_delta=1 if branch=="+i" else -1 if branch=="-i" else 0
        real=self.rational(source,"+",real_delta)
        imag=self.rational(0,"+",imag_delta)
        event={"id":"ZE"+str(len(self.energy)+1),"root":"Z0","branch":branch,
               "source":str(source),"formal_output":{"real":real["result"],"imag":imag["result"]},
               "paths":[p["id"] for p in self.paths[first:]],"physical_status":"unverified"}
        self.energy.append(event)
        return event
    def discover(self,minimum=3):
        groups={}
        for path in self.paths:
            seq=tuple(self.nodes[node]["step"] for node in path["chain"][1:])
            for width in range(1,len(seq)//2+1):
                if len(seq)%width:continue
                unit=seq[:width];count=len(seq)//width
                if count>=2 and unit*count==seq:
                    groups.setdefault(unit,{})[count]=path["id"]
        for unit,examples in groups.items():
            if len(examples)>=minimum:
                self.shortcuts["repeat_"+"".join(unit)]={"unit":list(unit),"evidence":examples,"root":"Z0"}
        return self.shortcuts
    def verify(self):
        if self.nodes.get("Z0")!={"parent":None,"value":0,"step":"origin"}:return False
        for name,node in self.nodes.items():
            if name=="Z0":continue
            parent=self.nodes.get(node["parent"])
            if parent is None or node["step"] not in ("S","P"):return False
            if node["value"]!=parent["value"]+(1 if node["step"]=="S" else -1):return False
        ids=set()
        for p in self.paths:
            if p["id"] in ids or p["root"]!="Z0":return False
            ids.add(p["id"]);chain=p["chain"]
            if not chain or chain[0]!="Z0" or self.nodes[chain[-1]]["value"]!=p["result"]:return False
            for before,after in zip(chain,chain[1:]):
                if self.nodes[after]["parent"]!=before:return False
        for e in self.energy:
            if e["root"]!="Z0" or not set(e["paths"])<=ids:return False
        return True
    def save(self,path):
        if not self.verify():raise ValueError("invalid provenance")
        data={"schema":"z0-reduced-energy-v1","nodes":self.nodes,"paths":self.paths,
              "energy":self.energy,"shortcuts":self.shortcuts}
        tmp=path+".tmp"
        with open(tmp,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=2);f.flush();os.fsync(f.fileno())
        os.replace(tmp,path)
    @classmethod
    def load(cls,path):
        with open(path,encoding="utf-8") as f:state=json.load(f)
        if state.get("schema")!="z0-reduced-energy-v1":raise ValueError("unknown schema")
        obj=cls()
        for field in ("nodes","paths","energy","shortcuts"):setattr(obj,field,state[field])
        if not obj.verify():raise ValueError("corrupt provenance")
        return obj

if __name__=="__main__":
    engine=Z0ReducedEnergy()
    for branch in ("+1","-1","+i","-i"):print(engine.energy_through_zero(Fraction(2,3),branch))
    print("verified",engine.verify(),"paths",len(engine.paths))
