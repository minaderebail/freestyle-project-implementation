
# this is the "web_app/routes/inflation_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.inflation import fetch_inflation, format_pct

inflation_routes = Blueprint("inflation_routes", __name__)


@inflation_routes.route("/inflation")
def inflation():
    print("INFLATION DASHBOARD...")

    try:
        data = fetch_inflation()
        latest = data[0]
        latest_rate_pct = format_pct(float(latest["value"]))
        latest_date = latest["date"]

        flash("Successfully fetched inflation data!", "success")
        return render_template("inflation.html",
            latest_rate_pct=latest_rate_pct,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print('OOPS', err)

        flash("Error fetching inflation data. Please try again!", "danger")
        return redirect("/")

#
# API ROUTES
#

@inflation_routes.route("/api/inflation.json")
def inflation_api():
    print("INFLATION DATA (API)...")

    try:
        data = fetch_inflation()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Error fetching inflation data. Please try again."}, 404