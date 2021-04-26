"""
    Weatherbit.io - Swagger UI Weather API documentation

    This is the documentation for the Weatherbit Weather API.  The base URL for the API is [http://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/) or [https://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/). Below is the Swagger UI documentation for the API. All API requests require the `key` parameter.        An Example for a 5 day forecast for London, UK would be `http://api.weatherbit.io/v2.0/forecast/3hourly?city=London`&`country=UK`. See our [Weather API description page](https://www.weatherbit.io/api) for additional documentation.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.5_day___3_hour_forecast_api import 5Day3HourForecastApi  # noqa: E501


class Test5Day3HourForecastApi(unittest.TestCase):
    """5Day3HourForecastApi unit test stubs"""

    def setUp(self):
        self.api = 5Day3HourForecastApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_forecast3hourlycity_idcity_id_get(self):
        """Test case for forecast3hourlycity_idcity_id_get

        Returns a 3-hourly forecast - Given a City ID.  # noqa: E501
        """
        pass

    def test_forecast3hourlycitycitycountrycountry_get(self):
        """Test case for forecast3hourlycitycitycountrycountry_get

        Returns a 3-hourly forecast - Given City and/or State, Country.  # noqa: E501
        """
        pass

    def test_forecast3hourlylatlatlonlon_get(self):
        """Test case for forecast3hourlylatlatlonlon_get

        Returns a 3-hourly forecast - Given a lat/lon.  # noqa: E501
        """
        pass

    def test_forecast3hourlypostal_codepostal_code_get(self):
        """Test case for forecast3hourlypostal_codepostal_code_get

        Returns a 3-hourly forecast - Given a Postal Code.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
