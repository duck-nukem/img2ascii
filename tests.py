import unittest

from img2ascii import match_brightness_to_character


class TestPixelCharacterRelation(unittest.TestCase):
    def test_with_pixel_0(self):
        self.assertEqual(' ', match_brightness_to_character(0))

    def test_with_pixel_below_52(self):
        self.assertEqual(' ', match_brightness_to_character(51))

    def test_with_pixel_between_52_and_101(self):
        self.assertEqual('░', match_brightness_to_character(52))

    def test_with_pixel_between_102_and_152(self):
        self.assertEqual('▒', match_brightness_to_character(151))

    def test_with_pixel_between_153_and_203(self):
        self.assertEqual('▓', match_brightness_to_character(202))

    def test_with_pixel_above_204(self):
        self.assertEqual('█', match_brightness_to_character(255))


if __name__ == '__main__':
    unittest.main()
