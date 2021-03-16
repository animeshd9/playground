# fname = input("Enter file name: ")
import re
fname ='text.txt'
fh = open(fname,"w")
txt=" "
for line in fh:
     if line != '\n':
         line.stip()
         fh.write(line.strip("\n"))
fh.close()
