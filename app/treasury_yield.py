# this is the app/treasury_yield.py file...

# LOCAL DEV (ENV VARS)

from statistics import mean
import requests
from plotly.express import line
from app.alpha import API_KEY

# percent formatter function
def format_pct(my_number):
    return f"{my_number:.2f}%"

# data fetching function
def fetch_treasury_yield():
    treasury_url = f"https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=monthly&maturity=10year&apikey={API_KEY}"
    treasury_response = requests.get(treasury_url)
    parsed_response = treasury_response.json()
    data = parsed_response["data"]
    for item in data:
        item["value"] = float(item["value"])
    return data

if __name__ == "__main__":

    # fetch data
    data = fetch_treasury_yield()

    # print data title
    print("Data: ")
    print("")

    # print the last 10 data points
    print("10-year treasury yield rates in the US over the last 10 months: ")
    for i in range(10):
        print(f"{data[i]['value']:.2f}%", "on", data[i]["date"])

    # compute and print averages for the last 5 years
    year_2024 = [d for d in data if "2024-" in d["date"]]
    year_2023 = [d for d in data if "2023-" in d["date"]]
    year_2022 = [d for d in data if "2022-" in d["date"]]
    year_2021 = [d for d in data if "2021-" in d["date"]]
    year_2020 = [d for d in data if "2020-" in d["date"]]

    rate_2024 = [float(d["value"]) for d in year_2024]
    rate_2023 = [float(d["value"]) for d in year_2023]
    rate_2022 = [float(d["value"]) for d in year_2022]
    rate_2021 = [float(d["value"]) for d in year_2021]
    rate_2020 = [float(d["value"]) for d in year_2020]

    mean_rate_2024 = mean(rate_2024)
    mean_rate_2023 = mean(rate_2023)
    mean_rate_2022 = mean(rate_2022)
    mean_rate_2021 = mean(rate_2021)
    mean_rate_2020 = mean(rate_2020)

    mean_rate_2024 = round(mean_rate_2024, 2)
    mean_rate_2023 = round(mean_rate_2023, 2)
    mean_rate_2022 = round(mean_rate_2022, 2)
    mean_rate_2021 = round(mean_rate_2021, 2)
    mean_rate_2020 = round(mean_rate_2020, 2)

    print(" ")
    print("Average 10-year treasury yield rates in the US over the last 5 years: ")
    print(f"{mean_rate_2024}%", "in 2024")
    print(f"{mean_rate_2023}%", "in 2023")
    print(f"{mean_rate_2022}%", "in 2022")
    print(f"{mean_rate_2021}%", "in 2021")
    print(f"{mean_rate_2020}%", "in 2020")

    # print graph title
    print("")
    print("Graph: ")
    print("")

    # make a line plot
    x_axis = [d["date"] for d in data]
    y_axis = [float(d["value"]) for d in data]
    fig = line(x=x_axis, y=y_axis, title="United States 10-year Treasury Yield Rates over Time", labels= {"x": "Time", "y": "10-year Treasury Yield Rates"}, markers=True)
    fig.show()