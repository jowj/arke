import requests, arkevars, json, logging, datetime, os, time

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p',level=logging.INFO,filename='arke.log')
logger = logging.getLogger("arke")

def monitor_AllTargets(monitoringtargets):
    responseTable = {}
    for target in monitoringtargets:
        try:
            statuscode = requests.get(target).status_code
            logger.info(f"target: {target} statuscode: {statuscode}")
            responseTable[target] = statuscode

        except requests.ConnectionError:
            logger.warn(f"target: {target} ERROR: Failure to connect.")
            responseTable[target] = "Failed to connect."
    
    return responseTable

is_on = True
while is_on:
    datastore = monitor_AllTargets(arkevars.httpTargets)
    json_string = json.dumps(datastore)

    file = open("/shared/results.json", "a+")
    file.write(json_string)
    file.write("\n")
    file.close()

    results = []
    with open("/shared/results.json", "r") as json_File:
        for line in json_File:
            results.append(json.loads(line))

    for key,value in results[-1].items():
        if value != 200:
            errorFile = open("alerts.log", "w")
            errorText = key + " is down." + "\n"
            errorFile.write(errorText)
            errorFile.close()
    time.sleep(60)
    os.remove("/shared/results.json")
