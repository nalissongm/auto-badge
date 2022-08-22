from time import sleep
from turtle import title
from PIL import Image
from other import Other
from tkinter import *
from tkinter import filedialog as fd

# with Image.open('./screenShot.png') as screeShot:
#     (left, upper, right, lower) = (100, 100, 200, 200)

#     im_crop = screeShot.crop((left, upper, right, lower))

#     im_crop.show()


def askdirectory(initialPath, destinationPath):
    print(initialPath, destinationPath)

    if (initialPath != "" and destinationPath == ""):
        print("Para continuar é necessário referenciar a parta para ")
        sleep(3)
        destinationPath = fd.askdirectory(
            title="Selecione a pasta de destino")

    elif (destinationPath != "" and initialPath == ""):
        initialPath = fd.askdirectory(title="Selecione pasta inicial")
        return FALSE

    else:
        print("Selecione a pasta onde estão as imagens para o modelo.")
        sleep(3)
        initialPath = fd.askdirectory(title="Selecione pasta inicial")
        print("Selecione a pasta onde serão salvos os modelos prontos.")
        sleep(3)
        destinationPath = fd.askdirectory(title="Selecione a pasta de destino")

    return [initialPath, destinationPath]


if __name__ == '__main__':
    initialPath = ""
    destinationPath = ""

    while destinationPath == "" or initialPath == "":
        paths = askdirectory(initialPath, destinationPath)

        if (len(paths[0]) > 0):
            initialPath = paths[0]

        if (len(paths[1]) > 0):
            destinationPath = paths[1]

    mypaths = Other(initialPath, destinationPath)

    mypaths.showPaths()
