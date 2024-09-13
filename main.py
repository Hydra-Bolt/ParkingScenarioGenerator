from PIL import Image, ImageDraw
import random
# Constants for the curb
PROTRUDE = 10  # Width of the curb
CURB_SEGMENT_HEIGHT = 20  # Height of each yellow/black curb segment
CAR_LENGTH = 100
VEHICLES = {"car": (80, 200), "jeep": (90, 220), "truck": (100, 280)}

def createCurbs(draw, streetWidth, streetHeight, curbWidth, segmentHeight, colors=("yellow", "black")):
    current_y = 0
    color_index = 0

    # Draw alternating segments on the left curb
    while current_y < streetHeight:
        draw.rectangle(
            (0, current_y, curbWidth, min(current_y + segmentHeight, streetHeight)),
            fill=colors[color_index]
        )
        color_index = (color_index + 1) % 2  # Alternate between colors
        current_y += segmentHeight

    # Reset variables for the right curb
    current_y = 0
    color_index = 0

    # Draw alternating segments on the right curb
    while current_y < streetHeight:
        draw.rectangle(
            (streetWidth - curbWidth, current_y, streetWidth, min(current_y + segmentHeight, streetHeight)),
            fill=colors[color_index]
        )
        color_index = (color_index + 1) % 2  # Alternate between colors
        current_y += segmentHeight

def fillLane(image, draw, lane, traffic, vehicles):
    current_y = 30
    while current_y < image.height:
        psNoise = random.randint(0, 40)
        if traffic > random.random():
            vehicle = random.choice(list(vehicles.keys()))
            vw, vh = vehicles[vehicle][0], vehicles[vehicle][1]
            paNoise = random.randint(0, 5)
            if lane == "left":

                draw.polygon(
                    [
                        (PROTRUDE + 5 + paNoise, current_y),
                        (PROTRUDE + 5 + paNoise + vw, current_y),
                        (PROTRUDE + 5 - paNoise + vw, current_y + vh),
                        (PROTRUDE + 5 - paNoise, current_y + vh),
                    ],
                    fill="black",
                )
            else:
                draw.polygon(
                    [
                        (image.width - (PROTRUDE + 5 + vw + paNoise), current_y),
                        (image.width - (PROTRUDE + 5 + paNoise), current_y),
                        (image.width - (PROTRUDE + 5 - paNoise), current_y + vh),
                        (image.width - (PROTRUDE + 5 + vw - paNoise), current_y + vh),
                    ],
                    fill="black",
                )
                

            current_y += vh + 5 + psNoise
        else:
            current_y += CAR_LENGTH + psNoise

def createStreet(streetWidth, streetHeight, traffic, vehicles):
    image = Image.new("RGB", (streetWidth, streetHeight), color="white")
    draw = ImageDraw.Draw(image)

    # Draw the curbs with alternating yellow and black
    createCurbs(draw, streetWidth, streetHeight, PROTRUDE, CURB_SEGMENT_HEIGHT)

    # Draw the middle lane marking
    draw.line((streetWidth // 2, 0, streetWidth // 2, streetHeight), fill="black")

    # Fill left lane
    fillLane(image, draw, "left", traffic, vehicles)
    # Fill right lane
    fillLane(image, draw, "right", traffic, vehicles)

    return image

# Example usage
streetWidth = 600
streetHeight = 800

street_image = createStreet(streetWidth, streetHeight, 0.7, VEHICLES)
street_image.show()
