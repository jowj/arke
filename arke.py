import requests, arkevars, json, logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p',level=logging.INFO,filename='example.log')
logger = logging.getLogger("arke")

def monitor_AllTargets(monitoringtargets):
    for target in monitoringtargets:
        try:
            statuscode = requests.get(target).status_code
            logger.info(f"target: {target} statuscode: {statuscode}")
            # prints the int of the status code. Find more at httpstatusrappers.com :)

        except requests.ConnectionError:
            logger.warn(f"target: {target} ERROR: Failure to connect.")

monitor_AllTargets(arkevars.httpTargets)
