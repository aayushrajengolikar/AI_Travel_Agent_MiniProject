import requests

def get_hotels(city):

    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo = requests.get(geo_url).json()

    if "results" not in geo:
        return []

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    query = f"""
    [out:json];
    node
      ["tourism"="hotel"]
      (around:5000,{lat},{lon});
    out;
    """

    url = "https://overpass-api.de/api/interpreter"
    data = requests.get(url, params={"data": query}).json()

    hotels = []

    for e in data["elements"][:10]:
        name = e.get("tags", {}).get("name")
        if name:
            hotels.append(name)

    return hotels