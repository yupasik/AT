import serial
import os
from json import load, dump
import sys
import datetime
from shutil import copy
import serial.tools.list_ports as pl
from time import strftime, localtime


def where_uart():
    port = serial.Serial()
    uart_port = ''
    ports = list(pl.comports())
    for p in ports:
        if "UART" in str(p[1]):
            port.port = str(p[0])
            try:
                port.open()
            except serial.serialutil.SerialException:
                pass
            if port.isOpen():
                uart_port = str(p[0])
                port.close()
    return uart_port


def read_info(com_port):
    port = serial.Serial(port=com_port, baudrate=115200, timeout=0.1)
    model_list = []
    version_list = []
    while 1:
        port.write("about\n")
        info = port.read(300)
        model_list = [i for i in info.split("\n") if i[0:5] == "Model"]
        version_list = [i for i in info.split("\n") if i[0:16] == "Stingray version"]
        if len(model_list) != 0 and len(version_list) != 0:
            port.close()
            break
    return model_list[0].split()[-1], version_list[0].split()[-1]


test = sys.argv[1]
domain = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
xls_file = os.path.join(domain, "Tests", test, test) + ".xlsx"
com = where_uart()
print(com)
stb, version = read_info(com)
print(stb.upper())
print(version)

now = datetime.datetime.now()
report_name = "%s-%s-sw-%s[%s]" % (test, stb.upper(), version, str(now.strftime("%d.%m.%y_%H-%M-%S")))
report_file = report_name + ".xlsx"
os.mkdir(os.path.join(domain, "Reports", report_name))
copy(xls_file, os.path.join(domain, "Reports", report_name, report_file))
f = file(os.path.join(domain, "Reports", report_name, "log.txt"), "w")
f.close()

with open(os.path.join(domain, "Configuration", "config_test.json"), "r") as s:
    config_test = load(s)
config_test["COM"] = com
config_test["STB"] = stb.upper()
config_test["version"] = version
config_test["report_name"] = report_name
config_test["test_status"] = "executing"
config_test["report_dir"] = os.path.join(domain, "Reports", report_name)
config_test["report_file"] = os.path.join(domain, "Reports", report_name, report_file)
config_test["log_file"] = os.path.join(domain, "Reports", report_name, "log.txt")
with open(os.path.join(domain, "Configuration", "config_test.json"), "w") as s:
    dump(config_test, s, indent=2)

date_time = strftime("%d.%m.%Y %H:%M:%S", localtime())
with open(config_test["log_file"], "a") as s:
    s.write("%s - %s\n" % (date_time, "TEST STARTED"))
print("TEST STARTED")



