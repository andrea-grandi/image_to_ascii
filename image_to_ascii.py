
"""
First of all i have to open the image file
Then i have to convert the image to grayscale
Then i have to resize the image to a smaller size
Then i have to convert the image to ascii
Finally i have to print the ascii image
"""

import numpy as np
from PIL import Image


def image_to_ascii():
    # Open the image
    image = Image.open('mona_lisa.jpg')

    # Then convert the image in grayscale
    image = image.convert('L')

    # Resize the image to a smaller size
    image = image.resize((100, 100))

    # Convert the image to ascii
    ascii_image = np.array(image)

    # Define the ascii characters
    ascii_chars = ' .:-=+*#%@'

    # Convert the image to ascii
    out = []
    for row in ascii_image:
        line = [ascii_chars[pixel // 32] for pixel in row]
        out.append(line)
    
    # Save the ascii image to a file
    with open('ascii_image.txt', 'w') as file:
        for row in out:
            file.write(''.join(row) + '\n')


if __name__ == '__main__':
    image_to_ascii()
