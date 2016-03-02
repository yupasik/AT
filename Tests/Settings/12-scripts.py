# Test name = Settings
# Script dir = R:\Stingray\Tests\Settings\12-scripts\12-scripts.py

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
    ScriptName = "12-scripts"
    ScriptIndex = "12"
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
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)k
    UART.default_settings()
    if platform in ["E501", "E502", "A230"]:
        RC.push(searching_from_wizard_general_E501)
    else:
        RC.push(searching_from_wizard_general_ALL)
    UART.start_app("settings")
    RC.push(["cinemahalls"])
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    RC.push(["help"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    MOD.stop(Modulation)
    MOD.play(Modulation)
    UART.start_app("scheduler")
    RC.push(["red", "ok 1 2400", "down 4 1000", "ok", "ok", "right 1 1000", "up 2 1000", "ok", "ok", "exit 5 2400"])
    UART.start_app("settings")
    sleep(80)
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
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["VolUp 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["VolDown 1 2400"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    RC.push(["mute"])
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    RC.push(["guide"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["tv/chat"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    RC.push(["star"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    RC.push(["sharp"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    RC.push(["tv/radio"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["stb"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    RC.push(["ID"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    RC.push(["format"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["red"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["green"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["yellow"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["blue"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    RC.push(["exit 2 3000"])
    UART.start_app("settings")
    RC.push(["down", "right", "down", "right"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    UART.start_app("settings")
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("active")
    RC.push(["left 10 2000", "right", "down", "left", "exit", "down", "right", "exit", "down", "right", "down", "right", "ok 1 8000", "left", "ok", "down", "right"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("active")
    RC.push(["exit 2 3000", "format 2 1000", "ok"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    RC.push(["exit", "format"])
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("active")
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 2 3000", "down", "right", "down", "left", "down", "right"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("active")
    RC.push(["exit 2 3000", "0 1 5000", "down 1 3000", "green 1 2000", "down", "ok"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    RC.push(["exit 2 5000", "green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("active")
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 3 3000"])
    RC.push(["down 1 3000", "right", "down 2 2000", "right"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 3 3000"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("active")
    RC.push(["exit 2 3000", "clock 1 2000"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    RC.push(["exit 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("active")
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 5 3000"])
    RC.push(["down 1 3000", "right", "down 1 2000", "right", "down 1 2000", "right", "down 1 2000", "right", "down 1 2000", "right", "down 1 2000", "right"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 5 3000"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("active")
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 6 3000"])
    RC.push(["down 1 3000", "right", "1 4 2000", "1 4 2000", "ok 1 2000", "down 2 2000", "right"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 6 3000"])
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("active")
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("active")
    UART.start_app("satelliteeditor")
    RC.push(["red 1 3000", "down", "right", "down", "right 2 2000", "down", "left 5 2000", "1 5 2000", "down", "left 5 2000", "1 2 2000", "2 3 2000", "down", "right", "down", "right", "down 2 2000", "ok 2 2000"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    UART.start_app("satelliteeditor")
    RC.push(["down 2 1000", "ok 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("active")
    UART.start_app("scheduler")
    RC.push(["red", "ok 1 3000", "right 1 2000", "ok", "ok", "right 4 1000", "up", "ok", "ok", "red", "ok 1 3000", "right 1 2000", "down 2 2000", "ok", "ok", "right 4 1000", "up 2 1000", "ok", "ok", "red", "ok 1 3000", "right 1 1000", "down", "ok", "ok", "right 4 1000", "up 3 1000", "ok", "ok"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    UART.start_app("scheduler")
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("active")
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1 5 2000", "ok 1 3000", "right 1 2000", "green 1 3000", "ok 5 2000", "exit 1 3000", "left 1 3000"])
    sleep(120)
    RC.push(["standby 1 5000", "standby 1 10000"])
    UART.start_app("channelseditor")
    RC.push(["down 2 1000"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 2 3000"])
    UART.start_app("settings")
    RC.push(["down", "right", "down", "right", "down", "right"])
    sleep(120)
    UART.reboot()
    UART.start_app("settings")
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    RC.push(["right", "down", "left", "exit", "down", "right", "exit", "down", "right", "down", "right", "ok 1 8000", "left", "ok", "down", "right"])
    sleep(120)
    UART.reboot()
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    RC.push(["exit 2 3000", "format 2 1000", "ok"])
    sleep(120)
    UART.reboot()
    RC.push(["exit 2 10000", "format"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 2 3000", "down", "right", "down", "left", "down", "right"])
    sleep(120)
    UART.reboot()
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("active")
    RC.push(["exit 2 3000", "0 1 5000", "down 1 3000", "green 1 2000", "down", "ok"])
    sleep(120)
    UART.reboot()
    RC.push(["exit 2 10000", "green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("active")
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 3 3000"])
    RC.push(["down 1 3000", "right", "down 2 2000", "right"])
    sleep(120)
    UART.reboot()
    RC.push(["exit 2 5000"])
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 3 3000"])
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("active")
    RC.push(["exit 2 3000", "clock 1 2000"])
    sleep(120)
    UART.reboot()
    RC.push(["exit 1 8000"])
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    status("active")
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 5 3000"])
    RC.push(["down 1 3000", "right", "down 1 2000", "right", "down 1 2000", "right", "down 1 2000", "right", "down 1 2000", "right", "down 1 2000", "right"])
    sleep(120)
    UART.reboot()
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 5 3000"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 6 3000"])
    RC.push(["down 1 3000", "ok", "0 4 2000", "0 4 2000", "ok 1 2000", "down 2 2000", "right"])
    sleep(120)
    UART.reboot()
    UART.start_app("settings")
    RC.push(["left 10 2000", "right 6 3000"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    GRAB.compare(testcase)
    OPER.unset_pin()
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    UART.start_app("satelliteeditor")
    RC.push(["red 1 3000", "down", "right", "down", "right 2 2000", "down", "left 5 2000", "1 5 2000", "down", "left 5 2000", "1 2 2000", "2 3 2000", "down", "right", "down", "right", "down 2 2000", "ok 2 2000"])
    sleep(120)
    UART.reboot()
    UART.start_app("satelliteeditor")
    RC.push(["down 2 1000", "ok 2 3000"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("active")
    UART.start_app("scheduler")
    RC.push(["red", "ok 1 3000", "right 1 2000", "ok", "ok", "right 4 1000", "up", "ok", "ok", "red", "ok 1 3000", "right 1 2000", "down 2 2000", "ok", "ok", "right 4 1000", "up 2 1000", "ok", "ok", "red", "ok 1 3000", "right 1 1000", "down", "ok", "ok", "right 4 1000", "up 3 1000", "ok", "ok", "OK 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "up 1 1000", "up 1 1000", "up 1 1000", "OK 1 1000", "OK 1 10000", "exit 1 1000", "exit 1 1000", "exit 1 1000"])
    sleep(120)
    UART.reboot()
    RC.push(["exit 1 10000", "clock 1 10000"])
    UART.start_app("scheduler")
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("active")
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "1 5 2000", "ok 1 3000", "ok 1 2000", "ok 1 3000", "ok 5 2000", "exit 1 3000", "left 1 3000"])
    sleep(120)
    UART.reboot()
    UART.start_app("channelseditor")
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    status("manual")
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
