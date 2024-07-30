import colorgram


def extract_rgb_colors(image, colornumber):
    """"
    Takes (image, no. of colors) as input and returns a list containing rgb tuples values of colors in the image.
    """
    rgb_colors = []
    colors = colorgram.extract(image, colornumber)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors
