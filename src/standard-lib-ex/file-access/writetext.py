from pathlib import Path

data = '456'
target = Path('writetext.data')
data = target.write_text(data, encoding='utf8')
