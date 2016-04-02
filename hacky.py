import sys

sys.argv
f = open('story1', 'a+')
line = f.file()
while line:
	line = f.readline()
print(line)
var = input("Next Line:")
var.replace('\n', ' ')
f.write(var)