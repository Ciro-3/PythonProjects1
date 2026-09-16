# 1. An empty list (like a dynamic database array) to store names
user_log = []

print("--- System Registration Portal ---")

# 2. A 'While' Loop to keep the program running until we tell it to stop
while True:
    print("\n[1] Register New Profile")
    print("[2] View Registered Profiles")
    print("[3] Exit")
    
    choice = input("Select an option (1-3): ")
    
    if choice == "1":
        name = input("Enter user name: ")
        birth_year = input("Enter birth year: ")
        
        # Calculate age dynamically
        age = 2026 - int(birth_year)
        
        # Save a clean text summary into our list box
        profile_details = name + " (Age: " + str(age) + ")"
        user_log.append(profile_details)
        print("✔ Profile successfully saved!")
        
    elif choice == "2":
        print("\n--- Current Profiles in Memory ---")
        if not user_log:
            print("No profiles recorded yet.")
        else:
            # A 'For' Loop to print every single item saved in our list
            for profile in user_log:
                print("- " + profile)
                
    elif choice == "3":
        print("Shutting down portal. Goodbye!")
        break # This breaks the loop and closes the program safely
        
    else:
        print("❌ Invalid selection. Please choose 1, 2, or 3.")
        git add app.py
