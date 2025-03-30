import random
import pandas as pd

# 🧱 Property data: position → (name, price, [rent per house level 0–5], house cost)
property_data = {
    1:  ("Mediterranean Avenue", 60,   [2, 10, 30, 90, 160, 250], 50),
    3:  ("Baltic Avenue", 60,          [4, 20, 60, 180, 320, 450], 50),
    5:  ("Reading Railroad", 200,      [25]*6, 0),
    6:  ("Oriental Avenue", 100,       [6, 30, 90, 270, 400, 550], 50),
    8:  ("Vermont Avenue", 100,        [6, 30, 90, 270, 400, 550], 50),
    9:  ("Connecticut Avenue", 120,    [8, 40, 100, 300, 450, 600], 50),
    11: ("St. Charles Place", 140,     [10, 50, 150, 450, 625, 750], 100),
    12: ("Electric Company", 150,      [8]*6, 0),
    13: ("States Avenue", 140,         [10, 50, 150, 450, 625, 750], 100),
    14: ("Virginia Avenue", 160,       [12, 60, 180, 500, 700, 900], 100),
    15: ("Pennsylvania Railroad", 200, [25]*6, 0),
    16: ("St. James Place", 180,       [14, 70, 200, 550, 750, 950], 100),
    18: ("Tennessee Avenue", 180,      [14, 70, 200, 550, 750, 950], 100),
    19: ("New York Avenue", 200,       [16, 80, 220, 600, 800, 1000], 100),
    21: ("Kentucky Avenue", 220,       [18, 90, 250, 700, 875, 1050], 150),
    23: ("Indiana Avenue", 220,        [18, 90, 250, 700, 875, 1050], 150),
    24: ("Illinois Avenue", 240,       [20, 100, 300, 750, 925, 1100], 150),
    25: ("B. & O. Railroad", 200,      [25]*6, 0),
    26: ("Atlantic Avenue", 260,       [22, 110, 330, 800, 975, 1150], 150),
    27: ("Ventnor Avenue", 260,        [22, 110, 330, 800, 975, 1150], 150),
    28: ("Water Works", 150,           [8]*6, 0),
    29: ("Marvin Gardens", 280,        [24, 120, 360, 850, 1025, 1200], 150),
    31: ("Pacific Avenue", 300,        [26, 130, 390, 900, 1100, 1275], 200),
    32: ("North Carolina Avenue", 300, [26, 130, 390, 900, 1100, 1275], 200),
    34: ("Pennsylvania Avenue", 320,   [28, 150, 450, 1000, 1200, 1400], 200),
    35: ("Short Line Railroad", 200,   [25]*6, 0),
    37: ("Park Place", 350,            [35, 175, 500, 1100, 1300, 1500], 200),
    39: ("Boardwalk", 400,             [50, 200, 600, 1400, 1700, 2000], 200)
}

# 🎴 Card effects
chance_cards = [None]*7 + [
    "Advance to GO", "Illinois Avenue", "St. Charles Place",
    "Nearest Utility", "Nearest Railroad", "Go Back 3 Spaces",
    "Go to Jail", "Reading Railroad", "Boardwalk"
]
community_chest_cards = [None]*14 + ["Advance to GO", "Go to Jail"]

# 🧪 Simulation for each house level
def simulate_with_house_level(house_level, rounds=2000):
    landings = {i: 0 for i in range(40)}
    position = 0

    for _ in range(rounds):
        roll = random.randint(1, 6) + random.randint(1, 6)
        position = (position + roll) % 40

        # Chance
        if position in [7, 22, 36]:
            card = random.choice(chance_cards)
            if card == "Advance to GO":
                position = 0
            elif card == "Illinois Avenue":
                position = 24
            elif card == "St. Charles Place":
                position = 11
            elif card == "Nearest Utility":
                position = 12 if position < 12 or position > 28 else 28
            elif card == "Nearest Railroad":
                if position < 5 or position >= 35: position = 5
                elif position < 15: position = 15
                elif position < 25: position = 25
                else: position = 35
            elif card == "Go Back 3 Spaces":
                position = (position - 3) % 40
            elif card == "Go to Jail":
                position = 10
            elif card == "Reading Railroad":
                position = 5
            elif card == "Boardwalk":
                position = 39

        # Community Chest
        elif position in [2, 17, 33]:
            card = random.choice(community_chest_cards)
            if card == "Advance to GO":
                position = 0
            elif card == "Go to Jail":
                position = 10

        # Go to Jail space
        if position == 30:
            position = 10

        landings[position] += 1

    # ROI calculation for this level
    results = []
    for space, (name, price, rents, house_cost) in property_data.items():
        visits = landings[space]
        rent = rents[house_level]
        expected_rent = visits * rent
        investment = price + (house_level * house_cost)
        roi = expected_rent / investment if investment else 0
        results.append({
            "Property": name,
            "House Level": house_level,
            "Visits": visits,
            "Rent": rent,
            "Expected Rent": expected_rent,
            "Investment": investment,
            "ROI": round(roi, 4)
        })
    return results

# Run for levels 0 through 5
all_results = []
for level in range(6):
    all_results.extend(simulate_with_house_level(level))

# Output to DataFrame
df = pd.DataFrame(all_results)
df = df.sort_values(by=["House Level", "ROI"], ascending=[True, False])
print(df.to_string(index=False))
