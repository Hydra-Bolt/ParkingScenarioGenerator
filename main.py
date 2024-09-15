import random

from generator import StreetGenerator, VEHICLES


def genStreets(amount, minStreetWidth, maxStreetWidth, minStreetHeight, maxStreetHeight, minTraffic, maxTraffic, saveDir="streets"):

    with open(f"{saveDir}/meta_data.csv", "w") as f:
        f.write("id,width,height,traffic\n")
        for i in range(amount):

            streetWidth = random.randrange(minStreetWidth, maxStreetWidth)
            streetHeight = random.randrange(minStreetHeight, maxStreetHeight)
            traffic = random.uniform(minTraffic, maxTraffic)

            street = StreetGenerator(streetWidth, streetHeight, traffic, VEHICLES)
            street.createStreet().save(f"{saveDir}/{i}.png")

            f.write(f"{i},{streetWidth},{streetHeight:.2f},{traffic:.2f}\n")


    print("Done!")

genStreets(400, 300, 600, 600, 1200, 0.1, 0.6)