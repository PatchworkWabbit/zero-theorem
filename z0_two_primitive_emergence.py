"""Z0 two-primitive integer construction and evidence-derived shortcut explorer.
Only numeric transitions are successor and predecessor. All paths retain Z0.
"""
import json
from collections import defaultdict
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Node:
    id: str
    value: int
    parent: str
    primitive: str
    root: str = 'Z0'

class ZeroExplorer:
    def __init__(self):
        self.nodes = {'Z0': Node('Z0', 0, '', 'origin')}
        self.next_id = 1
        self.traces = []
        self.shortcuts = {}

    def step(self, parent, direction):
        if direction not in ('S', 'P'):
            raise ValueError('Only successor S and predecessor P are arithmetic primitives')
        node = self.nodes[parent]
        value = node.value + (1 if direction == 'S' else -1)
        ident = f'N{self.next_id}'
        self.next_id += 1
        self.nodes[ident] = Node(ident, value, parent, direction)
        return ident

    def construct(self, directions, label=None):
        cursor = 'Z0'
        chain = [cursor]
        for direction in directions:
            cursor = self.step(cursor, direction)
            chain.append(cursor)
        trace = {'label': label, 'chain': chain, 'steps': list(directions),
                 'value': self.nodes[cursor].value, 'root': 'Z0'}
        self.traces.append(trace)
        return trace

    def repeated_pattern(self, unit, repetitions):
        if not isinstance(unit, (tuple, list)) or not unit or any(x not in ('S','P') for x in unit):
            raise ValueError('unit must be a nonempty primitive sequence')
        if not isinstance(repetitions, int) or repetitions < 1:
            raise ValueError('repetitions must be a positive integer')
        return self.construct(list(unit) * repetitions,
                              {'unit': list(unit), 'repetitions': repetitions})

    def discover(self, minimum_examples=3):
        groups = defaultdict(dict)
        for trace in self.traces:
            steps = trace['steps']
            for width in range(1, len(steps)//2 + 1):
                if len(steps) % width:
                    continue
                unit = steps[:width]
                count = len(steps)//width
                if count < 2 or unit * count != steps:
                    continue
                groups[tuple(unit)][count] = trace
        found = []
        for unit, examples in groups.items():
            if len(examples) < minimum_examples:
                continue
            evidence = []
            for count, trace in sorted(examples.items()):
                value = 0
                for direction in list(unit) * count:
                    value += 1 if direction == 'S' else -1
                if value != trace['value']:
                    raise AssertionError('Invalid trace evidence')
                evidence.append({'repetitions': count, 'trace': trace['chain'][-1], 'value': value})
            name = 'repeat_' + ''.join(unit)
            shortcut = {'name': name, 'unit': list(unit), 'evidence': evidence,
                        'rule': 'repeat the stored primitive path n times',
                        'status': 'discovered_from_traces'}
            self.shortcuts[name] = shortcut
            found.append(shortcut)
        return found

    def apply_shortcut(self, name, repetitions):
        if name not in self.shortcuts:
            raise KeyError('Shortcut has not been discovered')
        return self.repeated_pattern(self.shortcuts[name]['unit'], repetitions)

    def save(self, path):
        data = {'schema': 'z0-two-primitives-v1',
                'nodes': {key: asdict(node) for key,node in self.nodes.items()},
                'traces': self.traces, 'shortcuts': self.shortcuts}
        with open(path, 'w', encoding='utf-8') as output:
            json.dump(data, output, indent=2)

if __name__ == '__main__':
    engine = ZeroExplorer()
    for count in (2, 3, 4, 5):
        engine.repeated_pattern(['S', 'S', 'S'], count)
    discovered = engine.discover()
    assert any(item['unit'] == ['S','S','S'] for item in discovered)
    assert engine.apply_shortcut('repeat_SSS', 4)['value'] == 12
    assert engine.construct(['S','P'])['value'] == 0
    engine.save('z0_two_primitive_evidence.json')
    print('Discovered:', [item['name'] for item in discovered])
    print('3 repeated 4 times ->', engine.traces[-2]['value'])
