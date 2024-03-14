import os
from file_organizer import organize_files
def main():
    current_directory = os.getcwd()
    new_folder_name = "Destination"
    new_folder_path = os.path.join(current_directory, new_folder_name)
    organize_files(current_directory,new_folder_path)

if __name__ == "__main__":
    main()
