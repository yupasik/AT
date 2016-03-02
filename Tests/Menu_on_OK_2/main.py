# Test name = Menu_on_OK_2
# Script dir = R:\Stingray\Tests\Menu_on_OK_2\main\main.py
# Rev = 2.06

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
    TestName = "Menu_on_OK_2"
    ScriptName = "main"
    ScriptIndex = "1"
    Grabber = DO.grab_define()
    platform = DO.load_platform()
    Modulation = "DVBS"
    FEC = "3/4"
    SR = "27500000"
    Stream = "\\036E_20000_LCN-25_20140418a.ts"
    Stream_2 = "\\X_0000_00000_MUX_32000_EPG_Software_20130328a.ts"
    Frequency = 1476
    Modulator = "1"
    Modulator_2 = "2"
    COM = "COM7"
    settings = [ScriptName, ScriptIndex, Grabber, Modulation, FEC, SR, Stream, Frequency, Modulator, COM]
    DO.save_settings(settings)
    GRAB.start_capture()
    MOD.stop(Modulator)
    MOD.stop(Modulator_2)

    # macros
    searching_from_wizard_E501 = ["ok 1 2400", "ok 1 2400", "ok 1 2400", "right 1 2400", "ok 1 2400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_ALL = ["ok 1 2400", "ok 1 2400", "right 1 2400", "ok 1 2400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]

