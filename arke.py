import requests, arkevars, json, logging, datetime

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p',level=logging.INFO,filename='example.log')
logger = logging.getLogger("arke")

def monitor_AllTargets(monitoringtargets):
    responseTable = {}
    for target in monitoringtargets:
        try:
            statuscode = requests.get(target).status_code
            logger.info(f"target: {target} statuscode: {statuscode}")
            responseTable[target] = statuscode
            # prints the int of the status code. Find more at httpstatusrappers.com :)

        except requests.ConnectionError:
            logger.warn(f"target: {target} ERROR: Failure to connect.")
            responseTable[target] = "Failed to connect."
    
    return responseTable

target_Codes = monitor_AllTargets(arkevars.httpTargets)
currentdate = datetime.datetime.now().isoformat()

# export shit as a dict
with open(f'{currentdate}.py','w') as file:
    file.write("results = { \n")
    for k in sorted (target_Codes.keys()):
        file.write("'%s':'%s', \n" % (k, target_Codes[k]))
    file.write("}\n")
