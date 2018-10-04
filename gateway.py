import json, datetime, os

"""
basically read a log file,
if what is being read contains a WARN:
    Look at timestamp, target,
    if more > 1 consecutive timestamp with the same target:
        send to slack

"""
results = []
with open("results.json", "r") as json_File:
    for line in json_File:
        results.append(json.loads(line))

for key,value in results[-1].items():
    if value != 200:
        errorFile = open("errors.log", "w")
        errorText = key + " is down." + "\n"
        errorFile.write(errorText)