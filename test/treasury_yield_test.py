# this is the "test/treasury_yield_test.py" file...

from app.treasury_yield import fetch_treasury_yield

def test_data_fetching():
    data = fetch_treasury_yield()
    assert isinstance(data, list)
    assert len(data) > 800

    latest = data[0]
    assert isinstance(latest, dict)
    assert list(latest.keys()) == ["date", "value"]

    earliest = data[-1]
    assert earliest["date"] == '1953-04-01'
    assert earliest["value"] == 2.83