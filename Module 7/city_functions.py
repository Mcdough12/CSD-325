# city_functions.py  – Step 5-B (population AND language are OPTIONAL)

def city_country(city, country, population=None, language=None):
    """
    Formats a city string with optional population and language:
      • City, Country
      • City, Country - population nnnnnnn
      • City, Country - population nnnnnnn, Language
    """
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# --- final demo calls for your assignment screenshot ---
if __name__ == "__main__":
    # 1) City, Country
    print(city_country("santiago", "chile"))

    # 2) City, Country + population
    print(city_country("paris", "france", 2148000))

    # 3) City, Country + population + language
    print(city_country("cairo", "egypt", 9500000, "arabic"))
