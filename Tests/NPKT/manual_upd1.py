import os
import sys
modeules_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(modeules_path)
from Devices.application import Application


test = os.path.split(os.path.dirname(os.path.abspath(__file__)))[-1]
testintex = 1
testscript = os.path.basename(os.path.abspath(__file__)).split(".")[0]
stream = "036E_LCN-25_20140418a.ts"


app = Application(test=test,
                  testintex=testintex,
                  testscript=testscript)
"""
app.modulator1.set_options(dvb="DVBS",
                           fec="3/4",
                           frequency=1476,
                           symbolrate=27500,
                           modulation="QPSK")
"""

# app.modulator1.open(stream)
app.capture.start()

#  ------------------------------------------------------------------------
app.start_testcase(1)
# app.modulator1.play()
app.stb.default_settings()
app.stb.push(["exit"])
app.grabber.check_result(app.testcase)
#  ------------------------------------------------------------------------
app.start_testcase(2)
app.stb.push(["menu 1 3000"])
app.grabber.check_result(app.testcase)
#  ------------------------------------------------------------------------
app.start_testcase(3)
# app.modulator1.pause()
app.stb.reboot()
app.stb.launch("settings")
app.stb.push(["exit 1 2000", "menu 1 3000", "ok 1 2000", "ok 1 3000"])
app.grabber.check_result(app.testcase)
#  ------------------------------------------------------------------------
app.capture.stop()
app.fin()
