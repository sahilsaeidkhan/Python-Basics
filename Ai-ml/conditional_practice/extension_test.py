import os

files = ["photo.jpg",
    "resume.pdf",
    "movie.mp4",
    "report.docx" ]

for file in files:
    name,ext = os.path.splitext(file)

    if ext == ".jpg":
        print(f"{file} -> Image")
        
    elif ext == ".pdf":
        print(f"{file} -> PDF")

    elif ext == ".mp4":
        print(f"{file} -> Video")

    elif ext == ".docx":
        print(f"{file} -> Document")