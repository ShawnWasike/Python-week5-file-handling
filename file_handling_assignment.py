# file_handling_assignment.py

# File Creation
try:
    # Create a new file and write some lines of text
    with open('my_file.txt', 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("Here is the second line with a number: 42\n")
        file.write("And this is the third line with more text.\n")
    print("File created and initial content written successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred during file creation: {e}")

# File Reading and Display
try:
    # Read the content of the file
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nFile content:")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred during file reading: {e}")

# File Appending
try:
    # Append additional lines to the file
    with open('my_file.txt', 'a') as file:
        file.write("This is an additional line 1.\n")
        file.write("This is an additional line 2.\n")
        file.write("This is an additional line 3.\n")
    print("\nAdditional lines appended successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred during file appending: {e}")

# Display updated file content
try:
    # Read the updated content of the file
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nUpdated file content:")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred during file reading: {e}")

finally:
    print("\nFile handling operations completed.")
