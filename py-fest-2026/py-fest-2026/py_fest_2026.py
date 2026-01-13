print("\n--- PyFest 2026 Stage Manager ---")
print("1. View Lineup & Total Time")
print("2. Add a New Band")
print("3. Move First Band to End (Late Arrival)")
print("4. Remove a Band by Name")
print("5. Move Band to Specific Position")     # New Feature!
print("6. Exit")

choice = input("\nSelect an option (1-6): ").strip()

if choice == "1":
    print("\n--- Current Lineup ---")
    total_time = 0
    for i, (name, genre, duration) in enumerate(lineup, 1):
        print(f"{i}. {name} ({genre}) - {duration} mins")
total_time += duration
print(f"\nTotal Festival Duration: {total_time} minutes")