"""Build a standalone V4.7.2 from the user's V4.7.1, preserving the source.

Phone: keep this script and zero_recovery.py beside zero_theoremV4.7.1.py,
then run this script in Pydroid3. Optional CLI: python apply_zero_recovery_patch.py PATH
"""
import ast
from pathlib import Path
import sys


def patch(source, recovery):
    tree = ast.parse(source)
    required = {'zero_core', 'run', 'load_memory', 'save_memory', 'role_record',
                'calculus_record', 'archive_link_audit', 'exact_lookup_key'}
    functions = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)}
    if not required <= functions or 'ZERO_CORE_RULE' not in source:
        raise ValueError('Expected the complete V4.7.1 engine; no file was changed')
    if 'install_zero_recovery(globals())' in source:
        raise ValueError('This engine is already patched')
    guards = [node for node in tree.body if isinstance(node, ast.If)
              and ast.unparse(node.test) == "__name__ == '__main__'"]
    if len(guards) != 1:
        raise ValueError('Expected exactly one main entry point')
    lines = source.splitlines(keepends=True)
    index = guards[0].lineno - 1
    lines[index:index] = ['\n# V4.7.2: zero recovery, stable slots and manifest.\n',
                          recovery, '\ninstall_zero_recovery(globals())\n\n']
    result = ''.join(lines).replace('ZERO THEOREM V4.7.1 -', 'ZERO THEOREM V4.7.2 -')
    compile(result, '<patched-engine>', 'exec')
    return result


def main():
    root = Path(__file__).resolve().parent
    source = Path(sys.argv[1]) if len(sys.argv) == 2 else root / 'zero_theoremV4.7.1.py'
    if len(sys.argv) > 2:
        raise SystemExit('Usage: python apply_zero_recovery_patch.py [V4.7.1.py]')
    target = source.with_name('zero_theoremV4.7.2.py')
    try:
        result = patch(source.read_text(encoding='utf-8'),
                       (root / 'zero_recovery.py').read_text(encoding='utf-8'))
        with target.open('x', encoding='utf-8') as output:
            output.write(result)
    except (OSError, ValueError, SyntaxError) as exc:
        raise SystemExit(str(exc))
    print('Created:', target)
    print('Source and memory unchanged. Run the new script in your test folder.')


if __name__ == '__main__':
    main()
