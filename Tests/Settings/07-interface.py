# Test name = Settings
# Script dir = R:\Stingray\Tests\Settings\07-interface\07-interface.py

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
    ScriptName = "07-interface"
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
    searching_from_wizard_E501 = ["ok 1 2400", "ok 1 2400", "ok 1 2400", "right 1 2400", "ok 1 2400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_ALL = ["ok 1 2400", "ok 1 2400", "right 1 2400", "ok 1 2400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]

############################ TestCase 1 ##########################################
    testcase = 1
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000"])
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
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["up 1 1000", "up 1 1000", "up 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("manual")
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
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    RC.push(["right 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    RC.push(["menu 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    RC.push(["exit 1 7500", "red 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["exit 1 1000", "blue 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["exit 1 1000", "2 1 5000", "0 1 5000"])
    UART.start_app("mostPopular")
    RC.push(["down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["exit 1 1000", "ok 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["exit 1 1000", "id 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    RC.push(["exit 1 1000", "format 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("active")
    RC.push(["exit 1 8000", "clock 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("active")
    RC.push(["clock 1 1000", "mail 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("active")
    RC.push(["exit 1 1000", "guide 1 4000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("inactive")
    RC.push(["exit 1 1000", "help 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("inactive")
    RC.push(["exit 1 1000", "id 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 8000", "mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("active")
    RC.push(["mute 1 1000", "VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("active")
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "right 1 1000", "menu 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("active")
    RC.push(["exit 1 7500", "red 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("active")
    RC.push(["exit 1 1000", "blue 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("active")
    RC.push(["exit 1 1000", "2 1 5000", "0 1 5000"])
    UART.start_app("mostPopular")
    RC.push(["down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("inactive")
    RC.push(["exit 1 1000", "ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    RC.push(["exit 1 1000", "id 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("active")
    RC.push(["exit 1 1000", "format 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    RC.push(["exit 1 8000", "clock 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    RC.push(["clock 1 1000", "mail 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    RC.push(["exit 1 1000", "guide 1 4000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("inactive")
    RC.push(["exit 1 1000", "help 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("inactive")
    RC.push(["exit 1 1000", "id 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 8000", "mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    status("active")
    RC.push(["mute 1 1000", "VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "right 1 1000", "menu 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    RC.push(["exit 1 7500", "red 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    RC.push(["exit 1 1000", "blue 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("active")
    RC.push(["exit 1 1000", "2 1 5000", "0 1 5000"])
    UART.start_app("mostPopular")
    RC.push(["down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("inactive")
    RC.push(["exit 1 1000", "ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    status("active")
    RC.push(["exit 1 1000", "id 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    status("active")
    RC.push(["exit 1 1000", "format 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 52 ##########################################
    testcase = 52
    status("active")
    RC.push(["exit 1 8000", "clock 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 53 ##########################################
    testcase = 53
    status("active")
    RC.push(["clock 1 1000", "mail 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 54 ##########################################
    testcase = 54
    status("active")
    RC.push(["exit 1 1000", "guide 1 4000", "down 1 1000", "down 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 55 ##########################################
    testcase = 55
    status("inactive")
    RC.push(["exit 1 1000", "help 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 56 ##########################################
    testcase = 56
    status("inactive")
    RC.push(["exit 1 1000", "id 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 57 ##########################################
    testcase = 57
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 8000", "mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 58 ##########################################
    testcase = 58
    status("active")
    RC.push(["mute 1 1000", "VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 59 ##########################################
    testcase = 59
    status("active")
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "right 1 1000", "menu 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 60 ##########################################
    testcase = 60
    status("active")
    RC.push(["exit 1 7500", "red 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 61 ##########################################
    testcase = 61
    status("active")
    RC.push(["exit 1 1000", "blue 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 62 ##########################################
    testcase = 62
    status("active")
    RC.push(["exit 1 1000", "2 1 5000", "0 1 5000"])
    UART.start_app("mostPopular")
    RC.push(["down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 63 ##########################################
    testcase = 63
    status("inactive")
    RC.push(["exit 1 1000", "ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 64 ##########################################
    testcase = 64
    status("active")
    RC.push(["exit 1 1000", "id 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 65 ##########################################
    testcase = 65
    status("active")
    RC.push(["exit 1 1000", "format 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 66 ##########################################
    testcase = 66
    status("active")
    RC.push(["exit 1 8000", "clock 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 67 ##########################################
    testcase = 67
    status("active")
    RC.push(["clock 1 1000", "mail 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 68 ##########################################
    testcase = 68
    status("active")
    RC.push(["exit 1 1000", "guide 1 4000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 69 ##########################################
    testcase = 69
    status("active")
    RC.push(["exit 1 1000", "help 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 70 ##########################################
    testcase = 70
    status("active")
    RC.push(["exit 1 1000", "id 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 71 ##########################################
    testcase = 71
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 8000", "mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 72 ##########################################
    testcase = 72
    status("active")
    RC.push(["mute 1 1000", "VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 73 ##########################################
    testcase = 73
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "right 1 1000", "down 1 1000", "right 45 1000"])
    GRAB.compare(testcase)
############################ TestCase 74 ##########################################
    testcase = 74
    status("active")
    RC.push(["left 45 1000"])
    GRAB.compare(testcase)
############################ TestCase 75 ##########################################
    testcase = 75
    status("active")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 4000", "up 1 6500"])
    GRAB.compare(testcase)
############################ TestCase 76 ##########################################
    testcase = 76
    status("active")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 77 ##########################################
    testcase = 77
    status("active")
    sleep(120)
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "down 1 1000", "left 1 1500", "left 1 1500", "left 1 1500", "left 1 1500", "left 1 1500", "left 1 1500", "left 1 1500", "left 1 1500", "exit 1 1000", "exit 1 1000", "exit 1 11000", "up 1 500"])
    GRAB.compare(testcase)
############################ TestCase 78 ##########################################
    testcase = 78
    status("active")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 79 ##########################################
    testcase = 79
    status("active")
    sleep(100)
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "down 1 1000", "right 45 2500", "exit 1 1000", "exit 1 1000", "exit 1 31000", "up 1 29000"])
    GRAB.compare(testcase)
############################ TestCase 80 ##########################################
    testcase = 80
    status("active")
    sleep(2)
    GRAB.compare(testcase)
############################ TestCase 81 ##########################################
    testcase = 81
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    MOD.stop(Modulator)
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 82 ##########################################
    testcase = 82
    status("active")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 83 ##########################################
    testcase = 83
    status("active")
    RC.push(["ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 84 ##########################################
    testcase = 84
    status("active")
    RC.push(["ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 85 ##########################################
    testcase = 85
    status("active")
    RC.push(["ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 86 ##########################################
    testcase = 86
    status("active")
    RC.push(["0 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 87 ##########################################
    testcase = 87
    status("active")
    RC.push(["ok 1 1000", "1 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 88 ##########################################
    testcase = 88
    status("active")
    RC.push(["ok 1 1000", "2 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 89 ##########################################
    testcase = 89
    status("active")
    RC.push(["ok 1 1000", "3 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 90 ##########################################
    testcase = 90
    status("active")
    RC.push(["ok 1 1000", "4 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 91 ##########################################
    testcase = 91
    status("active")
    RC.push(["ok 1 1000", "5 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 92 ##########################################
    testcase = 92
    status("active")
    RC.push(["ok 1 1000", "6 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 93 ##########################################
    testcase = 93
    status("active")
    RC.push(["ok 1 1000", "7 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 94 ##########################################
    testcase = 94
    status("active")
    RC.push(["ok 1 1000", "8 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 95 ##########################################
    testcase = 95
    status("active")
    RC.push(["ok 1 1000", "9 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 96 ##########################################
    testcase = 96
    status("active")
    RC.push(["ok 1 1000", "backward 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 97 ##########################################
    testcase = 97
    status("active")
    RC.push(["OK 1 1000", "blue 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 98 ##########################################
    testcase = 98
    status("active")
    RC.push(["OK 1 1000", "ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 99 ##########################################
    testcase = 99
    status("active")
    RC.push(["OK 1 1000", "ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 100 ##########################################
    testcase = 100
    status("active")
    RC.push(["OK 1 1000", "cinemahalls 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 101 ##########################################
    testcase = 101
    status("active")
    RC.push(["OK 1 1000", "clock 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 102 ##########################################
    testcase = 102
    status("active")
    RC.push(["OK 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 103 ##########################################
    testcase = 103
    status("active")
    RC.push(["OK 1 1000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 104 ##########################################
    testcase = 104
    status("active")
    RC.push(["OK 1 1000", "format 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 105 ##########################################
    testcase = 105
    status("active")
    RC.push(["OK 1 1000", "forward 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 106 ##########################################
    testcase = 106
    status("active")
    RC.push(["OK 1 1000", "green 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 107 ##########################################
    testcase = 107
    status("active")
    RC.push(["OK 1 1000", "guide 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 108 ##########################################
    testcase = 108
    status("active")
    RC.push(["OK 1 1000", "help 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 109 ##########################################
    testcase = 109
    status("active")
    RC.push(["OK 1 1000", "ID 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 110 ##########################################
    testcase = 110
    status("active")
    RC.push(["OK 1 1000", "last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 111 ##########################################
    testcase = 111
    status("active")
    RC.push(["OK 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 112 ##########################################
    testcase = 112
    status("active")
    RC.push(["OK 1 1000", "mail 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 113 ##########################################
    testcase = 113
    status("active")
    RC.push(["OK 1 1000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 114 ##########################################
    testcase = 114
    status("active")
    RC.push(["OK 1 1000", "mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 115 ##########################################
    testcase = 115
    status("active")
    RC.push(["OK 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 116 ##########################################
    testcase = 116
    status("active")
    RC.push(["OK 1 1000", "play/pause 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 117 ##########################################
    testcase = 117
    status("active")
    RC.push(["OK 1 1000", "Rec 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 118 ##########################################
    testcase = 118
    status("active")
    RC.push(["OK 1 1000", "RecList 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 119 ##########################################
    testcase = 119
    status("active")
    RC.push(["OK 1 1000", "red 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 120 ##########################################
    testcase = 120
    status("active")
    RC.push(["OK 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 121 ##########################################
    testcase = 121
    status("active")
    RC.push(["OK 1 1000", "stb 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 122 ##########################################
    testcase = 122
    status("active")
    RC.push(["OK 1 1000", "stop 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 123 ##########################################
    testcase = 123
    status("active")
    RC.push(["OK 1 1000", "Tv/chat 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 124 ##########################################
    testcase = 124
    status("active")
    RC.push(["OK 1 1000", "Tv/radio 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 125 ##########################################
    testcase = 125
    status("active")
    RC.push(["OK 1 1000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 126 ##########################################
    testcase = 126
    status("active")
    RC.push(["OK 1 1000", "VolDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 127 ##########################################
    testcase = 127
    status("active")
    RC.push(["OK 1 1000", "VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 128 ##########################################
    testcase = 128
    status("active")    
    RC.push(["OK 1 1000", "www 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 129 ##########################################
    testcase = 129
    status("active")
    RC.push(["OK 1 1000", "yellow 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 130 ##########################################
    testcase = 130
    status("active")
    RC.push(["OK 1 1000", "standby 1 8000", "standby 1 8000"])
    GRAB.compare(testcase)
############################ TestCase 131 ##########################################
    testcase = 131
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 132 ##########################################
    testcase = 132
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 133 ##########################################
    testcase = 133
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 134 ##########################################
    testcase = 134
    status("active")
    RC.push(["Tv/radio 1 10000"])
    GRAB.compare(testcase)
    RC.push(["Tv/radio 1 1000"])
############################ TestCase 135 ##########################################
    testcase = 135
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 136 ##########################################
    testcase = 136
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 137 ##########################################
    testcase = 137
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    MOD.stop(Modulator)
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "up 1 1000", "up 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 138 ##########################################
    testcase = 138
    status("active")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 139 ##########################################
    testcase = 139
    status("active")
    RC.push(["left 15 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "menu 1 59000"])
    GRAB.compare(testcase)
############################ TestCase 140 ##########################################
    testcase = 140
    status("active")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 141 ##########################################
    testcase = 141
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "red 1 59000"])
    GRAB.compare(testcase)
############################ TestCase 142 ##########################################
    testcase = 142
    status("active")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 143 ##########################################
    testcase = 143
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "blue 1 59000"])
    GRAB.compare(testcase)
############################ TestCase 144 ##########################################
    testcase = 144
    status("active")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 145 ##########################################
    testcase = 145
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "www 1 59000"])
    GRAB.compare(testcase)
############################ TestCase 146 ##########################################
    testcase = 146
    status("active")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 147 ##########################################
    testcase = 147
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "6 1 5000", "ok 1 59000"])
    GRAB.compare(testcase)
############################ TestCase 148 ##########################################
    testcase = 148
    status("active")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 149 ##########################################
    testcase = 149
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "id 1 59000"])
    GRAB.compare(testcase)
############################ TestCase 150 ##########################################
    testcase = 150
    status("active")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 151 ##########################################
    testcase = 151
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "format 1 59000"])
    GRAB.compare(testcase)
############################ TestCase 152 ##########################################
    testcase = 152
    status("active")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 153 ##########################################
    testcase = 153
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "mail 1 59000"])
    GRAB.compare(testcase)
############################ TestCase 154 ##########################################
    testcase = 154
    status("active")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 155 ##########################################
    testcase = 155
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "guide 1 59000"])
    GRAB.compare(testcase)
############################ TestCase 156 ##########################################
    testcase = 156
    status("active")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 157 ##########################################
    testcase = 157
    status("manual")
    RC.push(["exit 1 1000", "exit 1 1000", "id 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "right 1 59000"])
    GRAB.compare(testcase)
############################ TestCase 158 ##########################################
    testcase = 158
    status("manual")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 159 ##########################################
    testcase = 159
    status("manual")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "id 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "right 1 59000"])
    GRAB.compare(testcase)
############################ TestCase 160 ##########################################
    testcase = 160
    status("manual")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 161 ##########################################
    testcase = 161
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000"])
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "up 1 1000", "up 1 1000", "right 9 5000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "menu 1 590000"])
    GRAB.compare(testcase)
############################ TestCase 162 ##########################################
    testcase = 162
    status("active")
    sleep(30)
    GRAB.compare(testcase)
############################ TestCase 163 ##########################################
    testcase = 163
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000"])
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "up 1 1000", "up 1 1000", "right 20 5000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "menu 1 1790000"])
    GRAB.compare(testcase)
############################ TestCase 164 ##########################################
    testcase = 164
    status("active")
    sleep(90)
    GRAB.compare(testcase)
############################ TestCase 165 ##########################################
    testcase = 165
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    MOD.stop(Modulator)
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "up 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 166 ##########################################
    testcase = 166
    status("active")
    GRAB.compare(testcase)
############################ TestCase 167 ##########################################
    testcase = 167
    status("active")
    GRAB.compare(testcase)
############################ TestCase 168 ##########################################
    testcase = 168 
    status("active")
    GRAB.compare(testcase)
############################ TestCase 169 ##########################################
    testcase = 169
    status("active")
    GRAB.compare(testcase)
############################ TestCase 170 ##########################################
    testcase = 170
    status("active")
    GRAB.compare(testcase)
############################ TestCase 171 ##########################################
    testcase = 171
    status("active")
    GRAB.compare(testcase)
############################ TestCase 172 ##########################################
    testcase = 172
    status("active")
    GRAB.compare(testcase)
############################ TestCase 173 ##########################################
    testcase = 173
    status("active")
    GRAB.compare(testcase)
############################ TestCase 174 ##########################################
    testcase = 174
    status("active")
    GRAB.compare(testcase)
############################ TestCase 175 ##########################################
    testcase = 175
    status("active")
    GRAB.compare(testcase)
############################ TestCase 176 ##########################################
    testcase = 176
    status("active")
    GRAB.compare(testcase)
############################ TestCase 177 ##########################################
    testcase = 177
    status("active")
    GRAB.compare(testcase)
############################ TestCase 178 ##########################################
    testcase = 178
    status("active")
    RC.push(["OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 179 ##########################################
    testcase = 179
    status("active")
    RC.push(["OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 180 ##########################################
    testcase = 180
    status("active")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 181 ##########################################
    testcase = 181
    status("active")
    RC.push(["left 1 1000", "OK 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 182 ##########################################
    testcase = 182
    status("active")
    RC.push(["left 1 1000", "OK 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 183 ##########################################
    testcase = 183
    status("active")
    RC.push(["right 1 1000", "OK 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 184 ##########################################
    testcase = 184
    status("active")
    RC.push(["right 1 1000", "OK 1 1000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 185 ##########################################
    testcase = 185
    status("active")
    RC.push(["down 1 1000", "OK 1 1000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 186 ##########################################
    testcase = 186
    status("active")
    RC.push(["down 1 1000", "OK 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 187 ##########################################
    testcase = 187
    status("active")
    RC.push(["up 1 1000", "OK 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 188 ##########################################
    testcase = 188
    status("active")
    RC.push(["up 1 1000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 189 ##########################################
    testcase = 189
    status("active")
    RC.push(["standby 1 10000", "standby 1 10000"])
    GRAB.compare(testcase)
############################ TestCase 190 ##########################################
    testcase = 190
    status("inactive")
    GRAB.compare(testcase)
############################ TestCase 191 ##########################################
    testcase = 191
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000"])
    UART.start_app("settings")
    RC.push(["up 1 1000", "OK 1 1000", "right 100 1000", "down 100 1000", "OK 1 1000", "left 100 1000", "up 100 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 192 ##########################################
    testcase = 192
    status("active")
    RC.push(["exit 1 1000", "exit 1 4000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 193 ##########################################
    testcase = 193
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "red 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 194 ##########################################
    testcase = 194
    status("inactive")
    RC.push(["exit 1 1000", "exit 1 1000", "green 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 195 ##########################################
    testcase = 195
    status("inactive")
    RC.push(["exit 1 1000", "exit 1 1000", "yellow 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 196 ##########################################
    testcase = 196
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "blue 1 1000", "down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 197 ##########################################
    testcase = 197
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "www 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 198 ##########################################
    testcase = 198
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "5 1 10000", "ok 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 199 ##########################################
    testcase = 199
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "id 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 200 ##########################################
    testcase = 200
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "format 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 201 ##########################################
    testcase = 201
    status("active")
    RC.push(["exit 1 1000", "exit 1 4000", "clock 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 202 ##########################################
    testcase = 202
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "mail 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 203 ##########################################
    testcase = 203
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "guide 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 204 ##########################################
    testcase = 204
    status("inactive")
    RC.push(["exit 1 1000", "exit 1 1000", "id 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 205 ##########################################
    testcase = 205
    status("inactive")
    RC.push(["exit 1 1000", "exit 1 1000", "id 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "down 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 206 ##########################################
    testcase = 206
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 207 ##########################################
    testcase = 207
    status("active")
    RC.push(["VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 208 ##########################################
    testcase = 208
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 209 ##########################################
    testcase = 209
    status("manual")
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
