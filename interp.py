import argparse
from datetime import datetime
import sys

filepath="data.txt"
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", metavar='file', type=str, help="file")
args = parser.parse_args()

filepath = args.f

ziff = 4

dayti=['','','']
data =  ['','','']


file = open(filepath, 'r')
lineidx = 0
for line in file:

    daytistring=line.split(";")[0]+"-"+line.split(";")[1]
    dayti[lineidx]=datetime.strptime(daytistring, "%d.%m.%Y-%H:%M")
    if lineidx < 2:
        data[lineidx]=float(line.split(";")[2].strip())
    lineidx += 1
file.close()

# output of read lines
print("Read file: "+filepath)
print(" 1st date: "+str(dayti[0])+" - with data: "+str(data[0]))
print(" 2st date: "+str(dayti[1])+" - with data: "+str(data[1]))


# check if day at line 2 is after day in line 1
if dayti[1] < dayti[0] or dayti[2] < dayti[0] or dayti[2]>dayti[1]:
    print("dates in wrong order")
    print("exiting ....")
    sys.exit()

dayti01 = dayti[1]-dayti[0]
dayti02 = dayti[2]-dayti[0]
data01 = data[1]-data[0]

# Dreisatz:
#
# y(x) = mx + b
# y(0) = b = data[0]
# y(1) = m + b = data[1] --> m+data[0] = data[1] --> m=data[1]-data[0]
# y(x) = (data[1]-data[0])*x + data[0]
# 
# search for x:
# if x=0 date0 and x=1 data1
# --> dayti01 is one step
# --> new step: x=dayti02/dayti01
#
# --> y(dayti02/dayti01) = (data[1]-data[0])*(dayti02/dayti01) + data[0]
#
data[2] = round(data01 * (dayti02/dayti01)+data[0],ziff)
print("goal date: "+str(dayti[2])+" >>>>>> data: "+str(data[2]))