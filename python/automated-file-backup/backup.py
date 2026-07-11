import os
import shutil
import datetime
import schedule
import time

source_dir = "/home/ash/Pictures"
destination_dir = "/home/ash/Projects/30days/python/automated-file-backup/backups"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists inside : {dest}")

def l():
    copy_folder_to_directory(source_dir, destination_dir)

#adding features for backup for particular day
schedule.every().day.at("11:15").do(l)
