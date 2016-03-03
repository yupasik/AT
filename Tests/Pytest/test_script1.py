from Devices.application import Application
import sys
import pytest


test = "Pytest"
testintex = 1
testscript = "test_script1"
stream = "036E_LCN-25_20140418a.ts"
fixture = None


@pytest.fixture(scope="module", autouse=True)
def app(request):
    global fixture
    global test
    global testintex
    global testscript
    if fixture is None:
        fixture = Application(test=test,
                              testintex=testintex,
                              testscript=testscript)

    def fin():
        fixture.capture.stop()
        fixture.capture.close_session()
    request.addfinalizer(fin)
    return fixture


def test_case1(app):
    app.capture.start()
    app.stb.default_settings()
    app.stb.push(["exit"])
    app.grabber.check_result(1)
    with pytest.allure.step("check testcase 1")
        assert 100 > 70


def test_case2(app):
    app.stb.push(["menu 1 5000"])
    app.grabber.check_result(2)
    with pytest.allure.step("check testcase 2")
        assert 100 < 70


def test_case3(app):
    app.stb.push(["ok 1 5000", "ok 1 2000"])
    app.grabber.check_result(3)
    with pytest.allure.step("check testcase 3")
        assert 100 > 70


