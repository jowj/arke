import requests, arkevars, json

responseTable = {}
for target in arkevars.httpTargets:
    try:
        statuscode = requests.get(target).status_code
        responseTable[target] = statuscode
        # prints the int of the status code. Find more at httpstatusrappers.com :)

    except requests.ConnectionError:
        print("failed to connect")

jsonData = json.dumps(responseTable)
