import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "location": [
        "Whitefield", "Sarjapur Road", "Electronic City", "Kanakpura Road", "Thanisandra",
        "Hebbal", "Yelahanka", "Raja Rajeshwari Nagar", "Marathahalli", "Electronic City Phase II",
        "Hennur Road", "7th Phase JP Nagar", "Bannerghatta Road", "Uttarahalli", "Haralur Road",
        "Hoodi", "Begur Road", "Chandapura", "Yeshwanthpur", "Rajaji Nagar", "Jakkur",
        "Electronics City Phase 1", "Harlur", "Hosa Road", "Thigalarapalya", "Bisuvanahalli",
        "Varthur", "Jigani", "Old Madras Road", "Bellandur"
    ],
    "frequency": [
        194, 134, 118, 114, 97, 87, 81, 71, 61, 58, 54, 53, 52, 51, 50, 40, 36, 35,
        31, 31, 31, 30, 28, 27, 27, 26, 26, 26, 26, 25
    ]
}

location_coords = {
    "Whitefield": (77.7500, 12.9698), "Sarjapur Road": (77.7167, 12.9050),
    "Electronic City": (77.6845, 12.8452), "Kanakpura Road": (77.5467, 12.8661),
    "Thanisandra": (77.6256, 13.0641), "Hebbal": (77.5913, 13.0358),
    "Yelahanka": (77.5969, 13.1007), "Raja Rajeshwari Nagar": (77.5044, 12.9269),
    "Marathahalli": (77.6974, 12.9568), "Electronic City Phase II": (77.6666, 12.8233),
    "Hennur Road": (77.6400, 13.0450), "7th Phase JP Nagar": (77.5850, 12.9014),
    "Bannerghatta Road": (77.5981, 12.8671), "Uttarahalli": (77.5371, 12.8983),
    "Haralur Road": (77.6487, 12.8990), "Hoodi": (77.7172, 12.9923),
    "Begur Road": (77.6253, 12.8806), "Chandapura": (77.6999, 12.8002),
    "Yeshwanthpur": (77.5543, 13.0173), "Rajaji Nagar": (77.5559, 12.9916),
    "Jakkur": (77.6204, 13.0681), "Electronics City Phase 1": (77.6677, 12.8451),
    "Harlur": (77.6494, 12.9052), "Hosa Road": (77.6471, 12.8751),
    "Thigalarapalya": (77.4786, 13.0168), "Bisuvanahalli": (77.7500, 12.9900),
    "Varthur": (77.7476, 12.9352), "Jigani": (77.6466, 12.7847),
    "Old Madras Road": (77.7100, 12.9967), "Bellandur": (77.6784, 12.9352)
}

df = pd.DataFrame(data)
df["lon"] = df["location"].map(lambda loc: location_coords.get(loc, (0, 0))[0])
df["lat"] = df["location"].map(lambda loc: location_coords.get(loc, (0, 0))[1])
df = df[df["lon"] != 0]

geometry = [Point(xy) for xy in zip(df.lon, df.lat)]
geo_df = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

fig, ax = plt.subplots(figsize=(10, 10))
geo_df.plot(ax=ax, markersize=geo_df["frequency"], color="skyblue", edgecolor="black", alpha=0.7)

for x, y, label in zip(geo_df.geometry.x, geo_df.geometry.y, geo_df["frequency"]):
    ax.text(x, y, str(label), fontsize=8, ha="center", va="center")

ax.set_title("Bangalore Property Listings Frequency by Location (Approximate Coordinates)")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.grid(True)
plt.show()