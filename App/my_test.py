import os
import pytest

from roboadvisor import to_usd, get_response

CI_ENV = os.environ.get("CI")==True

def test_get_response(): #Professor's Test code
    symbol="goog"

    parsed_response = get_response(symbol)
    assert isinstance(parsed_response, dict)
    assert "Meta Data" in parsed_response.keys()
    assert "Time Series (Daily)" in parsed_response.keys()
    assert parsed_response["Meta Data"]["2. Symbol"]==symbol

def test_to_usd():
    result= to_usd(73498.82)
    assert result == "$73,498.82"
    assert to_usd(9.9) == "$9.90"