# this is the app/real_gdp.py file...

from statistics import mean
from plotly.express import line
import requests
from app.alpha import API_KEY

def fetch_real_gdp():
    gdp_url = f"https://www.alphavantage.co/query?function=REAL_GDP_PER_CAPITA&apikey={API_KEY}&datatype=csv"
    gdp_response = requests.get(gdp_url)
    parsed_response = gdp_response.json()
    data = parsed_response["data"]
    for item in data:
        item["value"] = float(item["value"])
    return data

if __name__ == "__main__":
    # get data
    data = fetch_real_gdp()

    # print data title
    print("Data: ")
    print("")

    # print the last 10 data points
    print("Over the last 10 quarters, the real GDP per capita in the US has been: ")
    for i in range(10):
        print(f"${data[i]['value']}", "on", data[i]["date"])