import git
import tkinter as tk
from tkinter import filedialog
import sys
import os
import zipfile
import shutil

def clone_github_repo(repo_url, destination_path):
    try:
        git.Repo.clone_from(repo_url, destination_path)
        print("SurfSage has been downloaded/updated successfully!")
    except git.exc.GitCommandError as e:
        print("Error downloading/updating:", e)

def remove_git_files(destination_path):
    try:
        os.remove(os.path.join(destination_path, ".gitattributes"))
        os.remove(os.path.join(destination_path, "README.md"))
        print(".gitattributes and README.md have been removed from the destination folder.")
    except FileNotFoundError:
        print("Files not found.")
    except Exception as e:
        print("Error occurred while removing files:", e)

def extract_build_zip(destination_path):
    try:
        with zipfile.ZipFile(os.path.join(destination_path, "build.zip"), 'r') as zip_ref:
            zip_ref.extractall(destination_path)
        print("build.zip has been extracted to the destination folder.")
    except Exception as e:
        print("Error occurred while extracting build.zip:", e)

def delete_build_zip(destination_path):
    try:
        os.remove(os.path.join(destination_path, "build.zip"))
        print("build.zip has been deleted.")
    except Exception as e:
        print("Error occurred while deleting build.zip:", e)

def select_folder():
    folder_path = filedialog.askdirectory(title="SurfSage Install")
    if folder_path:
        clone_github_repo(github_repo_url, folder_path)
        remove_git_files(folder_path)
        extract_build_zip(folder_path)
        delete_build_zip(folder_path)
        root.destroy()

def prompt_yes_no(prompt): 
    while True:
        response = input(prompt + " (Yes/No): ").strip().lower()
        if response == 'yes':
            return True
        elif response == 'no':
            return False
        else:
            print("Invalid input. Please respond with 'Yes' or 'No'.")

if __name__ == "__main__":
    github_repo_url = "https://github.com/DieserGhost/SurfSageV1.git"

    root = tk.Tk()
    root.withdraw()  

    if prompt_yes_no("Do you want to download/update SurfSage?"):
        select_folder()
