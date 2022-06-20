from PIL import Image
import random

whiteBG = Image.open("whiteBG.png")
albaBG = Image.open("albaBG.png")
mintGB = Image.open("mintBG.png")
babyBlueBG = Image.open("babyBlueBG.png")
bgs = [whiteBG, albaBG, mintGB, babyBlueBG]
bgsArrayCount = len(bgs)-1

whiteSmallCircle = Image.open("whiteSmallCircle.png")
albaSmallCircle = Image.open("albaSmallCircle.png")
mintSmallCircle = Image.open("mintSmallCircle.png")
babyBlueSmallCircle = Image.open("babyBlueSmallCircle.png")
smallCircles = [whiteSmallCircle, albaSmallCircle, mintSmallCircle, babyBlueSmallCircle]
smallCirclesArrayCount = len(smallCircles)-1

whiteBigCircle = Image.open("whiteBigCircle.png")
albaBigCircle = Image.open("albaBigCircle.png")
mintBigCircle = Image.open("mintBigCircle.png")
babyBlueBigCircle = Image.open("babyBlueBigCircle.png")
bigCircles = [whiteBigCircle, albaBigCircle, mintBigCircle, babyBlueBigCircle]
bigCirclesArrayCount = len(bigCircles)-1

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
        newImage.save(f"{iString}.png")