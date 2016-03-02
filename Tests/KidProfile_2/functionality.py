# Test name = KidProfile_2
# Script dir = R:\Stingray\Tests\KidProfile_2\functionality\functionality.py
# Rev v.2.0

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
    ScriptName = "functionality"
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


############################ TestCase 1 ##########################################
    testcase = 1
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    RC.push(["exit 1 1000", "exit 1 1000"])
    
    #-----Activating KID Profile-----#
    UART.activate_app("kidsmode")
    #UART.start_app("settings")
    #sleep(5)
    #RC.push(["right 1 1500", "right 1 1500", "right 1 1500", "right 1 1500", "right 1 1500", "right 1 1500", "right 1 1500", "OK 1 1500", "down 1 1500", "4 1 500", "3 1 500", "2 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 500", "1 1 5500", "exit 1 500", "exit 1 500", "exit 1 500", "exit 1 500"])
    sleep(3)
    RC.push(["kid_standby 1 10500", "standby 1 15000"])
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = "2_1"
    status("active")
    UART.default_settings()
    RC.push(["exit 1 3500"])
    
    #The following line has been added because of #26846
    #RC.push(["kid_1 1 2500", "exit 1 6000"])
    
    RC.push(["kid_1 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_2"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_2 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_3"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_3 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_4"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_4 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_5"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_5 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_6"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_6 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_7"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_7 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_8"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_8 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_9"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_9 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_10"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_0 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_11"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_up 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_12"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_down 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_13"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_right 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_14"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_left 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_15"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_ok 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_16"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_ChUp 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_17"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_ChDown 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_18"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_VolUp 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_19"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_VolDown 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "2_20"
    status("active")
    RC.push(["exit 1 5000"])
    RC.push(["kid_star 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = "3_1"
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 2 7500"])
    RC.push(["kid_1 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_2"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_2 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_3"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_3 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_4"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_4 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_5"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_5 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_6"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_6 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_7"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_7 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_8"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_8 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_9"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_9 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_10"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_0 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_11"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_up 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_12"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_down 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_13"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_right 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_14"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_left 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_15"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_ok 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_16"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_ChUp 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_17"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_ChDown 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_18"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_VolUp 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_19"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_VolDown 1 4000"])
    GRAB.compare(testcase)
    
    testcase = "3_20"
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    RC.push(["kid_star 1 4000"])
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    RC.push(["exit 1 2000", "OK 1 1000", "exit 1 1000"])
    #UART.start_app("kidsmode")
    RC.push(["kid_star 1 4000"])
    sleep(2)
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    UART.reboot()
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
    #UART.start_app("kidsmode")
    RC.push(["kid_star 1 4000"])
    sleep(2)
    RC.push(["standby 1 15000", "standby 1 6000"])
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    #UART.start_app("kidsmode")
    RC.push(["kid_star 1 4000"])
    RC.push(["kid_standby 1 15000", "kid_standby 1 6000"])
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = "10_1" #TricolorTV Search
    status("active")
    RC.push(["exit 1 1500", "ok 1 1500"])
    UART.start_app("tricolorsearch")
    sleep(10)
    RC.push(["kid_OK 1 3000"])
    GRAB.compare(testcase)
    
    testcase = "10_2" #Wizard
    status("active")
    RC.push(["exit 1 1500", "ok 1 1500"])
    UART.start_app("wizard")
    sleep(3)
    RC.push(["kid_OK 1 3000"])
    if platform in ["E501", "E502", "A230"]:
        RC.push(["kid_OK 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "10_3" #Manual Search 
    #-----------
    #BUG 21762 is FIXED
    #-----------
    status("active")
    RC.push(["exit 1 1500", "ok 1 1500"])
    UART.start_app("dvbsmanualscanner")
    sleep(10)
    RC.push(["kid_OK 1 3000"])
    GRAB.compare(testcase)
    
    testcase = "10_4" #Terrestrial Search
    if platform == "E212":
        status("active")
    else:
        status("inactive")
    RC.push(["exit 1 1500", "ok 1 1500"])
    UART.start_app("dvbtscanner")
    sleep(10)
    RC.push(["kid_OK 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 278 ##########################################
    testcase = 278
    status("active")
    UART.start_app("channelsearch")
    RC.push(["kid_1 1 5500"])
    GRAB.compare(testcase)    
############################ TestCase 11 ##########################################
    testcase = 11
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 12 ##########################################
    testcase = 12
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 13 ##########################################
    testcase = 13
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "exit 1 1000", "mute 1 1000"])
    RC.push(["kid_4 1 3500"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = "14_1"
    status("active")
    RC.push(["exit 1 1500", "OK 1 1500", "mute 1 6000"])
    RC.push(["VolUp 1 100", "kid_4 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "14_2"
    status("active")
    RC.push(["exit 1 1500", "OK 1 1500", "exit 1 5500"])
    RC.push(["VolDown 1 1000", "kid_ok 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "14_3"
    status("active")
    RC.push(["exit 1 1500", "OK 1 1500", "exit 1 5000"])
    RC.push(["right 1 1000", "kid_star 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "14_4"
    status("active")
    RC.push(["exit 1 1500", "OK 1 1500", "exit 1 5000"])
    RC.push(["left 1 1000", "kid_9 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15 #TV Mail
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    OPER.search()
    MOD.stop(Modulator)
    UART.reboot()
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    sleep(60)
    RC.push(["kid_Left 1 1000", "kid_4 1 5500"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16 #InfoCAS
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    OPER.search()
    MOD.stop(Modulator)
    RC.push(["exit 1 1000", "OK 1 1000", "exit 1 1000", "OK 1 1000", "exit 1 1000"])
    MOD.stop(Modulator)
    UART.reboot()
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    RC.push(["exit 1 1000"])
    sleep(125)
    GRAB.compare("16_1")
    RC.push(["kid_star 1 4000"])
    GRAB.compare_invert("16_2")
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    RC.push(["exit 1 1000", "OK 1 1000", "exit 1 1000", "OK 1 1000", "exit 1 1000"])
    RC.push(["cinemahalls 1 1000", "kid_1 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    MOD.stop(Modulator)
    UART.default_settings()
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["exit 1 1500"])
    UART.start_app("scheduler")
    if platform == "E212":
        RC.push(["red 1 1500", "ok 1 1500", "down 1 1000", "ok 1 1000", "ok 1 1000", "right 1 1000", "0 1 1000", "4 1 1000", "ok 1 2000", "ok 1 2000", "exit 1 1500", "exit 1 1500", "exit 1 1500", "exit 1 1500"])
    else:
        RC.push(["red 1 1500", "ok 1 1500", "up 1 1000", "up 1 1000", "ok 1 1000", "ok 1 1000", "right 1 1000", "1 1 1000", "8 1 1000", "ok 1 2000", "ok 1 2000", "exit 1 1500", "exit 1 1500", "exit 1 1500", "exit 1 1500"])
    RC.push(["kid_1 1 1500"])
    if platform == "E212":
        sleep(41)
    else:
        sleep(70)
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    MOD.stop(Modulator)
    UART.default_settings()
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["exit 1 1500"])
    UART.start_app("scheduler")
    if platform == "E212":
        RC.push(["red 1 1500", "ok 1 1500", "down 1 1000", "ok 1 1000", "ok 1 1000", "right 1 1000", "0 1 1000", "4 1 1000", "ok 1 2000", "ok 1 2000", "exit 1 1500", "exit 1 1500", "exit 1 1500", "exit 1 1500"])
    else:
        RC.push(["red 1 1500", "ok 1 1500", "up 1 1000", "up 1 1000", "up 1 1000", "ok 1 1000", "ok 1 1000", "right 1 1000", "1 1 1000", "8 1 1000", "ok 1 2000", "ok 1 2000", "exit 1 1500", "exit 1 1500", "exit 1 1500", "exit 1 1500"])
    RC.push(["kid_1 1 1500"])
    if platform == "E212":
        sleep(41)
    else:
        sleep(70)
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["exit 1 1000", "clock 1 1000", "kid_1 1 10000"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    RC.push(["clock 1 1000", "exit 1 1000", "OK 1 1000", "yellow 1 2000", "kid_OK 1 3500"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["exit 1 1000", "OK 1 1000", "green 1 2000", "kid_OK 1 3500"])
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    RC.push(["exit 1 1000", "OK 1 1000", "format 1 2000", "kid_OK 1 3500"])
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
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("active")
    RC.push(["ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("active")
    RC.push(["exit 1 1000", "3 1 7000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("active")
    sleep(4)
    RC.push(["2 1 7000", "down 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("active")
    sleep(4)
    RC.push(["left 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("active")
    RC.push(["right 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("active")
    RC.push(["3 1 7000", "ChUp 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("active")
    RC.push(["2 1 7000", "ChDown 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("active")
    sleep(5)
    RC.push(["VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    RC.push(["VolDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = "37_1"
    status("active")
    RC.push(["2 1 1000"])
    sleep(5)
    RC.push(["1 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "37_2"
    status("active")
    sleep(5)
    RC.push(["2 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "37_3"
    status("active")
    sleep(5)
    RC.push(["3 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "37_4"
    status("active")
    sleep(5)
    RC.push(["4 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "37_5"
    status("active")
    sleep(5)
    RC.push(["5 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "37_6"
    status("active")
    sleep(5)
    RC.push(["6 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "37_7"
    status("active")
    sleep(5)
    RC.push(["7 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "37_8"
    status("active")
    sleep(5)
    RC.push(["8 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "37_9"
    status("active")
    sleep(5)
    RC.push(["9 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    sleep(5)
    RC.push(["9 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    RC.push(["standby 1 15000", "standby 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    UART.default_settings()
    OPER.search()
    OPER.set_pin()
    RC.push(["kid_OK 1 10000", "menu 1 1000"])
    GRAB.compare(testcase)
#____ВНИМАНИЕ! Дальше тесты идут не по порядку для удобства!_____#
############################ TestCase 41 ##########################################
    testcase = 42
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 44
    status("active")
    RC.push(["exit 1 1000", "last 1 1000"])
    GRAB.compare(testcase)
    RC.push(["0 1 1000", "0 1 1000", "0 1 1000", "0 1 1000"])
############################ TestCase 43 ##########################################
    testcase = 41
    status("active")
    OPER.unset_pin()
    RC.push(["kid_OK 1 10000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 43
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    RC.push(["exit 1 1000", "last 1 1000"])
    GRAB.compare(testcase)
#____ВНИМАНИЕ! Дальше тесты идут снова по порядку!_____#
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    RC.push(["exit 1 1000", "format 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    RC.push(["exit 1 7000", "mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("active")
    RC.push(["mute 1 1000", "blue 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("active")
    RC.push(["exit 1 1000", "red 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    status("active")
    RC.push(["exit 1 1000", "yellow 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    status("active")
    RC.push(["exit 1 1000", "green 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 52 ##########################################
    testcase = 52
    status("active")
    RC.push(["exit 1 1000", "Rec 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 53 ##########################################
    testcase = 53
    status("active")
    RC.push(["play/pause 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 54 ##########################################
    testcase = 54
    status("active")
    sleep(10)
    RC.push(["guide 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 55 ##########################################
    testcase = 55
    status("active")
    RC.push(["exit 1 1000", "forward 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 56 ##########################################
    testcase = 56
    status("active")
    sleep(10)
    RC.push(["backward 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 57 ##########################################
    testcase = 57
    status("active")
    sleep(10)
    RC.push(["stop 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 58 ##########################################
    testcase = 58
    status("active")
    sleep(10)
    RC.push(["clock 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 59 ##########################################    
    testcase = "59_1"
    status("active")
    RC.push(["clock 1 1000", "status 1 3000"])
    GRAB.compare(testcase)
    
    testcase = "59_2"
    status("active")
    sleep(10)
    RC.push(["help 1 3000"])
    GRAB.compare(testcase)
    
    testcase = "59_3"
    status("active")
    sleep(10)
    RC.push(["reclist 1 3000"])
    GRAB.compare(testcase)
    
    testcase = "59_4"
    status("active")
    sleep(10)
    RC.push(["cinemahalls 1 3000"])
    GRAB.compare(testcase)
    
    testcase = "59_5"
    status("active")
    sleep(10)
    RC.push(["www 1 3000"])
    GRAB.compare(testcase)
    
    testcase = "59_6"
    status("active")
    sleep(10)
    RC.push(["Tv/radio 1 3000"])
    GRAB.compare(testcase)
    
    #STB-131
    testcase = "59_7"
    status("active")
    sleep(10)
    RC.push(["stb 1 3000"])
    GRAB.compare(testcase)
    
    testcase = "59_8"
    status("active")
    sleep(10)
    RC.push(["Tv/chat 1 3000"])
    GRAB.compare(testcase)
    
    testcase = "59_9"
    status("active")
    sleep(10)
    RC.push(["mail 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 60 ##########################################
    testcase = 60
    status("active")
    RC.push(["kid_4 1 5500", "kid_ok 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 61 ##########################################
    testcase = 61
    status("active")
    RC.push(["exit 1 1000", "kid_3 1 6000", "kid_up 1 3500"])
    GRAB.compare(testcase)
############################ TestCase 62 ##########################################
    testcase = 62
    status("active")
    sleep(5)
    RC.push(["kid_1 1 6000", "kid_up 1 6000", "kid_down 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 63 ##########################################
    testcase = 63
    status("active")
    sleep(5)
    RC.push(["kid_left 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 64 ##########################################
    testcase = 64
    status("active")
    RC.push(["kid_right 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 65 ##########################################
    testcase = 65
    status("active")
    RC.push(["kid_3 1 6000", "kid_3 1 6000", "kid_ChUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 66 ##########################################
    testcase = 66
    status("active")
    RC.push(["kid_1 1 6000", "kid_up 1 6000", "kid_ChDown 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 67 ##########################################
    testcase = 67
    status("active")
    RC.push(["kid_VolUp 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 68 ##########################################
    testcase = 68
    status("active")
    RC.push(["kid_VolDown 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 69 ##########################################
    testcase = "69_1"
    status("active")
    RC.push(["2 1 6000", "kid_1 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "69_2"
    status("active")
    sleep(10)
    RC.push(["kid_2 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "69_3"
    status("active")
    sleep(10)
    RC.push(["kid_3 1 1000"])
    GRAB.compare(testcase)
    
    testcase = "69_4"
    status("active")
    sleep(10)
    RC.push(["kid_4 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "69_5"
    status("active")
    sleep(10)
    RC.push(["kid_5 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "69_6"
    status("active")
    sleep(10)
    RC.push(["kid_6 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "69_7"
    status("active")
    sleep(10)
    RC.push(["kid_7 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "69_8"
    status("active")
    sleep(10)
    RC.push(["kid_8 1 1500"])
    GRAB.compare(testcase)
    
    testcase = "69_9"
    status("active")
    sleep(10)
    RC.push(["kid_9 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 70 ##########################################
    testcase = 70
    status("active")
    sleep(10)
    RC.push(["kid_0 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 71 ##########################################
    testcase = 71
    status("active")
    RC.push(["kid_star 1 5500"])
    GRAB.compare(testcase)
############################ TestCase 72 ##########################################
    testcase = 72
    status("active")
    RC.push(["kid_standby 1 15000", "kid_standby 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 73 ##########################################
    testcase = 73
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["kid_star 1 7000", "OK 1 2000", "down 3 2000"])
    RC.push(["OK 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 74 ##########################################
    testcase = 74
    status("active")
    RC.push(["ok 1 2000", "up 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 75 ##########################################
    testcase = 75
    status("active")
    RC.push(["down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 76 ##########################################
    testcase = 76
    status("active")
    RC.push(["left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 77 ##########################################
    testcase = 77
    status("active")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 78 ##########################################
    testcase = 78
    status("active")
    RC.push(["left 1 1000", "chUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 79 ##########################################
    testcase = 79
    status("active")
    RC.push(["ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 80 ##########################################
    testcase = 80
    status("active")
    RC.push(["standby 1 15000", "standby 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 81 ##########################################
    testcase = 81
    status("active")
    RC.push(["exit 1 6000", "blue 1 1000", "mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 82 ##########################################
    testcase = 82
    status("active")
    RC.push(["mute 1 2000", "blue 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 83 ##########################################
    testcase = 83
    status("active")
    RC.push(["blue 1 1000", "menu 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 84 ##########################################
    testcase = 84
    status("active")
    RC.push(["blue 1 1000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 85 ##########################################
    testcase = 85
    status("active")
    RC.push(["blue 1 1000", "last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 86 ##########################################
    testcase = 86
    status("active")
    RC.push(["3 1 7000", "blue 1 1000", "down 1 1000", "kid_ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 87 ##########################################
    testcase = 87
    status("active")
    RC.push(["blue 1 1000", "kid_up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 88 ##########################################
    testcase = 88
    status("active")
    RC.push(["kid_down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 89 ##########################################
    testcase = 89
    status("active")
    RC.push(["kid_left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 90 ##########################################
    testcase = 90
    status("active")
    RC.push(["kid_right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 91 ##########################################
    testcase = 91
    status("active")
    RC.push(["kid_left 1 1000", "kid_ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 92 ##########################################
    testcase = 92
    status("active")
    RC.push(["kid_ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 93 ##########################################
    testcase = 93
    status("active")
    RC.push(["kid_VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 94 ##########################################
    testcase = 94
    status("active")
    RC.push(["kid_VolDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 95 ##########################################
    testcase = 95
    status("active")
    RC.push(["kid_standby 1 5000", "kid_standby 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 96 ##########################################
    testcase = 96
    status("active")
    RC.push(["blue 1 1000", "kid_star 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 97 ##########################################
    testcase = 97
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["kid_star 1 7000", "kid_star 1 7000", "down 3 2000"])
    RC.push(["OK 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 98 ##########################################
    testcase = 98
    status("active")
    RC.push(["up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 99 ##########################################
    testcase = 99
    status("active")
    RC.push(["down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 100 ##########################################
    testcase = 100
    status("active")
    RC.push(["left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 101 ##########################################
    testcase = 101
    status("active")
    RC.push(["up 1 1000", "up 1 1000", "up 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 102 ##########################################
    testcase = 102
    status("active")
    RC.push(["down 1 1000", "ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 103 ##########################################
    testcase = 103
    status("active")
    RC.push(["ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 104 ##########################################
    testcase = 104
    status("active")
    RC.push(["standby 1 15000", "standby 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 105 ##########################################
    testcase = 105
    status("active")
    RC.push(["exit 1 1000", "kid_star 1 2000", "mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 106 ##########################################
    testcase = 106
    status("active")
    RC.push(["mute 1 1000", "guide 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 107 ##########################################
    testcase = 107
    status("active")
    RC.push(["kid_star 1 2000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 108 ##########################################
    testcase = 108
    status("active")
    RC.push(["kid_star 1 2000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 109 ##########################################
    testcase = 109
    status("active")
    RC.push(["kid_star 1 2000", "last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 110 ##########################################
    testcase = 110
    status("active")
    RC.push(["3 1 5000", "kid_star 1 2000", "down 1 1000", "kid_ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 111 ##########################################
    testcase = 111
    status("active")
    RC.push(["kid_up 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 112 ##########################################
    testcase = 112
    status("active")
    RC.push(["kid_down 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 113 ##########################################
    testcase = 113
    status("active")
    RC.push(["kid_left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 114 ##########################################
    testcase = 114
    status("active")
    RC.push(["kid_up 1 1000", "kid_up 1 1000", "kid_up 1 1000", "kid_right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 115 ##########################################
    testcase = 115
    status("active")
    RC.push(["kid_down 1 1000", "kid_ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 116 ##########################################
    testcase = 116
    status("active")
    RC.push(["kid_ChDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 279 ##########################################
    testcase = 279
    status("active")
    RC.push(["kid_VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 280 ##########################################
    testcase = 280
    status("active")
    RC.push(["kid_VolDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 117 ##########################################
    testcase = 117
    status("active")
    RC.push(["kid_standby 1 15000", "kid_standby 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 118 ##########################################
    testcase = 118
    status("active")
    RC.push(["exit 1 1000", "kid_star 1 2000", "kid_star 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 119 ##########################################
    testcase = 119
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["kid_star 1 7000", "red 1 3000"])
    RC.push(["OK 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 120 ##########################################
    testcase = 120
    status("active")
    RC.push(["down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 121 ##########################################
    testcase = 121
    status("active")
    RC.push(["up 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 122 ##########################################
    testcase = 122
    status("active")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 123 ##########################################
    testcase = 123
    status("active")
    RC.push(["ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 124 ##########################################
    testcase = 124
    status("active")
    RC.push(["ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 125 ##########################################
    testcase = 125
    status("active")
    RC.push(["standby 1 15000", "standby 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 126 ##########################################
    testcase = 126
    status("active")
    RC.push(["exit 1 1000", "red 1 2000", "mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 127 ##########################################
    testcase = 127
    status("active")
    RC.push(["mute 1 1000", "red 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 128 ##########################################
    testcase = 128
    status("active")
    RC.push(["red 1 1000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 129 ##########################################
    testcase = 129
    status("active")
    RC.push(["red 1 1000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 130 ##########################################
    testcase = 130
    status("active")
    RC.push(["red 1 1000", "last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 131 ##########################################
    testcase = 131
    status("active")
    RC.push(["red 1 1000", "kid_ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 132 ##########################################
    testcase = 132
    status("active")
    RC.push(["kid_down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 133 ##########################################
    testcase = 133
    status("active")
    RC.push(["up 1 1000", "kid_left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 134 ##########################################
    testcase = 134
    status("active")
    RC.push(["kid_right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 135 ##########################################
    testcase = 135
    status("active")
    RC.push(["kid_ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 136 ##########################################
    testcase = 136
    status("active")
    RC.push(["kid_ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 281 ##########################################
    testcase = 281
    status("active")
    RC.push(["kid_VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 282 ##########################################
    testcase = 282
    status("active")
    RC.push(["kid_VolDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 137 ##########################################
    testcase = 137
    status("active")
    RC.push(["kid_standby 1 15000", "kid_standby 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 138 ##########################################
    testcase = 138
    status("active")
    RC.push(["exit 1 1000", "red 1 1000", "kid_star 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 139 ##########################################
    testcase = 139
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)    
    OPER.search()
    RC.push(["kid_star 1 7000", "format 1 3000", "down 1 1000", "down 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 140 ##########################################
    testcase = 140
    status("active")
    RC.push(["format 1 3000", "up 1 1000", "up 1 1000", "OK 1 4000", "format 1 1000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 141 ##########################################
    testcase = 141
    status("active")
    RC.push(["down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 142 ##########################################
    testcase = 142
    status("active")
    RC.push(["ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 143 ##########################################
    testcase = 143
    status("active")
    RC.push(["ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 144 ##########################################
    testcase = 144
    status("active")
    RC.push(["VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 145 ##########################################
    testcase = 145
    status("active")
    RC.push(["VolDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 146 ##########################################
    testcase = 146
    status("active")
    RC.push(["mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 147 ##########################################
    testcase = 147
    status("active")
    RC.push(["mute 1 1000", "up 1 1000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 148 ##########################################
    testcase = 148
    status("active")
    RC.push(["format 1 1000", "up 1 1000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 149 ##########################################
    testcase = 149
    status("active")
    RC.push(["format 1 1000", "up 1 1000", "last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 150 ##########################################
    testcase = 150
    status("active")
    RC.push(["format 1 1000", "down 1 6000", "standby 1 15000", "standby 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 151 ##########################################
    testcase = 151
    status("active")
    RC.push(["format 1 1000", "down 1 1000", "format 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 152 ##########################################
    testcase = 152
    status("active")
    RC.push(["format 1 1000", "up 1 1000", "kid_ok 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 153 ##########################################
    testcase = 153
    status("active")
    RC.push(["format 1 1000", "down 1 1000", "OK 1 1000", "format 1 1000", "kid_up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 154 ##########################################
    testcase = 154
    status("active")
    RC.push(["kid_down 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 155 ##########################################
    testcase = 155
    status("active")
    RC.push(["kid_ChUp 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 156 ##########################################
    testcase = 156
    status("active")
    RC.push(["kid_ChDown 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 157 ##########################################
    testcase = 157
    status("active")
    RC.push(["kid_VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 158 ##########################################
    testcase = 158
    status("active")
    RC.push(["kid_VolDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 159 ##########################################
    testcase = 159
    status("active")
    RC.push(["kid_standby 1 15000", "kid_standby 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 160 ##########################################
    testcase = 160
    status("active")
    RC.push(["exit 1 7000", "format 1 3000", "kid_0 1 500", "kid_1 1 500", "kid_2 1 500", "kid_3 1 500", "kid_4 1 500", "kid_5 1 500", "kid_6 1 500", "kid_7 1 500", "kid_8 1 500", "kid_9 1 500", "kid_right 1 500", "kid_left 1 500", "kid_star 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 161 ##########################################
    testcase = 161
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["5 1 6000", "kid_star 1 7000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 162 ##########################################
    testcase = 162
    status("active")
    RC.push(["exit 1 7000", "last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 163 ##########################################
    testcase = 163
    status("active")
    RC.push(["exit 1 7000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 164 ##########################################
    testcase = 164
    status("active")
    RC.push(["exit 1 2000", "red 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 165 ##########################################
    testcase = 165
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "right 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 166 ##########################################
    testcase = 166
    status("active")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 167 ##########################################
    testcase = 167
    status("active") #CANCEL
    RC.push(["ok 1 1000", "red 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 168 ##########################################
    testcase = 168
    status("active") #EXIT
    RC.push(["exit 1 1000", "exit 1 1000", "left 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 169 ##########################################
    testcase = 169
    status("active")
    sleep(7)
    RC.push(["kid_1 1 10000", "exit 1 3000", "standby 1 15000", "standby 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 170 ##########################################
    testcase = 170
    status("active")
    RC.push(["exit 1 10000", "exit 1 1000", "right 1 1000", "kid_left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 171 ##########################################
    testcase = 171
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "kid_right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 172 ##########################################
    testcase = 172 #CANCEL
    status("active")
    RC.push(["kid_ok 1 1000", "red 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 173 ##########################################
    testcase = 173 #EXIT
    status("active")
    RC.push(["exit 1 1000", "exit 1 1000", "kid_left 1 1500", "kid_ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 174 ##########################################
    testcase = 174
    status("active")
    RC.push(["kid_right 1 1000", "exit 1 1000", "kid_standby 1 15000", "kid_standby 1 5000"])
    GRAB.compare(testcase)
############################ TestCase 175 ##########################################
    testcase = 175
    status("active")
    UART.default_settings()
    OPER.search()
    OPER.set_pin()
    RC.push(["5 1 6000", "kid_star 1 7000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 176 ##########################################
    testcase = 176
    status("active")
    RC.push(["exit 1 4000", "last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 177 ##########################################
    testcase = 177
    status("active")
    RC.push(["exit 1 4000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 178 ##########################################
    testcase = 178
    status("active")
    RC.push(["exit 1 4000", "red 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 179 ##########################################
    testcase = 179
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 180 ##########################################
    testcase = 180
    status("active")
    RC.push(["exit 1 4000", "exit 1 4000", "0 1 1000", "1 1 1000", "2 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 181 ##########################################
    testcase = 181
    status("active")
    RC.push(["exit 1 4000", "exit 1 1000", "standby 1 15000", "standby 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 182 ##########################################
    testcase = 182
    status("active")
    RC.push(["exit 1 4000", "exit 1 1000", "1 1 1000", "2 1 1000", "3 1 1000", "4 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 183 ##########################################
    testcase = 183
    status("active")
    RC.push(["0 1 1000", "0 1 1000", "0 1 1000", "0 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 184 ##########################################
    testcase = 184
    status("active")
    RC.push(["kid_ok 1 7000", "exit 1 1000", "yellow 1 1000", "red 1 1000", "red 1 1000", "green 1 1000", "blue 1 2500"])
    GRAB.compare(testcase)
############################ TestCase 185 ##########################################
    testcase = 185
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 186 ##########################################
    testcase = 186
    status("active")
    RC.push(["kid_ok 1 7000", "exit 1 4000", "kid_0 1 1000", "kid_1 1 1000", "kid_7 1 1000", "kid_left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 187 ##########################################
    testcase = 187
    status("active")
    RC.push(["kid_standby 1 15000", "kid_standby 1 7000"])
    GRAB.compare(testcase)
############################ TestCase 188 ##########################################
    testcase = 188
    status("active")
    RC.push(["exit 1 4000", "exit 1 1000", "kid_0 1 1000", "kid_1 1 1000", "kid_5 1 1000", "kid_9 1 2000"])
############################ TestCase 189 ##########################################
    testcase = 189
    status("active")
    RC.push(["kid_0 1 1000", "kid_0 1 1000", "kid_0 1 1000", "kid_0 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 190 ##########################################
    testcase = 190
    status("active")
    UART.default_settings()
    OPER.search()
    RC.push(["kid_star 1 7000", "kid_star 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 191 ##########################################
    testcase = "191_1"
    status("active")
    RC.push(["exit 1 7000", "kid_3 1 2000", "kid_up 1 2000"])
    GRAB.compare(testcase)
    
    testcase = "191_2"
    status("active")
    RC.push(["2 1 1000", "kid_down 1 2000"])
    GRAB.compare(testcase)
    
    testcase = "191_3"
    status("active")
    RC.push(["3 1 1000", "kid_ChUp 1 2000"])
    GRAB.compare(testcase)
    
    testcase = "191_4"
    status("active")
    RC.push(["2 1 1000", "kid_ChDown 1 2000"])
    GRAB.compare(testcase)  
############################ TestCase 192 ##########################################
    testcase = 192
    status("manual")
    GRAB.compare(testcase)    
############################ TestCase 193 ##########################################
    testcase = 193
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 194 ##########################################
    testcase = 194
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 195 ##########################################
    testcase = 195
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 196 ##########################################
    testcase = 196
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 197 ##########################################
    testcase = 197
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 198 ##########################################
    testcase = 198
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 199 ##########################################
    testcase = 199
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 200 ##########################################
    testcase = 200
    status("inactive")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["kid_OK 1 7500", "Rec 1 3000"])
    RC.push(["OK 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 201 ##########################################
    testcase = 201
    status("inactive")
    RC.push(["exit 1 2000", "4 1 5000", "up 1 6000", "red 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 202 ##########################################
    testcase = 202
    status("inactive")
    RC.push(["exit 1 1000", "down 1 6000", "red 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 203 ##########################################
    testcase = 203
    status("inactive")
    RC.push(["exit 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 204 ##########################################
    testcase = 204
    status("inactive")
    RC.push(["right 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 205 ##########################################
    testcase = 205
    status("inactive")
    RC.push(["4 1 5000", "ChUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 206 ##########################################
    testcase = 206
    status("inactive")
    RC.push(["ChDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 207 ##########################################
    testcase = 207
    status("inactive")
    RC.push(["standby 1 12000", "standby 1 8000"])
    GRAB.compare(testcase)
############################ TestCase 208 ##########################################
    testcase = 208
    status("inactive")
    RC.push(["exit 1 1000", "mute 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 209 ##########################################
    testcase = 209
    status("inactive")
    RC.push(["mute 1 1000", "guide 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 210 ##########################################
    testcase = 210
    status("inactive")
    RC.push(["exit 1 1000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 211 ##########################################
    testcase = 211
    status("inactive")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 212 ##########################################
    testcase = 212
    status("inactive")
    RC.push(["last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 213 ##########################################
    testcase = 213
    status("inactive")
    RC.push(["stop 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 214 ##########################################
    testcase = 214
    status("inactive")
    RC.push(["exit 1 5000", "kid_ok 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 215 ##########################################
    testcase = 215
    status("inactive")
    RC.push(["exit 1 5000", "kid_up 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 216 ##########################################
    testcase = 216
    status("inactive")
    RC.push(["exit 1 5000", "kid_down 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 217 ##########################################
    testcase = 217
    status("inactive")
    RC.push(["exit 1 5000", "kid_left 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 218 ##########################################
    testcase = 218
    status("inactive")
    RC.push(["exit 1 5000", "kid_right 1 2000"])
    GRAB.compare(testcase)
    RC.push(["stop 1 1000", "left 1 1000", "OK 1 1000"])
############################ TestCase 219 ##########################################
    testcase = 219
    status("inactive")
    RC.push(["exit 1 5000", "4 1 1000", "kid_ChUp 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 220 ##########################################
    testcase = 220
    status("inactive")
    RC.push(["kid_ChDown 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 221 ##########################################
    testcase = 221
    status("inactive")
    RC.push(["kid_standby 1 12000", "kid_standby 1 12000"])
    GRAB.compare(testcase)
############################ TestCase 222 ##########################################
    testcase = 222
    status("inactive")
    RC.push(["exit 1 5000", "kid_star 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 223 ##########################################
    testcase = 223
    status("inactive")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream, Frequency, Modulator)
    OPER.search()
    RC.push(["kid_star 1 8000", "play/pause 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 224 ##########################################
    testcase = 224
    status("inactive")
    RC.push(["stop 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 225 ##########################################
    testcase = 225
    status("inactive")
    sleep(7)
    RC.push(["play/pause 1 1000", "OK 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 226 ##########################################
    testcase = 226
    status("inactive")
    RC.push(["exit 1 1000", "stop 1 1000", "3 1 6000", "play/pause 1 5000", "up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 227 ##########################################
    testcase = 227
    status("inactive")
    RC.push(["2 1 6000", "play/pause 1 1000", "down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 228 ##########################################
    testcase = 228
    status("inactive")
    sleep(2)
    RC.push(["play/pause 1 5000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 229 ##########################################
    testcase = 229
    status("inactive")
    RC.push(["right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 230 ##########################################
    testcase = 230
    status("inactive")
    RC.push(["stop 1 1000", "3 1 6000", "play/pause 1 1000", "ChUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 231 ##########################################
    testcase = 231
    status("inactive")
    RC.push(["2 1 6000", "play/pause 1 1000", "ChDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 232 ##########################################
    testcase = 232
    status("inactive")
    RC.push(["play/pause 1 1000", "VolUp 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 233 ##########################################
    testcase = 233
    status("inactive")
    RC.push(["VolDown 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 234 ##########################################
    testcase = "234_1"
    status("inactive")
    RC.push(["stop 1 1000", "2 1 6000", "play/pause 1 5000", "1 1 1800"])
    GRAB.compare(testcase)
    
    testcase = "234_2"
    status("inactive")
    RC.push(["play/pause 1 5000", "2 1 1800"])
    GRAB.compare(testcase)
    
    testcase = "234_3"
    status("inactive")
    RC.push(["play/pause 1 5000", "3 1 1800"])
    GRAB.compare(testcase)
    
    testcase = "234_4"
    status("inactive")
    RC.push(["play/pause 1 5000", "4 1 1800"])
    GRAB.compare(testcase)

############################ TestCase 235 ##########################################
    testcase = 235
    status("inactive")
    sleep(5)
    RC.push(["play/pause 1 1000", "8 1 700"])
    GRAB.compare(testcase)
############################ TestCase 236 ##########################################
    testcase = 236
    status("inactive")
    RC.push(["standby 1 12000", "standby 1 10000"])
    GRAB.compare(testcase)
    
#------- ВНИМАНИЕ! ДАЛЬШЕ ТЕСТЫ ИДУТ НЕ ПО ПОРЯДКУ! -----------
############################ TestCase 237 ##########################################
    testcase = 237
    status("inactive")
    RC.push(["exit 1 1000", "left 1 1000", "OK 1 1000"])
    OPER.set_pin()
    RC.push(["kid_1 1 7000", "play/pause 1 1000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 239 ##########################################
    testcase = 239
    status("inactive")
    RC.push(["exit 1 1000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 241 ##########################################
    testcase = 241
    status("inactive")
    RC.push(["exit 1 1000", "last 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 238 ##########################################
    testcase = 238
    status("inactive")
    RC.push(["0 1 1000", "0 1 1000", "0 1 1000", "0 1 1000"])
    OPER.unset_pin()
    RC.push(["kid_1 1 7000", "play/pause 1 1000", "menu 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 240 ##########################################
    testcase = 240
    status("inactive")
    RC.push(["exit 1 1000", "exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 242 ##########################################
    testcase = 242
    status("inactive")
    RC.push(["exit 1 1000", "last 1 1000"])
    GRAB.compare(testcase)
#------- ВНИМАНИЕ! ДАЛЬШЕ ТЕСТЫ ИДУТ СНОВА ПО ПОРЯДКУ! -----------
############################ TestCase 243 ##########################################
    testcase = 243
    status("inactive")
    RC.push(["exit 1 1000", "format 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 244 ##########################################
    testcase = 244
    status("inactive")
    RC.push(["exit 1 6000", "mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 245 ##########################################
    testcase = 245
    status("inactive")
    RC.push(["mute 1 1000", "blue 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 246 ##########################################
    testcase = 246
    status("inactive")
    RC.push(["exit 1 1000", "red 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 247 ##########################################
    testcase = 247
    status("inactive")
    RC.push(["exit 1 1000", "yellow 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 248 ##########################################
    testcase = 248 
    status("inactive")
    RC.push(["exit 1 1000", "green 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 249 ##########################################
    testcase = 249
    status("inactive")
    RC.push(["exit 1 1000", "kid_ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 250 ##########################################
    testcase = 250
    status("inactive")
    RC.push(["exit 1 1000", "stop 1 1000", "3 1 6000", "play/pause 1 1000", "kid_up 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 251 ##########################################
    testcase = 251
    status("inactive")
    RC.push(["2 1 6000", "play/pause 1 1000", "kid_down 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 252 ##########################################
    testcase = 252
    status("inactive")
    sleep(5)
    RC.push(["kid_left 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 253 ##########################################
    testcase = 253
    status("inactive")
    RC.push(["kid_right 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 254 ##########################################
    testcase = 254
    status("inactive")
    RC.push(["stop 1 1000", "3 1 6000", "play/pause 1 1000", "kid_ChUp 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 255 ##########################################
    testcase = 255
    status("inactive")
    RC.push(["2 1 6000", "play/pause 1 1000", "kid_ChDown 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 256 ##########################################
    testcase = 256
    status("inactive")
    sleep(7)
    RC.push(["play/pause 1 1000", "kid_VolUp 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 257 ##########################################
    testcase = 257
    status("inactive")
    RC.push(["play/pause 1 1000", "kid_VolDown 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 258 ##########################################
    testcase = "258_1"
    status("inactive")
    RC.push(["stop 1 1000", "2 1 6000", "play/pause 1 5000", "kid_1 1 1800"])
    GRAB.compare(testcase)
    
    testcase = "258_2"
    status("inactive")
    RC.push(["play/pause 1 5000", "kid_2 1 1800"])
    GRAB.compare(testcase)
    
    testcase = "258_3"
    status("inactive")
    RC.push(["play/pause 1 5000", "kid_3 1 1800"])
    GRAB.compare(testcase)
    
    testcase = "258_4"
    status("inactive")
    RC.push(["play/pause 1 5000", "kid_4 1 1800"])
    GRAB.compare(testcase)

############################ TestCase 259 ##########################################
    testcase = 259
    status("inactive")
    sleep(5)
    RC.push(["play/pause 1 1000", "kid_6 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 260 ##########################################
    testcase = 260
    status("inactive")
    sleep(3)
    RC.push(["kid_star 1 1500"])
    GRAB.compare(testcase)
############################ TestCase 261 ##########################################
    testcase = 261
    status("inactive")
    RC.push(["exit 1 1000", "kid_standby 1 12000", "kid_standby 1 12000"])
    GRAB.compare(testcase)
############################ TestCase 262 ##########################################
    testcase = 262
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 263 ##########################################
    testcase = 263
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 264 ##########################################
    testcase = 264
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 265 ##########################################
    testcase = 265
    status("active")
    UART.default_settings()
    sleep(10)
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    OPER.search()    
    MOD.stop(Modulator)
    UART.reboot()
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    RC.push(["exit 1 7000", "kid_1 1 7000"])
    sleep(250)
    RC.push(["exit 1 1000", "left 1 1000", "OK 1 3000"])
    GRAB.compare(testcase)
############################ TestCase 266 ##########################################
    testcase = 266
    status("active")
    OPER.set_pin()
    UART.start_app("channelseditor")
    RC.push(["right 1 1000", "up 1 1000"])
    OPER.channel_block()
    RC.push(["kid_0 1 7000"])
    GRAB.compare(testcase)
    OPER.unset_pin()
############################ TestCase 267 ##########################################
    testcase = 267
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 268 ##########################################
    testcase = 268
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    RC.push(["3 1 7000", "kid_1 1 7000"])
    sleep(25)
    GRAB.compare(testcase)
############################ TestCase 269 ##########################################
    testcase = 269
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 270 ##########################################
    testcase = 270
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    OPER.search()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    RC.push(["3 1 7000", "kid_1 1 7000", "3 1 1000"])
    sleep(500)
    GRAB.compare(testcase)
############################ TestCase 271 ##########################################
    testcase = 271
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 272 ##########################################
    testcase = 272
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 273 ##########################################
    testcase = 273
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 274 ##########################################
    testcase = 274
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 275 ##########################################
    testcase = 275
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 276 ##########################################
    testcase = 276
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 277 ##########################################
    testcase = 277
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 278 ##########################################
    """testcase = 278
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 273 ##########################################
    testcase = 273
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 274 ##########################################
    testcase = 274
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 275 ##########################################
    testcase = 275
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 276 ##########################################
    testcase = 276
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 277 ##########################################
    testcase = 277
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 278 ##########################################
    testcase = 278
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 279 ##########################################
    testcase = 279
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 280 ##########################################
    testcase = 280
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 281 ##########################################
    testcase = 281
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 282 ##########################################
    testcase = 282
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 283 ##########################################
    testcase = 283
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 284 ##########################################
    testcase = 284
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 285 ##########################################
    testcase = 285
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 286 ##########################################
    testcase = 286
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 287 ##########################################
    testcase = 287
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 288 ##########################################
    testcase = 288
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 289 ##########################################
    testcase = 289
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)
############################ TestCase 290 ##########################################
    testcase = 290
    status("active")
    UART.default_settings()
    UART.start_app("")
    RC.push([""])
    sleep(0)
    GRAB.compare(testcase)"""
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
