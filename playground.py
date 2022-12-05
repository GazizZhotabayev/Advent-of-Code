econ = [int(i) for i in '3353333244323244522413237452344312443323447498743663345243334433134232324'] + [10]

for c in sorted(list(set(econ))):
    print(f'There are {econ.count(c)} article(s) that take {c} min(s) to read')

print(f'There is a total of {len(econ)} articles for a total read time of {sum(econ)}')

x = ''.join(str(i) for i in range(1, 1000))
print(x.count('1'), x.count('9'), x.count('0'), x.count('2'))

from datetime import datetime

date1 = datetime.strptime('05/06/2022 23:59:59', '%d/%m/%y %H:%M:%S')
date1 = datetime.strptime('06/06/2022 00:00:01', '%d/%m/%y %H:%M:%S')

print(date1-date2)