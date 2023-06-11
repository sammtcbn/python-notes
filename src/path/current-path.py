from pathlib import Path

path= Path()
print(f'path is {path}')

current_path = Path.cwd()
print(f'Current path is {current_path}')

target_file = Path('current-path.py')
print(f'Target file is {target_file}')

abs_path = target_file.absolute()
print(f'Absolute path is {abs_path}')
