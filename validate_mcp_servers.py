import os
import json
import subprocess


def package_exists(pkg_name: str) -> bool:
    try:
        subprocess.run([
            'npm',
            'view',
            pkg_name,
            'version'
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False


def main():
    root = os.path.dirname(__file__)
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith('_mcp.json'):
                full_path = os.path.join(dirpath, filename)
                with open(full_path) as fh:
                    try:
                        data = json.load(fh)
                    except json.JSONDecodeError:
                        print(f'{full_path}: INVALID JSON')
                        continue
                for srv_name, srv_cfg in data.get('mcpServers', {}).items():
                    cmd = srv_cfg.get('command')
                    args = srv_cfg.get('args', [])
                    pkg = None
                    if cmd == 'npx' and args:
                        pkg = args[-1]
                    if pkg:
                        exists = package_exists(pkg)
                        status = 'OK' if exists else 'MISSING'
                        print(f'{full_path}: {srv_name}: {pkg}: {status}')


if __name__ == '__main__':
    main()
