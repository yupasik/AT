# Test name = ManualSearch
# Script dir = R:\Stingray\Tests\ManualSearch\conflicts\conflicts.py
# Rev = 1.11

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
    TestName = "ManualSearch"
    ScriptName = "conflicts"
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
    if platform in ["E501", "E502", "A230"]:
        RC.push(searching_from_wizard_general_E501)
    else:
        RC.push(searching_from_wizard_general_ALL)
    MOD.stop(Modulator)
    MOD.play(Modulator)
    UART.start_app("scheduler")
    RC.push(["red", "ok 1 2400", "down 2 1000", "ok 1 2000", "ok 1 2000", "right 1 1000", "up 2 1000", "ok 1 2000", "ok 1 2000", "exit 5 2400", "1 1 2400"])
    UART.start_app("dvbsmanualscanner")
    sleep(120)
    RC.push(["exit 2 3000", "red 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    RC.push(["exit 2 2400"])
    UART.activate_app("dvbsmanualscanner")
    UART.start_app("dvbsmanualscanner")
    RC.push(["cinemahalls"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    RC.push(["mail"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["red"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["blue"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    RC.push(["yellow"])
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    RC.push(["green"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["help"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    RC.push(["guide"])
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
