# test_cities.py  – should PASS with optional population

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_country()."""

    def test_city_country(self):
        """'santiago' + 'chile' ➜ 'Santiago, Chile'."""
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

if __name__ == "__main__":
    unittest.main(verbosity=2)   # verbosity=2 gives clearer output
