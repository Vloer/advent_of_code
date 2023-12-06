from pathlib import Path
import shutil

root = Path(__file__).parent

year = None
if not year:
    year = input('Enter year: ')
(root / year).mkdir(exist_ok=True)
(root / year / 'inputs').mkdir(exist_ok=True)
template = root / 'template.py'
for i in range(1, 26):
    Path(root/year/f'inputs/d{i}.txt').touch()
    d = root/year/f'd{i}.py'
    shutil.copy(template, d)
    print(f'Created files for day {i}')


