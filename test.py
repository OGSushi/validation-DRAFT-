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
