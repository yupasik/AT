import pytest
from fixture.application import Application
from time import strftime, localtime
from shutil import copy
import os


fixture = None


@pytest.fixture(scope="session", autouse=True)
def app(request):
    domain = os.path.dirname(os.path.abspath(__file__))
    report_folder = "%s-Stingray.%s-%s%s" % (request.config.getoption("--test"),
                                             request.config.getoption("--stb"),
                                             request.config.getoption("--ver"),
                                             strftime("[%d.%m.%Y_%H-%M-%S]", localtime()))
    report_file = report_folder + ".xlsx"
    os.mkdir(os.path.join(domain, "Reports", report_folder))
    copy( os.path.join(domain, "Tests", request.config.getoption("--test"), request.config.getoption("--test")) + ".xlsx", report_file)
    global fixture
    if fixture is None:
        fixture = Application(test=request.config.getoption("--test"),
                              testintex=None,
                              testscript=None,
                              stb=request.config.getoption("--stb"),
                              version=request.config.getoption("--ver"),
                              report_name=report_folder)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--test", action="store", default="Channel0")
    parser.addoption("--stb", action="store", default="E501")
    parser.addoption("--ver", action="store", default="0.0.0")
