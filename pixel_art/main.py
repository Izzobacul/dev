#!./env/bin/python

import sys
import numpy as np
import PIL
from PIL import Image

OUT_SIZE = (64, 64, 4)

def main(input, output="pixel_art.png"):
    image = Image.open(input)
    arr_image = np.array(image)
    arr_pixel_art = np.empty(OUT_SIZE)
    

if __name__ == '__main__':
    main("cheems.png")
    # if len(sys.argv) < 2:
    #     print("The path to the input file is needed.")
    #     exit()
    # elif len(sys.argv) == 2:
    #     main(sys.argv[1])
    # else:
    #     main(sys.argv[1], sys.argv[2])
