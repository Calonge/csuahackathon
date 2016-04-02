import sys
import os.path

if len(sys.argv) != 2:
	sys.exit(1)
workingfile = sys.argv[1].replace(' ', '')
workingfile.replace('\\\'', '')
workingfile_last = workingfile + "last"
f = open(workingfile, 'a')
num = 0
if os.path.isfile(workingfile_last):
	r = open(workingfile_last, 'r')
	line = r.readline().replace("\n", "")
	num = int(r.readline())
	num += 1
	print(line + "" + str(num))
	r.close()
r = open(workingfile_last, 'w')
var = raw_input('Next Line: ')
r.write(var + "\n" + str(num))
f.write(var)