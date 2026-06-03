import shutil

try:
    shutil.copy("sample.txt", "backup_sample.txt")

    with open("backup.log", "a") as log:
        log.write("sample.txt copied\n")

    print("Backup Completed")

except FileNotFoundError:
    print("File Not Found")

except PermissionError:
    print("Permission Denied")