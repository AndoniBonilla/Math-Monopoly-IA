import pandas as pd

# Sample data for House Level 1 properties (you can expand this list with full dataset)
data = {
    "Property": [
        "Mediterranean Avenue", "Baltic Avenue", "Oriental Avenue", "Vermont Avenue", 
        "Connecticut Avenue", "St. Charles Place", "States Avenue", "Virginia Avenue",
        "St. James Place", "Tennessee Avenue", "New York Avenue", "Kentucky Avenue", 
        "Indiana Avenue", "Illinois Avenue", "Atlantic Avenue", "Ventnor Avenue", 
        "Marvin Gardens", "Pacific Avenue", "North Carolina Avenue", "Pennsylvania Avenue", 
        "Park Place", "Boardwalk"
    ],
    "Color Set": [
        "Brown", "Brown", "Light Blue", "Light Blue", 
        "Light Blue", "Pink", "Pink", "Pink", 
        "Orange", "Orange", "Orange", "Red", 
        "Red", "Red", "Yellow", "Yellow", 
        "Yellow", "Green", "Green", "Green", 
        "Dark Blue", "Dark Blue"
    ],
    "House Level": [1]*22,
    "Visits": [48, 49, 58, 40, 31, 45, 47, 57, 53, 56, 49, 71, 57, 46, 55, 49, 52, 51, 60, 48, 40, 42],
    "Expected Rent": [
        96, 98, 116, 80, 62, 90, 94, 114, 106, 112, 98, 142, 114, 92, 
        110, 98, 104, 102, 120, 96, 80, 84
    ],
    "Cost": [
        110, 110, 150, 150, 170, 250, 240, 260, 280, 280, 300, 370, 370, 390,
        410, 410, 430, 500, 500, 520, 550, 600
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate ROI for each property
df["ROI"] = df["Expected Rent"] / df["Cost"]

# Group by Color Set and House Level
grouped = df.groupby(["Color Set", "House Level"]).agg(
    Total_Adjusted_ROI=pd.NamedAgg(column="Expected Rent", aggfunc="sum"),
    Average_Adjusted_ROI=pd.NamedAgg(column="ROI", aggfunc="mean")
).reset_index()

# Display results
print(grouped)
