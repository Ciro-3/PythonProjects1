# 1. Defining a New Data Collection (Updated IP list)
target_servers = ["192.168.1.50", "192.168.1.51", "192.168.2.100", "192.168.1.52"]

print("--- Initializing Network Sweep ---")

# 2. Iterating through the new collection
for server in target_servers:
    # 3. Checking for the new '192.168.2' subnet block
    if "192.168.2" in server:
        print(f"Skipping {server}: Isolated Management Subnet.")
    else:
        print(f"Scanning {server}: Connection stable. Port 80 Open.")

print("--- Sweep Sequence Completed ---")
