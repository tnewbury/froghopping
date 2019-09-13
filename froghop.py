#!/usr/bin/env python

import random
import sys
import time
from multiprocessing import Process, Value

joblist = []

isalive = 4
frogtripswanted = Value('i', 10000)
frogtrips = Value('i', 0)
frogjumps = Value('i', 0)
riverwidth = Value('i', 4096)


def jumpdistance(n):
    #frogjumps.value += 1
    return random.randint(1, riverwidth.value - n + 1)

def travel(threadid, riverwidth, frogtrips, frogtripswanted, frogjumps):
    while frogtrips.value <= frogtripswanted.value:
        print("Journeys made: " + str(frogtrips.value))
        distance = riverwidth.value
        jumps = 1
        while distance >= 1:
            hopdistance = jumpdistance(distance)
            #print(hopdistance)
            distance = distance - hopdistance
            frogjumps.value += 1
            #print ("Jumped " + str(distance))
            print("Thread:" + str(threadid) + " Journey: " + str(frogtrips.value) + " Hop: " + str(jumps) + " Distance: " + str(distance))
            jumps +=1
        frogtrips.value += 1 

for i in range(3):
    joblist.append(Process(target=travel, args=(i, riverwidth, frogtrips, frogtripswanted, frogjumps)))
    joblist[i].start()

while isalive >= 1:
    isalive = 0
    for y in range(3):
        if joblist[y].is_alive() == True:
            isalive +=1
        else:
            pass
            #print("Thread: " + str(y) + " is dead")

print("Trips: " + str(frogtripswanted.value))
print("Jumps: " + str(frogjumps.value))
print("Average jumps per trip: " + str(frogjumps.value/frogtripswanted.value))

