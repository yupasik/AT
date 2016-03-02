__author__ = 'Yuri.Perin'
# -*- coding: utf-8 -*-
import serial
from time import sleep
import os
from time import gmtime, strftime, localtime
from json import load


class uSTB:

    cmdCodes = {
    "0":       ["0CF3", "key 0"],
    "1":       ["03FC", "key 1"],
    "2":       ["04FB", "key 2"],
    "3":       ["05FA", "key 3"],
    "4":       ["06F9", "key 4"],
    "5":       ["07F8", "key 5"],
    "6":       ["08F7", "key 6"],
    "7":       ["09F6", "key 7"],
    "8":       ["0AF5", "key 8"],
    "9":       ["0BF4", "key 9"],
    "standby": ["00FF", "key Power"],
    "radio":   ["0DF2", "key TV/Radio"],
    "mute":    ["18E7", "key Mute Volume"],
    "red":     ["1CE3", "key Red"],
    "green":   ["1DE2", "key Green"],
    "yellow":  ["1AE5", "key Yellow"],
    "blue":    ["1EE1", "key Blue"],
    "white":   ["19E6", "key Clock"],
    "exit":    ["16E9", "key Back"],
    "menu":    ["0EF1", "key Menu"],
    "ok":      ["13EC", "key Select"],
    "up":      ["11EE", "key Up"],
    "down":    ["15EA", "key Down"],
    "left":    ["12ED", "key Left"],
    "right":   ["14EB", "key Right"],
    "VolUp":   ["1FE0", "key Up Volume"],
    "VolDown": ["40BF", "key Down Volume"],
    "ChUp":    ["10EF", "key Down Channel"],
    "ChDown":  ["0FF0", "key Up Channel"],
    "guide":   ["1BE4", "key Guide"],
    "help":    ["17E8", "key Help"],
    "last":    ["41BE", "key Last"],
    "status":  ["01FE", "key Status"]
    }

    def __init__(self, app):
        self.app = app
        self._bps = 115200
        with open(os.path.join(self.app.domain, "Configuration", "config_test.json")) as info:
            self._com = load(info)["COM"]
        self.port = serial.Serial(self._com, self._bps, timeout=0.1)

    def push(self, macros):
        t = 1   # default time delay between the RC commands
        count = 0
        for button in macros:
            count += 1
            command = [str(n) for n in button.split()]
            if len(command) == 1:
                button = command[0]
                try:
                    self.port.write("%s\n" % cmdCodes[button][1])
                    self.app.write_log("Push [%s]" % button)  # logger - Push button
                    sleep(t)
                except:
                    return
            if len(command) == 3:
                button = command[0]
                repeat_n = int(command[1])
                delay = int(command[2])/1000
                i = 0
                while i < repeat_n:
                    try:
                        self.port.write("%s\n" % cmdCodes[button][1])
                        self.app.write_log("Push [%s]" % button)  # logger - Push button
                        if i < (repeat_n - 1):
                            sleep(t)
                        else:
                            sleep(delay)
                        i += 1
                    except:
                        return

    def default_settings(self):
        try:
            self.port.write("reset\n")
            self.app.write_log("Reset STB to default settings")  # logger - Reset STB to default settings
            sleep(100)
        except:
            return

    def reboot(self):
        try:
            self.port.write("reboot\n")
            self.app.write_log("Power reboot STB")  # logger - Power reboot STB
            sleep(100)
        except:
            return

    def launch(self, application):
        try:
            self.port.write("run {0}\n".format(application))
            self.app.write_log("Open %s application" % application)  # logger - Power reboot STB
            sleep(3)
        except:
            return

cmdCodes = {
"0":       ["0CF3", "key 0"],
"1":       ["03FC", "key 1"],
"2":       ["04FB", "key 2"],
"3":       ["05FA", "key 3"],
"4":       ["06F9", "key 4"],
"5":       ["07F8", "key 5"],
"6":       ["08F7", "key 6"],
"7":       ["09F6", "key 7"],
"8":       ["0AF5", "key 8"],
"9":       ["0BF4", "key 9"],
"standby": ["00FF", "key Power"],
"radio":   ["0DF2", "key TV/Radio"],
"mute":    ["18E7", "key Mute Volume"],
"red":     ["1CE3", "key Red"],
"green":   ["1DE2", "key Green"],
"yellow":  ["1AE5", "key Yellow"],
"blue":    ["1EE1", "key Blue"],
"white":   ["19E6", "key Clock"],
"exit":    ["16E9", "key Back"],
"menu":    ["0EF1", "key Menu"],
"ok":      ["13EC", "key Select"],
"up":      ["11EE", "key Up"],
"down":    ["15EA", "key Down"],
"left":    ["12ED", "key Left"],
"right":   ["14EB", "key Right"],
"VolUp":   ["1FE0", "key Up Volume"],
"VolDown": ["40BF", "key Down Volume"],
"ChUp":    ["10EF", "key Down Channel"],
"ChDown":  ["0FF0", "key Up Channel"],
"guide":   ["1BE4", "key Guide"],
"help":    ["17E8", "key Help"],
"last":    ["41BE", "key Last"],
"status":  ["01FE", "key Status"]
}