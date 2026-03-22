import requests

def get_hotels(city):

    try:
        # Step 1: Get coordinates
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo = requests.get(geo_url).json()

        if "results" not in geo:
            return ["No location found"]

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        # Step 2: Overpass query
        query = f"""
        [out:json];
        node
          ["tourism"="hotel"]
          (around:5000,{lat},{lon});
        out;
        """

        url = "https://overpass-api.de/api/interpreter"

        headers = {
            "User-Agent": "AI-Travel-Agent-App"
        }

        response = requests.get(url, params={"data": query}, headers=headers)

        # 🔥 Check if response is valid
        if response.status_code != 200:
            return ["Unable to fetch hotels right now"]

        if not response.text.strip():
            return ["No hotel data received"]

        data = response.json()

        hotels = []

        for e in data.get("elements", [])[:10]:
            name = e.get("tags", {}).get("name")
            if name:
                hotels.append(name)

        return hotels if hotels else ["No hotels found"]

    except Exception as e:
        return [f"Error fetching hotels: {str(e)}"]