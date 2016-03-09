from fixture.modulator import Modulator
from fixture.uart import uSTB
from fixture.grabber import Display, FrameStorage, Capture
from time import strftime, localtime
import os
from json import load, dump


class Application:

    testcase = None
    result = None

    def __init__(self, test, testintex, testscript):
        self.domain = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(self.domain, "Configuration", "config_test.json"), "r") as s:
            config_test = load(s)
        self.test = test
        self.testintex = testintex
        self.testscript = testscript
        self.stb = uSTB(self)
        self.report_name = config_test["report_name"]
        self.report_dir = config_test["report_dir"]
        self.report_file = config_test["report_file"]
        self.stb_model = config_test["STB"]
        self.version = config_test["version"]
        self.log_file = config_test["log_file"]
        config_test["current_script"] = self.testscript
        with open(os.path.join(self.domain, "Configuration", "config_test.json"), "w") as s:
            dump(config_test, s, indent=2)
        self.modulator1 = Modulator(self, 1)
        self.modulator2 = Modulator(self, 2)
        self.capture = Capture(self)
        self.display = Display(self)
        self.grabber = FrameStorage(self)
        self.capture.register_handler(self.display.display)
        self.capture.register_handler(self.grabber.set)
        self.write_log("START %s" % self.testscript)
        print("START %s" % self.testscript)

    def write_log(self, info):
        date_time = strftime("%d.%m.%Y %H:%M:%S", localtime())
        with open(self.log_file, "a") as l:
            l.write("%s - %s\n" % (date_time, info))

    def fin(self):
        self.write_log("STOP %s" % self.testscript)
        print("STOP %s" % self.testscript)
        self.stb.port.close()
        self.modulator1.close_session()
        self.modulator2.close_session()
        self.capture.close_session()

    def start_testcase(self, test_case):
        self.testcase = test_case
        self.write_log("TEST CASE %s" % self.testcase)
        print("TEST CASE %s" % self.testcase)



