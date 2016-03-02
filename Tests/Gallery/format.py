# Test name = Gallery
# Script dir = R:\Stingray\Tests\Gallery\format\format.py
# Rev = 1.1

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
    TestName = "Gallery"
    ScriptName = "format"
    ScriptIndex = "6"
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

############################ TestCase 1 ##########################################
    testcase = 1
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    UART.start_app("")
    RC.push(["key_1", "key_2", "key_3"])    # set of the RC buttons
    sleep(0)
    RC.push("[macros_name]")    # RC macros from remote_control.ini file
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
