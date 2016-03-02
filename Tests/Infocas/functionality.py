# Test name = Infocas
# Script dir = R:\Stingray\Tests\Infocas\functionality\functionality.py
# Smartcard used = 23025500420005

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
    TestName = "Infocas"
    ScriptName = "functionality"
    ScriptIndex = "1"
    Grabber = DO.grab_define()
    platform = DO.load_platform()
    Modulation = "DVBS"
    FEC = "3/4"
    SR = "27500000"
    Stream1 = "\\DRE Services\\X_0000_00000_MUX_38000_DRE4_Infocas_1.ts"
    Stream2 = "\\DRE Services\\X_0000_00000_MUX_38000_DRE4_Infocas_2.ts"
    Frequency = 1476
    Modulator = "1"
    COM = "COM7"
    settings = [ScriptName, ScriptIndex, Grabber, Modulation, FEC, SR, Stream1, Frequency, Modulator, COM]
    DO.save_settings(settings)
    GRAB.start_capture()
    MOD.stop(Modulator)

    # macros
    searching_from_wizard_general_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_general_english_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "down", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_english_E501 = ["up 3 3400", "right 1 1000", "down 3 3400", "ok 1 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 45000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_south_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "down", "down", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_general_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_general_english_ALL = ["up 3 3400", "right 1 1000", "down 3 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 45000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "down", "ok 1 5000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_centre_english_ALL = ["up 3 3400", "right 1 1000", "down 3 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 45000", "down 1 1000", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    searching_from_wizard_south_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000", "down", "down", "ok 1 15000", "ok 1 10000", "exit 2 3000"]
    load_regions_E501 = ["ok 1 3400", "ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000"]
    load_regions_english_E501 = ["up 3 2400", "right 1 1000", "down 3 2400", "ok 1 3400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 45000"]
    load_regions_ALL = ["ok 1 3400", "ok 1 3400", "right 1 3400", "ok 1 3400", "ok 1 45000"]
    load_regions_english_ALL = ["up 3 2400", "right 1 1000", "down 3 2400", "ok 1 3400", "ok 1 3400", "right", "ok 1 3400", "ok 1 45000"]

