__author__ = 'Yuri.Perin'
# -*- coding: utf-8 -*-

import urllib2
from urlgrabber.keepalive import HTTPHandler
from suds.transport.http import HttpTransport
from time import gmtime, strftime, localtime
from suds.client import Client
import os.path


class PersistentTransport(HttpTransport):
    def __init__(self):
        HttpTransport.__init__(self)
        self._handler = HTTPHandler()

    def u2opener(self):
        return urllib2.build_opener(self._handler)


class Modulator:
    """Modulator"""
    def __init__(self, app, n):
        self.app = app
        self.N = n
        self._wsdl_file = "file:///" + os.path.join(self.app.domain, "Configuration", "MOD-%s.wsdl" % n)
        self.client = Client(self._wsdl_file, transport=PersistentTransport())
        self.client.service.OpenSession()
        self.client.service.SetPlayoutState(2)

    def open(self, stream):
        # Open TS file
        ts_location = "F:\\RT-RK\\Streams"
        self.client.service.OpenFile(os.path.join(ts_location, stream))
        self.app.write_log("[MOD]   Open stream: %s" % stream)  # logger - Open stream
        print("[MOD]   Open stream: %s" % stream)  # print - Open stream

    def play(self):
        # Open TS file
        self.client.service.SetPlayoutState(1)
        self.app.write_log("[MOD]   Play stream")  # logger - Play stream
        print("[MOD]   Play stream")  # print - Play stream

    def pause(self):
        # Open TS file
        self.client.service.SetPlayoutState(0)
        self.app.write_log("[MOD]   Pause stream")  # logger - Pause stream
        print("[MOD]   Pause stream")  # print - Pause stream

    def stop(self):
        # Open TS file
        self.client.service.SetPlayoutState(2)
        self.app.write_log("[MOD]   Stop stream")  # logger - Stop stream
        print("[MOD]   Stop stream")  # print - Stop stream

    def set_freq(self, frequency):
        # Set frequency in Hz
        RfPars = self.client.service.GetRfPars()["RfPars"]
        RfPars["Frequency"] = long(frequency*1000000)
        self.client.service.SetRfPars(RfPars=RfPars)
        self.app.write_log("[MOD] Set frequency %s" % frequency)  # logger - Set Frequency
        print("[MOD]   Set frequency %s" % frequency)  # print - Set Frequency

    def set_standard(self, dvb):
        ModPars = self.client.service.GetModPars()["ModPars"]
        if dvb == "DVBS":
            ModPars["ParXtra2"] = -1
            ModPars["ModType"] = 0
            ModPars["ParXtra1"] = -1
        if dvb == "DVBS2":
            ModPars["ParXtra2"] = 0
            ModPars["ModType"] = 32
            ModPars["ParXtra1"] = 1792
        self.client.service.SetModPars(ModPars=ModPars)
        self.app.write_log("[MOD]   Set DVB standard: %s" % dvb)  # logger - Set DVB standard
        print("[MOD]   Set DVB standard: %s" % dvb)  # print - Set DVB standard

    def set_modulation(self, modulation):
        ModPars = self.client.service.GetModPars()["ModPars"]
        if modulation == "8PSK":
            ModPars["ModType"] = 33
        if modulation == "QPSK" and self.client.service.GetRfPars()["ModPars"]["ParXtra2"] == 0:
            ModPars["ModType"] = 32
        if modulation == "QPSK" and self.client.service.GetRfPars()["ModPars"]["ParXtra2"] == -1:
            ModPars["ModType"] = 0
        self.client.service.SetModPars(ModPars=ModPars)
        self.app.write_log("[MOD]   Set Modulation: %s" % modulation)  # logger - Set Modulation
        print("[MOD]   Set Modulation: %s" % modulation)  # print - Set Modulation

    def set_symbolrate(self, symbolrate):
        ModPars = self.client.service.GetModPars()["ModPars"]
        ModPars["SymRate"] = symbolrate*1000
        self.client.service.SetModPars(ModPars=ModPars)
        self.app.write_log("[MOD]   Set symbolrate: %s" % symbolrate)  # logger - Set symbolrate
        print("[MOD]   Set symbolrate: %s" % symbolrate)  # print - Set symbolrate

    def set_fec(self, fec):
        fec_dict = {"1/2": 0,
                    "2/3": 1,
                    "3/4": 2,
                    "4/5": 3,
                    "5/6": 4,
                    "7/8": 6,
                    "1/4": 7,
                    "1/3": 8,
                    "2/5": 9,
                    "3/5": 10,
                    "8/9": 11,
                    "9/10": 12}
        ModPars = self.client.service.GetModPars()["ModPars"]
        ModPars["ParXtra0"] = fec_dict[fec]
        self.client.service.SetModPars(ModPars=ModPars)
        self.app.write_log("[MOD]   Set FEC: %s" % fec)  # logger - Set FEC
        print("[MOD]   Set FEC: %s" % fec)  # print - Set FEC

    def set_options(self, dvb="DVBS", fec="3/4", frequency=1476, symbolrate=27500, modulation="QPSK"):
        ModPars = self.client.service.GetModPars()["ModPars"]
        RfPars  = self.client.service.GetRfPars()["RfPars"]
        fec_dict = {"1/2": 0,
                    "2/3": 1,
                    "3/4": 2,
                    "4/5": 3,
                    "5/6": 4,
                    "7/8": 6,
                    "1/4": 7,
                    "1/3": 8,
                    "2/5": 9,
                    "3/5": 10,
                    "8/9": 11,
                    "9/10": 12}
        RfPars["Frequency"] = long(frequency*1000000)
        ModPars["SymRate"] = symbolrate*1000
        if dvb == "DVBS":
            ModPars["ParXtra2"] = -1
            ModPars["ModType"] = 0
            ModPars["ParXtra1"] = -1
        if dvb == "DVBS2":
            ModPars["ParXtra2"] = 0
            if modulation == "QPSK":
                ModPars["ModType"] = 32
            if modulation == "8PSK":
                ModPars["ModType"] = 33
            ModPars["ParXtra1"] = 1792
        ModPars["ParXtra0"] = fec_dict[fec]
        self.client.service.SetModPars(ModPars=ModPars)
        self.client.service.SetRfPars(RfPars=RfPars)
        self.app.write_log("[MOD]   Set Modulator parameters: standard - %s, FEC - %s, frequency - %s, symbolrate - %s, "
                           "modulation - %s" % (dvb, fec, frequency, symbolrate, modulation))  # logger - Set Modulator parameters
        print("[MOD]   Set Modulator parameters: standard - %s, FEC - %s, frequency - %s, symbolrate - %s, "
              "modulation - %s" % (dvb, fec, frequency, symbolrate, modulation))  # print - Set Modulator parameters

    def close_session(self):
        self.client.service.OpenSession()
