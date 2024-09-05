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
print("""
      
                                                                                                                                                                                                   
+:+:+:+:+:+:++:+:+:+:+:+:++:+:+:+:+:+:++:+:+:+:+:+:++:+:+:+:+:+:
                                                                                                                                                                                                   
+#+#+#+#+#+#++#+#+#+#+#+#++#+#+#+#+#+#++#+#+#+#+#+#++#+#+#+#+#+#
      

      
__  /_ _|  _ \   |      _ \   ___| |  / ____|  _ \ 
   /   |  |   |  |     |   | |     ' /  __|   |   |
  /    |  ___/   |     |   | |     . \  |     __ < 
____|___|_|     _____|\___/ \____|_|\_\_____|_| \_\



                                                                                                                                                                                                   
+:+:+:+:+:+:++:+:+:+:+:+:++:+:+:+:+:+:++:+:+:+:+:+:++:+:+:+:+:+:
                                                                                                                                                                                                   
+#+#+#+#+#+#++#+#+#+#+#+#++#+#+#+#+#+#++#+#+#+#+#+#++#+#+#+#+#+#
      


 _____         _ _     _   _        _____     _   _             
|  _  |_ _ ___|_| |___| |_| |___   |     |___| |_|_|___ ___ ___ 
|     | | | .'| | | .'| . | | -_|  |  |  | . |  _| | . |   |_ -|
|__|__|\_/|__,|_|_|__,|___|_|___|  |_____|  _|_| |_|___|_|_|___|      


1. Files to Zip - zip

2. Zip to Files - unzip
      
3. Lock Zip - LockZip
      
4. Unlock Zip - UnlockZip
      

      
""")         

options = input("Select a Options :")
if options == 1:
    files=[]
    getFiles=input("Enter the files: ")
    splitFiles=getFiles.split()
    for x in splitFiles:
        files.append(x)
        files_to_zip = files  # Replace with your file names
        zipFileName = input("Enter the zip file name: ")
        create_zip_file(zipFileName+'.zip', files_to_zip)
elif options == 2:
    print("else")

