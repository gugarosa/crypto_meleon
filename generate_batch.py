import argparse

import utils.image as im
import utils.requester as r

# List of replacement colors
REPLACEMENT_COLORS = ['#265c42', '#3e8948', '#63c74d', '#e4a673', '#e6a875', '#d77641', '#be4b30']


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Generates a batch of randomized CryptoMeleons.')

    parser.add_argument('input_image', help='Input .png image', type=str)

    parser.add_argument('initial_seed', help='Initial seed value', type=int)

    parser.add_argument('batch_size', help='Size of batch', type=int)

    parser.add_argument('-mode', help='Generation mode', type=str, default='monochrome')

    parser.add_argument('-n_colors', help='Number of color replacements', type=int, default=3)

    return parser.parse_args()

if __name__ == '__main__':
    # Gathers the input arguments and its variables
    args = get_arguments()
    input_image = args.input_image
    initial_seed = args.initial_seed
    batch_size = args.batch_size
    mode = args.mode
    n_colors = args.n_colors

    # Iterates from initial seed till the amount of samples
    for i in range(initial_seed, initial_seed + batch_size):
        # Loads the image
        im_array = im.load_image(input_image)

        # Generates a random color based on seed
        hex_color, _ = im.random_color(seed=i)

        # Generates a seed color image
        colors = r.get_color_scheme(hex_color=hex_color, mode=mode, count=n_colors)
        
        # Iterates through the amount of possible colors
        for j, color in enumerate(colors):
            # Replaces the color accordingly
            im.replace_color(im_array, REPLACEMENT_COLORS[j], color)

        # Saves the output image
        im.save_image(im_array, f'{input_image.split(".")[0]}_{i}.png')
