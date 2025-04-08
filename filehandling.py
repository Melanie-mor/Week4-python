# Read from input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Modify the content
modified_content = content.upper()

# Write the modified content to a new file
with open("output.txt", "w") as file:
    file.write(modified_content)

print("File has been read and written successfully.")
