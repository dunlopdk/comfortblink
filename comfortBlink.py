import machine
import utime
import time
from machine import Timer
from machine import Pin

leftactivated = False
rightactivated = False
timeActivated = 3000
checkperiod = 1000
timestart = None

leftblink = Pin(6, Pin.OUT)
rightblink = Pin(8, Pin.OUT)
listenleft = Pin(2, Pin.IN, Pin.PULL_UP)
listenright = Pin(4, Pin.IN, Pin.PULL_UP)

leftblink.value(0)
rightblink.value(0)
leftTimer = None
rightTimer = None

def blinkLeft(pin):
    global rightactivated
    if rightactivated == True:
        cancelLeft()
    else:
        doBlinkLeft()

def blinkRight(pin):
    global leftactivated
    if leftactivated == True:
        cancelRight()
    else:
        doBlinkRight()

def cancelLeft():
    global leftblink, leftactivated, leftTimer, timestart
    leftactivated = False
    leftblink.value(0)
    timestart = None
    if leftTimer != None:
        leftTimer.deinit()
        leftTimer = None

def doBlinkLeft():
    global leftactivated, leftblink, timeActivated, leftTimer, timestart, checkperiod
    if timestart == None:
        timestart = time.ticks_ms()
    leftblink.value(1)
    leftactivated = True
    if time.ticks_diff(time.ticks_ms(), timestart) < checkperiod:
        if leftTimer == None:
            leftTimer = Timer(period = timeActivated, mode = Timer.ONE_SHOT, callback = turnOffLeft)
    elif leftTimer != None:
        leftTimer.deinit()

def cancelRight():
    global rightblink, rightactivated, rightTimer, timestart
    rightactivated = False
    rightblink.value(0)
    timestart = None
    if rightTimer != None:
        rightTimer.deinit()
        rightTimer = None

def doBlinkRight():
    global rightactivated, rightblink, timeActivated, rightTimer, timestart, checkperiod
    if timestart == None:
        timestart = time.ticks_ms()
    rightblink.value(1)
    rightactivated = True
    if time.ticks_diff(time.ticks_ms(), timestart) < checkperiod:
        if rightTimer == None:
            rightTimer = Timer(period = timeActivated, mode = Timer.ONE_SHOT, callback = turnOffRight)
    elif leftTimer != None:
        rightTimer.deinit()

def turnOffLeft(t):
    global leftblink, leftactivated, listenleft, timestart, leftTimer
    leftblink.value(0)
    leftactivated = False
    timestart = None
    leftTimer = None

def turnOffRight(t):
    global rightblink, rightactivated, listenright, timestart, rightTimer
    rightblink.value(0)
    rightactivated = False
    timestart = None
    rightTimer = None
 
def cancelAll():
    global timestart, leftactivated, leftblink, rightactivated, rightblink, timestart, leftTimer, rightTimer, timeActivated
    if time.ticks_diff(time.ticks_ms(), timestart) > timeActivated:
        leftactivated = False
        rightactivated = False
        leftblink.value(0)
        rightblink.value(0)
        timestart = None
        if rightTimer != None:
            rightTimer.deinit()
            rightTimer = None
        if leftTimer != None:
            leftTimer.deinit()
            leftTimer = None

while True:    
    if listenleft.value() == 0:
        blinkLeft(None)
    elif listenright.value() == 0:
        blinkRight(None)
    else:
        cancelAll()
    utime.sleep(0.25)
