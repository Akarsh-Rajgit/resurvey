import requests

data = {
    "location": "HSR Layout",
    "size": 2,
    "total_sqft": 1200,
    "bath": 2,
    "price_lakhs": 75.0,
    "price_per_sqft": 6250.0
}
r = requests.post("http://127.0.0.1:5000/add", json=data)
print("Insert:", r.json())

r = requests.get("http://127.0.0.1:5000/filter?location=HSR Layout&min_price=70")
print("Filter:", r.json())
