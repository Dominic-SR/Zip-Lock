import zipfile
import os

def create_zip_file(zip_name, files):
    # Create a ZipFile object in write mode
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            if os.path.isfile(file):  # Check if the file exists
                zipf.write(file, os.path.basename(file))  # Add file to the zip
            else:
                print(f"File {file} does not exist.")

# Example usage
files_to_zip = ['test']  # Replace with your file names
create_zip_file('my_files.zip', files_to_zip)

