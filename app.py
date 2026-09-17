# 1. Initialize an empty list to track discovered nodes
inventory_list = []

print("--- Starting Dynamic Discovery Tool ---")

# 2. Dynamically appending new items to the list
inventory_list.append("192.168.1.50")
inventory_list.append("192.168.2.100")
inventory_list.append("192.168.1.55")

# 3. Verifying the final list contents
print(f"Total Devices Discovered: {len(inventory_list)}")
print(f"Current Inventory: {inventory_list}")

# 4. Processing the dynamically built list
for device in inventory_list:
    if "192.168.2" in device:
        print(f" Alert: Found management node at {device}")
