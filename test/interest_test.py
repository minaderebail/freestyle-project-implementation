# this is the "test/interest_test.py" file...

from app.interest import fetch_interest

def test_data_fetching():
    data = fetch_interest()
    assert isinstance(data, list)
    assert len(data) > 800

    latest = data[0]
    assert isinstance(latest, dict)
    assert list(latest.keys()) == ["date", "value"]

    earliest = data[-1]
    assert earliest["date"] == '1954-07-01'
    assert earliest["value"] == 0.8