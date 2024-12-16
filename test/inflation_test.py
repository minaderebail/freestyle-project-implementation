# this is the "test/inflation_test.py" file...

from app.inflation import fetch_inflation

def test_data_fetching():
    data = fetch_inflation()
    assert isinstance(data, list)
    assert len(data) > 60

    latest = data[0]
    assert isinstance(latest, dict)
    assert list(latest.keys()) == ["date", "value"]

    earliest = data[-1]
    assert earliest["date"] == '1960-01-01'
    assert earliest["value"] == 1.45797598627791