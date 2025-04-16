#errorhandling.py
filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
    print("File content:\n")
    print(content)

except FileNotFoundError:
    print("Error: That file does not exist.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



#filehandling.py
# Read from input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Modify the content
modified_content = content.upper()

# Write the modified content to a new file
with open("output.txt", "w") as file:
    file.write(modified_content)

print("File has been read and written successfully.")
