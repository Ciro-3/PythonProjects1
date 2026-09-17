# 1. System Trackers
developer_name = "Cecil"
server_ip = "10.10.20.10"
allocated_hours = 5  # Change this value later to test different paths

print(f"--- Running Shift Analysis for {developer_name} ---")

# 2. Multi-Tiered Condition using if, elif, and else
if allocated_hours > 8:
    print("Shift Category: Extended Maintenance Window (Requires senior approval).")
elif allocated_hours >= 4:
    print("Shift Category: Standard Operational Window (Normal monitoring active).")
else:
    print("Shift Category: Emergency Patch Window (Rapid deployment rules apply).")
