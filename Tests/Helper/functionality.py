# Test name = Helper
# Script dir = R:\Stingray\Tests\Helper\functionality\functionality.py
# Rev = v.1.05

from time import sleep
from device import handler, updateTestResult
import RC
import UART
import DO
import GRAB
import MOD
import OPER
import os
from DO import status


def runTest():
    status("active")
    TestName = "Helper"
    ScriptName = "functionality"
    ScriptIndex = "1"
    Grabber = DO.grab_define()
    platform = DO.load_platform()
    Modulation = "DVBS"
    FEC = "3/4"
    SR = "27500000"
    Stream = "\\X_0000_00000_MUX_32000_EPG_Software_20130328a.ts"
    Stream2 = "\\DRE Services\\X_0000_00000_MUX_38000_DRE4_Infocas_1.ts"
    Stream3 = "\\DRE Services\\X_0000_00000_MUX_38000_DRE4_TVMail_1.ts"
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

    """############################ TestCase 1 ##########################################
    testcase = 1
    status("active")
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    UART.default_settings()
    UART.start_app("")
    RC.push(["key_1", "key_2", "key_3"])    # set of the RC buttons
    sleep(0)
    RC.push("[macros_name]")    # RC macros from remote_control.ini file
    GRAB.compare(testcase)"""
