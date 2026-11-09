import os

# File Path
main_folder = "your_folder_path_here"  # Replace with your directory path
files = os.listdir(main_folder)

# Folder Names
pdfs_folder = "Pdf Files"

images_folder = "Images"

excel_folder = "Excel Files"

documents_folder = "Documents"

powerpoints_folder = "Powerpoints"

gifs_folder = "Gifs"

videos = "videos"

aduio = "Audio Files"

# List of folder types
folder_types = [pdfs_folder, images_folder, excel_folder, documents_folder, powerpoints_folder, gifs_folder]


# Function to create directories for each file type (if they exist in the folder)
def create_directory(folder_name):
    try:
        os.makedirs(main_folder, exist_ok=True)
        for item in files:
            if os.path.splitext(item)[1] == '.pdf' and folder_name == pdfs_folder:
                folder = os.path.join(main_folder, folder_name)
                return os.mkdir(folder)
            
            elif os.path.splitext(item)[1] in ('.png', '.jpeg', '.jpg') and folder_name == images_folder:
                folder = os.path.join(main_folder, folder_name)
                return os.mkdir(folder)
            
            elif os.path.splitext(item)[1] in ('.xlsx', '.xls', '.gsheet') and folder_name == excel_folder:
                folder = os.path.join(main_folder, folder_name)
                return os.mkdir(folder)
            
            elif os.path.splitext(item)[1] in ('.doc', '.docx', '.gdoc') and folder_name == documents_folder:
                folder = os.path.join(main_folder, folder_name)
                return os.mkdir(folder)
            
            elif os.path.splitext(item)[1] in ('.pptx', '.gslides') and folder_name == powerpoints_folder:
                folder = os.path.join(main_folder, folder_name)
                return os.mkdir(folder)
            
            elif os.path.splitext(item)[1] == '.gif' and folder_name == gifs_folder:
                folder = os.path.join(main_folder, folder_name)
                return os.mkdir(folder)
            
            elif os.path.splitext(item)[1] == '.mp4' and folder_name == videos:
                folder = os.path.join(main_folder, folder_name)
                return os.mkdir(folder)

            elif os.path.splitext(item)[1] == '.mp3' and folder_name == aduio:
                folder = os.path.join(main_folder, folder_name)
                return os.mkdir(folder)
            
    except FileExistsError:
        pass
    except Exception as e:
        print(f"An error occurred while creating the directory {folder_name}: {e}")

# Creating the directories
for folder in folder_types:
    create_directory(folder)     

# To go through each file in the folder and organize them in the corresponding folder
try:
    os.makedirs(main_folder, exist_ok=True)
    for item in files:
        if item.endswith('.pdf'):
            os.rename((main_folder + '\\' + item), (main_folder + '\\' + pdfs_folder + '\\' + item))
        elif item.endswith(('.png', 'jpeg', 'jpg')):
            os.rename((main_folder + '\\' + item), (main_folder + '\\' + images_folder + '\\' + item))
        elif item.endswith(('.xlsx', 'xls', '.gsheet')):
            os.rename((main_folder + '\\' + item), (main_folder + '\\' + excel_folder + '\\' + item))
        elif item.endswith(('doc', 'docx', '.gdoc')):
            os.rename((main_folder + '\\' + item), (main_folder + '\\' + documents_folder + '\\' + item))
        elif item.endswith(('pptx', '.gslides')):
            os.rename((main_folder + '\\' + item), (main_folder + '\\' + powerpoints_folder + '\\' + item))
        elif item.endswith('gif'):
            os.rename((main_folder + '\\' + item), (main_folder + '\\' + gifs_folder + '\\' + item))
        elif item.endswith('mp4'):
            os.rename((main_folder + '\\' + item), (main_folder + '\\' + videos + '\\' + item))
        elif item.endswith('mp3'):
            os.rename((main_folder + '\\' + item), (main_folder + '\\' + aduio + '\\' + item))
except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
except Exception as e:
    print(f"An error occurred while organizing files: {e}")

print("Files Organized Successfully")
