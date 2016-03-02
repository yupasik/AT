# Test name = Infobanner_2
# Script dir = R:\Stingray\Tests\Infobanner_2\main\main.py

from time import sleep
from device import handler, updateTestResult
import RC
import UART
import DO
import GRAB
import MOD
import os
from DO import status
import OPER


def runTest():
    status("active")
    TestName = "Infobanner_2"
    ScriptName = "main"
    ScriptIndex = "1"
    Grabber = DO.grab_define()
    platform = DO.load_platform()
    Modulation = "DVBS"
    FEC = "3/4"
    SR = "27500000"
    Stream = "\\X_0000_00000_MUX_32000_EPG_Software_20130328a.ts"
    Stream_1 = "\\DRE Services\\X_0000_00000_MUX_38000_DRE4_Infocas_1.ts"
    Stream_2 = "\\DRE Services\\X_0000_00000_MUX_38000_DRE4_TVMail_1.ts"
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
    RC.push(["exit 1 3000", "red 1 3000"])    # RC macros from remote_control.ini file
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    UART.default_settings()
    OPER.search()
    MOD.stop(Modulator)
    MOD.play(Modulator)
    RC.push(["exit 1 3000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    RC.push(["exit 1 3000", "green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    RC.push(["exit 1 3000", "6 1 5000", "yellow 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    RC.push(["exit 2 5000", "0 1 5000", "play/pause 1 50000", "play/pause 1 5000", "red 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    RC.push(["exit 1 5000", "green 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    RC.push(["exit 1 5000", "yellow 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["stop 1 5000", "exit 2 5000", "red 1 5000", "up"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    RC.push(["up 1 3000", "left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    RC.push(["right 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    RC.push(["red 1 3000", "mute"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["red 1 3000", "standby 1 5000", "standby 1 10000"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["exit 1 3000", "red 1 5000", "menu 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    RC.push(["exit 1 3000", "red 1 5000", "VolUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    RC.push(["VolDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["ChUp 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["ChDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["last 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["red 1 5000", "1 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    RC.push(["left 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("active")
    RC.push(["green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("active")
    RC.push(["exit 1 3000", "6 1 5000", "red 1 3000", "yellow 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("active")
    RC.push(["blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("active")
    RC.push(["exit 2 3000", "rec 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("active")
    RC.push(["red 1 3000", "rec 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("active")
    RC.push(["left 1 3000", "ok 1 3000", "exit 2 5000", "play/pause 1 40000"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("active")
    RC.push(["red 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("active")
    RC.push(["play/pause 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("active")
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("active")
    RC.push(["stop 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("active")
    RC.push(["exit 2 5000", "0 1 5000", "red 1 3000", "down 1 3000", "up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("active")
    RC.push(["down 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    RC.push(["exit 2 5000", "6 1 5000", "red 1 3000", "down 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    RC.push(["ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("active")
    RC.push(["exit 2 5000", "6 1 5000", "red 1 3000", "down 1 3000", "right 3 2000", "ok 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("active")
    RC.push(["up 1 3000", "left 1 3000", "ok 1 5000", "down 1 2000", "right 1 2000",  "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    status("active")
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    RC.push(["down 2 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    RC.push(["exit 2 3000", "6 1 5000", "yellow 1 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("active")
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("active")
    RC.push(["down 2 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    status("active")
    RC.push(["exit 1 6000"])
    GRAB.compare(testcase)
############################ TestCase 52 ##########################################
    testcase = 52
    status("active")
    RC.push(["yellow 1 3000", "ok 1 3000", "up 2 3000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 53 ##########################################
    testcase = 53
    status("active")
    RC.push(["exit 2 6000"])
    GRAB.compare(testcase)
############################ TestCase 54 ##########################################
    testcase = 54
    status("active")
    RC.push(["0 1 6000", "red 1 3000", "down 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 55 ##########################################
    testcase = 55
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 56 ##########################################
    testcase = 56
    status("active")
    RC.push(["ChDown 12 3000"])
    GRAB.compare(testcase)
############################ TestCase 57 ##########################################
    testcase = 57
    status("active")
    RC.push(["ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 58 ##########################################
    testcase = 58
    status("active")
    RC.push(["ChUp 12 3000"])
    GRAB.compare(testcase)
############################ TestCase 59 ##########################################
    testcase = 59
    status("active")
    RC.push(["down 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 60 ##########################################
    testcase = 60
    status("active")
    RC.push(["down 12 3000"])
    GRAB.compare(testcase)
############################ TestCase 61 ##########################################
    testcase = 61
    status("active")
    RC.push(["up 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 62 ##########################################
    testcase = 62
    status("active")
    RC.push(["up 12 3000"])
    GRAB.compare(testcase)
############################ TestCase 63 ##########################################
    testcase = 63
    status("active")
    RC.push(["exit 1 3000", "ok 1 3000", "down 1 2000", "ok 1 3500"])
    GRAB.compare(testcase)
############################ TestCase 64 ##########################################
    testcase = 64
    status("active")
    RC.push(["id 1 3000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 65 ##########################################
    testcase = 65
    status("active")
    RC.push(["0 1 3500"])
    GRAB.compare(testcase)
############################ TestCase 66 ##########################################
    testcase = 66
    status("active")
    RC.push(["6 1 3500"])
    GRAB.compare(testcase)
############################ TestCase 67 ##########################################
    testcase = 67
    status("active")
    RC.push(["0 1 4000"])
    GRAB.compare(testcase)
############################ TestCase 68 ##########################################
    testcase = 68
    status("active")
    RC.push(["red 1 3000", "exit 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 69 ##########################################
    testcase = 69
    status("active")
    RC.push(["red 1 3000", "right 1 2000", "ok 1 3000", "exit 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 70 ##########################################
    testcase = 70
    status("active")
    RC.push(["red 1 3000", "left 3 2000"])
    GRAB.compare(testcase)
############################ TestCase 71 ##########################################
    testcase = 71
    status("active")
    RC.push(["ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 72 ##########################################
    testcase = 72
    status("active")
    RC.push(["left 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 73 ##########################################
    testcase = 73
    status("active")
    RC.push(["exit 1 3000", "0 1 5000", "red 1 5000"])
    sleep(60)
    GRAB.compare(testcase)
############################ TestCase 74 ##########################################
    testcase = 74
    status("active")
    UART.reboot()
    RC.push(["exit 1 3000", "red 1 5000", "right 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 75 ##########################################
    testcase = 75
    status("active")
    RC.push(["ok 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 76 ##########################################
    testcase = 76
    status("active")
    sleep(120)
    GRAB.compare(testcase)
############################ TestCase 77 ##########################################
    testcase = 77
    status("active")
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 78 ##########################################
    testcase = 78
    status("active")
    RC.push(["ok 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 79 ##########################################
    testcase = 79
    status("active")
    RC.push(["right 3 5000"])
    GRAB.compare(testcase)
############################ TestCase 80 ##########################################
    testcase = 80
    status("active")
    GRAB.compare(testcase)
############################ TestCase 81 ##########################################
    testcase = 81
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 82 ##########################################
    testcase = 82
    status("active")
    RC.push(["ok 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 83 ##########################################
    testcase = 83
    status("active")
    RC.push(["right 1 5000"])
    sleep(120)
    GRAB.compare(testcase)
############################ TestCase 84 ##########################################
    testcase = 84
    status("active")
    RC.push(["exit 2 3000", "0 1 5000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 85 ##########################################
    testcase = 85
    status("active")
    GRAB.compare(testcase)
############################ TestCase 86 ##########################################
    testcase = 86
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 87 ##########################################
    testcase = 87
    status("active")
    RC.push(["exit 2 3000", "red 1 5000", "play/pause 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 88 ##########################################
    testcase = 88
    status("active")
    RC.push(["stop 1 5000", "rec 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 89 ##########################################
    testcase = 89
    status("active")
    RC.push(["stop 1 10000", "left 1 2000", "ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 90 ##########################################
    testcase = 90
    status("active")
    GRAB.compare(testcase)
############################ TestCase 91 ##########################################
    testcase = 91
    status("active")
    GRAB.compare(testcase)
############################ TestCase 92 ##########################################
    testcase = 92
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 93 ##########################################
    testcase = 93
    status("active")
    RC.push(["exit 2 5000", "6 1 5000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 94 ##########################################
    testcase = 94
    status("active")
    RC.push(["exit 2 5000", "0 1 5000", "red 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 95 ##########################################
    testcase = 95
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 96 ##########################################
    testcase = 96
    status("active")
    GRAB.compare(testcase)
############################ TestCase 97 ##########################################
    testcase = 97
    status("active")
    RC.push(["blue 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 98 ##########################################
    testcase = 98
    status("active")
    GRAB.compare(testcase)
############################ TestCase 99 ##########################################
    testcase = 99
    status("active")
    MOD.stop(Modulator)
    GRAB.compare(testcase)
############################ TestCase 100 ##########################################
    testcase = 100
    status("active")
    MOD.play(Modulator)
    RC.push(["right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 101 ##########################################
    testcase = 101
    status("active")
    RC.push(["left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 102 ##########################################
    testcase = 102
    status("active")
    RC.push(["ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 103 ##########################################
    testcase = 103
    status("active")
    RC.push(["ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 104 ##########################################
    testcase = 104
    status("active")
    RC.push(["exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 105 ##########################################
    testcase = 105
    if platform == "E212":
        status("active")
    else:
        status("inactive")
    GRAB.compare(testcase)
############################ TestCase 106 ##########################################
    testcase = 106
    status("active")
    RC.push(["exit 2 4000", "red 1 3000", "cinemahalls 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 107 ##########################################
    testcase = 107
    status("active")
    RC.push(["help 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 108 ##########################################
    testcase = 108
    status("active")
    UART.start_app("scheduler")
    RC.push(["red", "ok 1 3000", "down 2 1000", "ok", "ok 1 2000", "right 1 1000", "up 2 2000", "ok", "ok", "exit 5 2400", "6 1 5000", "red 1 5000"])
    sleep(120)
    GRAB.compare(testcase)
############################ TestCase 109 ##########################################
    testcase = 109
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 110 ##########################################
    testcase = 110
    status("active")
    UART.default_settings()
    MOD.play_stream(Modulation, FEC, SR, Stream_1, Frequency, Modulator)
    OPER.search()
    RC.push(["exit 3 3000"])
    MOD.stop(Modulator)
    MOD.play(Modulator)
    RC.push(["red 1 40000", "exit 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 111 ##########################################
    testcase = 111
    status("active")
    UART.default_settings()
    MOD.play_stream(Modulation, FEC, SR, Stream_2, Frequency, Modulator)
    OPER.search()
    RC.push(["exit 3 3000"])
    MOD.stop(Modulator)
    MOD.play(Modulator)
    RC.push(["red 1 34000"])
    GRAB.compare(testcase)
############################ TestCase 112 ##########################################
    testcase = 112
    status("active")
    RC.push(["tv/mail 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 113 ##########################################
    testcase = 113
    status("active")
    RC.push(["sharp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 114 ##########################################
    testcase = 114
    status("active")
    RC.push(["star 1 3000"])
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
