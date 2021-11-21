import time


def onstart():
	a = open("log", "w")
	a.write(time.time())

def ws(tittle, alist1, timetf=False):
	data = []
	with open("log","r+") as a:
		data = a.readlines()
	alist = []
	for line in data:
		c1 = False
		while c1 is False:
			if "\n" in line:
				line = line.split("\n")
				line = line[0]
			else:
				c1 = True
		alist.append(line)
	if timetf:
		alist.append(str(time.ctime()))
	alist.append(tittle)
	for i in alist1:
		alist.append(str(i))
	alist.append("========")
	a = open("log", "w")
	for i in alist:
		a.write(i+"\n")