############################ TestCase 1 ##########################################
    testcase = 1
    status("active")
    MOD.stop(Modulator)
    UART.default_settings()
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    UART.default_settings()
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000"])
    if platform == "E212":
        RC.push(["left 1 1000", "ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3 # Terrestrial search
    status("inactive")
    UART.default_settings
    RC.push([""])
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4 # Siberia
    status("inactive")
    RC.push([""])
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5 # Siberia
    status("inactive")
    RC.push([""])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    UART.default_settings()
    RC.push(["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000"])
    if platform == "E212":
        RC.push(["left 1 1000", "ok 1 1000"])
    RC.push(["standby 1 10000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    UART.default_settings()
    RC.push(["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000"])
    if platform == "E212":
        RC.push(["left 1 1000", "ok 1 1000"])
    UART.reboot()
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["standby 1 10000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["clock 1 2000"])
    GRAB.compare(testcase)
    RC.push(["clock 1 2000"])
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    RC.push(["standby 1 10000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    RC.push(["Tv/radio 1 1000"])
    GRAB.compare(testcase)
    RC.push(["Tv/radio 1 1000"])
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["standby 1 10000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    RC.push(["ID 1 1000"])
    GRAB.compare(testcase)
#------- Следующая строка добавлена для избавления от тормозов Телегида при первом запуске------
    RC.push(["guide 1 20000", "exit 1 1000", "guide 1 10000", "exit 1 1000", "guide 1 10000", "exit 1 1000"])
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["guide 1 10000", "right 1 3000", "left 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    RC.push(["help 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["ChUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["ChDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    RC.push(["Rec 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("active")
    RC.push(["play/pause 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("active")
    RC.push(["stop 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("active")
    RC.push(["RecList 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("active")
    RC.push(["cinemahalls 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("active")
    RC.push(["www 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("active")
    RC.push(["format 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("active")
    RC.push(["mail 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    RC.push(["Tv/chat 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("active")
    RC.push(["0 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("active")
    RC.push(["1 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    RC.push(["2 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    RC.push(["3 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("active")
    RC.push(["4 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    status("active")
    RC.push(["5 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 52 ##########################################
    testcase = 52
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 53 ##########################################
    testcase = 53
    status("active")
    RC.push(["6 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 54 ##########################################
    testcase = 54
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 55 ##########################################
    testcase = 55
    status("active")
    RC.push(["7 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 56 ##########################################
    testcase = 56
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 57 ##########################################
    testcase = 57
    status("active")
    RC.push(["8 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 58 ##########################################
    testcase = 58
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 59 ##########################################
    testcase = 59
    status("active")
    RC.push(["9 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 60 ##########################################
    testcase = 60
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 61 ##########################################
    testcase = 61
    status("active")
    RC.push(["red 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 62 ##########################################
    testcase = 62
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 63 ##########################################
    testcase = 63
    status("active")
    RC.push(["green 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 64 ##########################################
    testcase = 64
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 65 ##########################################
    testcase = 65
    status("active")
    RC.push(["yellow 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 66 ##########################################
    testcase = 66
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 67 ##########################################
    testcase = 67
    status("active")
    RC.push(["blue 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 68 ##########################################
    testcase = 68
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 69 ##########################################
    testcase = 69
    status("active")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 70 ##########################################
    testcase = 70
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 71 ##########################################
    testcase = 71
    status("active")
    RC.push(["left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 72 ##########################################
    testcase = 72
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 73 ##########################################
    testcase = 73
    status("active")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 74 ##########################################
    testcase = 74
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 75 ##########################################
    testcase = 75
    status("active")
    RC.push(["ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 76 ##########################################
    testcase = 76
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 77 ##########################################
    testcase = 77
    status("active")
    RC.push(["right 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 78 ##########################################
    testcase = 78
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 79 ##########################################
    testcase = 79
    status("active")
    RC.push(["right 1 1000", "right 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 80 ##########################################
    testcase = 80
    status("active")
    UART.default_settings()
    RC.push(["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000"])
    if platform == "E212":
        RC.push(["left 1 1000", "ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 81 ##########################################
    testcase = 81
    status("active")
    RC.push(["VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 82 ##########################################
    testcase = 82
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 83 ##########################################
    testcase = 83
    status("active")
    RC.push(["VolDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 84 ##########################################
    testcase = 84
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 85 ##########################################
    testcase = 85
    status("active")
    RC.push(["stb 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 86 ##########################################
    testcase = 86
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 87 ##########################################
    testcase = 87
    status("active")
    RC.push(["mute 1 1000"])
    GRAB.compare(testcase)
    RC.push(["mute 1 1000"])
############################ TestCase 88 ##########################################
    testcase = 88
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 89 ##########################################
    testcase = 89
    status("active")
    RC.push(["menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 90 ##########################################
    testcase = 90
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 91 ##########################################
    testcase = 91
    status("active")
    RC.push(["last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 92 ##########################################
    testcase = 92
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 93 ##########################################
    testcase = 93
    status("active")
    RC.push(["standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 94 ##########################################
    testcase = 94
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000"])
    if platform == "E212":
        RC.push(["left 1 1000", "ok 1 1000"])
    RC.push(["6 1 1000"])
#----Setting PIN and blocking the channel----
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "OK 1 5000", "1 1 1000", "1 1 1000", "1 1 1000", "1 1 1000", "1 1 1000", "1 1 1000", "1 1 1000", "1 1 2000", "OK 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000"])
    UART.start_app("channelseditor")
    RC.push(["right 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "0 1 1000"])
    OPER.channel_block()
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "0 1 1000"])
#----/Setting PIN and blocking the channel----
    RC.push(["standby 1 60000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 95 ##########################################
    testcase = 95
    status("active")
    RC.push(["1 1 1000", "1 1 1000", "1 1 1000", "1 1 10500"])
    GRAB.compare(testcase)
############################ TestCase 96 ##########################################
    testcase = 96
    status("active")
#----Unsetting PIN----
    UART.start_app("settings")
    RC.push(["right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1000", "OK 1 3000", "1 1 1000", "1 1 1000", "1 1 1000", "1 1 2000", "exit 1 1000", "exit 1 1000", "exit 1 1000"])
#----/Unsetting PIN----
    UART.start_app("scheduler")
    RC.push(["red 1 1000", "OK 1 1000", "down 1 1000", "OK 1 1000", "OK 1 1000", "right 1 1000", "up 1 1000", "up 1 1000", "OK 1 1000", "OK 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "standby 1 120000"])
    GRAB.compare(testcase)
############################ TestCase 97 ##########################################
    testcase = 97
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 98 ##########################################
    testcase = 98
    status("active")
    MOD.stop(Modulator)
    UART.default_settings()
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    RC.push(["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000"])
    if platform == "E212":
        RC.push(["left 1 1000", "ok 1 1000"])
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 1 1000", "down 1 5000", "standby 1 15000", "standby 1 15000"])
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    sleep(40)
    GRAB.compare(testcase)
############################ TestCase 99 ##########################################
    testcase = 99
    status("active")
    RC.push(["exit 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 100 ##########################################
    testcase = 100
    status("active")
    MOD.stop(Modulator)
    UART.default_settings()
    MOD.play_stream(Modulation, FEC, SR, Stream3, Frequency, Modulator)
    RC.push(["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000"])
    if platform == "E212":
        RC.push(["left 1 1000", "ok 1 1000"])
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 1 1000", "down 1 5000", "standby 1 15000", "standby 1 15000"])
    MOD.play_stream(Modulation, FEC, SR, Stream3, Frequency, Modulator)
    sleep(80)
    GRAB.compare(testcase)
############################ TestCase 101 ##########################################
    testcase = 101
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 102 ##########################################
    testcase = 102
    status("active")
    MOD.stop(Modulator)
    UART.default_settings()
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000"])
    if platform == "E212":
        RC.push(["left 1 1000", "ok 1 1000"])
    RC.push(["right 1 1000", "right 1 1000", "OK 1 1000", "standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 103 ##########################################
    testcase = 103
    status("active")
    MOD.stop(Modulator)
    UART.default_settings()
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000"])
    if platform == "E212":
        RC.push(["left 1 1000", "ok 1 1000"])
    RC.push(["right 1 1000", "right 1 1000", "OK 1 1000"])
    UART.reboot()
    GRAB.compare(testcase)
############################ TestCase 104 ##########################################
    testcase = 104
    status("active")
    MOD.stop(Modulator)
    UART.default_settings()
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000"])
    if platform == "E212":
        RC.push(["left 1 1000", "ok 1 1000"])
    RC.push(["right 1 1000", "right 1 1000", "OK 1 1000"])
    UART.start_app("wizard")
    RC.push(["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "ok 1 15000", "ok 1 10000", "standby 1 15000", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 105 ##########################################
    testcase = 105
    status("manual")
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
