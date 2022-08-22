import math
from turtle import position

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class HandleImage:
    # def __init__(self, image, frameSize):
    #     self.image = image
    #     self.frame = frameSize
    def addText(self, image, text, fontSize, fontFamily, fill, position_x, position_y):
        imageDraw = ImageDraw.Draw(image)

        myFont = ImageFont.truetype(fontFamily, fontSize)
        w, h = myFont.getsize(text)

        axis_x = position_x == "center" and (
            image.size[0] - w) / 2 or position_x
        axis_y = position_y == "center" and (
            image.size[1] - h) / 2 or position_y

        imageDraw.text((math.ceil(axis_x), math.ceil(axis_y)),
                       text=text, fill=fill, font=myFont)

        return image

    def saveImage(self, image, destinationPath, filename, formatInput):
        format = formatInput.lower()
        fullPath = f"{destinationPath}/{filename}.{format}"

        if format != "pdf":
            image.save(fullPath, save_all=True)

        if format == "pdf":
            imageConverted = image.convert("RGB")
            imageConverted.save(fullPath, save_all=True)

        return fullPath

    def mergeImages(self, image, mold, positionY):
        coordinates = self.calcPosition(image.size, mold.size, positionY)

        mold.paste(image, coordinates)

        return mold

    def cropImage(self, image, frameSize):
        sizeToCrop = self.calcCrop(image.size, frameSize)

        imageCropped = image.crop(sizeToCrop)

        return imageCropped

    def resizeImage(self, image, frameSize):
        size = self.calcResize(image.size, frameSize)

        imageResized = image.resize(size)

        return imageResized

    def calcResize(self, imageSize, modelSize):
        widthImage = imageSize[0]
        heightImage = imageSize[1]

        widthModel = modelSize[0]
        heightModel = modelSize[1]

        diffW = widthImage - widthModel

        if diffW >= 0:
            reductionPercent = (100 * widthModel) / widthImage

            reducedImageHeight = math.ceil(
                (heightImage * reductionPercent) / 100)

            if reducedImageHeight < heightModel:
                valueOfDiff = heightModel - reducedImageHeight

                increasedWidth = math.ceil(widthModel + valueOfDiff)
                increasedHeight = math.ceil(reducedImageHeight + valueOfDiff)

                return (increasedWidth, increasedHeight)

            return (math.ceil(widthModel), math.ceil(reducedImageHeight))

    def calcCrop(self, imageSize, frameSize):

        widthFrame = math.ceil(frameSize[0])
        heightFrame = math.ceil(frameSize[1])

        widthImage = imageSize[0]
        heightImage = imageSize[1]

        cropWidth = math.ceil((widthImage - widthFrame) / 2)
        cropHeight = heightImage - heightFrame

        leftCrop = cropWidth
        rightCrop = widthImage - cropWidth
        upCrop = cropHeight / 2
        bottomCrop = heightImage - cropHeight / 2

        return (leftCrop, upCrop, rightCrop, bottomCrop)

    def calcPosition(self, imageSize, moldSize, positionY):
        widthMold = moldSize[0]

        widthImage = imageSize[0]

        position_x = math.floor((widthMold - widthImage) / 2) + 3
        position_y = positionY

        return (position_x, position_y)


image = Image.open("./models/test_01.jpeg")
frameSize = (383.31, 414.51)
mold = Image.open("./models/mold_front.png")

handleImage = HandleImage()
imageResized = handleImage.resizeImage(image, frameSize)
imageCropped = handleImage.cropImage(imageResized, frameSize)
assemblyImages = handleImage.mergeImages(imageCropped, mold, 300)

imageWithName = handleImage.addText(assemblyImages, "Rosangela da Silva", 30,
                                    "./fonts/verdana/verdana-bold.ttf", "#363A79", "center", 786)

imageWithRole = handleImage.addText(imageWithName, "Professora", 28,
                                    "./fonts/verdana/verdana.ttf", "#363A79", "center", 826)

handleImage.saveImage(imageWithRole, "./save", "test", "png")
