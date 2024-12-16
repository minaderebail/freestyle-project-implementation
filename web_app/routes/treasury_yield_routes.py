
# this is the "web_app/routes/treasury_yield_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.treasury_yield import fetch_treasury_yield, format_pct

treasury_yield_routes = Blueprint("treasury_yield_routes", __name__)


@treasury_yield_routes.route("/treasury/yield")
def treasury_yield():
    print("TREASURY YIELD DASHBOARD...")

    try:
        data = fetch_treasury_yield()
        latest = data[0]
        latest_rate_pct = format_pct(float(latest["value"]))
        latest_date = latest["date"]

        flash("Successfully fetched treasury yield rate data!", "success")
        return render_template("treasury_yield.html",
            latest_rate_pct=latest_rate_pct,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print('OOPS', err)

        flash("Error fetching treasury yield rate data. Please try again!", "danger")
        return redirect("/")

#
# API ROUTES
#

@treasury_yield_routes.route("/api/treasury/yield.json")
def treasury_yield_api():
    print("TREASURY YIELD DATA (API)...")

    try:
        data = fetch_treasury_yield()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Error fetching treasury yield rate data. Please try again."}, 404