from Devices.application import Application
import sys
import pytest
import allure


test = "Pytest"
testintex = 1
testscript = "test_script1"
stream = "036E_LCN-25_20140418a.ts"


@pytest.fixture(scope="module", autouse=True)
def app(request):
    """
    Main fixture of test environment
    :return: app fixture
    """
    global fixture
    global test
    global testintex
    global testscript
    fixture = Application(test=test,
                          testintex=testintex,
                          testscript=testscript)

    def fin():
        """
        Tear Down method for app fixture
        """
        fixture.capture.stop()
        fixture.capture.close_session()
    request.addfinalizer(fin)
    return fixture


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
def test_case1(app):
    app.capture.start()
    with pytest.allure.step("default settings"):
        app.stb.default_settings()
    app.stb.push(["exit"])
    app.grabber.check_result(1)
    with pytest.allure.step("check testcase 1"):
        assert app.grabber.compare_result > 70


def test_case2(app):
    app.stb.push(["menu 1 5000"])
    app.grabber.check_result(2)
    with pytest.allure.step("check testcase 2"):
        assert app.grabber.compare_result < 70


@pytest.allure.issue('https://jira.exset.com/browse/DTI-1000')
def test_case3(app):
    app.stb.push(["ok 1 5000", "ok 1 2000"])
    app.grabber.check_result(3)
    with pytest.allure.step("check testcase 3"):
        assert app.grabber.compare_result > 70