############################ TestCase 1 ##########################################
    """testcase = 1
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    OPER.search()
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    MOD.stop(Modulator)
    UART.default_settings()
    RC.push(["exit 2 2400", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    OPER.search()
    RC.push(["up 2 5000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    OPER.search()
    RC.push(["tv/radio 1 5000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    UART.default_settings()
    OPER.search()
    OPER.fav_create("123")
    RC.push(["blue 1 3000", "left 1 3000", "down 20 5000", "ok 2 5000", "exit 1 3000", "ok 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["blue 1 3000", "left 1 3000", "down 3 5000", "ok 2 5000", "exit 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 95 ##########################################
    testcase = 95
    status("inactive")
    #UART.default_settings()
    #if platform in ["E501", "E502", "A230"]:
    #    RC.push(searching_from_wizard_E501)
    #else:
    #    RC.push(searching_from_wizard_ALL)
    #GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream_2, Frequency, Modulator)
    UART.default_settings()
    OPER.search()
    RC.push(["ok 1 3000", "down 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["exit 1 1000"])
    OPER.fav_create("123")
    RC.push(["ok 1 3000", "down 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000", "down 1 1500"])
    OPER.channel_block()
    RC.push(["down 1 1500"])
    OPER.channel_block()
    RC.push(["exit 3 2400", "ok 1 3000", "down 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    OPER.search()
    RC.push(["ok 1 3000"])
    RC.push(["up 1 2400", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    RC.push(["up 1 2400", "ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "up 1 2000", "right", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "right 1 2000", "up 1 2000", "down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "up 1 2000", "right", "down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "up 1 2000", "mute"])
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("active")
    RC.push(["VolUp 2 2200"])
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("active")
    RC.push(["VolDown 2 2200"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "up 1 2000", "menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "up 1 2000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "up 1 2000", "last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "up 1 2000", "stb 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "up 1 2000", "tv/radio 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "up 1 2000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "down 1 3000", "ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    RC.push(["exit 2 3000", "ok 1 3000", "down 3 3000", "ChUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("active")
    RC.push(["ChDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    RC.push(["left 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    RC.push(["left 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    RC.push(["right 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("active")
    RC.push(["right 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("active")
    RC.push(["up 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("active")
    RC.push(["exit 2 3000", "0 1 5000", "ok 1 3000", "up 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    status("active")
    RC.push(["down 1 3000", "down 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    RC.push(["left 1 3000", "down 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    RC.push(["exit 1 2000", "OK 1 2000", "mute 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    RC.push(["VolUp 2 2000"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("active")
    RC.push(["VolDown 2 2000"])
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("active")
    RC.push(["menu 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    status("active")
    RC.push(["exit 3 2000", "ok 1 3000", "exit 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    status("active")
    RC.push(["exit 3 2000", "ok 1 3000", "last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 52 ##########################################
    testcase = 52
    status("active")
    RC.push(["exit 3 2000", "ok 1 3000", "stb 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 53 ##########################################
    testcase = 53
    status("active")
    RC.push(["exit 3 2000", "ok 1 3000", "tv/radio 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 54 ##########################################
    testcase = 54
    status("active")
    RC.push(["exit 3 2000", "ok 1 3000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 96 ##########################################
    testcase = 96
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["OK 1 2000", "red 1 2000", "down 1 1000", "left 1 1000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 97 ##########################################
    testcase = 97
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 98 ##########################################
    testcase = 98
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 99 ##########################################
    testcase = 99
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 100 ##########################################
    testcase = 100
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 101 ##########################################
    testcase = 101
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "up 15 5000"])
    GRAB.compare(testcase)
############################ TestCase 102 ##########################################
    testcase = 102
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "down 1 1000", "right 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 103 ##########################################
    testcase = 103
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["ok 1 3000", "left 1 1000", "down 30 5000"])
    GRAB.compare(testcase)
############################ TestCase 104 ##########################################
    testcase = 104
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "down 1 1000", "ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 105 ##########################################
    testcase = 105
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "mute 1 1000", "exit 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 106 ##########################################
    testcase = 106
    status("active")
    RC.push(["mute 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "VolUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 107 ##########################################
    testcase = 107
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "VolDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 108 ##########################################
    testcase = 108
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 109 ##########################################
    testcase = 109
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 110 ##########################################
    testcase = 110
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 111 ##########################################
    testcase = 111
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "stb 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 112 ##########################################
    testcase = 112
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "Tv/radio 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 113 ##########################################
    testcase = 113
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 114 ##########################################
    testcase = 114
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "OK 1 4500"])
    GRAB.compare(testcase)
############################ TestCase 115 ##########################################
    testcase = 115
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 116 ##########################################
    testcase = 116
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 117 ##########################################
    testcase = 117
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 118 ##########################################
    testcase = 118
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 119 ##########################################
    testcase = 119
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 120 ##########################################
    testcase = 120
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 121 ##########################################
    testcase = 121
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 122 ##########################################
    testcase = 122
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 123 ##########################################
    testcase = 123
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 124 ##########################################
    testcase = 124
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 125 ##########################################
    testcase = 125
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "mute 1 1000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 126 ##########################################
    testcase = 126
    status("active")
    RC.push(["mute 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 127 ##########################################
    testcase = 127
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "down 1 1000", "VolDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 128 ##########################################
    testcase = 128
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 129 ##########################################
    testcase = 129
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 130 ##########################################
    testcase = 130
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 131 ##########################################
    testcase = 131
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "stb 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 132 ##########################################
    testcase = 132
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "Tv/radio 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 133 ##########################################
    testcase = 133
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000"])
    RC.push(["OK 1 2000", "standby 1 8000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 55 ##########################################
    testcase = 55
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["up 1 2400", "ok 1 3000", "exit 1 2000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 56 ##########################################
    testcase = 56
    status("active")
    RC.push(["exit 3 2000", "ok 1 3000", "up 2 2000", "right", "down", "exit 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 57 ##########################################
    testcase = 57
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["ok 1 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 58 ##########################################
    testcase = 58
    status("active")
    RC.push(["right 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 59 ##########################################
    testcase = 59
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 60 ##########################################
    testcase = 60
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 61 ##########################################
    testcase = 61
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 62 ##########################################
    testcase = 62
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 63 ##########################################
    testcase = 63
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 64 ##########################################
    testcase = 64
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 65 ##########################################
    testcase = 65
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 66 ##########################################
    testcase = 66
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 67 ##########################################
    testcase = 67
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 68 ##########################################
    testcase = 68
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 69 ##########################################
    testcase = 69
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 70 ##########################################
    testcase = 70
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 71 ##########################################
    testcase = 71
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 72 ##########################################
    testcase = 72
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 73 ##########################################
    testcase = 73
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 74 ##########################################
    testcase = 74
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 75 ##########################################
    testcase = 75
    status("active")
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 76 ##########################################
    testcase = 76
    status("active")
    OPER.fav_create("76")
    RC.push(["0 1 5000", "ok 1 3000", "up 1 2000", "left 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 94 ##########################################
    testcase = 94
    status("inactive")
    UART.default_settings()
    OPER.search()
    RC.push(["up 1 1000", "down 1 1000", "down 1 1000"])
    OPER.fav_create("94")
    RC.push(["0 1 4000", "OK 1 1000", "up 1 1000", "left 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 77 ##########################################
    testcase = 77
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream_2, Frequency, Modulator)
    UART.default_settings()
    OPER.search()
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 78 ##########################################
    testcase = 78
    status("active")
    OPER.fav_create("11111222223333344444555556666677777888889999900000")
    RC.push(["0 1 5000", "ok 1 3000", "up 1 2000", "right 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 79 ##########################################
    testcase = 79
    status("inactive")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    OPER.search()
    OPER.fav_create("79")
    RC.push(["0 1 5000", "ok 1 3000", "up 1 2000", "left 3 3000", "down 2 2000", "ok 1 5000", "last 1 1000", "OK 1 5000", "exit 1 3000", "red 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 80 ##########################################
    testcase = 80
    status("inactive")
    UART.default_settings()
    OPER.search()
    RC.push(["red 1 2000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 81 ##########################################
    testcase = 81
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream_2, Frequency, Modulator)
    OPER.search()
    UART.start_app("channelseditor")
    RC.push(["right 1 3000", "down 1 1500"])
    OPER.channel_block()
    RC.push(["down 1 1500"])
    OPER.channel_block()
    RC.push(["exit 3 2400", "ok 1 3000"])
    GRAB.compare(testcase) 
############################ TestCase 153 ##########################################
    testcase = 153
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 154 ##########################################
    testcase = 154
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 82 ##########################################
    testcase = 82
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 83 ##########################################
    testcase = 83
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 84 ##########################################
    testcase = 84
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["exit 5 2400", "ok 1 3000", "green 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 85 ##########################################
    testcase = 85
    status("active")
    RC.push(["exit 5 2400", "ok 1 3000", "yellow 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 86 ##########################################
    testcase = 86
    status("active")
    RC.push(["exit 5 2400", "ok 1 3000", "blue 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 87 ##########################################
    testcase = 87
    status("active")
    RC.push(["exit 5 2400", "ok 1 3000", "red 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 88 ##########################################
    testcase = 88
    status("active")
    MOD.stop(Modulator)
    MOD.play(Modulator)
    RC.push(["red 1 1000", "exit 3 3400"])
    UART.start_app("scheduler")
    RC.push(["red", "ok 1 3000", "down 2 1000", "ok", "ok", "right 1 1000", "up", "ok", "ok", "exit 5 2400", "ok 1 5000"])
    sleep(45)
    GRAB.compare(testcase)
############################ TestCase 155 ##########################################
    testcase = 155
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 89 ##########################################
    testcase = 89
    status("active")
    RC.push(["exit 5 2400", "ok 1 3000", "cinemahalls"])
    GRAB.compare(testcase)
############################ TestCase 90 ##########################################
    testcase = 90
    status("active")
    RC.push(["exit 5 2400", "ok 1 3000", "help"])
    GRAB.compare(testcase)
############################ TestCase 91 ##########################################
    testcase = 91
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 92 ##########################################
    testcase = 92
    status("active")
    RC.push(["exit 5 2400", "3 1 3000"])
    OPER.set_pin()
    OPER.block(1)
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "ok 1 3000", "up 1 1000", "up 1 100000", "ok 1 10000"])
    GRAB.compare(testcase)
############################ TestCase 93 ##########################################
    testcase = 93
    status("manual")
    GRAB.compare(testcase)"""
