import argparse

import utils.image as i


def get_arguments():
    """Gets arguments from the command line.

    Returns:
        A parser with the input arguments.

    """

    parser = argparse.ArgumentParser(usage='Converts the desired colors from a CryptoMeleon.')

    parser.add_argument('input_image', help='Input .png image', type=str)

    parser.add_argument('output_image', help='Output .png image', type=str)

    parser.add_argument('-inner_body', help='Inner body color replacement', type=str, default='#63c74d')

    parser.add_argument('-body', help='Body color replacement', type=str, default='#3e8948')

    parser.add_argument('-lower_body', help='Lower body color replacement', type=str, default='#265c42')

    parser.add_argument('-stick', help='Stick color replacement', type=str, default='#e4a673')

    parser.add_argument('-highlight_body', help='Highlight body color replacement', type=str, default='#e6a875')

    parser.add_argument('-back', help='Back color replacement', type=str, default='#d77641')

    parser.add_argument('-belly', help='Belly color replacement', type=str, default='#be4b30')

    return parser.parse_args()


if __name__ == '__main__':
    # Gathers the input arguments and its main variables
    args = get_arguments()
    input_image = args.input_image
    output_image = args.output_image

    # Gathers the color replacements
    inner_body = args.inner_body
    body = args.body
    lower_body = args.lower_body
    stick = args.stick
    highlight_body = args.highlight_body
    back = args.back
    belly = args.belly

    # Loads the image
    im_array = i.load_image(input_image)

    # Performs the color replacement
    i.replace_color(im_array, '#63c74d', inner_body)
    i.replace_color(im_array, '#3e8948', body)
    i.replace_color(im_array, '#265c42', lower_body)
    i.replace_color(im_array, '#e4a673', stick)
    i.replace_color(im_array, '#e6a875', highlight_body)
    i.replace_color(im_array, '#d77641', back)
    i.replace_color(im_array, '#be4b30', belly)

    # Saves the output image
    i.save_image(im_array, output_image)
