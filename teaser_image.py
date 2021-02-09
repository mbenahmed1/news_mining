from PIL import Image


class TeaserImage:
    """A class that the teaser image.

    A class that holds the teaser image and its alternative text.

    Attributes:
        image:          The image data.
        alttext:        Alternative text describing whats in the image.
    """

    def __init__(self, image: Image, alttext: str):
        """Inits TeaserImage class"""

        self.image = image
        self.alttext = alttext

    def show(self):
        """Shows the image with its text."""

        self.image.show()
        print(self.alttext)
