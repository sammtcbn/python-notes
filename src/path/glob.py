from pathlib import Path

currpath= Path()
print(f'curr path is {currpath}')

for eachfile in currpath.glob('*.py'):
    print(eachfile)
