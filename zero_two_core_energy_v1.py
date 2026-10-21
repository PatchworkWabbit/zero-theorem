"""Zero Theorem: two primitive integer movements and formal energy through Z0.
Experimental independent implementation. Z0 is a provenance nexus, not multiplication.
"""
from dataclasses import dataclass, asdict
from fractions import Fraction
import json

@dataclass(frozen=True)
class Node:
    id: str
    parent: str | None
    value: int
    primitive: str
    root: str = 'Z0'

class TwoCoreEnergy:
    def __init__(self, step_budget=200000):
        self.step_budget = step_budget
        self.nodes = {'Z0': Node('Z0', None, 0, 'origin')}
        self.paths = []
        self.energy = []
        self._next = 1

    def step(self, parent, primitive):
        if primitive not in ('S', 'P'):
            raise ValueError('Only S and P are arithmetic movement primitives')
        if parent not in self.nodes:
            raise KeyError(parent)
        p = self.nodes[parent]
        node = Node(f'N{self._next}', parent, p.value + (1 if primitive == 'S' else -1), primitive)
        self._next += 1
        self.nodes[node.id] = node
        return node.id

    def construct(self, start, displacement, label=None):
        if type(start) is not int or type(displacement) is not int:
            raise TypeError('Integer movements only')
        if abs(start) + abs(displacement) > self.step_budget:
            raise ArithmeticError('Primitive movement budget exceeded')
        cursor = 'Z0'
        chain = [cursor]
        for count in (start, displacement):
            primitive = 'S' if count >= 0 else 'P'
            for _ in range(abs(count)):
                cursor = self.step(cursor, primitive)
                chain.append(cursor)
        record = {'id': f'PATH{len(self.paths)+1}', 'root': 'Z0', 'label': label,
                  'start': start, 'displacement': displacement,
                  'result': self.nodes[cursor].value, 'chain': chain,
                  'steps': [self.nodes[n].primitive for n in chain[1:]]}
        self.paths.append(record)
        return record

    def energy_through_zero(self, source, branch):
        """Formal complex-energy branch; every +/- unit uses S or P evidence."""
        if branch not in ('+1', '-1', '+i', '-i'):
            raise ValueError('Unknown energy branch')
        if not isinstance(source, int) or isinstance(source, bool):
            raise TypeError('V1 supports integer source values')
        real_delta = (1 if branch == '+1' else -1 if branch == '-1' else 0)
        imag_delta = (1 if branch == '+i' else -1 if branch == '-i' else 0)
        real_path = self.construct(source, real_delta, 'energy-real')
        imag_path = self.construct(0, imag_delta, 'energy-imag')
        event = {'id': f'ZE{len(self.energy)+1}', 'root': 'Z0', 'source': source,
                 'branch': branch, 'formal_unit': 'dimensionless',
                 'output': {'real': str(real_path['result']), 'imag': str(imag_path['result'])},
                 'real_path': real_path['id'], 'imag_path': imag_path['id'],
                 'physical_law_verified': False}
        self.energy.append(event)
        return event

    def verify(self):
        for key, node in self.nodes.items():
            if key == 'Z0':
                if node.value != 0 or node.parent is not None: return False
                continue
            parent = self.nodes.get(node.parent)
            if parent is None or node.root != 'Z0': return False
            if node.value != parent.value + (1 if node.primitive == 'S' else -1): return False
        for path in self.paths:
            if path['chain'][0] != 'Z0' or path['result'] != self.nodes[path['chain'][-1]].value: return False
            for a, b in zip(path['chain'], path['chain'][1:]):
                if self.nodes[b].parent != a: return False
        return True

    def export(self):
        return {'schema': 'zero-two-core-energy-v1', 'nodes': {k: asdict(v) for k,v in self.nodes.items()},
                'paths': self.paths, 'energy': self.energy}

if __name__ == '__main__':
    engine = TwoCoreEnergy()
    for branch in ('+1', '-1', '+i', '-i'):
        print(engine.energy_through_zero(2, branch))
    assert engine.verify()
    print('V1 verified:', len(engine.paths), 'construction paths')
