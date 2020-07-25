### file read/write practice ###
### 2020.07.26 ###

#f=open("newfile.txt", 'w')

#for i in range(1,10):
 #   data = "%d line.\n " % i
  #  f.write(data)

#f.close()

f = open("test.t", 'r')
while 1:
    line = f.readline()
    if not line: break
    print(line)
f.close()


