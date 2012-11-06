import serial
s = serial.Serial('/dev/ttyUSB0', 9600)
empty = ""
for i in range(24*4):
    empty = empty+" "
    

def chop(s):
    length = len(s)
    if(length < 20):
        p = 20-length
        empty = ""
        for e in range(p):
            empty = empty+" "
        s = s+empty
        return s
    else:
        return s[:20]

def write(list_in):
    line1 = chop(list_in[0])
    line2 = chop(list_in[1])
    line3 = chop(list_in[2])
    line4 = chop(list_in[3])

    s.write(line1+line2+line3+line4)



import time
write(["hi","how","are","you?"])
time.sleep(10)
write(["I","am","goodddddddddddddddddddddddddddddddddd","you?"])

s.close()
