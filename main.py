import os 
import shutil
import time

def get_files_in_folder(folder_path):
    files = []
    for entry in os.scandir(folder_path):
        if entry.is_file():
            files.append(entry.path)        
        if entry.is_dir():
            files.append(entry.path)
    return files

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move_file_to_folder(file_path, folder_path):
    try:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(folder_path, file_name)

        # Check if the file already exists in the destination folder
        if os.path.exists(destination_path):
            base_name, extension = os.path.splitext(file_name)
            new_name = base_name + "(1)" + extension

            counter = 2
            while os.path.exists(os.path.join(folder_path, new_name)):
                new_name = base_name + f"({counter})" + extension
                counter += 1

            destination_path = os.path.join(folder_path, new_name)
        sleep_value = 0.1
        time.sleep(sleep_value)
        shutil.move(file_path, destination_path)
        print("Successfully moved" + file_path + "to " + folder_path)
    except Exception as e:
        error_message = str(e)
        excluded_errors = ["No such file or directory"]
        if not any (error in error_message for error in excluded_errors):
            print(f"Error: {e}")
try:
    downloads_path = input("Enter the path to the folder to be sorted: ")
    downloaded_files = get_files_in_folder(downloads_path)
    final_dir = input("Enter the Path of the final Directory: ")
    print(downloaded_files)
except Exception as e:
    print(f"Error: {e}")

user_folder_name = os.path.basename(os.path.normpath(downloads_path))

doc_folder = os.path.join(final_dir, user_folder_name + " Assorted Documents")
code_folder = os.path.join(final_dir, user_folder_name + " Code")
folders_folder = os.path.join(final_dir, user_folder_name + " Folders & Zips")
data_folder = os.path.join(final_dir, user_folder_name + " Data")
images_folder = os.path.join(final_dir, user_folder_name + " Images")
videos_folder = os.path.join(final_dir, user_folder_name + " Videos + Audio") 
executables_folder = os.path.join(final_dir, user_folder_name + " Executables")
random_folder = os.path.join(final_dir, user_folder_name + " Random Files")

create_folder_if_not_exists(doc_folder)
create_folder_if_not_exists(code_folder)
create_folder_if_not_exists(folders_folder)
create_folder_if_not_exists(data_folder)
create_folder_if_not_exists(images_folder)
create_folder_if_not_exists(videos_folder)
create_folder_if_not_exists(random_folder)

downloaded_files = get_files_in_folder(downloads_path)

extensions_to_folders = {
    ".cpp" : code_folder,
    ".java": code_folder,
    ".js": code_folder,
    ".css": code_folder,
    ".h": code_folder,
    ".php": code_folder,
    ".sql": code_folder,
    ".r": code_folder,
    ".mat": code_folder,
    ".py": code_folder,
    ".ipynb": code_folder,
    ".c": code_folder,
    ".hmtl": code_folder,
    ".pdf": doc_folder,
    ".doc": doc_folder,
    ".docx": doc_folder,
    ".ppt": doc_folder,
    ".xls": doc_folder,
    ".pptx": doc_folder,
    ".txt": doc_folder,
    ".md": doc_folder,
    ".json": data_folder,
    ".csv": data_folder,
    ".xml": data_folder,
    ".xlsx": data_folder,
    ".jpg": images_folder,
    ".png": images_folder,
    ".jpeg": images_folder,
    ".gif": images_folder,
    ".bmp": images_folder,
    ".raw": images_folder,
    ".svg": images_folder,
    ".ico": images_folder,
    ".webp": images_folder,
    ".tiff": images_folder,
    ".tif": images_folder,
    ".mp4": videos_folder,
    ".mov": videos_folder,
    ".avi": videos_folder,
    ".mkv": videos_folder,
    ".wmv": videos_folder,
    ".flv": videos_folder,
    ".m4v": videos_folder,
    ".mpg": videos_folder,
    ".webm": videos_folder,
    ".mp3": videos_folder,
    ".wav": videos_folder,
    "m4a": videos_folder,
    ".aiff": videos_folder,
    ".mid": videos_folder,
    ".midi": videos_folder,
    ".flac": videos_folder,
    ".wma": videos_folder,
    ".zip": folders_folder,
    ".app": executables_folder,
    ".sh": executables_folder,
    ".exe": executables_folder,
    ".deb": executables_folder,
    ".jar": executables_folder,
    ".out": executables_folder,
    ".run": executables_folder,
    ".msi": executables_folder
}

for file_path in downloaded_files:
    file_extension = os.path.splitext(file_path)[1]

    if file_extension in extensions_to_folders:
        folder_path = extensions_to_folders[file_extension]
        move_file_to_folder(file_path, folder_path)
    else:
        move_file_to_folder(file_path, random_folder)
for folder_path in downloaded_files:
    move_file_to_folder(folder_path, folders_folder)
print("Files and folders sorted successfully")