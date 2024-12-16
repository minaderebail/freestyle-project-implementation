
# this is the "web_app/routes/interest_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.interest import fetch_interest, format_pct

interest_routes = Blueprint("interest_routes", __name__)


@interest_routes.route("/interest")
def interest():
    print("INTEREST DASHBOARD...")

    try:
        data = fetch_interest()
        latest = data[0]
        latest_rate_pct = format_pct(float(latest["value"]))
        latest_date = latest["date"]

        flash("Successfully fetched interest rate data!", "success")
        return render_template("interest.html",
            latest_rate_pct=latest_rate_pct,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print('OOPS', err)

        flash("Error fetching interest rate data. Please try again!", "danger")
        return redirect("/")

#
# API ROUTES
#

@interest_routes.route("/api/interest.json")
def interest_api():
    print("INTEREST DATA (API)...")

    try:
        data = fetch_interest()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Error fetching interest rate data. Please try again."}, 404