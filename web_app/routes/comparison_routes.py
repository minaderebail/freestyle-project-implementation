
# this is the "web_app/routes/comparison_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.inflation import fetch_inflation, format_pct
from app.interest import fetch_interest, format_pct
from app.treasury_yield import fetch_treasury_yield, format_pct
from app.unemployment import fetch_unemployment, format_pct

comparison_routes = Blueprint("comparison_routes", __name__)


@comparison_routes.route("/comparison")
def comparison():
    print("COMPARISON DASHBOARD...")

    try:
        inflation = fetch_inflation()
        interest = fetch_interest()
        treasury_yield = fetch_treasury_yield()
        unemployment = fetch_unemployment()
        return render_template("comparison.html", inflation=inflation,
                               interest=interest, 
                               treasury_yield=treasury_yield,
                               unemployment=unemployment)

    except Exception as err:
        print('OOPS', err)
        return {"message":"Error fetching data. Please try again."}, 404

#
# API ROUTES
#

@comparison_routes.route("/api/comparison.json")
def comparison_api():
    print("COMPARISON DATA (API)...")

    try:
        data_inflation = fetch_inflation()
        data_interest = fetch_interest()
        data_treasury = fetch_treasury_yield()
        data_unemployment = fetch_unemployment()
        return {
            'inflation': data_inflation,
            'interest': data_interest,
            'treasury_yield': data_treasury,
            'unemployment': data_unemployment
        }
    except Exception as err:
        print('OOPS', err)
        return {"message":"Error fetching data. Please try again."}, 404