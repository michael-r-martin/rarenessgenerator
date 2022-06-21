from PIL import Image
import random
import glob
import os


class LayerImages:
    layer1Images = []
    layer2Images = []
    layer3Images = []
    layer4Images = []
    layer5Images = []


numberLayers = 5


def get_layer_images(layer):
    image_folder = "images/"

    layer_folder_path = f'{image_folder}{layer}/'

    image_array = []

    for x in os.listdir(layer_folder_path):
        image_path = os.path.basename(x)

        if image_path.__contains__(".png"):
            image = Image.open(image_path)
            image_array.append(image)

    if layer == "layer1Images":
        LayerImages.layer1Images = image_array
    elif layer == "layer2Images":
        LayerImages.layer2Images = image_array
    elif layer == "layer3Images":
        LayerImages.layer3Images = image_array
    elif layer == "layer4Images":
        LayerImages.layer4Images = image_array
    elif layer == "layer5Images":
        LayerImages.layer5Images = image_array


for i in range(1, numberLayers):
    get_layer_images(f'layer{i}Images')

print(f'1 images: {LayerImages.layer1Images}')
print(f'2 images: {LayerImages.layer2Images}')
print(f'3 images: {LayerImages.layer3Images}')

# import folder
# for loop of folder and get all names of images
# append to array
# define number of layers and layer order

whiteBG = Image.open("whiteBG.png")
albaBG = Image.open("albaBG.png")
mintGB = Image.open("mintBG.png")
babyBlueBG = Image.open("babyBlueBG.png")
bgs = [whiteBG, albaBG, mintGB, babyBlueBG]
bgsArrayCount = len(bgs) - 1

whiteSmallCircle = Image.open("whiteSmallCircle.png")
albaSmallCircle = Image.open("albaSmallCircle.png")
mintSmallCircle = Image.open("mintSmallCircle.png")
babyBlueSmallCircle = Image.open("babyBlueSmallCircle.png")
smallCircles = [whiteSmallCircle, albaSmallCircle, mintSmallCircle, babyBlueSmallCircle]
smallCirclesArrayCount = len(smallCircles) - 1

whiteBigCircle = Image.open("whiteBigCircle.png")
albaBigCircle = Image.open("albaBigCircle.png")
mintBigCircle = Image.open("mintBigCircle.png")
babyBlueBigCircle = Image.open("babyBlueBigCircle.png")
bigCircles = [whiteBigCircle, albaBigCircle, mintBigCircle, babyBlueBigCircle]
bigCirclesArrayCount = len(bigCircles) - 1

createdImages = []

i = 1
for i in range(100):

    randomBGInt = random.randint(0, 100)
    if randomBGInt < 90:
        BGInt = 0
    if 90 <= randomBGInt < 95:
        BGInt = 1
    if 95 <= randomBGInt < 97:
        BGInt = 2
    if 97 <= randomBGInt <= 100:
        BGInt = 3

    chosenBG = bgs[BGInt]

    randomSmallCircle = random.randint(0, smallCirclesArrayCount)
    chosenSmallCircle = smallCircles[randomSmallCircle]

    randomBigCircle = random.randint(0, bigCirclesArrayCount)
    chosenBigCircle = bigCircles[randomBigCircle]

    newImage = Image.alpha_composite(chosenBG, chosenBigCircle)

    newImage = Image.alpha_composite(newImage, chosenSmallCircle)

    createdImage = [BGInt, randomSmallCircle, randomBigCircle]

    if createdImage in createdImages:
        pass
    else:
        i += 1
        iString = str(i)

        createdImages.append(createdImage)
        # newImage.save(f"{iString}.png")
