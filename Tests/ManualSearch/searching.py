# Test name = ManualSearch
# Script dir = R:\Stingray\Tests\ManualSearch\searching\searching.py

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
    ScriptName = "searching"
    ScriptIndex = "2"
    Grabber = DO.grab_define()
    platform = DO.load_platform()
    Modulation = "DVBS"
    FEC = "3/4"
    SR = "27500000"
    Stream = "\\X_0000_00000_MUX_32000_EPG_Software_20130328a.ts"
    Stream_2 = "\\S_036E_12226_ASI_27500_3k_TTX_20110707a.ts"
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
    MOD.play_stream(Modulation, FEC, SR, Stream_2, Frequency, Modulator)
    UART.default_settings()
    RC.push(["exit 2 2400"])
    UART.activate_app("dvbsmanualscanner")
    UART.start_app("dvbsmanualscanner")
    RC.push(["1", "2", "2", "2", "6", "ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6", "ok 1 1500", "menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6", "ok 1 2500", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6", "ok 1 2500", "last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6", "ok 1 1500", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6", "ok 1 1500", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6", "ok 1 2500", "VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6", "ok 1 2500", "VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6", "ok 1 2500", "mute 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 20000"])
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6", "ok 1 2500", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6", "ok 1 1500", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6", "ok 1 7500", "menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 70000"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 20000", "right", "ok 1 5000", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 20000", "ok 1 5000", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    UART.default_settings()
    RC.push(["exit 2 2400"])
    UART.activate_app("dvbsmanualscanner")
    UART.start_app("dvbsmanualscanner")
    RC.push(["1", "2", "2", "2", "6 1 2000", "ok 1 20000", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 20000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 20000", "mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 20000", "VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("active")
    MOD.stop(Modulator)
    UART.default_settings()
    RC.push(["exit 2 2400"])
    UART.activate_app("dvbsmanualscanner")
    UART.start_app("dvbsmanualscanner")
    RC.push(["1", "2", "2", "2", "6", "ok 1 70000"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("active")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("active")
    RC.push(["right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("active")
    RC.push(["left 1 2400", "ok 1 30000"])
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("active")
    RC.push(["ok 1 30400", "right 1 2000", "ok 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 20000", "exit 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 20000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 20000", "mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("active")
    RC.push(["VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("active")
    MOD.pause(Modulator)
    UART.default_settings()
    RC.push(["exit 2 2400"])
    UART.activate_app("dvbsmanualscanner")
    UART.start_app("dvbsmanualscanner")
    RC.push(["3 1 2000", "4 1 2000", "0 1 2000", "0 1 2000", "down 5 2400", "ok 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("active")
    RC.push(["ok 1 5000", "left", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    RC.push(["right", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 6 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 20000"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    RC.push(["right", "ok 1 5000", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "ok 1 20000", "ok 1 5000", "exit 3 5000"])
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
