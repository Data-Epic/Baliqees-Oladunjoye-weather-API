import pytest
import requests
from weather_client import get_weather, get_forecast

#inputing a fake api key for testing
api_key = "fake_api_key"

def test_get_weather_success(monkeypatch):
    # Simulate a successful API response
    class MockResponse:
        status_code = 200
        def json(self):
            return {
                "weather": [{"description": "clear sky"}],
                "main": {"temp": 25, "humidity": 50},
                "wind": {"speed": 3},
                "name": "Lagos",
                "sys": {"country": "NG"}
            }

    # Patch requests.get to return the mock response
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: MockResponse())

    # Run the function (it should just print output, no crash)
    get_weather("Lagos", api_key)


def test_get_weather_failure(monkeypatch):
    # Simulate an API failure (e.g., city not found)
    class MockResponse:
        status_code = 404
        def json(self):
            return {"message": "city not found"}

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: MockResponse())

    # Run the function (it should print an error message)
    get_weather("FakeCity", api_key)


def test_get_forecast_success(monkeypatch):
    # Simulate forecast data
    class MockResponse:
        status_code = 200
        def json(self):
            return {
                "list": [
                    {
                        "dt_txt": "2025-04-10 12:00:00",
                        "main": {"temp": 28},
                        "weather": [{"description": "scattered clouds"}]
                    },
                    {
                        "dt_txt": "2025-04-11 12:00:00",
                        "main": {"temp": 29},
                        "weather": [{"description": "light rain"}]
                    }
                ]
            }

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: MockResponse())

    get_forecast("Lagos", api_key)