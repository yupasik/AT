# Test name = Channels_editor_3
# Script dir = R:\Stingray\Tests\Channels_editor_3\main\main.py
# Rev = 3.0

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
    TestName = "Channels_editor_3"
    ScriptName = "main"
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
    OPER.search()
    UART.start_app("channelseditor")
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 3000", "ok 1 3000", "down 2 3000", "ok 1 20000", "ok 1 5000"])
    #if platform == "E212":
    #    UART.start_app("dvbtscanner")
    #    RC.push(["ok 1 20000", "ok 1 5000", "exit 3 3000"])
    UART.start_app("channelseditor")
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    RC.push(["exit 2 3000"])
    UART.start_app("settings")
    RC.push(["right 7 3000", "down 1 2000", "4 1 2000", "3 1 2000", "2 1 2000", "1 1 2000", "1 16 2000"])
    UART.start_app("channelseditor")
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1 5 2000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    RC.push(["down 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["up 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["down 2 3000"])
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
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    RC.push(["exit 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["left 1 3000", "up 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["down 2 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    RC.push(["ok 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["exit 1 3000", "left 1 2000", "down 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["up 1 3000", "right 1 2000", "down 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("inactive")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("inactive")
    UART.start_app("channelseditor")
    RC.push(["last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("inactive")
    UART.start_app("channelseditor")
    RC.push(["exit 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("inactive")
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("inactive")
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["left 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("inactive")
    RC.push(["right 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("inactive")
    RC.push(["left 1 2000", "up"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("inactive")
    RC.push(["down"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("inactive")
    RC.push(["ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("inactive")
    RC.push(["left 1 2000", "red"])
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("inactive")
    RC.push(["green"])
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("inactive")
    RC.push(["yellow"])
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("inactive")
    RC.push(["blue"])
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("inactive")
    RC.push(["stb"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("inactive")
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["ChUp"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("inactive")
    RC.push(["ChDown"])
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("inactive")
    RC.push(["VolUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("inactive")
    RC.push(["VolDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("inactive")
    RC.push(["mute 1 2000", "exit 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("active")
    UART.default_settings()
    if platform in ["E501", "E502", "A230"]:
        RC.push(searching_from_wizard_general_E501)
    else:
        RC.push(searching_from_wizard_general_ALL)
    UART.start_app("channelseditor")
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("active")
    RC.push(["exit 1 3000", "ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    RC.push(["left"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    RC.push(["left 1 3000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("active")
    RC.push(["yellow", "down 4 1000", "right 6 1000", "ok", "left 4 1000", "up", "ok", "blue 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("active")
    RC.push(["exit 1 3000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 52 ##########################################
    testcase = 52
    status("active")
    RC.push(["up 1 3000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 53 ##########################################
    testcase = 53
    status("active")
    RC.push(["blue 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 54 ##########################################
    testcase = 54
    status("active")
    RC.push(["blue 1 3000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 55 ##########################################
    testcase = 55
    status("active")
    RC.push(["blue 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 56 ##########################################
    testcase = 56
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 3000", "ok 1 3000", "down 2 3000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["blue 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 57 ##########################################
    testcase = 57
    status("active")
    RC.push(["yellow 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 58 ##########################################
    testcase = 58
    status("active")
    RC.push(["exit", "green 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 59 ##########################################
    testcase = 59
    status("active")
    RC.push(["mute", "exit 2 5000"])
    GRAB.compare(testcase)
############################ TestCase 60 ##########################################
    testcase = 60
    status("active")
    UART.start_app("channelseditor")
    RC.push(["VolUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 61 ##########################################
    testcase = 61
    status("active")
    RC.push(["VolDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 62 ##########################################
    testcase = 62
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 63 ##########################################
    testcase = 63
    status("active")
    UART.start_app("channelseditor")
    RC.push(["last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 64 ##########################################
    testcase = 64
    status("active")
    UART.start_app("channelseditor")
    RC.push(["stb 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 65 ##########################################
    testcase = 65
    status("active")
    UART.start_app("channelseditor")
    RC.push(["exit 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 66 ##########################################
    testcase = 66
    status("active")
    UART.start_app("channelseditor")
    RC.push(["standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 67 ##########################################
    testcase = 67
    status("active")
    UART.default_settings()
    if platform in ["E501", "E502", "A230"]:
        RC.push(searching_from_wizard_general_E501)
    else:
        RC.push(searching_from_wizard_general_ALL)
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1 5 2000", "ok 1 3000", "right 1 2000", "ok 1 3000", "ok 5 2000", "exit 1 3000", "left 1 3000", "up 2 2000"])
    GRAB.compare(testcase)
############################ TestCase 68 ##########################################
    testcase = 68
    status("active")
    RC.push(["ok 3000"])
    GRAB.compare(testcase)
############################ TestCase 69 ##########################################
    testcase = 69
    status("active")
    RC.push(["exit", "ChUp 2 2000"])
    GRAB.compare(testcase)
############################ TestCase 70 ##########################################
    testcase = 70
    status("active")
    RC.push(["ChDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 71 ##########################################
    testcase = 71
    status("active")
    RC.push(["ChDown 1 2000", "left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 72 ##########################################
    testcase = 72
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 73 ##########################################
    testcase = 73
    status("active")
    RC.push(["left 1 2000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 74 ##########################################
    testcase = 74
    status("active")
    RC.push(["yellow", "down 4 1000", "right 6 1000", "ok", "left 4 1000", "up", "ok", "blue 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 75 ##########################################
    testcase = 75
    status("active")
    RC.push(["exit 1 2000", "blue 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 76 ##########################################
    testcase = 76
    status("active")
    RC.push(["up 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 77 ##########################################
    testcase = 77
    status("active")
    RC.push(["down 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 78 ##########################################
    testcase = 78
    status("active")
    RC.push(["blue 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 79 ##########################################
    testcase = 79
    status("active")
    RC.push(["blue 1 2000", "ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 80 ##########################################
    testcase = 80
    status("active")
    RC.push(["blue 1 2000", "exit 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 81 ##########################################
    testcase = 81
    status("active")
    RC.push(["blue 1 2000", "right 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 82 ##########################################
    testcase = 82
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["blue 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 83 ##########################################
    testcase = 83
    status("active")
    RC.push(["yellow 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 84 ##########################################
    testcase = 84
    status("active")
    RC.push(["ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 85 ##########################################
    testcase = 85
    status("active")
    RC.push(["yellow 1 2000", "left", "ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 86 ##########################################
    testcase = 86
    status("active")
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["green 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 87 ##########################################
    testcase = 87
    status("active")
    RC.push(["mute 1 2000", "exit 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 88 ##########################################
    testcase = 88
    status("active")
    UART.start_app("channelseditor")
    RC.push(["VolUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 89 ##########################################
    testcase = 89
    status("active")
    RC.push(["VolDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 90 ##########################################
    testcase = 90
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 91 ##########################################
    testcase = 91
    status("active")
    UART.start_app("channelseditor")
    RC.push(["last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 92 ##########################################
    testcase = 92
    status("active")
    UART.start_app("channelseditor")
    RC.push(["stb 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 93 ##########################################
    testcase = 93
    status("active")
    UART.start_app("channelseditor")
    RC.push(["exit 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 94 ##########################################
    testcase = 94
    status("active")
    RC.push(["exit 2 2000"])
    UART.start_app("channelseditor")
    RC.push(["standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 95 ##########################################
    testcase = 95
    status("active")
    UART.default_settings()
    if platform in ["E501", "E502", "A230"]:
        RC.push(searching_from_wizard_general_E501)
    else:
        RC.push(searching_from_wizard_general_ALL)
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1 5 2000", "ok 1 3000", "right 1 2000", "ok 1 3000", "ok 5 2000", "exit 1 3000", "left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 96 ##########################################
    testcase = 96
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 97 ##########################################
    testcase = 97
    status("active")
    RC.push(["exit 1 3000", "ChUp 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 98 ##########################################
    testcase = 98
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 99 ##########################################
    testcase = 99
    status("active")
    RC.push(["ChDown 1 3000", "left 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 100 ##########################################
    testcase = 100
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 101 ##########################################
    testcase = 101
    status("active")
    RC.push(["left 1 3000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 102 ##########################################
    testcase = 102
    status("active")
    RC.push(["yellow", "down 4 1000", "right 6 1000", "ok", "left 4 1000", "up", "ok", "blue 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 103 ##########################################
    testcase = 103
    status("active")
    RC.push(["exit 1 3000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 104 ##########################################
    testcase = 104
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 105 ##########################################
    testcase = 105
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 106 ##########################################
    testcase = 106
    status("active")
    RC.push(["blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 107 ##########################################
    testcase = 107
    status("active")
    RC.push(["blue 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 108 ##########################################
    testcase = 108
    status("active")
    RC.push(["blue 1 3000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 109 ##########################################
    testcase = 109
    status("active")
    RC.push(["blue 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 110 ##########################################
    testcase = 110
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1 5 2000", "ok 1 3000", "right 1 2000", "ok 1 3000", "ok 5 2000", "exit 1 3000", "left 1 3000", "up 1 2000", "yellow 1 2000", "left", "ok 1 2000"])
    RC.push(["blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 111 ##########################################
    testcase = 111
    status("active")
    RC.push(["yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 112 ##########################################
    testcase = 112
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 113 ##########################################
    testcase = 113
    status("active")
    RC.push(["yellow 1 3000", "left", "ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 114 ##########################################
    testcase = 114
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1 5 2000", "ok 1 3000", "right 1 2000", "ok 1 3000", "ok 5 2000", "exit 1 3000", "left 1 3000", "up 1 2000", "yellow 1 2000", "left", "ok 1 2000"])
    RC.push(["blue 1 3000"])
    RC.push(["green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 115 ##########################################
    testcase = 115
    status("active")
    RC.push(["yellow", "down 4 1000", "right 6 1000", "ok", "left 4 1000", "up", "ok", "blue 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 116 ##########################################
    testcase = 116
    status("active")
    RC.push(["2 5 3000", "ok 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 117 ##########################################
    testcase = 117
    status("active")
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["down 1 2000", "mute 1 2000", "exit 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 118 ##########################################
    testcase = 118
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 2000", "VolUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 119 ##########################################
    testcase = 119
    status("active")
    RC.push(["VolDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 120 ##########################################
    testcase = 120
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 121 ##########################################
    testcase = 121
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 2000", "last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 122 ##########################################
    testcase = 122
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 2000", "stb 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 123 ##########################################
    testcase = 123
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 2000", "exit 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 124 ##########################################
    testcase = 124
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 2000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 125 ##########################################
    testcase = 125
    status("active")
    UART.start_app("channelseditor")
    RC.push(["up 1 2000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 126 ##########################################
    testcase = 126
    status("active")
    RC.push(["yellow", "2 5 3000", "blue 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 127 ##########################################
    testcase = 127
    status("active")
    UART.default_settings()
    if platform in ["E501", "E502", "A230"]:
        RC.push(searching_from_wizard_general_E501)
    else:
        RC.push(searching_from_wizard_general_ALL)
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 128 ##########################################
    testcase = 128
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 129 ##########################################
    testcase = 129
    status("active")
    RC.push(["exit", "ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 130 ##########################################
    testcase = 130
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 131 ##########################################
    testcase = 131
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 132 ##########################################
    testcase = 132
    status("active")
    RC.push(["right 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 133 ##########################################
    testcase = 133
    status("active")
    RC.push(["red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 134 ##########################################
    testcase = 134
    status("active")
    RC.push(["red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 135 ##########################################
    testcase = 135
    status("active")
    RC.push(["green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 136 ##########################################
    testcase = 136
    status("active")
    RC.push(["yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 137 ##########################################
    testcase = 137
    status("active")
    RC.push(["blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 138 ##########################################
    testcase = 138
    status("active")
    RC.push(["mute 1 3000", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 139 ##########################################
    testcase = 139
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 140 ##########################################
    testcase = 140
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 141 ##########################################
    testcase = 141
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 142 ##########################################
    testcase = 142
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 143 ##########################################
    testcase = 143
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["stb 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 144 ##########################################
    testcase = 144
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 145 ##########################################
    testcase = 145
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 146 ##########################################
    testcase = 146
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 147 ##########################################
    testcase = 147
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 148 ##########################################
    testcase = 148
    status("active")
    RC.push(["exit", "ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 149 ##########################################
    testcase = 149
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 150 ##########################################
    testcase = 150
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 151 ##########################################
    testcase = 151
    status("active")
    RC.push(["right 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 152 ##########################################
    testcase = 152
    status("active")
    RC.push(["green 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 153 ##########################################
    testcase = 153
    status("active")
    RC.push(["exit 1 2000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 154 ##########################################
    testcase = 154
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 155 ##########################################
    testcase = 155
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 156 ##########################################
    testcase = 156
    status("active")
    RC.push(["blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 157 ##########################################
    testcase = 157
    status("active")
    RC.push(["blue 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 158 ##########################################
    testcase = 158
    status("active")
    RC.push(["blue 1 3000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 159 ##########################################
    testcase = 159
    status("active")
    RC.push(["blue 1 3000", "left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 160 ##########################################
    testcase = 160
    status("active")
    RC.push(["right 1 3000"])
    RC.push(["yellow 8 3000"])
    RC.push(["blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 161 ##########################################
    testcase = 161
    status("active")
    GRAB.compare(testcase)
############################ TestCase 162 ##########################################
    testcase = 162
    status("active")
    RC.push(["left 1 3000", "red 1 3000", "3 5 3000", "ok 1 3000", "right 1 2000", "ok 1 3000", "ok 1 2000", "exit 1 2000"])
    RC.push(["yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 163 ##########################################
    testcase = 163
    status("active")
    RC.push(["up 1 3000", "right 1 2000", "yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 164 ##########################################
    testcase = 164
    if platform in ["E212"]:
        status("active")
    else:
        status("inactive")

    GRAB.compare(testcase)
############################ TestCase 165 ##########################################
    testcase = 165
    status("active")

    GRAB.compare(testcase)
############################ TestCase 166 ##########################################
    testcase = 166
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 167 ##########################################
    testcase = 167
    status("active")
    RC.push(["red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 168 ##########################################
    testcase = 168
    status("active")
    RC.push(["mute 1 3000", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 169 ##########################################
    testcase = 169
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["VolUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 170 ##########################################
    testcase = 170
    status("active")
    RC.push(["VolDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 171 ##########################################
    testcase = 171
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 172 ##########################################
    testcase = 172
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 173 ##########################################
    testcase = 173
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["stb 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 174 ##########################################
    testcase = 174
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 175 ##########################################
    testcase = 175
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 176 ##########################################
    testcase = 176
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["up 1 3000", "ok 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 177 ##########################################
    testcase = 177
    status("active")
    RC.push(["exit 1 3000", "up 1 3000", "left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 178 ##########################################
    testcase = 178
    status("active")
    RC.push(["right 1 3000", "up 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 179 ##########################################
    testcase = 179
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 180 ##########################################
    testcase = 180
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 181 ##########################################
    testcase = 181
    status("active")
    RC.push(["ok 1 3000", "left", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 182 ##########################################
    testcase = 182
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1 5 3000", "ok 1 5000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 183 ##########################################
    testcase = 183
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 184 ##########################################
    testcase = 184
    status("active")
    RC.push(["exit 1 3000", "ChUp"])
    GRAB.compare(testcase)
############################ TestCase 185 ##########################################
    testcase = 185
    status("active")
    RC.push(["ChDown"])
    GRAB.compare(testcase)
############################ TestCase 186 ##########################################
    testcase = 186
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 187 ##########################################
    testcase = 187
    status("active")
    RC.push(["right 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 188 ##########################################
    testcase = 188
    status("active")
    RC.push(["green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 189 ##########################################
    testcase = 189
    status("active")
    RC.push(["exit 1 3000", "red"])
    GRAB.compare(testcase)
############################ TestCase 190 ##########################################
    testcase = 190
    status("active")
    RC.push(["yellow"])
    GRAB.compare(testcase)
############################ TestCase 191 ##########################################
    testcase = 191
    status("active")
    RC.push(["blue"])
    GRAB.compare(testcase)
############################ TestCase 192 ##########################################
    testcase = 192
    status("active")
    RC.push(["mute 1 3000", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 193 ##########################################
    testcase = 193
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 3000", "right 1 3000", "VolUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 194 ##########################################
    testcase = 194
    status("active")
    RC.push(["VolDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 195 ##########################################
    testcase = 195
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 196 ##########################################
    testcase = 196
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 3000", "right 1 3000", "last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 197 ##########################################
    testcase = 197
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 3000", "right 1 3000", "stb 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 198 ##########################################
    testcase = 198
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 199 ##########################################
    testcase = 199
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 3000", "right 1 3000"])
    RC.push(["standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 200 ##########################################
    testcase = 200
    status("active")
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1", "2", "3", "4", "5", "6", "7", "8", "9", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 201 ##########################################
    testcase = 201
    status("active")
    RC.push(["red 1 3000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 202 ##########################################
    testcase = 202
    status("active")
    RC.push(["red 1 3000", "0 3 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 203 ##########################################
    testcase = 203
    status("active")
    RC.push(["red 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 204 ##########################################
    testcase = 204
    status("active")
    UART.default_settings()
    if platform in ["E501", "E502", "A230"]:
        RC.push(searching_from_wizard_general_E501)
    else:
        RC.push(searching_from_wizard_general_ALL)
    UART.start_app("channelseditor")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 205 ##########################################
    testcase = 205
    status("active")
    RC.push(["blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 206 ##########################################
    testcase = 206
    status("active")
    RC.push(["ok 2 3000", "ChUp"])
    GRAB.compare(testcase)
############################ TestCase 207 ##########################################
    testcase = 207
    status("active")
    RC.push(["ChDown"])
    GRAB.compare(testcase)
############################ TestCase 208 ##########################################
    testcase = 208
    status("active")
    RC.push(["left"])
    GRAB.compare(testcase)
############################ TestCase 209 ##########################################
    testcase = 209
    status("active")
    RC.push(["right"])
    GRAB.compare(testcase)
############################ TestCase 210 ##########################################
    testcase = 210
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 211 ##########################################
    testcase = 211
    status("active")
    RC.push(["up 1 3000", "ok 1 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 212 ##########################################
    testcase = 212
    status("active")
    RC.push(["down 2 3000", "ok 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 213 ##########################################
    testcase = 213
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 214 ##########################################
    testcase = 214
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "ok 1 3000", "down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 215 ##########################################
    testcase = 215
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "ok 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 216 ##########################################
    testcase = 216
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 217 ##########################################
    testcase = 217
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 218 ##########################################
    testcase = 218
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["ok 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 219 ##########################################
    testcase = 219
    status("active")
    RC.push(["ok 1 3000"])
    RC.push(["red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 220 ##########################################
    testcase = 220
    status("active")
    RC.push(["yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 221 ##########################################
    testcase = 221
    status("active")
    RC.push(["exit 1 2000", "ok 1 2000", "green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 222 ##########################################
    testcase = 222
    status("active")
    RC.push(["mute 1 3000", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 223 ##########################################
    testcase = 223
    status("active")
    UART.start_app("channelseditor")
    RC.push(["ok 1 3000", "VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 224 ##########################################
    testcase = 224
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 225 ##########################################
    testcase = 225
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 226 ##########################################
    testcase = 226
    status("active")
    UART.start_app("channelseditor")
    RC.push(["ok 1 3000", "last 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 227 ##########################################
    testcase = 227
    status("active")
    UART.start_app("channelseditor")
    RC.push(["ok 1 3000", "stb 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 228 ##########################################
    testcase = 228
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 229 ##########################################
    testcase = 229
    status("active")
    RC.push(["ok 1 3000"])
    RC.push(["standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 230 ##########################################
    testcase = 230
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 231 ##########################################
    testcase = 231
    status("active")
    RC.push(["blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 232 ##########################################
    testcase = 232
    status("active")
    RC.push(["ok 1 3000", "ChDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 233 ##########################################
    testcase = 233
    status("active")
    RC.push(["ChUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 234 ##########################################
    testcase = 234
    status("active")
    RC.push(["right 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 235 ##########################################
    testcase = 235
    status("active")
    RC.push(["left 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 236 ##########################################
    testcase = 236
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 237 ##########################################
    testcase = 237
    status("active")
    RC.push(["ok 1 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 238 ##########################################
    testcase = 238
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 239 ##########################################
    testcase = 239
    status("active")
    RC.push(["ok 1 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 240 ##########################################
    testcase = 240
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 241 ##########################################
    testcase = 241
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 242 ##########################################
    testcase = 242
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 243 ##########################################
    testcase = 243
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 244 ##########################################
    testcase = 244
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["ok 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 245 ##########################################
    testcase = 245
    status("active")
    RC.push(["ok 1 3000", "right", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 246 ##########################################
    testcase = 246
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 247 ##########################################
    testcase = 247
    status("active")
    RC.push(["ok 1 3000", "right", "ok 1 3000", "left", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 248 ##########################################
    testcase = 248
    status("active")
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["ok 1 3000"])
    RC.push(["red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 249 ##########################################
    testcase = 249
    status("active")
    RC.push(["yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 250 ##########################################
    testcase = 250
    status("active")
    RC.push(["exit 1 3000", "ok 1 3000", "green"])
    GRAB.compare(testcase)
############################ TestCase 251 ##########################################
    testcase = 251
    status("active")
    RC.push(["mute 1 3000", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 252 ##########################################
    testcase = 252
    status("active")
    UART.start_app("channelseditor")
    RC.push(["ok 1 3000"])
    RC.push(["VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 253 ##########################################
    testcase = 253
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 254 ##########################################
    testcase = 254
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 255 ##########################################
    testcase = 255
    status("active")
    UART.start_app("channelseditor")
    RC.push(["ok 1 3000"])
    RC.push(["last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 256 ##########################################
    testcase = 256
    status("active")
    UART.start_app("channelseditor")
    RC.push(["ok 1 3000"])
    RC.push(["stb 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 257 ##########################################
    testcase = 257
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 258 ##########################################
    testcase = 258
    status("active")
    RC.push(["ok 1 3000"])
    RC.push(["standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 259 ##########################################
    testcase = 259
    status("active")
    UART.default_settings()
    if platform in ["E501", "E502", "A230"]:
        RC.push(searching_from_wizard_general_E501)
    else:
        RC.push(searching_from_wizard_general_ALL)
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1 5 3000", "ok 1 5000", "right 1 3000", "ok 1 3000", "ok 5 3000", "exit 1 2000", "left 1 2000", "ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 260 ##########################################
    testcase = 260
    status("active")
    RC.push(["blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 261 ##########################################
    testcase = 261
    status("active")
    RC.push(["ok 2 3000", "ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 262 ##########################################
    testcase = 262
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 263 ##########################################
    testcase = 263
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 264 ##########################################
    testcase = 264
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 265 ##########################################
    testcase = 265
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 266 ##########################################
    testcase = 266
    status("active")
    RC.push(["up 2 3000", "ok 1 2000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 267 ##########################################
    testcase = 267
    status("active")
    RC.push(["down 1 3000", "ok 1 2000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 268 ##########################################
    testcase = 268
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 269 ##########################################
    testcase = 269
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 270 ##########################################
    testcase = 270
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 271 ##########################################
    testcase = 271
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 272 ##########################################
    testcase = 272
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 273 ##########################################
    testcase = 273
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1 5 3000", "ok 1 5000", "right 1 3000", "ok 1 3000", "ok 5 3000", "exit 1 2000", "left 1 2000", "up 1 3000", "yellow 1 2000", "left", "ok 1 3000"])
    RC.push(["ok 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 274 ##########################################
    testcase = 274
    status("active")
    RC.push(["ok 1 3000", "right 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 275 ##########################################
    testcase = 275
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 276 ##########################################
    testcase = 276
    status("active")
    RC.push(["ok 1 3000", "right 1 3000", "ok 1 3000", "left", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 277 ##########################################
    testcase = 277
    status("active")
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1 5 3000", "ok 1 5000", "right 1 3000", "ok 1 3000", "ok 5 3000", "exit 1 2000", "left 1 2000", "up 1 3000", "yellow 1 2000", "left", "ok 1 3000"])
    RC.push(["ok 1 3000", "right 2 2000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 278 ##########################################
    testcase = 278
    status("active")
    RC.push(["1 5 3000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 279 ##########################################
    testcase = 279
    status("active")
    RC.push(["2 5 3000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 280 ##########################################
    testcase = 280
    status("active")
    RC.push(["ok 1 3000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 281 ##########################################
    testcase = 281
    status("active")
    RC.push(["ok 1 3000", "yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 282 ##########################################
    testcase = 282
    status("active")
    RC.push(["exit 1 2000", "ok 1 3000", "green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 283 ##########################################
    testcase = 283
    status("active")
    RC.push(["exit 1 2000", "ok 1 3000", "mute 1 3000", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 284 ##########################################
    testcase = 284
    status("active")
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1", "2", "2", "2", "6 1 2000", "down 3 2000", "ok 1 2000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["down 1 2000", "ok 1 3000", "VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 285 ##########################################
    testcase = 285
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 286 ##########################################
    testcase = 286
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 287 ##########################################
    testcase = 287
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 2000", "ok 1 3000", "last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 288 ##########################################
    testcase = 288
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 2000", "ok 1 3000", "stb 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 289 ##########################################
    testcase = 289
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 290 ##########################################
    testcase = 290
    status("active")
    RC.push(["ok 1 3000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 291 ##########################################
    testcase = 291
    status("active")
    UART.default_settings()
    if platform in ["E501", "E502", "A230"]:
        RC.push(searching_from_wizard_general_E501)
    else:
        RC.push(searching_from_wizard_general_ALL)
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 292 ##########################################
    testcase = 292
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 293 ##########################################
    testcase = 293
    status("active")
    RC.push(["ok 1 3000", "ChUp"])
    GRAB.compare(testcase)
############################ TestCase 294 ##########################################
    testcase = 294
    status("active")
    RC.push(["ChDown"])
    GRAB.compare(testcase)
############################ TestCase 295 ##########################################
    testcase = 295
    status("active")
    RC.push(["left"])
    GRAB.compare(testcase)
############################ TestCase 296 ##########################################
    testcase = 296
    status("active")
    RC.push(["right"])
    GRAB.compare(testcase)
############################ TestCase 297 ##########################################
    testcase = 297
    status("active")
    RC.push(["ok 1 3000", "down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 298 ##########################################
    testcase = 298
    status("active")
    RC.push(["ok 1 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 299 ##########################################
    testcase = 299
    status("active")
    RC.push(["ok 1 3000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 300 ##########################################
    testcase = 300
    status("active")
    RC.push(["ok 1 3000", "green"])
    GRAB.compare(testcase)
############################ TestCase 301 ##########################################
    testcase = 301
    status("active")
    RC.push(["yellow"])
    GRAB.compare(testcase)
############################ TestCase 302 ##########################################
    testcase = 302
    status("active")
    RC.push(["blue"])
    GRAB.compare(testcase)
############################ TestCase 303 ##########################################
    testcase = 303
    status("active")
    RC.push(["mute", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 304 ##########################################
    testcase = 304
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["ok 1 3000", "VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 305 ##########################################
    testcase = 305
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 306 ##########################################
    testcase = 306
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 307 ##########################################
    testcase = 307
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["ok 1 3000", "last 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 308 ##########################################
    testcase = 308
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["ok 1 3000", "stb 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 309 ##########################################
    testcase = 309
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 310 ##########################################
    testcase = 310
    status("active")
    UART.start_app("channelseditor")
    RC.push(["right 1 3000"])
    RC.push(["ok 1 3000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 311 ##########################################
    testcase = 311
    status("active")
    UART.default_settings()
    RC.push(["exit 2 3000"])
    UART.start_app("dvbsmanualscanner")
    RC.push(["left 5 2400", "1 1 2000", "2 1 2000", "2 1 2000", "2 1 2000", "6 1 4000", "down 3 2000", "ok 1 3000", "down 2 2000", "ok 1 20000", "ok 1 5000"])
    RC.push(["exit 2 3000"])
    UART.start_app("channelseditor")
    RC.push(["right 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 312 ##########################################
    testcase = 312
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 313 ##########################################
    testcase = 313
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 314 ##########################################
    testcase = 314
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 315 ##########################################
    testcase = 315
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 316 ##########################################
    testcase = 316
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 317 ##########################################
    testcase = 317
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 318 ##########################################
    testcase = 318
    status("active")
    RC.push(["ok 1 3000", "ok 1 3000", "left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 319 ##########################################
    testcase = 319
    status("active")
    RC.push(["red 1 3000", "1 5 3000", "ok 1 3000", "right 1 3000", "ok 1 3000", "ok 1 3000", "exit 1 3000", "ok 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 320 ##########################################
    testcase = 320
    status("active")
    RC.push(["ok 1 3000", "right 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 321 ##########################################
    testcase = 321
    status("active")
    GRAB.compare(testcase)
############################ TestCase 322 ##########################################
    testcase = 322
    status("active")
    RC.push(["right 1 3000", "ok 1 3000", "ok 1 3000", "ok 1 3000", "exit 1 3000", "ok 1 3000", "right 2 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 323 ##########################################
    testcase = 323
    status("active")
    RC.push(["ok 1 3000", "ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 324 ##########################################
    testcase = 324
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 325 ##########################################
    testcase = 325
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 326 ##########################################
    testcase = 326
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 327 ##########################################
    testcase = 327
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 328 ##########################################
    testcase = 328
    status("active")
    RC.push(["ok 1 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 329 ##########################################
    testcase = 329
    status("active")
    RC.push(["ok 1 3000", "green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 330 ##########################################
    testcase = 330
    status("active")
    RC.push(["ok 1 3000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 331 ##########################################
    testcase = 331
    status("active")
    RC.push(["ok 1 3000", "yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 332 ##########################################
    testcase = 332
    status("active")
    RC.push(["ok 1 3000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 333 ##########################################
    testcase = 333
    status("active")
    RC.push(["ok 1 3000", "mute 1 3000", "exit 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 334 ##########################################
    testcase = 334
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 3000", "right 1 3000", "ok 1 3000", "VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 335 ##########################################
    testcase = 335
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 336 ##########################################
    testcase = 336
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 337 ##########################################
    testcase = 337
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 3000", "right 1 3000", "ok 1 3000", "last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 338 ##########################################
    testcase = 338
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 1 3000", "right 1 3000", "ok 1 3000", "stb 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 339 ##########################################
    testcase = 339
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 340 ##########################################
    testcase = 340
    status("active")
    RC.push(["ok 1 3000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 341 ##########################################
    testcase = 341
    status("active")
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "2 5 3000", "ok 1 3000", "right 1 3000", "ok 1 3000", "ok 3 3000", "exit 1 3000", "left 1 3000"])
    RC.push(["red 1 3000", "3 5 3000", "ok 1 3000", "right 1 3000", "ok 1 3000", "ok 4 3000", "exit 1 3000"])
    RC.push(["green 1 8000"])
    GRAB.compare(testcase)
############################ TestCase 342 ##########################################
    testcase = 342
    status("active")
    GRAB.compare(testcase)
############################ TestCase 343 ##########################################
    testcase = 343
    status("active")
    GRAB.compare(testcase)
############################ TestCase 344 ##########################################
    testcase = 344
    status("active")
    GRAB.compare(testcase)
############################ TestCase 345 ##########################################
    testcase = 345
    status("active")
    GRAB.compare(testcase)
############################ TestCase 346 ##########################################
    testcase = 346
    status("active")
    GRAB.compare(testcase)
############################ TestCase 347 ##########################################
    testcase = 347
    status("active")
    GRAB.compare(testcase)
############################ TestCase 348 ##########################################
    testcase = 348
    status("active")
    GRAB.compare(testcase)
############################ TestCase 349 ##########################################
    testcase = 349
    status("active")
    GRAB.compare(testcase)
############################ TestCase 350 ##########################################
    testcase = 350
    status("active")
    GRAB.compare(testcase)
############################ TestCase 351 ##########################################
    testcase = 351
    status("active")
    GRAB.compare(testcase)
############################ TestCase 352 ##########################################
    testcase = 352
    status("active")
    GRAB.compare(testcase)
############################ TestCase 353 ##########################################
    testcase = 353
    status("active")
    GRAB.compare(testcase)
############################ TestCase 354 ##########################################
    testcase = 354
    status("active")
    GRAB.compare(testcase)
############################ TestCase 355 ##########################################
    testcase = 355
    status("active")
    RC.push(["red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 356 ##########################################
    testcase = 356
    status("active")
    GRAB.compare(testcase)
############################ TestCase 357 ##########################################
    testcase = 357
    status("active")
    GRAB.compare(testcase)
############################ TestCase 358 ##########################################
    testcase = 358
    status("active")
    GRAB.compare(testcase)
############################ TestCase 359 ##########################################
    testcase = 359
    status("active")
    GRAB.compare(testcase)
############################ TestCase 360 ##########################################
    testcase = 360
    status("active")
    GRAB.compare(testcase)
############################ TestCase 361 ##########################################
    testcase = 361
    status("active")
    GRAB.compare(testcase)
############################ TestCase 362 ##########################################
    testcase = 362
    status("active")
    GRAB.compare(testcase)
############################ TestCase 363 ##########################################
    testcase = 363
    status("active")
    GRAB.compare(testcase)
############################ TestCase 364 ##########################################
    testcase = 364
    status("active")
    GRAB.compare(testcase)
############################ TestCase 365 ##########################################
    testcase = 365
    status("active")
    GRAB.compare(testcase)
############################ TestCase 366 ##########################################
    testcase = 366
    status("active")
    GRAB.compare(testcase)
############################ TestCase 367 ##########################################
    testcase = 367
    status("active")
    RC.push(["red 1 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 368 ##########################################
    testcase = 368
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 369 ##########################################
    testcase = 369
    status("active")
    RC.push(["up 1 3000", "ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 370 ##########################################
    testcase = 370
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 371 ##########################################
    testcase = 371
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 372 ##########################################
    testcase = 372
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 373 ##########################################
    testcase = 373
    status("active")
    RC.push(["down 4 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 374 ##########################################
    testcase = 374
    status("active")
    RC.push(["up 3 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 375 ##########################################
    testcase = 375
    status("active")
    RC.push(["down 1 3000", "left 1 3000", "right 1 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 376 ##########################################
    testcase = 376
    status("active")
    RC.push(["down 2 3000", "up 1 3000", "down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 377 ##########################################
    testcase = 377
    status("active")
    RC.push(["down 3 3000", "down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 378 ##########################################
    testcase = 378
    status("active")
    RC.push(["up 1 3000", "left 2 3000", "down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 379 ##########################################
    testcase = 379
    status("active")
    RC.push(["exit 3 3000"])
    UART.start_app("tricolorsearch")
    RC.push(["right 1 3000", "ok 1 3000", "ok 1 5000", "ok 1 20000", "ok 1 3000"])
    UART.start_app("channelseditor")
    RC.push(["down 4 3000", "right 1 3000", "green 1 3000", "tv/radio 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 380 ##########################################
    testcase = 380
    status("active")
    RC.push(["mute 1 3000", "exit 3 3000"])
    GRAB.compare(testcase)
############################ TestCase 381 ##########################################
    testcase = 381
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 3 3000", "right 1 3000", "green 1 3000", "down 2 3000", "VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 382 ##########################################
    testcase = 382
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 383 ##########################################
    testcase = 383
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 384 ##########################################
    testcase = 384
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 3 3000", "right 1 3000", "green 1 3000", "down 2 3000", "last 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 385 ##########################################
    testcase = 385
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 3 3000", "right 1 3000", "green 1 3000", "down 2 3000", "stb 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 386 ##########################################
    testcase = 386
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 387 ##########################################
    testcase = 387
    status("active")
    RC.push(["green 1 3000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 388 ##########################################
    testcase = 388
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 2 3000", "right 1 3000", "green 1 3000", "down 2 3000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 389 ##########################################
    testcase = 389
    status("active")
    RC.push(["red 1 3000", "blue"])
    GRAB.compare(testcase)
############################ TestCase 390 ##########################################
    testcase = 390
    status("active")
    RC.push(["green"])
    GRAB.compare(testcase)
############################ TestCase 391 ##########################################
    testcase = 391
    status("active")
    RC.push(["yellow"])
    GRAB.compare(testcase)
############################ TestCase 392 ##########################################
    testcase = 392
    status("active")
    RC.push(["red 1 3000", "left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 393 ##########################################
    testcase = 393
    status("active")
    RC.push(["down 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 394 ##########################################
    testcase = 394
    status("active")
    RC.push(["left 1 3000", "ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 395 ##########################################
    testcase = 395
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 396 ##########################################
    testcase = 396
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 397 ##########################################
    testcase = 397
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 398 ##########################################
    testcase = 398
    status("active")
    RC.push(["left 1 3000", "down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 399 ##########################################
    testcase = 399
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 400 ##########################################
    testcase = 400
    status("active")
    RC.push(["right 1 3000", "down 2 2000", "left 1 2000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 401 ##########################################
    testcase = 401
    status("active")
    RC.push(["up 2 3000", "left 1 2000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 402 ##########################################
    testcase = 402
    status("active")
    RC.push(["left 1 3000", "down 1 2000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 403 ##########################################
    testcase = 403
    status("active")
    RC.push(["left 1 3000", "up 1 2000", "right 1 3000", "down 2 3000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 404 ##########################################
    testcase = 404
    status("active")
    RC.push(["tv/radio 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 405 ##########################################
    testcase = 405
    status("active")
    RC.push(["mute 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 406 ##########################################
    testcase = 406
    status("active")
    RC.push(["VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 407 ##########################################
    testcase = 407
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 408 ##########################################
    testcase = 408
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 409 ##########################################
    testcase = 409
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 2 3000", "right 1 3000", "green 1 3000", "down 2 3000", "red 1 3000", "left 1 3000", "last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 410 ##########################################
    testcase = 410
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 2 3000", "right 1 3000", "green 1 3000", "down 2 3000", "red 1 3000", "left 1 3000", "stb 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 411 ##########################################
    testcase = 411
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 412 ##########################################
    testcase = 412
    status("active")
    RC.push(["green 1 3000", "down 2 3000", "left 1 3000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 413 ##########################################
    testcase = 413
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 2 3000", "right 1 3000", "green 1 3000", "left 1 3000", "down 2 3000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 414 ##########################################
    testcase = 414
    status("active")
    RC.push(["red 1 3000", "left 1 2000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 415 ##########################################
    testcase = 415
    status("active")
    RC.push(["green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 416 ##########################################
    testcase = 416
    status("active")
    RC.push(["yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 417 ##########################################
    testcase = 417
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 2 3000", "right 1 3000", "green 1 8000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 418 ##########################################
    testcase = 418
    status("active")
    RC.push(["down 2 5000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 419 ##########################################
    testcase = 419
    status("active")
    RC.push(["ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 420 ##########################################
    testcase = 420
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 421 ##########################################
    testcase = 421
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 422 ##########################################
    testcase = 422
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 423 ##########################################
    testcase = 423
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 424 ##########################################
    testcase = 424
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 425 ##########################################
    testcase = 425
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 426 ##########################################
    testcase = 426
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 427 ##########################################
    testcase = 427
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 428 ##########################################
    testcase = 428
    status("active")
    RC.push(["down 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 429 ##########################################
    testcase = 429
    status("active")
    RC.push(["tv/radio 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 430 ##########################################
    testcase = 430
    status("active")
    RC.push(["left 1 3000", "down 1 3000", "mute 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 431 ##########################################
    testcase = 431
    status("active")
    RC.push(["VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 432 ##########################################
    testcase = 432
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 433 ##########################################
    testcase = 433
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 434 ##########################################
    testcase = 434
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 2 3000", "right 1 3000", "green 1 8000", "last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 435 ##########################################
    testcase = 435
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 2 3000", "right 1 3000", "green 1 14000", "stb 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 436 ##########################################
    testcase = 436
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 437 ##########################################
    testcase = 437
    status("active")
    RC.push(["green 1 8000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 438 ##########################################
    testcase = 438
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 3 3000", "right 1 3000", "green 1 8000", "left 1 2000", "down 1 2000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 439 ##########################################
    testcase = 439
    status("active")
    RC.push(["red 1 3000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 440 ##########################################
    testcase = 440
    status("active")
    RC.push(["green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 441 ##########################################
    testcase = 441
    status("active")
    RC.push(["yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 442 ##########################################
    testcase = 442
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 5 3000", "right 1 3000", "green 1 8000", "red 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 443 ##########################################
    testcase = 443
    status("active")
    RC.push(["down 2 8000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 444 ##########################################
    testcase = 444
    status("active")
    RC.push(["ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 445 ##########################################
    testcase = 445
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 446 ##########################################
    testcase = 446
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 447 ##########################################
    testcase = 447
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 448 ##########################################
    testcase = 448
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 449 ##########################################
    testcase = 449
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 450 ##########################################
    testcase = 450
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 451 ##########################################
    testcase = 451
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 452 ##########################################
    testcase = 452
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 453 ##########################################
    testcase = 453
    status("active")
    RC.push(["down 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 454 ##########################################
    testcase = 454
    status("active")
    RC.push(["tv/radio 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 455 ##########################################
    testcase = 455
    status("active")
    RC.push(["left 1 3000", "down 1 3000", "mute 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 456 ##########################################
    testcase = 456
    status("active")
    RC.push(["VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 457 ##########################################
    testcase = 457
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 458 ##########################################
    testcase = 458
    status("active")
    RC.push(["menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 459 ##########################################
    testcase = 459
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 2 3000", "right 1 3000", "green 1 8000", "last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 460 ##########################################
    testcase = 460
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 2 3000", "right 1 3000", "green 1 8000", "stb 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 461 ##########################################
    testcase = 461
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 462 ##########################################
    testcase = 462
    status("active")
    RC.push(["green 1 8000", "standby 1 5000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 463 ##########################################
    testcase = 463
    status("active")
    UART.start_app("channelseditor")
    RC.push(["down 2 3000", "right 1 3000", "green 1 8000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 464 ##########################################
    testcase = 464
    status("active")
    RC.push(["red 1 3000", "blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 465 ##########################################
    testcase = 465
    status("active")
    RC.push(["green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 466 ##########################################
    testcase = 466
    status("active")
    RC.push(["yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 467 ##########################################
    testcase = 467
    status("active")
    RC.push(["exit 3 3000"])
    UART.start_app("channelseditor")
    RC.push(["cinemahalls 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 468 ##########################################
    testcase = 468
    status("active")
    RC.push(["help 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 469 ##########################################
    testcase = 469
    status("active")
    RC.push(["exit 3 3000", "1 1 3000"])
    UART.start_app("scheduler")
    RC.push(["red", "ok 1 3000", "down 2 1000", "ok", "ok 1 2000", "right 1 1000", "up 2 2000", "ok", "ok", "exit 5 2400",])
    UART.start_app("channelseditor")
    sleep(50)
    GRAB.compare(testcase)
############################ TestCase 470 ##########################################
    testcase = 470
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 471 ##########################################
    testcase = 471
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 472 ##########################################
    testcase = 472
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 473 ##########################################
    testcase = 473
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 474 ##########################################
    testcase = 474
    status("active")
    RC.push(["exit 3 3000"])
    UART.start_app("channelseditor")
    RC.push(["VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 475 ##########################################
    testcase = 475
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 476 ##########################################
    testcase = 476
    status("active")
    RC.push(["mute 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 477 ##########################################
    testcase = 477
    status("active")
    RC.push(["guide 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 478 ##########################################
    testcase = 478
    status("active")
    RC.push(["tv/chat 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 479 ##########################################
    testcase = 479
    status("active")
    RC.push(["star 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 480 ##########################################
    testcase = 480
    status("active")
    RC.push(["right 1 2500", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 481 ##########################################
    testcase = 481
    status("active")
    RC.push(["red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 482 ##########################################
    testcase = 482
    status("active")
    RC.push(["exit 3 3000"])
    UART.start_app("settings")
    RC.push(["right 6 2500", "down 1 2000", "ok 1 3000", "1 8 3000", "ok 1 3000"])
    RC.push(["exit 3 3000"])
    UART.start_app("channelseditor")
    RC.push(["right 1 2500", "down 1 2000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 483 ##########################################
    testcase = 483
    status("active")
    RC.push(["0 4 3000"])
    GRAB.compare(testcase)
############################ TestCase 484 ##########################################
    testcase = 484
    status("active")
    RC.push(["1 4 3000"])
    GRAB.compare(testcase)
############################ TestCase 485 ##########################################
    testcase = 485
    status("active")
    RC.push(["exit 3 3000"])
    UART.start_app("channelseditor")
    RC.push(["right 1 2500", "down 1 2000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 486 ##########################################
    testcase = 486
    status("active")
    RC.push(["0 4 3000"])
    GRAB.compare(testcase)
############################ TestCase 487 ##########################################
    testcase = 487
    status("active")
    RC.push(["1 4 3000"])
    GRAB.compare(testcase)
############################ TestCase 488 ##########################################
    testcase = 488
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 489 ##########################################
    testcase = 489
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 490 ##########################################
    testcase = 490
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 491 ##########################################
    testcase = 491
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 492 ##########################################
    testcase = 492
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 493 ##########################################
    testcase = 493
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 494 ##########################################
    testcase = 494
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 495 ##########################################
    testcase = 495
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 496 ##########################################
    testcase = 496
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 497 ##########################################
    testcase = 497
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 498 ##########################################
    testcase = 498
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 499 ##########################################
    testcase = 499
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 500 ##########################################
    testcase = 500
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 501 ##########################################
    testcase = 501
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 502 ##########################################
    testcase = 502
    status("inactive")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
