from pathlib import Path

target = Path('readtext.data')

print(target)

data = target.read_text()
print(data)

data = target.read_text(encoding='utf8')
print(data)
