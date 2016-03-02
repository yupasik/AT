# Test name = Gallery
# Script dir = R:\Stingray\Tests\Gallery\empty_flash\empty_flash.py

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
    ScriptName = "empty_flash"
    ScriptIndex = "2"
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
    UART.start_app("photos")
    sleep(60)
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    RC.push(["exit 1 3000", "menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    UART.start_app("photos")
    RC.push(["down 1 3000", "last 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    UART.start_app("photos")
    RC.push(["down 1 3000", "exit 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    UART.start_app("photos")
    RC.push(["down 1 3000", "standby 1 5000", "standby 1 10000"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    UART.start_app("photos")
    RC.push(["down 1 3000", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "clock", "stb", "www", "id", "format", "tv/radio", "guide", "red", "green", "blue", "yellow", "cinemahalls", "rec", "reclist", "forward", "backward", "play", "stop", "mute", "VolUp", "VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["exit 3 3500"])
    UART.start_app("photos")
    RC.push(["down 1 2000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["right 1 3000", "left 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    RC.push(["exit 1 2000", "ok 1 3000", "right 3 3000"])
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    RC.push(["exit 1 2000", "ok 1 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["down", "ok 1 3000", "down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    if platform in ["E502"]:
        RC.push(["up 1 3000"])
    RC.push(["ok 1 3000", "left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    RC.push(["exit 1 2000", "ok 1 3000", "right 3 3000"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["ok 1 3000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["ok 1 3000", "menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    UART.start_app("photos")
    RC.push(["down 1 3000", "ok 1 3000", "last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    UART.start_app("photos")
    RC.push(["down 1 3000", "ok 1 3000", "standby 1 5000", "standby 1 10000"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    UART.start_app("photos")
    RC.push(["down 1 3000", "ok 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["exit 3 3000"])
    UART.start_app("photos")
    RC.push(["down 1 3000", "ok 1 3000", "right 2 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["exit 3 3000"])
    UART.start_app("photos")
    RC.push(["down 1 3000", "ok 1 3000", "right 1 3000", "ok 1 15000"])
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
