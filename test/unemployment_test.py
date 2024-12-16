# this is the "test/unemployment_test.py" file...

from app.unemployment import fetch_unemployment

def test_data_fetching():
    data = fetch_unemployment()
    assert isinstance(data, list)
    assert len(data) > 900

    latest = data[0]
    assert isinstance(latest, dict)
    assert list(latest.keys()) == ["date", "value"]

    earliest = data[-1]
    assert earliest["date"] == '1948-01-01'
    assert earliest["value"] == 3.4