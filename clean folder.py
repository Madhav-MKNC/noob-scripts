import os

def createIfNot(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file,folderName)

files = os.listdir()

createIfNot("Images")
createIfNot("Audios")
createIfNot("Videos")
createIfNot("Docs")

Imgs = [".png",".jpg",".jpeg"]
Images = [file for file in files if os.path.split(file)[1].lower() in Imgs]

Auds = [".mp3",".m4a",".wav",".flv"]
Audios = [file for file in files if os.path.split(file)[1].lower() in Auds]

Videos = [file for file in files if os.path.split(file)[1].lower() == ".mp4"]

Dcs = [".pdf",".doc",".docx",".txt"]
Docs = [file for file in files if os.path.split(file)[1].lower() in Dcs]

move("Images",Images)
move("Audios",Audios)
move("Videos",Videos)
move("Docs",Docs)
