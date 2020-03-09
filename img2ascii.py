import math
import sys
from typing import List

from PIL import Image

_TERMINAL_FONT_ASPECT_RATIO = 0.5
_MAX_PIXEL_VALUE = 255
_CHARSET = [' ', '░', '▒', '▓', '█']


def match_brightness_to_character(pixel: int) -> str:
    charset_steps = int(_MAX_PIXEL_VALUE / len(_CHARSET))
    char_index = 0 if pixel == 0 else math.ceil(pixel / charset_steps) - 1

    return _CHARSET[char_index]


def resize(image: Image, width_px: int) -> Image:
    width, height = image.size
    aspect_ratio = height / width

    new_width = width_px
    new_height = int(aspect_ratio * new_width * _TERMINAL_FONT_ASPECT_RATIO)

    return image.resize((new_width, new_height))


def convert_to_grayscale(image: Image) -> Image:
    return image.convert('L')


def convert_to_ascii(image: Image) -> List[str]:
    brightness_by_datum = image.getdata()

    return [match_brightness_to_character(b) for b in brightness_by_datum]


def print_ascii(ascii_image: List[str], row_width: int) -> None:
    rows = range(0, len(ascii_image), row_width)

    for row_index in rows:
        row_start = row_index
        row_end = row_index + width

        row = ''.join(ascii_image[row_start:row_end])

        print(row)


if __name__ == '__main__':
    image_path = sys.argv[1]
    width = int(sys.argv[2])

    img = convert_to_grayscale(resize(Image.open(image_path), width_px=width))
    img_as_ascii = convert_to_ascii(img)

    print_ascii(img_as_ascii, row_width=width)
