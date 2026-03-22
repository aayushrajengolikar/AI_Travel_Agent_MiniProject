import requests

def get_tourist_places(city):

    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_response = requests.get(geo_url).json()

    if "results" not in geo_response:
        return []

    lat = geo_response["results"][0]["latitude"]
    lon = geo_response["results"][0]["longitude"]

    overpass_query = f"""
    [out:json];
    node
      ["tourism"="attraction"]
      (around:5000,{lat},{lon});
    out;
    """

    url = "https://overpass-api.de/api/interpreter"

    headers = {
        "User-Agent": "AI-Travel-Agent-App"
    }

    response = requests.get(url, params={"data": overpass_query}, headers=headers)

    if response.status_code != 200:
        return ["Unable to fetch tourist places right now"]

    data = response.json()

    places = []

    for element in data.get("elements", [])[:10]:
        name = element.get("tags", {}).get("name")
        if name:
            places.append(name)

    return places