import os

folders = [
    "Images",
    "PDFs",
    "Videos",
    "Documents"
]

def create_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        print("folder successfully created")
    else:
        print("folder already exists")

create_folder("ram")