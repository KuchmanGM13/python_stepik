import sys
import time

for i in range(30):
    t = time.time_ns()
    print(
        f'{i}',
        chr(33 + i),
        sep=['  '* 2, '    ', '  ' '  ', '\t'][t % 4],
        end=', ',
        file=[sys.stdout, sys.stderr][t % 2],
    )
    time.sleep((t % 7) / 10)