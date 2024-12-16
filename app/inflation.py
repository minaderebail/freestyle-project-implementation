# this is the app/inflation.py file...

# LOCAL DEV (ENV VARS)

from statistics import mean
import requests
from plotly.express import line
from app.alpha import API_KEY

# percent formatter function
def format_pct(my_number):
    return f"{my_number:.2f}%"

# data fetching function
def fetch_inflation():
    inflation_url = f"https://www.alphavantage.co/query?function=INFLATION&apikey={API_KEY}"
    inflation_response = requests.get(inflation_url)
    parsed_response = inflation_response.json()
    data = parsed_response["data"]
    for item in data:
        item["value"] = float(item["value"])
    return data

if __name__ == "__main__":

    # fetch data
    data = fetch_inflation()

    # print data title
    print("Data: ")
    print("")

    # print the last 10 data points
    print("Inflation rates in the US over the last 10 years: ")
    for i in range(10):
        print(f"{data[i]['value']:.2f}%", "on", data[i]["date"])

    # print graph title
    print("")
    print("Graph: ")
    print("")

    # make a line plot
    x_axis = [d["date"] for d in data]
    y_axis = [float(d["value"]) for d in data]
    fig = line(x=x_axis, y=y_axis, title="United States Inflation Rate over Time", labels= {"x": "Time", "y": "Inflation Rate"}, markers=True)
    fig.show()