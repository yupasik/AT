# Test name = EPG
# Script dir = R:\Stingray\Tests\EPG\functionality\functionality.py
# Rev = 1.7

from time import sleep
from device import handler, updateTestResult
import RC
import UART
import DO
import GRAB
import MOD
import os
import OPER
from DO import status


def runTest():
    status("active")
    TestName = "EPG"
    ScriptName = "content"
    ScriptIndex = "1"
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

    # macros
    searching_from_wizard_general_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_general_english_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "down", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_english_E501 = ["up 3 3400", "right 1 1000", "down 3 3400", "ok 1 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 45000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_south_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "down", "down", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_general_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_general_english_ALL = ["up 3 3400", "right 1 1000", "down 3 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 45000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "down", "ok 1 5000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_english_ALL = ["up 3 3400", "right 1 1000", "down 3 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 45000", "down 1 1000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_south_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "down", "down", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    load_regions_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000"]
    load_regions_english_E501 = ["up 3 2400", "right 1 1000", "down 3 2400", "ok 1 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 45000"]
    load_regions_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000"]
    load_regions_english_ALL = ["up 3 2400", "right 1 1000", "down 3 2400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 45000"]

    """############################ TestCase 1 ##########################################
    testcase = 1
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    UART.start_app("")
    RC.push(["key_1", "key_2", "key_3"])    # set of the RC buttons
    sleep(0)
    RC.push("[macros_name]")    # RC macros from remote_control.ini file
    GRAB.compare(testcase)"""
############################ TestCase 1 ##########################################
    testcase = 1
    status("active")
    UART.default_settings()
#    RC.push(["exit 1 500", "exit 1 500", "exit 1 500", "menu 1 1000", "left 1 1000", "left 1 1000", "ok 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1500",  "ok 1 1500", "left 1 1000", "ok 1 1000"])
    sleep(15)
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    sleep(3)
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["guide 1 7000", "right 1 5000", "down 1 1000", "ok 1 1000", "left 1 1000"]) #1ST SHOW
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    RC.push(["down 1 1000", "down 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    RC.push(["down 1 1000", "down 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["exit 1 1000"])
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["down 1 1000", "down 1 1000", "ok 1 1000", "left 1 1000"]) #2ND SHOW
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    RC.push(["exit 1 1000"]) 
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["down 1 1000", "ok 1 1000", "left 1 1000"]) #3RD SHOW
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("active")
    RC.push(["exit 1 1000"])
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["down 1 1000", "ok 1 1000", "left 1 1000"]) #4TH SHOW
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("active")
    RC.push(["exit 1 1000", "down 1 1000", "ok 1 1000", "left 1 1000"]) #5TH SHOW
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("active")
    RC.push(["exit 1 1000"]) 
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["down 1 1000", "ok 1 1000", "left 1 1000"]) #6TH SHOW
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 52 ##########################################
    testcase = 52
    status("active")
    RC.push(["exit 1 1000", "down 1 1000", "ok 1 1000", "left 1 1000"]) #7TH SHOW
    GRAB.compare(testcase)
############################ TestCase 53 ##########################################
    testcase = 53
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 54 ##########################################
    testcase = 54
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 55 ##########################################
    testcase = 55
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 56 ##########################################
    testcase = 56
    status("active")
    RC.push(["exit 1 1000", "down 1 1000", "ok 1 1000", "left 1 1000"]) #8TH SHOW
    GRAB.compare(testcase)
############################ TestCase 57 ##########################################
    testcase = 57
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 58 ##########################################
    testcase = 58
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 59 ##########################################
    testcase = 59
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 60 ##########################################
    testcase = 60
    status("active")
    RC.push(["exit 1 1000", "down 1 1000", "ok 1 1000", "left 1 1000"]) #9TH SHOW
    GRAB.compare(testcase)
############################ TestCase 61 ##########################################
    testcase = 61
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 62 ##########################################
    testcase = 62
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 63 ##########################################
    testcase = 63
    status("active")
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "down 1 1500"])
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
