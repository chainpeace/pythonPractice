### practice reading file, parsing, wrting csv file ###
### 2020.07.26 ###

import csv
from parse import compile

inf=open("test.t", 'r')
outf=open("test.csv", 'w', newline='')
wr = csv.writer(outf)

wr.writerow(["time","cpu usage(%)","memory usage(%)","process time","process name"])

pattern1 = compile("top - {time} up {}")
print(pattern1)
#pattern2 = compile("{:>d} {} {cpu:f} {mem:f} {ptime:>}.{:d} {name}")
pattern2 = compile("{:>d} {} {cpu:f} {mem:f} {min:>d}:{sec:d}.{:d} {name}")
print(pattern2)


while True:
    line = inf.readline()
    if not line: break
    result1 = pattern1.parse(line)

    line = inf.readline()
    if not line: break
    result2 = pattern2.parse(line)
    
    tstamp = result2['min']*60 + result2['sec']

    wr.writerow([result1['time'],result2['cpu'],result2['mem'],tstamp,result2['name']])

inf.close()
outf.close()
