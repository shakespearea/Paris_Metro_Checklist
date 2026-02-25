from file_manager import load_stations, load_states, save_state

# Initialisation
metro = load_stations()
print(f"Found {len(metro)} metro stations.")

# Test 1: Setting
print("Set pasteur to visited")
print(f"Local state {metro['Pasteur']}")
metro["Pasteur"]["visited"] = True
print(f"Local state {metro['Pasteur']}")

# Test 2: Save and recall
print("Save state and check pasteur visited")
save_state(metro)
states = load_states()
print(f"Saved state {states['Pasteur']}")

# Test 3: Saving and retention
print("Unvisit pasteur but verify state remains same")
print(metro["Pasteur"])
metro["Pasteur"]["visited"] = False
print(f"Local state {metro['Pasteur']}")
print(f"Saved state {states['Pasteur']}")


# Test 4: Verify new state saved
print("Save state and reverify")
save_state(metro)
states = load_states()
print(f"Saved state {states['Pasteur']}")
