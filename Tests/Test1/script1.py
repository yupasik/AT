from Devices.application import Application
import sys


test = "Test1"
testintex = 1
testscript = "script1"
stream = "036E_LCN-25_20140418a.ts"

"""
app = Application(test=test,
                  testintex=testintex,
                  testscript=testscript,
                  stb=sys.argv[1],
                  version=sys.argv[2],
                  report_name=sys.argv[3])
"""

app = Application(test=test,
                  testintex=testintex,
                  testscript=testscript,
                  report_name=sys.argv[1])

app.modulator1.set_options(dvb="DVBS",
                           fec="3/4",
                           frequency=1476,
                           symbolrate=27500,
                           modulation="QPSK")

app.modulator1.open(stream)
app.capture.start()

#  ------------------------------------------------------------------------
testcase = 1
app.modulator1.play()
app.stb.default_settings()
app.stb.push(["exit"])
app.grabber.check_result(testcase)
#  ------------------------------------------------------------------------
testcase = 2
app.stb.push(["menu 1 3000"])
app.grabber.check_result(testcase)
#  ------------------------------------------------------------------------
testcase = 3
app.modulator1.pause()
app.stb.reboot()
app.stb.push(["exit 1 2000", "menu 1 3000", "ok 1 2000"])
app.grabber.check_result(testcase)
#  ------------------------------------------------------------------------
app.capture.stop()
app.fin()
