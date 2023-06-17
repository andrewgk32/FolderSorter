#Written by Andrewgk32 on June 17 2023

import os
import shutil
import tkinter as tk
import platform
from tkinter import filedialog, messagebox
from file_extensions import extensions_to_folders

def get_user_documents_folder():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.path.expanduser("~"), "Documents")
    elif system == "Linux":
        return os.path.join(os.path.expanduser("~"), "Documents")
    elif system == "Darwin":  # macOS
        return os.path.join(os.path.expanduser("~"), "Documents")
    else:
        return ""

def get_user_downloads_folder():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Linux":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Darwin":  # macOS
        return os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        return ""

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

        if os.path.exists(destination_path):
            base_name, extension = os.path.splitext(file_name)
            new_name = base_name + "(1)" + extension

            counter = 2
            while os.path.exists(os.path.join(folder_path, new_name)):
                new_name = base_name + f"({counter})" + extension
                counter += 1

            destination_path = os.path.join(folder_path, new_name)

        shutil.move(file_path, destination_path)
        print("Successfully moved " + file_path + " to " + folder_path)
    except Exception as e:
        error_message = str(e)
        excluded_errors = ["No such file or directory"]
        if not any(error in error_message for error in excluded_errors):
            print(f"Error: {e}")

def sort_files():
    allowed_folders = ["Desktop", "Documents", "Downloads", "Music", "Pictures", "Videos"]

    downloads_path = filedialog.askdirectory(title="Select the folder to be sorted", initialdir=get_user_downloads_folder())
    final_dir = filedialog.askdirectory(title="Select the final directory", initialdir=get_user_documents_folder())

    if downloads_path and final_dir:

        folder_name = downloads_path.split("/")[-1]
        if folder_name in allowed_folders:
            downloaded_files = get_files_in_folder(downloads_path)

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
            create_folder_if_not_exists(executables_folder)
            create_folder_if_not_exists(random_folder)

            downloaded_files = get_files_in_folder(downloads_path)

            

            for file_path in downloaded_files:
                file_extension = os.path.splitext(file_path)[1]

                if file_extension in extensions_to_folders:
                    folder_path = extensions_to_folders[file_extension]
                    move_file_to_folder(file_path, folder_path)
                else:
                    move_file_to_folder(file_path, random_folder)
            
            messagebox.showinfo("Sorting Complete", "Files and folders sorted successfully")
        else:
            messagebox.showwarning("Invalid Folder", "Please select a valid folder to sort")
    else:
        messagebox.showwarning("Invalid Path", "Please select valid folders")

# Create the GUI window
window = tk.Tk()
window.title("File Sorter")
window.geometry("500x300")
window.configure(bg="#FF7E30")

# Create a label for the title
title_label = tk.Label(window, text="File Sorter", font=("Arial", 24), bg="#FF7E30", fg="white")
title_label.pack(pady=20)

# Create a button to trigger the file sorting process
sort_button = tk.Button(window, text="Sort Files", font=("Arial", 16), command=sort_files)
sort_button.pack(pady=(0, 30))

# Apply styling to the button
sort_button.configure(bg="#FFA04D", fg="white", activebackground="#FF8742", activeforeground="white", relief="flat")
sort_button.pack(side ="bottom", pady = 10)
# Run the GUI event loop
window.mainloop()
