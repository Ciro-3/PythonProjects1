import sys

def main():
    # Define system attributes
    developer_name = "Cecil"
    project_status = "Active"
    
    print("====================================")
    print(f" Welcome to Python Coding, {developer_name}! ")
    print("====================================")
    print(f"Project Status : {project_status}")
    print(f"Python Version : {sys.version.split()[0]}")
    print("------------------------------------")
    print("Environment setup verified successfully.")

if __name__ == "__main__":
    main()
