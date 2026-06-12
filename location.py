import requests

def get_location():
    try:
        response = requests.get(
            "http://ip-api.com/json/",
            timeout=5
        )

        data = response.json()

        if data["status"] == "success":
            return {
                "city": data["city"],
                "country": data["country"]
            }

        return None

    except requests.exceptions.RequestException:
        return None