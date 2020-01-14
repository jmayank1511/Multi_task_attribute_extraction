import sys
filename = sys.argv[1]
cnt = sys.argv[2]
f = open(filename+".txt" ,"r")
data = f.read().strip().split("\n \n")
file  = open(filename+"_.txt", "w")
for i in range(int(cnt)):
	file.write(data[i].strip()+"\n \n")
