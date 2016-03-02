from fixture.modulator import Modulator
from fixture.uart import uSTB
from fixture.grabber import Display, FrameStorage, Capture
from time import strftime, localtime
import os


class Application:

    def __init__(self, test, testintex, testscript, stb, version, report_name):
        self.domain = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.test = test
        self.testintex = testintex
        self.testscript = testscript
        self.stb_model = stb
        self.stb = uSTB(self)
        self.version = version
        self.report_name = report_name
        self.report_dir = os.path.join(self.domain, "Reports", self.report_name)
        self.report_file = os.path.join(self.report_dir, self.report_name + ".xlsx")
        self.log_file = os.path.join(self.report_dir, "log.txt")
        self.modulator1 = Modulator(self, 1)
        self.modulator2 = Modulator(self, 2)
        self.capture = Capture(self)
        self.display = Display(self)
        self.grabber = FrameStorage(self)
        self.capture.register_handler(self.display.display)
        self.capture.register_handler(self.grabber.set)
        self.write_log("TEST STARTED")

    def write_log(self, info):
        date_time = strftime("%d.%m.%Y %H:%M:%S", localtime())
        with open(self.log_file, "a") as l:
            l.write("%s - %s\n" % (date_time, info))

    def fin(self):
        self.write_log("TEST FINISHED")
        self.stb.port.close()


