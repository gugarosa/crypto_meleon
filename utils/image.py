import numpy as np
from PIL import Image

import utils.converter as c


def load_image(image_path):
    """Loads an image based on its path.

    Args:
        image_path (str): Image path.

    Returns:
        Array of pixels.

    """

    # Opens the image
    im = Image.open(image_path)

    # Converts to 4-based channels
    im.convert('RGBA')

    # Gathers the image as a pixels' array
    pixels = np.array(im)

    return pixels


def save_image(array, output_path):
    """Saves the image-based array into an output file.

    Args:
        array (np.array): Array of pixels.
        output_path (str): Output path.

    """

    # Creates an Pillow-based image from array
    im = Image.fromarray(array)

    # Saves the image to the output path
    im.save(output_path)


def random_color(seed=0):
    """Generates a random color based on input seed.

    Args:
        seed (int): Seed to be used as generator.
    
    Returns:
        Hexdecimal and a tuple of RGB from the generated color.

    """

    # Defines the numpy seed
    np.random.seed(seed)

    # Generates the RGB
    r, g, b = list((np.random.random(size=3) * 256).astype('int'))

    # Converts the RGB into a hexdecimal value
    hex_color = c.rgb2hex(r, g, b)

    return hex_color, (r, g, b)


def replace_color(array, input_color, output_color):
    """Replaces the array's color with a new given one.

    Args:
        array (np.array): Array of pixels.
        input_color (str): Hexdecimal input color.
        output_color (str): Hexdecimal output color.

    """

    # Gathers the input and output colors as RGB
    r, g, b = c.hex2rgb(input_color)
    r2, g2, b2 = c.hex2rgb(output_color)

    # Gathers each image's array channel
    red_array, green_array, blue_array = array[:, :, 0], array[:, :, 1], array[:, :, 2]

    # Creates a replacement mask
    mask = (red_array == r) & (green_array == g) & (blue_array == b)

    # Replaces the desired colors
    array[:, :, :3][mask] = [r2, g2, b2]
