# Test name = ManualSearch
# Script dir = R:\Stingray\Tests\ManualSearch\manual_search\manual_search.py
# Rev = 1.07

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
    ScriptName = "manual_search"
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

############################ TestCase 1 ##########################################
    testcase = 1
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    RC.push(["exit 2 2400"])
    UART.activate_app("dvbsmanualscanner")
    UART.start_app("dvbsmanualscanner")
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    RC.push(["menu 1 3000"])
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
    UART.start_app("dvbsmanualscanner")
    RC.push(["standby 1 5000", "standby 1 20000"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    RC.push(["exit 1 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    RC.push(["last 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    UART.start_app("dvbsmanualscanner")
    RC.push(["up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["down 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    RC.push(["down 4 2400", "right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 183 ##########################################
    testcase = 183
    status("active")
    RC.push(["left 1 2400", "up 2 2000", "right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 184 ##########################################
    testcase = 184
    status("active")
    RC.push(["left 1 2400", "up 1 2000", "right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    RC.push(["down 1 2000", "left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["right 1 2400", "up 1 2000", "left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 185 ##########################################
    testcase = 185
    status("active")
    RC.push(["0 1 2400", "down 2 2000", "left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["right 1 2000"])
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    RC.push(["up 3 2000", "ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 186 ##########################################
    testcase = 186
    status("active")
    RC.push(["down 2 2000", "ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    RC.push(["ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["down 2 2400", "ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["up 2 2400", "ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["down 2 2400", "ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    if platform in ["U210CI"]:
        RC.push(["up 6 2400"])
    else:
        RC.push(["up 5 2400"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("manual")
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
    status("active")
    UART.start_app("dvbsmanualscanner")
    if platform in ["U210CI"]:
        RC.push(["up 2 2400"])
    else:
        RC.push(["up 1 2400"])
    RC.push(["last 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("active")
    UART.start_app("dvbsmanualscanner")
    if platform in ["U210CI"]:
        RC.push(["up 2 2400"])
    else:
        RC.push(["up 1 2400"])
    RC.push(["up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("active")
    RC.push(["right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("active")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("active")
    RC.push(["down 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("active")
    RC.push(["up 1 2000", "mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("active")
    RC.push(["standby 1 5000", "standby 1 20000"])
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("active")
    RC.push(["exit 1 2400"])
    UART.start_app("dvbsmanualscanner")
    if platform in ["U210CI"]:
        RC.push(["up 2 2400"])
    else:
        RC.push(["up 1 2400"])
    RC.push(["VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 182 ##########################################
    testcase = 182
    status("active")
    RC.push(["exit 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("active")
    RC.push(["ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    RC.push(["ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["exit 3 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["menu 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    UART.start_app("dvbsmanualscanner")
    RC.push(["up 1 2400", "last 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    UART.start_app("dvbsmanualscanner")
    RC.push(["up 1 2400", "right 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["down 2 2400"])
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["up 1 2400", "mute"])
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["standby 1 5400", "standby 1 10000"])
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["up 1 2400", "VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 52 ##########################################
    testcase = 52
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 53 ##########################################
    testcase = 53
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["ok 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 54 ##########################################
    testcase = 54
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["ChUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 55 ##########################################
    testcase = 55
    if platform == "U210CI":
        status("active")
    else:
        status("inactive")
    RC.push(["ChDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 56 ##########################################
    testcase = 56
    status("inactive")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 57 ##########################################
    testcase = 57
    status("inactive")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 58 ##########################################
    testcase = 58
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 59 ##########################################
    testcase = 59
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 60 ##########################################
    testcase = 60
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 61 ##########################################
    testcase = 61
    status("inactive")
    UART.start_app("dvbsmanualscanner")
    RC.push(["up 1 2400", "last 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 62 ##########################################
    testcase = 62
    status("inactive")
    UART.start_app("dvbsmanualscanner")
    RC.push(["up 1 2400", "right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 63 ##########################################
    testcase = 63
    status("inactive")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 64 ##########################################
    testcase = 64
    status("inactive")
    RC.push(["up 1 2400", "up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 65 ##########################################
    testcase = 65
    status("inactive")
    RC.push(["down 2 2400"])
    GRAB.compare(testcase)
############################ TestCase 66 ##########################################
    testcase = 66
    status("inactive")
    RC.push(["up 1 2400", "mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 67 ##########################################
    testcase = 67
    status("inactive")
    RC.push(["standby 1 5000", "standby 1 20000"])
    GRAB.compare(testcase)
############################ TestCase 68 ##########################################
    testcase = 68
    status("inactive")
    RC.push(["exit 1 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["up 1 2400", "VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 69 ##########################################
    status("inactive")
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 70 ##########################################
    testcase = 70
    status("inactive")
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 71 ##########################################
    testcase = 71
    status("inactive")
    RC.push(["ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 72 ##########################################
    testcase = 72
    status("inactive")
    RC.push(["ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 73 ##########################################
    testcase = 73
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    GRAB.compare(testcase)
############################ TestCase 74 ##########################################
    testcase = 74
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 75 ##########################################
    testcase = 75
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 76 ##########################################
    testcase = 76
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 77 ##########################################
    testcase = 77
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 78 ##########################################
    testcase = 78
    status("active")
    UART.start_app("dvbsmanualscanner")
    RC.push(["last 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 79 ##########################################
    testcase = 79
    status("active")
    UART.start_app("dvbsmanualscanner")
    RC.push(["up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 80 ##########################################
    testcase = 80
    status("active")
    RC.push(["down 2 2400"])
    GRAB.compare(testcase)
############################ TestCase 81 ##########################################
    testcase = 81
    status("active")
    RC.push(["up 1 2400", "right 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 82 ##########################################
    testcase = 82
    status("active")
    RC.push(["1 1 2400", "left 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 83 ##########################################
    testcase = 83
    status("active")
    RC.push(["up 1 2400", "mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 84 ##########################################
    testcase = 84
    status("active")
    RC.push(["standby 1 5000", "standby 1 20000"])
    GRAB.compare(testcase)
############################ TestCase 85 ##########################################
    testcase = 85
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 86 ##########################################
    testcase = 86
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 87 ##########################################
    testcase = 87
    status("active")
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 88 ##########################################
    testcase = 88
    status("active")
    RC.push(["ok 1 2400", "ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 89 ##########################################
    testcase = 89
    status("active")
    RC.push(["ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 90 ##########################################
    testcase = 90
    status("active")
    RC.push(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 91 ##########################################
    testcase = 91
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 92 ##########################################
    testcase = 92
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 93 ##########################################
    testcase = 93
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 94 ##########################################
    testcase = 94
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 95 ##########################################
    testcase = 95
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 96 ##########################################
    testcase = 96
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 1 2400", "last 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 97 ##########################################
    testcase = 97
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 1 2400", "right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 98 ##########################################
    testcase = 98
    status("active")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 99 ##########################################
    testcase = 99
    status("active")
    RC.push(["9 1 2000", "exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 1 2400", "up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 100 ##########################################
    testcase = 100
    status("active")
    RC.push(["down 2 2400"])
    GRAB.compare(testcase)
############################ TestCase 101 ##########################################
    testcase = 101
    status("active")
    RC.push(["up 1 2400", "mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 102 ##########################################
    testcase = 102
    status("active")
    RC.push(["standby 1 5000", "standby 1 20000"])
    GRAB.compare(testcase)
############################ TestCase 103 ##########################################
    testcase = 103
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 1 2400", "VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 104 ##########################################
    testcase = 104
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 105 ##########################################
    testcase = 105
    status("active")
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 106 ##########################################
    testcase = 106
    status("active")
    RC.push(["ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 107 ##########################################
    testcase = 107
    status("active")
    RC.push(["ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 108 ##########################################
    testcase = 108
    status("active")
    RC.push(["left 5 2400", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 109 ##########################################
    testcase = 109
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 2 2400"])
    GRAB.compare(testcase)
############################ TestCase 110 ##########################################
    testcase = 110
    status("active")
    RC.push(["menu 1 2400"])
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
############################ TestCase 114 ##########################################
    testcase = 114
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 2 2400", "last 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 115 ##########################################
    testcase = 115
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 2 2400", "right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 116 ##########################################
    testcase = 116
    status("active")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 117 ##########################################
    testcase = 117
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 2 2400", "up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 118 ##########################################
    testcase = 118
    status("active")
    RC.push(["down 2 2400"])
    GRAB.compare(testcase)
############################ TestCase 119 ##########################################
    testcase = 119
    status("active")
    RC.push(["up 1 2400", "mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 120 ##########################################
    testcase = 120
    status("active")
    RC.push(["standby 1 5000", "standby 1 20000"])
    GRAB.compare(testcase)
############################ TestCase 121 ##########################################
    testcase = 121
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 2 2400", "VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 122 ##########################################
    testcase = 122
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 123 ##########################################
    testcase = 123
    status("active")
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 124 ##########################################
    testcase = 124
    status("active")
    RC.push(["ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 125 ##########################################
    testcase = 125
    status("active")
    RC.push(["ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 126 ##########################################
    testcase = 126
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 3 2400"])
    GRAB.compare(testcase)
############################ TestCase 127 ##########################################
    testcase = 127
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 128 ##########################################
    testcase = 128
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 129 ##########################################
    testcase = 129
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 130 ##########################################
    testcase = 130
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 131 ##########################################
    testcase = 131
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 3 2400", "right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 132 ##########################################
    testcase = 132
    status("active")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 133 ##########################################
    testcase = 133
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 3 2400", "last 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 134 ##########################################
    testcase = 134
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 3 2400", "up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 135 ##########################################
    testcase = 135
    status("active")
    RC.push(["down 2 2400"])
    GRAB.compare(testcase)
############################ TestCase 136 ##########################################
    testcase = 136
    status("active")
    RC.push(["up 1 2400", "mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 137 ##########################################
    testcase = 137
    status("active")
    RC.push(["standby 1 5000", "standby 1 20000"])
    GRAB.compare(testcase)
############################ TestCase 138 ##########################################
    testcase = 138
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 3 2400", "VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 139 ##########################################
    testcase = 139
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 140 ##########################################
    testcase = 140
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 141 ##########################################
    testcase = 141
    status("active")
    RC.push(["ok 1 3000", "ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 142 ##########################################
    testcase = 142
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 143 ##########################################
    testcase = 143
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 4 2400"])
    GRAB.compare(testcase)
############################ TestCase 144 ##########################################
    testcase = 144
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 145 ##########################################
    testcase = 145
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 146 ##########################################
    testcase = 146
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 147 ##########################################
    testcase = 147
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 148 ##########################################
    testcase = 148
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 4 2400", "right 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 149 ##########################################
    testcase = 149
    status("active")
    RC.push(["left 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 150 ##########################################
    testcase = 150
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 4 2400", "last 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 151 ##########################################
    testcase = 151
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 4 2400", "up 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 152 ##########################################
    testcase = 152
    status("active")
    RC.push(["down 2 2400"])
    GRAB.compare(testcase)
############################ TestCase 153 ##########################################
    testcase = 153
    status("active")
    RC.push(["up 1 2400", "mute 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 154 ##########################################
    testcase = 154
    status("active")
    RC.push(["standby 1 5000", "standby 1 20000"])
    GRAB.compare(testcase)
############################ TestCase 155 ##########################################
    testcase = 155
    status("active")
    RC.push(["exit 2 2400"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["down 4 2400", "VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 156 ##########################################
    testcase = 156
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 157 ##########################################
    testcase = 157
    status("active")
    RC.push(["ok 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 158 ##########################################
    testcase = 158
    status("active")
    RC.push(["ChUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 159 ##########################################
    testcase = 159
    status("active")
    RC.push(["ChDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 160 ##########################################
    testcase = 160
    status("active")
    UART.default_settings()
    RC.push(["exit 2 2400"])
    UART.activate_app("dvbsmanualscanner")
    UART.start_app("dvbsmanualscanner")
    RC.push(["1", "2", "2", "2", "6 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 161 ##########################################
    testcase = 161
    status("active")
    GRAB.compare(testcase)
############################ TestCase 162 ##########################################
    testcase = 162
    status("active")
    RC.push(["down 5 2400", "ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 163 ##########################################
    testcase = 163
    status("active")
    UART.default_settings()
    RC.push(["exit 2 2400"])
    UART.activate_app("dvbsmanualscanner")
    UART.start_app("dvbsmanualscanner")
    GRAB.compare(testcase)
############################ TestCase 164 ##########################################
    testcase = 164
    status("active")
    GRAB.compare(testcase)
############################ TestCase 165 ##########################################
    testcase = 165
    status("active")
    RC.push(["ok 1 20000"])
    GRAB.compare(testcase)
############################ TestCase 166 ##########################################
    testcase = 166
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 167 ##########################################
    testcase = 167
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 168 ##########################################
    testcase = 168
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 169 ##########################################
    testcase = 169
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 170 ##########################################
    testcase = 170
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 171 ##########################################
    testcase = 171
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 172 ##########################################
    testcase = 172
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 173 ##########################################
    testcase = 173
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 174 ##########################################
    testcase = 174
    status("manual")
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
