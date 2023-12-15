import os
import shutil

def manageFiles(folder_path):
    Folders = ["Images" , "Videos" , "PDFs" , "Others"]

    for folder in Folders:
        if not os.path.exists(os.path.join(folder_path , folder)):
            os.makedirs(os.path.join(folder_path , folder))

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path , filename)


        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lower()


            if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
                shutil.move(file_path, os.path.join(folder_path, 'Images', filename))

            elif file_extension in ['.mp4', '.avi', '.mkv']:
                shutil.move(file_path, os.path.join(folder_path, 'Videos', filename))

            elif file_extension in ['.pdf']:
                shutil.move(file_path, os.path.join(folder_path, 'PDFs', filename))

            else:
                shutil.move(file_path, os.path.join(folder_path, 'Others', filename))  
    
    print("File organization completed!")


if __name__ == "__main__":
    folder_path = input("Enter the path of the folder you want to organize: ")
    manageFiles(folder_path)