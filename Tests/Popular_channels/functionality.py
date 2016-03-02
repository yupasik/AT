# Test name = Popular_channels
# Script dir = R:\Stingray\Tests\Popular_channels\functionality\functionality.py
# Rev = v.1.01

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
    TestName = "Popular_channels"
    ScriptName = "functionality"
    ScriptIndex = "1"
    Grabber = DO.grab_define()
    platform = DO.load_platform()
    Modulation = "DVBS"
    FEC = "3/4"
    SR = "27500000"
    Stream = "\\12226MHz.ts"
    Stream2 = "\\036E_LCN-01_20140409a.ts"
    Frequency = 1476
    Modulator = "1"
    Modulator2 = "2"
    COM = "COM7"
    settings = [ScriptName, ScriptIndex, Grabber, Modulation, FEC, SR, Stream, Frequency, Modulator, COM]
    DO.save_settings(settings)
    GRAB.start_capture()
    MOD.stop(Modulator)
    MOD.stop(Modulator2)

############################ TestCase 1 ##########################################
#    testcase = 1
#    status("active")
#    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
#    UART.default_settings()
#    UART.start_app("")
#    RC.push(["key_1", "key_2", "key_3"])    # set of the RC buttons
#    sleep(0)
#    RC.push("[macros_name]")    # RC macros from remote_control.ini file
#    GRAB.compare(testcase)
############################ TestCase 1 ##########################################
    """testcase = 1
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    RC.push(["down 1 5500"])
    UART.start_app("mostPopular")
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    UART.default_settings()
    RC.push(["Exit 2 500"])
    UART.start_app("mostPopular")
    sleep(5)
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("manual")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    RC.push(["down 1 5500"])
    UART.start_app("mostPopular")
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    RC.push(["0 1 20000", "up 1 40000", "up 1 60000", "up 1 80000", "up 1 100000", "up 1 500"])
    UART.start_app("mostPopular")
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    RC.push(["exit 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    UART.start_app("mostPopular")
    RC.push(["menu 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    RC.push(["standby 1 17000", "standby 1 15000"])
    UART.start_app("mostPopular")
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("manual")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    GRAB.compare(testcase)"""
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["exit 2 2000"])
    UART.start_app("mostPopular")
    RC.push(["ok"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("manual")
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    UART.start_app("wizard")
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    RC.push(["0 1 20000", "up 1 40000", "up 1 60000", "up 1 80000", "up 1 100000"])
    UART.start_app("mostPopular")
    RC.push(["down 1 1500", "ok 1 5500", "exit 1 1500", "red 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(3)
    RC.push(["up 1 10000", "up 1 15000", "up 1 20000", "up 1 25000", "up 1 30000", "up 1 35000", "up 1 40000", "up 1 45000", "up 1 1500", "standby 1 7000", "standby 1 10000", "down 1 500", "down 1 500", "down 1 500", "down 1 500", "down 1 500", "down 1 500", "down 1 500", "down 1 500", "down 1 1500"])
    UART.start_app("mostPopular")
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("manual")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("manual")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(1)
    RC.push(["down 1 5500"])
    UART.start_app("mostPopular")
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["exit 1 2000"])
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(3)
    RC.push(["0 1 5500", "down 1 300000", "down 1 240000", "down 1 5000", "standby 1 600000", "standby 1 25000"])
    UART.start_app("mostPopular")
    sleep(3)
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(3)
    RC.push(["0 1 5500", "up 1 10000", "up 1 15000", "up 1 20000", "up 1 25000", "up 1 30000", "up 1 35000", "up 1 40000", "up 1 45000", "cinemahalls 1 15000", "right 1 1500", "OK 1 1500", "OK 1 240000", "exit 1 1500", "OK 1 1500", "exit 1 1500", "exit 1 1500"])
    UART.start_app("mostPopular")
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(3)
    RC.push(["0 1 5500", "up 1 10000", "up 1 15000", "up 1 20000", "up 1 25000", "up 1 30000", "up 1 35000", "up 1 40000", "up 1 45000", "up 1 50000", "up 1 55000"])
    UART.start_app("mostPopular")
    RC.push(["red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["exit"])
    UART.start_app("settings")
    RC.push(["exit", "right", "right", "right", "right", "right", "right", "down", "ok", "1", "1", "1", "1", "1", "1", "1", "1", "OK", "exit", "exit", "exit"])
    UART.start_app("channelseditor")
    RC.push(["right 1 1000"])
    OPER.channel_block()
    RC.push(["exit 1 1000", "exit 1 1000"])
    UART.start_app("mostPopular")
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    RC.push(["down 1 5500", "www 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["www 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    UART.reboot()
    RC.push(["exit 1 1500", "down 1 5500", "www 1 1500", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    UART.reboot()
    RC.push(["exit 1 1500", "down 1 5500", "www 1 1500", "last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("active")
    UART.reboot()
    RC.push(["exit 1 1500", "down 1 5500", "www 1 1500", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("active")
    UART.reboot()
    sleep(30)
    RC.push(["OK 1 1000", "exit 1 1000", "exit 1 1000", "down 1 5500", "www 1 1500", "www 1 1500", "menu 1 1500", "down 1 1500", "OK 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    RC.push(["www 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("active")
    UART.reboot()
    RC.push(["exit 1 1500", "down 1 5500", "1 1 1500", "9 1 1500", "1 1 1500", "www 1 1500", "www 1 1500", "menu 1 1500", "down 1 1500", "OK 1 1500", "exit 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    UART.reboot()
    RC.push(["www 1 1500", "www 1 1500", "down 1 5500", "menu 1 1500", "down 1 1500", "OK 1 1500", "last 1 3500", "red 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    UART.reboot()
    sleep(30)
    RC.push(["OK 1 1000", "exit 1 1000", "exit 1 1500", "down 1 5000", "www 1 1500", "www 1 1500", "menu 1 1500", "down 1 1500", "OK 1 1500", "menu 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(3)
    RC.push(["down 1 5500"])
    UART.start_app("mostPopular")
    sleep(3)
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("active")
    RC.push(["VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    status("active")
    RC.push(["ChUp 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    RC.push(["ChDown 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    RC.push(["up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    RC.push(["down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("active")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("active")
    RC.push(["left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    status("active")
    RC.push(["exit 1 1000", "down 1 4000", "www 1 1000", "ok 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    status("active")
    RC.push(["exit 1 1000", "down 1 5500", "www 1 1000", "standby 1 10000", "standby 1 10000"])
    GRAB.compare(testcase)
############################ TestCase 52 ##########################################
    testcase = 52
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 53 ##########################################
    testcase = 53
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 54 ##########################################
    testcase = 54
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 55 ##########################################
    testcase = 55
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(30)
    RC.push(["OK 1 1000", "exit 1 1000", "exit 1 1000", "0 1 5500", "down 1 120000"])
    UART.start_app("settings")
    RC.push(["exit", "right", "right", "right", "right", "right", "right", "down", "ok", "1", "1", "1", "1", "1", "1", "1", "1", "OK", "exit", "exit", "exit"])
    UART.start_app("channelseditor")
    RC.push(["right", "exit", "exit", "0 1 5500", "down 1 5500", "www 1 1000", "2 1 5500"])
    OPER.channel_block()
    RC.push(["down 1 1000"])
    OPER.channel_block()
    RC.push(["down 1 1000"])
    OPER.channel_block()
    RC.push(["down 1 1000"])
    OPER.channel_block()
    RC.push(["exit", "exit", "exit 1 3000", "0 1 5500", "down 1 5500", "www 1 1000", "2 1 5500"])
    GRAB.compare(testcase)
############################ TestCase 56 ##########################################
    testcase = 56
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(3)
    UART.activate_app("dvbsmanualscanner")
    RC.push(["0 1 5500", "down 1 120000", "down 1 90000", "down 1 60000", "down 1 5500"])
    UART.start_app("dvbsmanualscanner")
    sleep(60)
    RC.push(["exit"])
    UART.start_app("mostPopular")
    sleep(5)
    GRAB.compare(testcase)
############################ TestCase 57 ##########################################
    testcase = 57
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(3)
    UART.activate_app("dvbsmanualscanner")
    RC.push(["0 1 5500", "down 1 120000", "down 1 90000", "down 1 60000", "down 1 5500"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["1", "2", "2", "2", "6", "OK 1 5000", "OK 1 5000", "exit 1 1500", "exit 1 1500"])
    sleep(50)
    RC.push(["exit 1 1500", "exit 1 1500", "exit 1 1500"])
    UART.start_app("mostPopular")
    sleep(5)
    GRAB.compare(testcase)
############################ TestCase 58 ##########################################
    testcase = 58
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(3)
    RC.push(["0 1 5500", "down 1 120000", "down 1 90000", "down 1 60000", "down 1 5500"])
    UART.start_app("tricolorsearch")
    sleep(60)
    RC.push(["exit 1 1500", "exit 1 1500", "exit 1 1500"])
    UART.start_app("mostPopular")
    sleep(5)
    GRAB.compare(testcase)
############################ TestCase 59 ##########################################
    testcase = 59
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(3)
    RC.push(["0 1 5500", "down 1 120000", "down 1 90000", "down 1 60000", "down 1 5500"])
    UART.start_app("tvmail")
    sleep(60)
    RC.push(["exit 1 1500", "exit 1 1500", "exit 1 1500"])
    UART.start_app("mostPopular")
    sleep(5)
    GRAB.compare(testcase)
############################ TestCase 60 ##########################################
    testcase = 60
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 61 ##########################################??????????????????????????????
    testcase = 61
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 62 ##########################################
    testcase = 62
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    if platform in ["E501", "E502", "A230"]:
        RC.push(["ok 1 2000", "ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 30000", "ok 1 400000", "ok 1 5000", "ok 1 10000", "exit 2 2000"])
    else:
        RC.push(["ok 1 2000", "ok 1 2000", "right 1 2000", "ok 1 2000", "ok 1 15000", "ok 1 180000", "ok 1 5000", "exit 2 2000"])
    sleep(30)
    RC.push(["OK 1 1000", "exit 1 1000", "exit 1 1000", "0 1 5500", "up 1 120000", "up 1 240000", "0 1 5500"])
    UART.reboot()
    sleep(5)
    RC.push(["exit 1 1000", "up 1 4000"])
    UART.start_app("mostPopular")
    sleep(5)
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
