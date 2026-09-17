# This removes the entry and saves the IP string into 'removed_ip'
removed_ip = network_inventory.pop("BIQ_Server")
print(f"Removed node address was: {removed_ip}")
