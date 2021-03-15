import requests


def get_color_scheme(hex_color='', rgb_color='', mode='monochrome', count=5):
    """Gets a scheme of color from TheColorAPI.

    Args:
        hex_color (string): Hexdecimal color.
        rgb_color (string): RGB color.
        mode (string): Mode to generate the scheme (monochrome, analogic, analogic-complement).
        count (int): Amount of colors to be generated.

    Returns:
        A list holding the color scheme.

    """

    # Creates the request payload
    payload = {
        'hex': hex_color,
        'rgb': rgb_color,
        'mode': mode,
        'count': count        
    }

    # Performs the request
    r = requests.get(f'https://www.thecolorapi.com/scheme', params=payload)

    # Parses the color-scheme and saves the hex-based colors
    colors = [c['hex']['value'] for c in r.json()['colors']]

    # Outputs back the color-scheme
    return colors
