from Devices.application import Application
import sys
import pytest


test = "Channel0"
testintex = 1
testscript = "script1"
stream = "036E_LCN-25_20140418a.ts"


def test_case_1(app):
    app.testintex = testintex
    app.testscript = testscript
    app.modulator1.set_options(dvb="DVBS",
                               fec="3/4",
                               frequency=1476,
                               symbolrate=27500,
                               modulation="QPSK")
    app.modulator1.open(stream)
    app.capture.start()
    app.modulator1.play()
    app.stb.default_settings()
    app.stb.push(["exit"])
    app.grabber.check_result(1)
