### practice drawing subgraphs ###
### 2020.07.26 ###


from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot
import numpy

usage = read_csv("test.csv")

ind = list(usage['process time'])
xpos = numpy.arange(len(usage.index))

pyplot.figure(1) # figure identifier
pyplot.subplot(211) # subplot rownum, colnum, plot id
usage['cpu usage(%)'].plot()
pyplot.grid()
pyplot.legend()
pyplot.title("process cpu usage")
pyplot.xlabel("time")
pyplot.ylabel("CPU usage(%)")
pyplot.ylim(0,100)
pyplot.xticks(xpos, ind)

pyplot.subplot(212)
usage['memory usage(%)'].plot()

pyplot.grid()
pyplot.legend()
pyplot.title("process memory usage")
pyplot.xlabel("time")
pyplot.ylabel("Memory usage(%)")
pyplot.ylim(0,50)
pyplot.xticks(xpos, ind)

pyplot.figure(1).tight_layout() # modify subplot layout automatically

pyplot.savefig("test.png")
#pyplot.show()
