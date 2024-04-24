"""Compstagram: Image Filters in COMP110!"""

__author__ = "YOUR PID HERE"

# The following special variable establishes the front-end GUI in Trailhead
__template__ = "https://24s.comp110.com/static/compstagram/"


# The support code provides scaffolding and machinery for you to focus on filtering
# You should read through `support.py`, especially the Color, Bitmap, and Request
# classes and the Filter protocol. The technical details behind Base64 encoding
# are beyond our concern in this course.
from .support import (
    Color,
    Bitmap,
    Request,
    Base64ImageStr,
    bitmap_to_base64,
    FilterSettings,
)


def main(request: Request) -> Base64ImageStr:
    """Primary endpoint for to the Compstagram backend.

    This function is called each time a new image is loaded, a filter is
    added/removed, or a filter's amount is changed.
    """
    image: Bitmap = request.image

    # TODO: Replace the following if statement with a for-in loop that moves
    # through each Filter in the Request object's filters list & processes the image
    # with it. The following code snippet only applies the first filter added.
    if len(request.filters) > 0:
        image = request.filters[0].process(image)

    # Finally, we convert the Bitmap back to a special data string for the GUI
    return bitmap_to_base64(image)


def get_filter_types() -> list[FilterSettings]:
    """Produces a list of default Filters users can choose from.

    As you add new Filter classes, add additional instances of FilterSettings
    to this list for them to appear in the front-end. The name must match the Filter's
    class name and the amount represents the default intensity of a filter
    when added to the front-end.
    """
    return [
        FilterSettings(name="InvertFilter", amount=1.0),
        # TODO: Enable the BorderFilter on the next line and remove this one
        # FilterSettings(name="BorderFilter", amount=0.05)
    ]


class InvertFilter:
    """
    The InvertFilter's process method is provided to you as an example for
    some ideas on how to implement an image processing algorithm given an input
    image. All of yours will also iterate through each pixel using a nested for loop,
    and modify each pixel by applying logic and/or arithmetic to manipulate it.
    """

    amount: float

    def __init__(self, amount: float):
        self.amount = amount

    def process(self, bitmap: Bitmap) -> Bitmap:
        # We'll work our way through the image one pixel at a time
        for row in range(bitmap.height):
            for col in range(bitmap.width):
                # Get a reference to the Color at row, col and
                # store it in the pixel local variable
                pixel = bitmap.pixels[row][col]

                # The goal of this filter, when applied with an amount of 1.0 or 100%,
                # is for black to become white, red to become cyan, green to become
                # purple, blue to become yellow, etc. Coming in, we know our component
                # values *must* be between 0.0 and 1.0. Thus, we can "invert" a
                # component by subtracting it from 1.0:

                # Original  Formula      Inverted
                # ========  =======      ========
                #   0   ->  255 -   0 -> 255
                #  63   ->  255 -  63 -> 192
                # 127   ->  255 - 127 -> 128
                # 192   ->  255 - 192 -> 63
                # 255   ->  255 - 255 -> 0
                red_inverted = 255 - pixel.red
                green_inverted = 255 - pixel.green
                blue_inverted = 255 - pixel.blue

                # This is Carolina. We're not making filters that are merely "on"
                # or "off" -- nope -- we're making filters that can be applied
                # with a variable amount between 0.0 and 1.0. QR credit FTW.

                # For the invert filter, an `amount` of 0.0 means 0% inverted,
                # 0.5 means 50% inverted, and 1.0 means 100% inverted.

                # The way we'll do this is first figure out how "far away" from our
                # inverted target each component component is via subtraction.
                # Then we'll take that distance and multiply it by the percentage
                # *amount* property of the filter.

                # This will give us a delta we can add to our original color values.
                red_delta = int((red_inverted - pixel.red) * self.amount)
                green_delta = int((green_inverted - pixel.green) * self.amount)
                blue_delta = int((blue_inverted - pixel.blue) * self.amount)

                # Finally, we'll add the delta to each original component value.
                # Since pixel is a reference to a Color object in the Bitmap's
                # 2D list, changing its RGB components influences the Bitmap. Thus, we
                # do not need to assign pixel back to bitmap.pixels[row][col].
                pixel.red += red_delta
                pixel.green += green_delta
                pixel.blue += blue_delta

        return bitmap


class BorderFilter:
    """Produce a border around the Bitmap."""

    amount: float
    color: Color

    def __init__(self, amount: float):
        """Initializes the Border filter with a thickness amount and a default color."""
        self.amount = amount
        # Color is initialized to Carolina Blue
        self.color = Color(75, 156, 211)

    def process(self, bitmap: Bitmap) -> Bitmap:
        """TODO"""
        return bitmap


# TODO: Define the BrightnessFilter Class

# TODO: Define the SaturationFilter Class
