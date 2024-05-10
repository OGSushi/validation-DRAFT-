#File Existence: Check if the file exists.
#Permissions: Check the file's permissions (read, write, execute).
#File Type: Determine the type of file (text, binary, etc.).
#File Content: Read and analyze the content of the file (search for specific patterns, keywords, etc.).
#Checksums: Calculate and compare checksums (MD5, SHA-1, SHA-256, etc.) to ensure file integrity.
#Metadata: Access and verify file metadata (creation date, modification date, owner, etc.).
#Encoding: Check file encoding (ASCII, UTF-8, etc.) if dealing with text files.
#Line Count: Count the number of lines in a file.
#Syntax Checking: For code files, check syntax correctness (for example, for Python files, you could use py_compile module).
#Data Validation: Validate data within the file against predefined rules or constraints.
#File Structure: Ensure the file adheres to a specific structure or format.
#Signature Verification: Check digital signatures or cryptographic hashes to verify file authenticity.
#File Dependencies: Check if the file depends on other files or resources.
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\


    
    # Metadata: Access and verify file metadata (creation date, modification date, owner, etc.).
    # File Existence: Check if the files you intend to update exist.
    # Permissions: Check the file's permissions (read, write, execute).
    # File Integrity: Verify the integrity of the files using checksums or digital signatures.
    # File Compatibility: Ensure that the files are compatible with the target hardware or software version.
    # File Versioning: Check the version information embedded in the files to determine if an update is necessary.
    # File Dependencies: Verify if the files have any dependencies or prerequisites.
    # Security Verification: Ensure that the files come from trusted sources and are not tampered with or infected by malware.
    


import os
import datetime  
import mimetypes

user_input = input("Validate files?: ") 
if user_input.lower() == "yes":
    print("Files will be validated.")   
    # check_file function performs checks on individual files.
    def check_file(file_path):
    # check: metadata
        metadata = os.stat(file_path)
        creation_time = datetime.datetime.fromtimestamp(metadata.st_ctime)
        print("Creation time:", creation_time)
    
    #check: file existance
        if os.path.exists(file_path):
            print("File exists")
        else:
            print("File does not exist")
    
    # check: print file size
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

    directory_paths = [r"C:\Notepad++\Batch", r"C:\Images"]

# Iterate over each directory path
    for directory_path in directory_paths:
    # Check if the provided path exists
        if not os.path.exists(directory_path):
            print("Directory not found:", directory_path)
        else:
            list_files(directory_path)
            
elif user_input.lower() == "no":
    print("Files will not be validated.")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")

input("Press Enter to close.....")
