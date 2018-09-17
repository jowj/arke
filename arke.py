import requests, arkevars, json, logging

FORMAT = "%(asctime)-15s %(clientip)s %(user)-8s %(message)s"
logging.basicConfig(format=FORMAT)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("arke")

def gather_JsonData(monitoringtargets):
    responseTable = {}
    for target in monitoringtargets:
        try:
            statuscode = requests.get(target).status_code
            logger.info(f"target: {target} statuscode: {statuscode}")
            # prints the int of the status code. Find more at httpstatusrappers.com :)

        except requests.ConnectionError:
            logger.info(f"target: {target} ERROR: Failure to connect.")
    
    return responseTable

gather_JsonData(arkevars.httpTargets)