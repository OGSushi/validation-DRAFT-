import os
import datetime  
import mimetypes
import hashlib

user_input = input("Validate files?: ") 
if user_input.lower() == "yes":
    print("Files will be validated.")

    # check: function to calculate checksum
    def calculate_checksum(file_path):
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()

    # Function to check file
    def check_file(file_path):
        # Check metadata
        metadata = os.stat(file_path)
        creation_time = datetime.datetime.fromtimestamp(metadata.st_ctime)
        print("Creation time:", creation_time)

        # check: file existence
        if os.path.exists(file_path):
            print("File exists")
        else:
            print("File does not exist")

        # check: file size
        file_size = os.path.getsize(file_path)
        print("File:", file_path, ", Size:", file_size, "bytes")

        # check: file permissions
        if os.access(file_path, os.R_OK):
            print("Readable")
        if os.access(file_path, os.W_OK):
            print("Writable")
        if os.access(file_path, os.X_OK):
            print("Executable")

        # check: file type
        file_type, _ = mimetypes.guess_type(file_path)
        print("File type:", file_type)

        # check: Calculate checksum
        expected_checksums = {
            "{PATH_TO_FILE}": "{EXPECTED_CHECKSUM}",
            "{PATH_TO_FILE}": "{EXPECTED_CHECKSUM}"
        }
        actual_checksum = calculate_checksum(file_path)
        expected_checksum = expected_checksums.get(file_path)
        if expected_checksum and actual_checksum == expected_checksum:
            print("File integrity verified.")
        else:
            print("Checksums mismatch. File may be corrupted or tampered with.")

    # check: function to list files
    def list_files(directory):
        # Loop through all items in the directory
        for item in os.listdir(directory):
            # Construct full path
            item_path = os.path.join(directory, item)

            # If item is a directory, recursively call list_files
            if os.path.isdir(item_path):
                print("Directory:", item_path)
                list_files(item_path)  # Recursively call list_files
            else:
                # Otherwise, it's a file, perform checks
                check_file(item_path)

    # List of file paths to validate
    file_paths = [r"{PATH_TO_FILE}", r"{PATH_TO_FILE}"]

    # Validate each file
    for file_path in file_paths:
        # Check if the provided path exists
        if not os.path.exists(file_path):
            print("File not found:", file_path)
        else:
            check_file(file_path)
elif user_input.lower() == "no":
    print("Files will not be validated.")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")

input("Press Enter to close.....")  
