import subprocess

subprocess.call(["rm","-rf","output/"])
subprocess.call(["rm","-rf","input/"])
subprocess.call(["rm","-rf","unknown/"])
subprocess.call(["mkdir", "input"])
subprocess.call(["mkdir", "unknown"])
subprocess.call(["touch","input/.keep"])
subprocess.call(["touch","unknown/.keep"])