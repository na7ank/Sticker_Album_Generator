import os
import random as rd
from PIL import Image

# Images Layers
layer_1 = os.listdir("layer 1 directory")
layer_2 = os.listdir("layer 2 directory")
layer_3 = os.listdir("layer 3 directory")
layer_4 = os.listdir("layer 4 directory")
layer_5 = os.listdir("layer 5 directory")

def generate_combination(runs):
    run = 0
    for i in range(0, runs):
        bg = Image.open(r"skyes\%s"%(rd.choice(layer_1)) )
        planet = Image.open(r"planets\%s"%(rd.choice(layer_2)) )
        obj = Image.open(r"objetos\%s"%(rd.choice(layer_3)) )
        land = Image.open(r"lands\%s"%(rd.choice(layer_4)) )
        man = Image.open(r"spaceman\%s"%(rd.choice(layer_5)) )

        bg.paste(obj, (0, 0), mask = obj)
        bg.paste(planet, (0, 0), mask = planet)
        bg.paste(land, (0, 0), mask = land)
        bg.paste(man, (0, 0), mask = man)

        bg.save("collection/%d.png"%run)

        run += 1

# Create Images
generate_combination(10)
