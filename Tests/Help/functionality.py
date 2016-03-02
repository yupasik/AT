# Test name = Help
# Script dir = R:\Stingray\Tests\Help\functionality\functionality.py
# Rev = 1.04

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
    ScriptName = "functionality"
    ScriptIndex = "1"
    Grabber = DO.grab_define()
    platform = DO.load_platform()
    Modulation = "DVBS"
    FEC = "3/4"
    SR = "27500000"
    Stream = "\\036E_20000_LCN-25_20140418a.ts"
    Frequency = 1476
    Modulator = "1"
    COM = "COM7"
    settings = [ScriptName, ScriptIndex, Grabber, Modulation, FEC, SR, Stream, Frequency, Modulator, COM]
    DO.save_settings(settings)
    GRAB.start_capture()
    MOD.stop(Modulator)

    # macros
    searching_from_wizard_E501 = ["ok 1 2400", "ok 1 2400", "ok 1 2400", "right 1 2400", "ok 1 2400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_ALL = ["ok 1 2400", "ok 1 2400", "right 1 2400", "ok 1 2400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]

############################ TestCase 1 ##########################################
    testcase = 1
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    if platform in ["E501", "E502", "A230"]:
        RC.push(searching_from_wizard_E501)
    else:
        RC.push(searching_from_wizard_ALL)
    RC.push(["help 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    RC.push(["exit 3 1000", "menu", "left", "ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    RC.push(["right", "ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    RC.push(["exit 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    RC.push(["exit 1 2000", "ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    RC.push(["menu 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "exit 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "help 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["exit 3 2400", "3 1 5000", "help 1 2000", "last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("manual")
    RC.push(["exit 3 2400", "help 1 2000", "mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("manual")
    RC.push(["exit 3 2400", "help 1 2000", "stb 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    RC.push(["standby 1 15000", "standby 1 30000"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "ok 1 2000", "up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["down 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["left 2 1000"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["left", "ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    RC.push(["ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("active")
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "right 1 2000", "up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    RC.push(["down 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("active")
    RC.push(["right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("active")
    RC.push(["left 2 1000"])
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("active")
    RC.push(["right", "ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    status("active")
    RC.push(["ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    RC.push(["exit"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "ok 1 2000", "help 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "ok 1 2000", "VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 52 ##########################################
    testcase = 52
    status("manual")
    RC.push(["mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 53 ##########################################
    testcase = 53
    status("active")
    RC.push(["standby 1 15000", "standby 1 30000"])
    GRAB.compare(testcase)
############################ TestCase 54 ##########################################
    testcase = 54
    status("active")
    RC.push(["exit 3 2400", "3 1 5000", "help 1 2000", "ok 1 2000", "last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 55 ##########################################
    testcase = 55
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "ok 1 2000", "menu 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 56 ##########################################
    testcase = 56
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "ok 1 2000", "down 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 57 ##########################################
    testcase = 57
    status("active")
    RC.push(["up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 58 ##########################################
    testcase = 58
    status("active")
    RC.push(["right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 59 ##########################################
    testcase = 59
    status("active")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 60 ##########################################
    testcase = 60
    status("active")
    RC.push(["ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 61 ##########################################
    testcase = 61
    status("active")
    RC.push(["ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 62 ##########################################
    testcase = 62
    status("active")
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 63 ##########################################
    testcase = 63
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "ok 1 2000", "down 2 2400", "right 1 2000", "down 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 64 ##########################################
    testcase = 64
    status("active")
    RC.push(["up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 65 ##########################################
    testcase = 65
    status("active")
    RC.push(["right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 66 ##########################################
    testcase = 66
    status("active")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 67 ##########################################
    testcase = 67
    status("active")
    RC.push(["right 1 2400", "ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 68 ##########################################
    testcase = 68
    status("active")
    RC.push(["ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 69 ##########################################
    testcase = 69
    status("active")
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 70 ##########################################
    testcase = 70
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 71 ##########################################
    testcase = 71
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 72 ##########################################
    testcase = 72
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "right 1 2000", "ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 73 ##########################################
    testcase = 73
    status("active")
    RC.push(["exit 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 74 ##########################################
    testcase = 74
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 75 ##########################################
    testcase = 75
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "right 1 2000", "ok 1 2000", "help 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 76 ##########################################
    testcase = 76
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "right 1 2000", "ok 1 2000", "VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 77 ##########################################
    testcase = 77
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 78 ##########################################
    testcase = 78
    status("manual")
    RC.push(["mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 79 ##########################################
    testcase = 79
    status("active")
    RC.push(["standby 1 15000", "standby 1 30000"])
    GRAB.compare(testcase)
############################ TestCase 80 ##########################################
    testcase = 80
    status("active")
    RC.push(["exit 3 2400", "3 1 5000", "help 1 2000", "right 1 2000", "ok 1 2000", "last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 81 ##########################################
    testcase = 81
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "right 1 2000", "ok 1 2000", "menu 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 82 ##########################################
    testcase = 82
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "right 1 2000", "ok 1 2000", "down 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 83 ##########################################
    testcase = 83
    status("active")
    RC.push(["up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 84 ##########################################
    testcase = 84
    status("active")
    RC.push(["right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 85 ##########################################
    testcase = 85
    status("active")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 86 ##########################################
    testcase = 86
    status("active")
    RC.push(["ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 87 ##########################################
    testcase = 87
    status("active")
    RC.push(["ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 88 ##########################################
    testcase = 88
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "right 1 2000", "ok 1 2000", "right 1 2400", "down 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 89 ##########################################
    testcase = 89
    status("active")
    RC.push(["up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 90 ##########################################
    testcase = 90
    status("active")
    RC.push(["right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 91 ##########################################
    testcase = 91
    status("active")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 92 ##########################################
    testcase = 92
    status("active")
    RC.push(["ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 93 ##########################################
    testcase = 93
    status("active")
    RC.push(["ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 94 ##########################################
    testcase = 94
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "cinemahalls 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 95 ##########################################
    testcase = 95
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "help 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 96 ##########################################
    testcase = 96
    status("active")
    MOD.stop(Modulation)
    MOD.play(Modulation)
    UART.start_app("scheduler")
    RC.push(["red", "ok 1 2400", "down 2 1000", "ok 1 2000", "ok 1 2000", "right 1 1000", "up 2 1000", "ok 1 2000", "ok 1 2000", "exit 5 2400", "1 1 2400", "help 1 2000"])
    sleep(70)
    GRAB.compare(testcase)
############################ TestCase 97 ##########################################
    testcase = 97
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 98 ##########################################
    testcase = 98
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 99 ##########################################
    testcase = 99
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 100 ##########################################
    testcase = 100
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 101 ##########################################
    testcase = 101
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "VolUp 3 1000"])
    GRAB.compare(testcase)
############################ TestCase 102 ##########################################
    testcase = 102
    status("active")
    RC.push(["VolDown 3 1000"])
    GRAB.compare(testcase)
############################ TestCase 103 ##########################################
    testcase = 103
    status("manual")
    RC.push(["mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 104 ##########################################
    testcase = 104
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "guide 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 105 ##########################################
    testcase = 105
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "format 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 106 ##########################################
    testcase = 106
    status("active")
    RC.push(["exit 3 2400", "help 1 2000", "star 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 107 ##########################################
    testcase = 107
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 108 ##########################################
    testcase = 108
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 109 ##########################################
    testcase = 109
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 110 ##########################################
    testcase = 110
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 111 ##########################################
    testcase = 111
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 112 ##########################################
    testcase = 112
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 113 ##########################################
    testcase = 113
    status("manual")
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
