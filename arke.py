import requests, arkevars, json

def gather_JsonData(monitoringtargets):
    responseTable = {}
    for target in monitoringtargets:
        try:
            statuscode = requests.get(target).status_code
            responseTable[target] = statuscode
            # prints the int of the status code. Find more at httpstatusrappers.com :)

        except requests.ConnectionError:
            responseTable[target] = "Failed to connect."
    
    return responseTable

gather_JsonData(arkevars.httpTargets)