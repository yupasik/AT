from Devices.application import Application
import sys
import pytest


test = "Pytest"
testintex = 1
testscript = "test_script1"
stream = "036E_LCN-25_20140418a.ts"


@pytest.fixture(scope="session")
def test_case1(app):
    app.modulator1.play()
    app.stb.default_settings()
    app.stb.push(["exit"])
    assert app.grabber.check_result()


@pytest.fixture(scope="session")
def test_case2(app):
    app.stb.push(["menu 1 5000"])
    app.grabber.check_result()


@pytest.fixture(scope="session")
def test_case3(app):
    app.modulator1.pause()
    app.stb.push(["ok 1 5000", "ok 1 2000"])
    app.grabber.check_result()