############################ TestCase 1 ##########################################
    """testcase = 1
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
    UART.default_settings()
#    RC.push(["exit 1 500", "exit 1 500", "exit 1 500", "menu 1 1000", "left 1 1000", "left 1 1000", "ok 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "right 1 1000", "down 1 1500",  "ok 1 1500", "left 1 1000", "ok 1 1000"])
    sleep(15)
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    OPER.search()
    MOD.stop(Modulator)
    UART.reboot()
    sleep(5)
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit 2 1000", "2 1 1000", "0 1 1000", "0 1 1000"])
    sleep(10) 
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    GRAB.compare(testcase)
############################ TestCase 2 ##########################################
    testcase = 2
    status("active")
    if platform == "E212":
        sleep(7)
        RC.push(["ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 3 ##########################################
    testcase = 3
    status("active")
    GRAB.compare(testcase)
############################ TestCase 4 ##########################################
    testcase = 4
    status("active")
    sleep(10) 
    GRAB.wait_until("wait04.bmp", [680, 415, 1235, 665], 30) #message 2 (120 "SHCH" letters, broadcast)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 5 ##########################################
    testcase = 5
    status("active")
    sleep(50) 
    GRAB.wait_until("wait05.bmp", [680, 415, 1235, 665], 30) #message 3 (120 "SHCH" letters + symbol "|" + 2 "SHCH" letters, broadcast)
    GRAB.compare(testcase)
############################ TestCase 6 ##########################################
    testcase = 6
    status("active")
    sleep(5)
    GRAB.compare(testcase)
############################ TestCase 7 ##########################################
    testcase = 7
    status("active")
    sleep(40) 
    GRAB.wait_until("wait07.bmp", [680, 415, 1235, 665], 30) #common message 4 (rus, individual)
    GRAB.compare(testcase)
############################ TestCase 8 ##########################################
    testcase = 8
    status("active")
    sleep(5)
    GRAB.compare(testcase)
############################ TestCase 9 ##########################################
    testcase = 9
    status("active")
    sleep(40) 
    GRAB.wait_until("wait09.bmp", [680, 415, 1235, 665], 40) #common message 5 (eng, broadcast)
    GRAB.compare(testcase)
############################ TestCase 10 ##########################################
    testcase = 10
    status("active")
    sleep(30) 
    GRAB.wait_until("wait10.bmp", [680, 415, 1235, 665], 45) #message 6 (various symbols, broadcast)
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
    UART.reboot()
    RC.push(["exit 1 1000"])
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    sleep(10)
    RC.push(["exit 1 1000", "2 1 1100", "0 1 1100", "0 1 1100"])
    sleep(47) #messages 1, 2 and 3
    if platform == "E212":
        RC.push(["ok 1 1000"])
    sleep(89)
    RC.push(["standby 1 10000", "standby 1 10000"])
    GRAB.compare(testcase)
############################ TestCase 14 ##########################################
    testcase = 14
    status("active")
    sleep(60)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    UART.reboot()
    sleep(15)
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit 3 1000", "2 1 1000", "0 1 1000", "0 1 1000"])
    sleep(7)
    GRAB.compare(testcase)
############################ TestCase 15 ##########################################
    testcase = 15
    status("active")
    UART.reboot()
    RC.push(["exit 3 1000", "2 1 1000", "0 1 1000", "0 1 1000"])
    sleep(5)
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    sleep(15)
    RC.push(["standby 1 15000"])
    sleep(15)
    RC.push(["standby 1 10000", "ok 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 16 ##########################################
    testcase = 16
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 1 1500", "exit 1 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    sleep(20)
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 17 ##########################################
    testcase = 17
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 1 1500", "exit 1 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    sleep(20)
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    RC.push(["standby 1 10000", "standby 1 10000"])
    GRAB.compare(testcase)
############################ TestCase 18 ##########################################
    testcase = 18
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 1 1500", "exit 1 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    sleep(20)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", timeout = 30) #common message 1 (rus, broadcast)
    RC.push(["VolUp 1 1000", "right 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 19 ##########################################
    testcase = 19
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 1 1500", "exit 1 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    sleep(20)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", timeout = 30) #common message 1 (rus, broadcast)
    RC.push(["VolDown 1 1000", "left 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 20 ##########################################
    testcase = 20
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 1 1500", "exit 1 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    sleep(20)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", timeout = 30) #common message 1 (rus, broadcast)
    RC.push(["mute 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 21 ##########################################
    testcase = 21
    status("active")
    MOD.stop(Modulator)
    RC.push(["exit 1 1000"])
    UART.reboot()
    RC.push(["exit 1 1500", "exit 1 1500", "2 1 1100", "0 1 1100", "0 1 3100", "mute 1 1000"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    sleep(20)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", timeout = 30) #common message 1 (rus, broadcast)
    sleep(3)
    RC.push(["clock 1 2000"])
    GRAB.compare(testcase)
############################ TestCase 22 ##########################################
    testcase = 22
    status("active")
    RC.push(["clock 1 1000"])
    sleep(25)
    GRAB.compare(testcase)
############################ TestCase 23 ##########################################
    testcase = 23
    status("active")
    UART.default_settings()
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    OPER.search()
    MOD.stop(Modulator)
    UART.reboot()
    sleep(5)
    RC.push(["exit 1 5500", "exit 1 1500", "2 1 1000", "0 1 1000", "0 1 1000"])
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    sleep(23)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait23.bmp", [680, 415, 1235, 665], 30) 
    sleep(15)
    GRAB.compare(testcase)
############################ TestCase 24 ##########################################
    testcase = 24
    status("active")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 25 ##########################################
    testcase = 25
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    sleep(5)
    RC.push(["exit 6 1000", "2 1 1000", "0 1 1000", "0 1 1000"])
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    sleep(27)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait23.bmp", [680, 415, 1235, 665], 30) 
    sleep(30)
    GRAB.compare(testcase)
############################ TestCase 26 ##########################################
    testcase = 26
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 2 1000"])
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    RC.push(["exit 6 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    sleep(27)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    sleep(80)
    GRAB.wait_until("wait26.bmp", [680, 415, 1235, 665], 30) 
    sleep(20)
    GRAB.compare(testcase)
############################ TestCase 27 ##########################################
    testcase = 27
    status("active")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 28 ##########################################
    testcase = 28
    status("active")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 29 ##########################################
    testcase = 29
    status("active")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 30 ##########################################
    testcase = 30
    status("active")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 31 ##########################################
    testcase = 31
    status("active")
    sleep(70) 
    GRAB.wait_until("wait31.bmp", [680, 415, 1235, 665], 30) #the 1st message is shown
    GRAB.compare(testcase)
############################ TestCase 32 ##########################################
    testcase = 32
    status("active")
    GRAB.wait_until("wait32.bmp", [680, 415, 1235, 665], 20)#the 1st message is closed because of 6th has come, the 2nd is shown
    GRAB.compare(testcase)
############################ TestCase 33 ##########################################
    testcase = 33
    status("active")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 34 ##########################################
    testcase = 34
    status("active")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 35 ##########################################
    testcase = 35
    status("active")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 36 ##########################################
    testcase = 36
    status("active")
    RC.push(["exit 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 37 ##########################################
    testcase = 37
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 1 1500", "exit 2 1000", "down 1 3000"])
    MOD.play_stream(Modulation, FEC, SR, Stream2, Frequency, Modulator)
    UART.start_app("settings")
    sleep(241)
    GRAB.compare(testcase)
############################ TestCase 38 ##########################################
    testcase = 38
    status("active")
    sleep(4)
    GRAB.compare(testcase)
############################ TestCase 39 ##########################################
    testcase = 39
    status("active")
    sleep(4)
    GRAB.compare(testcase)
############################ TestCase 40 ##########################################
    testcase = 40
    status("active")
    sleep(4)
    GRAB.compare(testcase)
############################ TestCase 41 ##########################################
    testcase = 41
    status("active")
    sleep(4)
    GRAB.compare(testcase)
############################ TestCase 42 ##########################################
    testcase = 42
    status("active")
    sleep(4)
    GRAB.compare(testcase)
############################ TestCase 43 ##########################################
    testcase = 43
    status("active")
    sleep(1)
    RC.push(["exit 1 2000"])
    if platform == "E212":
        RC.push(["ok 1 1000"])
    sleep(1)
    GRAB.compare(testcase)
############################ TestCase 44 ##########################################
    testcase = 44
    status("active")
    RC.push(["exit"])
    GRAB.compare(testcase)
############################ TestCase 45 ##########################################
    testcase = 45
    status("active")
    RC.push(["exit"])
    GRAB.compare(testcase)
############################ TestCase 46 ##########################################
    testcase = 46
    status("active")
    RC.push(["exit"])
    GRAB.compare(testcase)
############################ TestCase 47 ##########################################
    testcase = 47
    status("active")
    RC.push(["exit"])
    GRAB.compare(testcase)
############################ TestCase 48 ##########################################
    testcase = 48
    status("active")
    RC.push(["exit"])
    GRAB.compare(testcase)
############################ TestCase 49 ##########################################
    testcase = 49
    status("active")
    UART.default_settings()
    sleep(15)
    MOD.stop(Modulator)
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    OPER.search()
    MOD.stop(Modulator)
    UART.reboot()
    sleep(5)
    RC.push(["exit 2 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit", "exit"])
    sleep(29)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    RC.push(["mail 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 50 ##########################################
    testcase = 50
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit", "exit", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    sleep(15)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    RC.push(["help 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 51 ##########################################
    testcase = 51
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 2 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit", "exit"])
    sleep(15)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    RC.push(["guide 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 52 ##########################################
    testcase = 52
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 2 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit", "exit"])
    sleep(15)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    RC.push(["cinemahalls 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 53 ##########################################
    testcase = 53
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 2 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit", "exit"])
    sleep(15)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    RC.push(["TV/chat 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 54 ##########################################
    testcase = 54
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 55 ##########################################
    testcase = 55
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 2 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit", "exit"])
    sleep(15)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    RC.push(["red 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 56 ##########################################
    testcase = 56
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 2 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit", "exit"])
    sleep(15)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    RC.push(["green 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 57 ##########################################
    testcase = 57
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 2 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit", "exit"])
    sleep(15)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    RC.push(["yellow 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 58 ##########################################
    testcase = 58
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 2 1500", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit", "exit"])
    sleep(15)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    RC.push(["blue 1 1000"])
    GRAB.compare(testcase)
############################ TestCase 59 ##########################################
    testcase = 59
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 60 ##########################################
    testcase = 60
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit 2 1500", "2 1 1000", "0 1 1000", "0 1 4000"])
    UART.start_app("scheduler")
    RC.push(["red 1 1000", "ok 1 1500", "ok 1 1500", "ok 1 1500", "1", "1", "1", "4", "ok 1 1500", "ok 1 1500", "exit 2 1000", "exit 2 1000", "0"])
    sleep(15)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    GRAB.compare(testcase)
############################ TestCase 61 ##########################################
    testcase = 61
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 62 ##########################################
    testcase = 62
    status("manual")
    GRAB.compare(testcase)
############################ TestCase 63 ##########################################
    testcase = 63
    status("active")
    MOD.stop(Modulator)
    UART.reboot()
    RC.push(["exit 2 800", "2 1 1100", "0 1 1100", "0 1 1100"])
    MOD.play_stream(Modulation, FEC, SR, Stream1, Frequency, Modulator)
    RC.push(["exit", "exit"])
    sleep(15)
    if platform == "E212":
        RC.push(["ok 1 1000"])
    GRAB.wait_until("wait01.bmp", [680, 415, 1235, 665], 30) #common message 1 (rus, broadcast)
    GRAB.compare(testcase)
###################################################################################
    status("active")
    MOD.stop(Modulator)
    GRAB.stop_capture()
