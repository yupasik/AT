# Test name = Help
# Script dir = R:\Stingray\Tests\Help\htp_content\htp_content.py

from time import sleep
from device import handler, updateTestResult
import RC
import UART
import DO
import GRAB
import MOD
import os
from DO import status


def runTest():
    status("active")
    TestName = "Help"
    ScriptName = "htp_content"
    ScriptIndex = "3"
    Grabber = DO.grab_define()
    platform = DO.load_platform()
    Modulation = "DVBS"
    FEC = "3/4"
    SR = "27500000"
    Stream = "\\X_0000_00000_MUX_32000_EPG_Software_20130328a.ts"
    Frequency = 1476
    Modulator = "1"
    COM = "COM7"
    settings = [ScriptName, ScriptIndex, Grabber, Modulation, FEC, SR, Stream, Frequency, Modulator, COM]
    DO.save_settings(settings)
    GRAB.start_capture()
    MOD.stop(Modulator)

############################ TestCase 1 ##########################################
    testcase = 1
    status("active")
    UART.default_settings()
    RC.push(["exit 3 2400", "help", "right", "ok 1 2400", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    RC.push(["left", "down 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    RC.push(["down 13 3000"])
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    RC.push(["left", "down 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    RC.push(["down 4 3000"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    RC.push(["left", "down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["down 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["down 3 3000"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    RC.push(["left", "down 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    RC.push(["down 13 3000"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["down 5 3000"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    RC.push(["left", "down 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    RC.push(["down 13 3000"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["left", "down 1 3000"])
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
