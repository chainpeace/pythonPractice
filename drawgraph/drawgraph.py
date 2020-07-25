### practice for drawing graph from pandas DataFrame from csv file ###
### 2020.07.26 ###

from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot
import numpy

usage = read_csv("test.csv")
print(usage)

ind = list(usage['process time'])
print(ind)

xpos = numpy.arange(len(usage.index))
print(xpos)
usage['cpu usage(%)'].plot()

pyplot.grid()
pyplot.legend()
pyplot.title("process cpu usage")
pyplot.xlabel("time")
pyplot.ylabel("CPU usage(%)")
pyplot.ylim(0,100)
pyplot.xticks(xpos, ind)
#pyplot.show()
pyplot.savefig("test.png")
print(type(usage['process time'][1]))
