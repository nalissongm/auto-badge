import os
from time import sleep

from tkinter import *
from tkinter import filedialog as fd

from PIL import Image

from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator


def initialization():
    print("Initializing...")
    sleep(2)


def getImage():
    proceed, service, confirm = False, False, False
    proceed = inquirer.confirm(
        message="Desejar selecionar uma foto para o crachá?", default=True).execute()
    if proceed:
        src_file = fd.askopenfilename()
        print(src_file)

        return src_file

    return None


getImage()

if __name__ == "__main__":
    run = True
    image = ""
    model = Image.open("./models/mold_front.png")
    frameSize = (383.31, 414.51)
    imagePosition_y = 300

    name = ""
    role = ""

    fontSize = 30
    fontFamily = "./fonts/verdana/verdana.ttf"
    fill = "#363A79"
    textPosition_x = "center"
    textPosition_y = 786

    initialization()

    # while run:


# image = Image.open("./models/test_02.jpeg")
# frameSize = (383.31, 414.51)
# mold = Image.open("./models/mold_front.png")

# handleImage = HandleImage()
# imageResized = handleImage.resizeImage(image, frameSize)
# imageCropped = handleImage.cropImage(imageResized, frameSize)
# assemblyImages = handleImage.mergeImages(imageCropped, mold, 300)

# imageWithName = handleImage.addText(assemblyImages, "Glauco Rocha", 30,
#                                     "./fonts/verdana/verdana-bold.ttf", "#363A79", "center", 786)

# imageWithRole = handleImage.addText(imageWithName, "Professor", 28,
#                                     "./fonts/verdana/verdana.ttf", "#363A79", "center", 826)
# imageWithRole.show()
# handleImage.saveImage(assemblyImages, "./save", "test", "pdf")
