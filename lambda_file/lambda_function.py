import pandas as pd
import requests
import os
def lambda_handler(event,context):

    print("git hub action workflow")

    request = requests.get("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    # convert json format
    data = request.json()

    # convert dataframe to json
    df = pd.DataFrame(data)
    df.head(5)

    # envs
    print("enviroment variables.....")
    defined_variables = ["ENV","API_key","LOG_LEVEL"]

    for key in defined_variables:
        value = os.environ.get(key)
        if value is not None:
            print(f"{key}:{value}")

    return {
        "StatusCode":200,
        "body":"lambda function executed sucessfully"
    }
