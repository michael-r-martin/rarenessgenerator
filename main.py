from PIL import Image
import random
import glob
import sys


class LayerImages:
    layer1Images = []
    layer2Images = []
    layer3Images = []
    layer4Images = []
    layer5Images = []


numberLayers = 5


def get_layer_images(layer):
    image_array = []

    for x in glob.glob(f'images/{layer}/*.png'):

        image = Image.open(x)
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
        print("running")


for i in range(1, numberLayers+1):
    get_layer_images(f'layer{i}Images')

print(f'1 images: {LayerImages.layer1Images}')
print(f'2 images: {LayerImages.layer2Images}')
print(f'3 images: {LayerImages.layer3Images}')
print(f'4 images: {LayerImages.layer4Images}')
print(f'5 images: {LayerImages.layer5Images}')

# import folder
# for loop of folder and get all names of images
# append to array
# define number of layers and layer order

createdImages = []

i = 1
for i in range(100):

    if numberLayers < 1:
        sys.exit("no layer 1")

    randomLayer1Int = random.randint(0, 100)

    if randomLayer1Int < 80:
        randomLayer1Int = 0
    if 80 <= randomLayer1Int < 90:
        randomLayer1Int = 1
    if 90 <= randomLayer1Int < 95:
        randomLayer1Int = 2
    if 95 <= randomLayer1Int < 97:
        randomLayer1Int = 3
    if 97 <= randomLayer1Int <= 100:
        randomLayer1Int = 4

    if numberLayers < 2:
        sys.exit("no layer 2")

    randomLayer2Int = random.randint(0, 100)

    if randomLayer2Int < 80:
        randomLayer2Int = 0
    if 80 <= randomLayer2Int < 90:
        randomLayer2Int = 1
    if 90 <= randomLayer2Int < 95:
        randomLayer2Int = 2
    if 95 <= randomLayer2Int < 97:
        randomLayer2Int = 3
    if 97 <= randomLayer2Int <= 100:
        randomLayer2Int = 4

    if numberLayers < 3:
        sys.exit("no layer 3")

    randomLayer3Int = random.randint(0, 100)

    if randomLayer3Int < 80:
        randomLayer3Int = 0
    if 80 <= randomLayer3Int < 90:
        randomLayer3Int = 1
    if 90 <= randomLayer3Int < 95:
        randomLayer3Int = 2
    if 95 <= randomLayer3Int < 97:
        randomLayer3Int = 3
    if 97 <= randomLayer3Int <= 100:
        randomLayer3Int = 4

    if numberLayers < 4:
        sys.exit("no layer 4")

    randomLayer4Int = random.randint(0, 100)

    if randomLayer4Int < 80:
        randomLayer4Int = 0
    if 80 <= randomLayer4Int < 90:
        randomLayer4Int = 1
    if 90 <= randomLayer4Int < 95:
        randomLayer4Int = 2
    if 95 <= randomLayer4Int < 97:
        randomLayer4Int = 3
    if 97 <= randomLayer4Int <= 100:
        randomLayer4Int = 4

    if numberLayers < 5:
        sys.exit("no layer 5")

    randomLayer5Int = random.randint(0, 100)

    if randomLayer5Int < 80:
        randomLayer5Int = 0
    if 80 <= randomLayer5Int < 90:
        randomLayer5Int = 1
    if 90 <= randomLayer5Int < 95:
        randomLayer5Int = 2
    if 95 <= randomLayer5Int < 97:
        randomLayer5Int = 3
    if 97 <= randomLayer5Int <= 100:
        randomLayer5Int = 4

    chosenLayer1Image = LayerImages.layer1Images[randomLayer1Int]
    chosenLayer2Image = LayerImages.layer2Images[randomLayer2Int]
    chosenLayer3Image = LayerImages.layer3Images[randomLayer3Int]
    chosenLayer4Image = LayerImages.layer4Images[randomLayer4Int]
    chosenLayer5Image = LayerImages.layer5Images[randomLayer5Int]

    firstComposite = Image.alpha_composite(chosenLayer1Image, chosenLayer2Image)

    secondComposite = Image.alpha_composite(firstComposite, chosenLayer3Image)

    thirdComposite = Image.alpha_composite(secondComposite, chosenLayer4Image)

    fourthComposite = Image.alpha_composite(thirdComposite, chosenLayer5Image)

    createdImage = [randomLayer1Int, randomLayer2Int, randomLayer3Int, randomLayer4Int, randomLayer5Int]

    if createdImage in createdImages:
        pass
    else:
        i += 1
        iString = str(i)

        createdImages.append(createdImage)
        fourthComposite.save(f"{iString}.png")
