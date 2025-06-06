import os
import json
import subprocess
import urllib.request


def npm_package_exists(pkg_name: str) -> bool:
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


def pip_package_exists(pkg_name: str) -> bool:
    try:
        with urllib.request.urlopen(f"https://pypi.org/pypi/{pkg_name}/json"):
            return True
    except Exception:
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
                    checker = None

                    if cmd == 'npx' and args:
                        pkg = args[-1]
                        checker = npm_package_exists

                    elif cmd in {'uv', 'python'} and args:
                        if args[:3] == ['run', 'python', '-m'] and len(args) >= 4:
                            pkg = args[3]
                            checker = pip_package_exists
                        elif args and args[0] == '-m' and len(args) >= 2:
                            pkg = args[1]
                            checker = pip_package_exists

                    if pkg and checker:
                        exists = checker(pkg)
                        status = 'OK' if exists else 'MISSING'
                        print(f'{full_path}: {srv_name}: {pkg}: {status}')


if __name__ == '__main__':
    main()
