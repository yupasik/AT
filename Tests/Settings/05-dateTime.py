# Test name = Settings
# Script dir = R:\Stingray\Tests\Settings\05-dateTime\05-dateTime.py

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
    TestName = "Settings"
    ScriptName = "05-dateTime"
    ScriptIndex = "5"
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
    searching_from_wizard_general_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_general_english_E501 = ["up 2 3400", "right 1 1000", "down 2 3400", "ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "down", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_english_E501 = ["up 3 3400", "right 1 1000", "down 3 3400", "ok 1 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 22200", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_south_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "down", "down", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_general_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_general_english_ALL = ["up 2 3400", "right 1 1000", "down 2 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "down", "ok 1 5000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_english_ALL = ["up 3 3400", "right 1 1000", "down 3 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 22200", "down 1 1000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_south_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "down", "down", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    load_regions_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200"]
    load_regions_english_E501 = ["up 2 2400", "right 1 1000", "down 2 2400", "ok 1 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 22200"]
    load_regions_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200"]
    load_regions_english_ALL = ["up 2 2400", "right 1 1000", "down 2 2400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 22200"]

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
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    RC.push(["OK 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    RC.push(["OK 1 1000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("inactive")
    RC.push(["down 1 2000", "left 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("inactive")
    RC.push(["left 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["OK 1 1000", "ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    RC.push(["ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "ok 1 1000", "down 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["right 1 2000", "right 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    RC.push(["right 1 2000", "right 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    RC.push(["left 1 1000", "left 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["left 1 1000", "left 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    RC.push(["down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["ok 1 1000", "up 1 1000", "up 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["up 1 1000", "OK 1 10000", "OK 1 1000", "down 1 1000", "ok 1 1000", "0 1 1000", "0 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "2 1 1000", "5 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000", "0 1 1000", "0 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000", "6 1 1000", "0 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000", "2 1 1000", "5 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000", "right 1 1000", "0 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000", "right 1 1000", "0 1 1000", "0 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000", "right 1 1000", "2 1 1000", "2 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000", "right 1 1000", "4 1 1000", "5 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000", "right 1 1000", "9 1 1000", "9 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "0 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "1 1 1000", "2 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "2 1 1000", "0 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 6 2000", "down 1 1000", "left 1 1000", "down 1 1000", "left 1 1000", "2 1 1000", "9 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 6 2000", "left 1 1000", "down 1 1000", "left 1 1000", "2 1 1000", "9 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 6 2000", "0 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 6 2000", "1 1 1000", "9 1 1000", "6 1 1000", "9 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 6 2000", "1 1 1000", "9 1 1000", "7 1 1000", "0 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    RC.push(["ok 1 1000", "right 6 2000", "2 1 1000", "0 1 1000", "3 1 1000", "7 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    RC.push(["ok 1 1000", "right 6 2000", "1 1 1000", "0 1 1000", "3 1 1000", "7 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 6 2000", "8 1 1000", "8 1 1000", "8 1 1000", "8 1 1000", "OK 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "down 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("active")
    RC.push(["right 15 5000"])
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("active")
    RC.push(["left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    status("active")
    RC.push(["left 30 5000"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    RC.push(["ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    RC.push(["ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "OK 1 1000", "down 1 1000", "OK 1 1000", "2 1 1000", "3 1 1000", "2 1 1000", "5 1 1000", "right 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "left 1 1000", "3 1 1000", "1 1 1000", "right 1 1000", "2 1 1000", "0 1 1000", "1 1 1000", "2 1 1000", "OK 1 1000", "down 1 1000"]) 
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("active")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("manual")
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
