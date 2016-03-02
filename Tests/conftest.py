import pytest
from fixture.application import Application
from time import strftime, localtime
from shutil import copy
import os


fixture = None


@pytest.yield_fixture(scope="session", autouse=True)
def app(request):
    global fixture
    if fixture is None:
        fixture = Application(test=request.config.getoption("--test"),
                              testintex=testintex,
                              testscript=testscript)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--test", action="store", default="Channel0")
    parser.addoption("--stb", action="store", default="E501")
    parser.addoption("--ver", action="store", default="0.0.0")
