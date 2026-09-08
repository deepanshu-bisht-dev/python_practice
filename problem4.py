import os

directory_path = "/documents"

try:
    items = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    
    for item in items:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
