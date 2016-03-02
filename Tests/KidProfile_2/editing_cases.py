# Test name = KidProfile_2
# Script dir = R:\Stingray\Tests\KidProfile_2\editing_cases\editing_cases.py

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
    TestName = "KidProfile_2"
    ScriptName = "editing_cases"
    ScriptIndex = "1"
    Grabber = DO.grab_define()
    platform = DO.load_platform()
    Modulation = "DVBS"
    FEC = "3/4"
    SR = "27500000"
    Stream2 = "\\Kid Profile\\X_0000_00000_MUX_38000_kidsprofile-test_12226_20130905a.ts"
    Stream = "\\Kid Profile\\X_0000_00000_MUX_38000_KidProfile_Auto_20140905a.ts"
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
    searching_from_wizard_centre_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "down", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_english_ALL = ["up 3 3400", "right 1 1000", "down 3 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 22200", "down 1 1000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_south_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200", "down", "down", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    load_regions_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200"]
    load_regions_english_E501 = ["up 2 2400", "right 1 1000", "down 2 2400", "ok 1 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 22200"]
    load_regions_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 22200"]
    load_regions_english_ALL = ["up 2 2400", "right 1 1000", "down 2 2400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 22200"]

############################ TestCase 1 ##########################################
    testcase = 1
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["exit 1 1000", "exit 1 1000"])
    
    #-----Activating KID Profile-----#
    #UART.activate_app("kidsmode")
    #UART.start_app("settings")
    #sleep(5)
    #RC.push(["right 1 1500", "right 1 1500", "right 1 1500", "right 1 1500", "right 1 1500", "right 1 1500", "right 1 1500", "OK 1 1500", "down 1 1500", "4 1 1500", "3 1 500", "2 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 1500", "1 1 1500", "1 1 1500", "1 1 1500", "1 1 1500", "1 1 1500", "1 1 1500", "1 1 1500", "1 1 5500", "exit 1 1500", "exit 1 1500", "exit 1 1500", "exit 1 1500"])
    sleep(3)
    RC.push(["kid_1 1 10500", "exit 1 1500", "left 1 1000", "OK 1 7000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 10000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    RC.push(["OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    RC.push(["exit 1 1000", "up 1 1000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    RC.push(["down 1 1000", "down 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    RC.push(["ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    RC.push(["ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    RC.push(["left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    RC.push(["right 1 1000", "green 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    RC.push(["exit 1 1000", "yellow 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 11 ##########################################
    testcase = 11
    status("active")
    RC.push(["up 1 1000", "blue 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("active")
    RC.push(["exit 1 1000", "red 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["exit 1 1000", "exit 1 1000"])
    sleep(3)
    RC.push(["kid_1 1 10500", "exit 1 1500", "left 1 1000", "OK 1 7000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 10000", "right 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = "14_1"
    status("active")
    RC.push(["green 1 1000", "OK 1 1000", "OK 1 1000", "exit 1 2000"])
    GRAB.compare(testcase)
    
    testcase = "14_2"
    status("active")
    RC.push(["exit 1 2000", "exit 1 1000", "exit 1 1000", "kid_7 1 10000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    RC.push(["exit 1 1000", "up 1 7000", "up 1 7000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 1000", "right 1 1000", "down 1 1000", "down 1 1000", "yellow 1 3000"])
    RC.push(["exit 1 7000", "red 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["kid_1 1 1000", "down 1 10000", "exit 1 1000", "left 1 1000", "OK 1 1000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 1000", "right 1 1000", "yellow 1 1000", "yellow 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "kid_1 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = "18_1"
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["kid_1 1 1000", "exit 1 1000", "left 1 1000", "OK 1 1000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 1000", "right 1 1000", "up 1 1000", "right 1 3000", "OK 1 1000", "left 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "18_2"
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "kid_OK 1 10000", "red 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "left 1 1000", "OK 1 1000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    RC.push(["up 1 1000", "right 1 1000", "OK 1 1000", "left 1 1000", "OK 1 1000", "right 1 1000", "green 1 1000", "OK 1 1000", "OK 1 1000", "OK 1 1000", "exit 1 2000"])
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000", "kid_star 1 10000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["kid_OK 1 7500", "exit 1 1000", "left 1 1000", "OK 1 1000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 1000", "yellow 1 1000", "left 1 1000", "OK 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000"])
    RC.push(["kid_OK 1 10500", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "left 1 1000", "OK 1 1000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    OPER.channel_block()
    OPER.set_pin("1111")
    RC.push(["kid_5 1 10000"])
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = "24_1"
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    UART.start_app("channelseditor")
    RC.push(["red 1 3000", "yellow 1 1000"])
    #"Детский"
    RC.push(["down 1 1000", "down 1 1000", "down 1 1000", "left 1 1500", "left 1 1500", "left 1 1500", "left 1 1500", "down 1 1500", "OK 1 1000", "yellow 1 1000", "left 1 1500", "left 1 1500", "left 1 1500", "left 1 1500", "up 1 1500", "OK 1 1000", "down 1 1500", "down 1 1500", "right 1 1500", "right 1 1500", "OK 1 1000", "left 3 1000", "OK 1 1000", "up 2 1000", "OK 1 1000", "down 1 1500", "down 1 1500", "right 1 1500", "right 1 1500", "OK 1 1000", "left 1 1500", "left 1 1500", "left 1 1500", "left 1 1500", "left 1 1500", "up 1 1000", "up 1 1000", "OK 1 1000"])
    #" режим"
    RC.push(["down 1 1500", "down 1 1500", "down 1 1500", "right 1 1500", "right 1 1500", "OK 1 1000", "yellow 1 1000", "up 1 1000", "up 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "OK 1 1000", "yellow 1 1000", "up 1 1000", "left 1 1000", "OK 1 1000", "down 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "OK 1 1000", "down 1 1000", "left 1 1000", "left 1 1000", "left 1 1000", "left 1 1000", "OK 1 1000", "left 1 1000", "OK 1 1000"])
    RC.push(["blue 1 1000", "right 1 1000", "OK 1 3000", "OK 1 1000", "OK 1 1000", "OK 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "kid_OK 1 8500", "OK 1 3000"])
    GRAB.compare(testcase)
    
    testcase = "24_2"
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "left 1 1000", "OK 1 1000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["kid_OK 1 7500", "exit 1 1000", "left 1 1000", "OK 1 1000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 1000", "green 1 1000", "5 1 1000", "6 1 1000", "7 1 1000", "blue 1 1000", "exit 1 1000", "exit 1 1000", "exit 1 1000", "kid_0 1 8000", "red 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("active")
    RC.push(["exit 1 1000", "left 1 1000", "OK 1 1000"])
    UART.start_app("channelseditor")
    RC.push(["up 1 1000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("manual") #Не удается обновить список каналов, "Список регионов недоступен"
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["kid_9 1 10000", "3 1 10000", "exit 1 1000", "left 1 1000", "OK 1 10000", "3 1 10000"])
    sleep(400)
    RC.push(["OK 1 40000", ])
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
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
