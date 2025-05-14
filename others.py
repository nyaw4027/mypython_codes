#range, for, in
#for r in range(10,31,+1):
   # print(r, end = " ")




#for x in range(11,33,+2):
 
#print(x, end = " ")


#for v in range(0,10,+2):
    
#    print(v+1, end = " ")


def rangeOfnum(start, stop, interval):

    for x in range(start , stop, interval):
        #  num = int(input(" Enter the number: "))
        print(x, end =" ")

start = int(input("start: "))
stop = int(input("Stop: "))
interval = int(input("Interval: "))


rangeOfnum(start, stop, interval)

