from PIL import Image, ImageDraw, ImageFont
import random

PROTUDE = 10
CAR_LENGTH = 100
VEHICLES = {"car": (40, 100), "jeep": (50, 120), "truck": (50, 180)}


def fillLane(image, draw, lane, traffic, vehicles):
    i = 30
    while i < image.height:
        if traffic > random.random():
            vehicle = random.choice(list(vehicles.keys()))
            vw, vh = vehicles[vehicle][0], vehicles[vehicle][1]

            if lane == "left":
                draw.rectangle((PROTUDE + 5, i, PROTUDE + 5 + vw, i + vh), fill="black")
            else:
                draw.rectangle(
                    (
                        image.width - (PROTUDE + 5 + vw),
                        i,
                        image.width - (PROTUDE + 5),
                        i + vh,
                    ),
                    fill="black",
                )

            i += vh + 5
        else:
            i += CAR_LENGTH

    pass


def createStreet(streetWidth, streetHeight, traffic, vehicles):
    image = Image.new("RGB", (streetWidth, streetHeight), color="white")

    draw = ImageDraw.Draw(image)

    # Draw the curbs
    draw.line((PROTUDE, 0, PROTUDE, streetHeight), fill="black")
    draw.line(
        (streetWidth - PROTUDE, 0, streetWidth - PROTUDE, streetHeight), fill="black"
    )

    # Draw the middle lane marking
    draw.line((streetWidth // 2, 0, streetWidth // 2, streetHeight), fill="black")

    # Fill left lane
    fillLane(image, draw, "left", traffic, vehicles)
    # Fill right lane
    fillLane(image, draw, "right", traffic, vehicles)

    return image


street = createStreet(600, 800, 0.5, VEHICLES)

street.show()
street.save("street.png")
