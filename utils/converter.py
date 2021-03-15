"""Module to perform color-hex conversions."""

from PIL import ImageColor


def rgb2hex(r, g, b):
    """Transforms RGB values into a hexdecimal string.

    Args:
        r (int): Red channel.
        g (int): Green channel.
        b (int): Blue channel.

    Returns:
        Hexdecimal string of the corresponding color.

    """

    return f'#{r:02x}{g:02x}{b:02x}'


def hex2rgb(hex_string):
    """Transforms hexdecimal values into a tuple of RGB colors.

    Args:
        hex (string): Hexdecimal color string.

    Returns:
        Tuple of corresponding RGB colors.

    """

    return ImageColor.getcolor(hex_string, 'RGB')