############################ TestCase 152 ##########################################
    testcase = 152
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    UART.reboot()
    RC.push(["exit 1 10000", "OK 1 1000", "red 1 1000", "left 1 1000", "down 10 1000", "right 1 1000", "down 1 1000", "down 1 1000", "OK 1 10000", "OK 1 1000", "red 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 134 ##########################################
    testcase = 134
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 1 1000", "up 1 3000", "up 1 3000", "up 1 3000", "last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 135 ##########################################
    testcase = 135
    status("inactive")
    RC.push(["exit 1 1000", "0 1 3500", "ok 1 3000", "up 1 3000", "left 1 2000", "left 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 136 ##########################################
    testcase = 136
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 1 1000", "last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 137 ##########################################
    testcase = 137
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 1 1000", "0 1 3000", "up 1 2000", "up 1 2000", "up 1 2000", "up 1 2000", "up 1 2000", "up 1 2000", "up 1 2000", "up 1 2000", "up 1 2000", "Tv/radio 1 2000", "up 1 2000", "up 1 2000", "up 1 2000", "up 1 2000", "last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 138 ##########################################
    testcase = 138
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 139 ##########################################
    testcase = 139
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 151 ##########################################
    testcase = 151
    status("active")
    UART.default_settings()
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000", "last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 140 ##########################################
    testcase = 140
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 1 1000", "0 1 3000", "up 1 3000", "up 1 3000", "up 1 3000", "last 1 3000", "down 1 3000", "down 1 3000", "OK 1 4000", "last 1 3000"])        
    GRAB.compare(testcase)
############################ TestCase 141 ##########################################
    testcase = 141
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 1 1000", "OK 1 1000", "up 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "OK 1 4000", "OK 1 1000", "up 1 1000", "left 1 1000", "left 1 1000", "down 1 1000", "down 1 1000", "OK 1 4000", "last 1 1000", "OK 1 4000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 142 ##########################################
    testcase = 142
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 1 1000"])
    OPER.fav_create("142")
    RC.push(["OK 1 1000", "up 1 1000", "left 1 1000", "left 1 1000", "OK 1 1000", "down 1 1000", "OK 1 1000"])
    RC.push(["Tv/radio 1 1000"])
    RC.push(["last 1 1000", "OK 1 4000", "OK 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 143 ##########################################
    testcase = 143
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 1 1000"])
    OPER.fav_create("143")
    RC.push(["OK 1 1000", "up 1 1000", "left 1 1000", "left 1 1000", "left 1 1000", "OK 1 1000", "down 1 1000", "OK 1 1000"])
    RC.push(["OK 1 1000", "up 1 1000", "up 1 1000", "left 1 1000", "OK 1 1000", "right 1 1000", "OK 1 1000"])
    RC.push(["OK 1 1000", "up 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "OK 1 1000", "down 1 1000", "OK 1 1000"])
    RC.push(["last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 144 ##########################################
    testcase = 144
    status("active")
    RC.push(["exit 1 1000", "0 1 4000", "last 1 1000", "OK 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 145 ##########################################
    testcase = 145
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 1 1000"])
    OPER.fav_create("123")
    RC.push(["OK 1 1000", "up 1 1000", "left 1 1000", "left 1 1000", "left 1 1000", "OK 1 1000", "down 1 1000", "down 1 1000", "OK 1 1000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 1000", "right 1 1000", "down 1 1000", "down 1 1000", "OK 1 1000", "right 1 1000", "OK 1 1000", "left 1 1000", "OK 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 146 ##########################################
    testcase = 146
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 1 1000"])
    OPER.fav_create("123")
    RC.push(["OK 1 1000", "up 1 1000", "left 1 1000", "left 1 1000", "left 1 1000", "OK 1 1000", "down 1 1000", "down 1 1000", "OK 1 5000"])
    RC.push(["OK 1 1000", "down 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "OK 1 5000"]) 
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 1000", "right 1 1000", "down 1 1000", "down 1 1000", "OK 1 1000", "right 1 1000", "OK 1 1000", "left 1 1000", "OK 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 147 ##########################################
    testcase = 147
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["ok 1 1000", "up 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 148 ##########################################
    testcase = 148
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 149 ##########################################
    testcase = 149
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 150 ##########################################
    testcase = 150
    status("manual")
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
