import os
from json import load, dump
from time import strftime, localtime


domain = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(domain, "Configuration", "config_test.json"), "r") as s:
    config_test = load(s)

config_test["test_status"] = "finished"

with open(os.path.join(domain, "Configuration", "config_test.json"), "w") as s:
    dump(config_test, s, indent=2)

date_time = strftime("%d.%m.%Y %H:%M:%S", localtime())
with open(config_test["log_file"], "a") as s:
    s.write("%s - %s\n" % (date_time, "TEST FINISHED"))
print("TEST FINISHED")
