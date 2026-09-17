# 1. System Trackers
developer_name = "Cecil"
server_ip = "10.10.20.10"
allocated_hours = 9
is_connection_secure = True

print(f"--- Running Diagnostic Check for {developer_name} ---")

# 2. IF Statement evaluating a Boolean
if is_connection_secure:
    print(f"SUCCESS: Secure connection established to {server_ip}.")
else:
    print("WARNING: Unsecured connection! Check firewall rules.")

# 3. IF Statement evaluating Numeric Values
if allocated_hours > 8:
    print("Notice: Extended window active. Acting allowance rules apply.")
else:
    print("Notice: Standard operational hours window.")
