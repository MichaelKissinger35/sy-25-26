# The initial lineup
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]

# 1. Add the headliner
headliner = ("The Byte Beats", "Synthwave", 90)
lineup.append(headliner)

# 2. Emergency Swap: Move the first band to the end
late_band = lineup.pop(0)
lineup.append(late_band)

# 3. Security Check: Remove "The Pythonistas" by value
for artist in lineup:
    if artist[0] == "The Pythonistas":
        lineup.remove(artist)
        break

# 4. Calculate Total Time
total_minutes = 0
for name, genre, duration in lineup:
    total_minutes += duration

print("Final Lineup:", lineup)
print("Total Festival Duration:", total_minutes, "minutes")