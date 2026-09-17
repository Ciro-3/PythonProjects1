# STEP 1: Define the dictionary first
network_inventory = {
    "Core_Switch": "192.168.1.50",
    "Access_Switch_01": "192.168.1.55",
    "Firewall_Gateway": "192.168.2.100",
    "BIQ_Server": "10.10.20.10"
}

print(f"Initial Inventory Count: {len(network_inventory)}")

# STEP 2: Use .pop() now that the dictionary officially exists
# This safely removes the key and holds onto its value
removed_ip = network_inventory.pop("BIQ_Server")

print(f"Successfully disconnected from node address: {removed_ip}")
print(f"Updated Inventory Count: {len(network_inventory)}")

# STEP 3: Print remaining operational nodes
print("\n--- Remaining Active Infrastructure ---")
for device, ip in network_inventory.items():
    print(f" -> Active Node: {device} ({ip})")
