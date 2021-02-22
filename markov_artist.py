"""
Mission 3: A Markov Distinction
Nicole Nigro
2/22/21

This program uses a Markov chain to paint a painting where the color used to paint each pixel in 
the background relies on the Markov chain's probabilities, and then uses the same Markov chain
to paint linear art on top.

Dependencies: random, numpy, PIL, itertools
"""

import random
import numpy as np
from PIL import Image, ImageDraw
from itertools import product

RGB_VALUES = {
    "color1": (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 
    "color2": (random.randint(0,255),random.randint(0,255),random.randint(0,255)),
    "color3": (random.randint(0,255),random.randint(0,255),random.randint(0,255)),
    "color4": (random.randint(0,255),random.randint(0,255),random.randint(0,255))
}

class MarkovArtist:
    def __init__(self, transition_matrix):
        """Simulates an artist that relies on a simple Markov chain.
            Args:
                transition_matrix (dict): transition probabilities
        """
        self.transition_matrix = transition_matrix
        self.colors = list(transition_matrix.keys())

    def get_next_color(self, current_color):
        """Decides which color to use next based on the current color.
            Args: 
                current_color (str): the current color being used to paint.
        """
        return np.random.choice(
            self.colors,
            p=[self.transition_matrix[current_color][next_color] for next_color in self.colors]
        )
    
    def paint_artwork(self, current_color):
        """Paints the entire background of the painting pixel by pixel, draws lines on top, and 
        then saves it.
            Args:
                current_color (str): the current color being used to paint.
        """
        width = 800
        height = 600
        img = Image.new('RGB', (width,height), (255,255,255)) #using RGB scale for colors

        #PIXEL BACKGROUND
        for x, y in product(range(width), range(height)):
            next_color = self.get_next_color(current_color)
            img.putpixel((x, y), RGB_VALUES[next_color])
            current_color = next_color
        
        #LINES
        counter = 0
        maximum = random.randint(0,200)
        start_x = random.uniform(0, width)
        start_y = random.uniform(0, height)
        end_x = random.uniform(0, width)
        end_y = random.uniform(0, height)

        while counter < maximum:
            lines = ImageDraw.Draw(img)

            next_color = self.get_next_color(current_color)
            lines.line((start_x, start_y, end_x, end_y), RGB_VALUES[next_color])
            current_color = next_color

            start_x = end_x
            start_y = end_y

            end_x = random.uniform(0, width)
            end_y = random.uniform(0, height)

            counter = counter + 1

        img.show()
        
        img.save('exampleArt.png') #change 'exampleArt' to change the name the painting is saved under

        return img


def main():
    painting_maker1 = MarkovArtist({
        "color1": {"color1": 0.3, "color2": 0.2, "color3": 0.2, "color4": 0.3},
        "color2": {"color1": 0.6, "color2": 0.2, "color3": 0.1, "color4": 0.1},
        "color3": {"color1": 0.1, "color2": 0.2, "color3": 0.2, "color4": 0.5},
        "color4": {"color1": 0.2, "color2": 0.4, "color3": 0.1, "color4": 0.3}    
    })

    painting_maker2 = MarkovArtist({
        "color1": {"color1": 0.5, "color2": 0.1, "color3": 0.2, "color4": 0.2},
        "color2": {"color1": 0.2, "color2": 0.5, "color3": 0.1, "color4": 0.2},
        "color3": {"color1": 0.2, "color2": 0.2, "color3": 0.5, "color4": 0.1},
        "color4": {"color1": 0.1, "color2": 0.2, "color3": 0.2, "color4": 0.5}
    })

    painting_maker3 = MarkovArtist({
        "color1": {"color1": 0.8, "color2": 0.05, "color3": 0.05, "color4": 0.1},
        "color2": {"color1": 0.1, "color2": 0.15, "color3": 0.6, "color4": 0.15},
        "color3": {"color1": 0.7, "color2": 0.24, "color3": 0.03, "color4": 0.03},
        "color4": {"color1": 0.02, "color2": 0.02, "color3": 0.9, "color4": 0.06}
    })

    painting_maker4 = MarkovArtist({
        "color1": {"color1": 0.01, "color2": 0.9, "color3": 0.08, "color4": 0.01},
        "color2": {"color1": 0.03, "color2": 0.9, "color3": 0.01, "color4": 0.06},
        "color3": {"color1": 0.04, "color2": 0.9, "color3": 0.04, "color4": 0.02},
        "color4": {"color1": 0.05, "color2": 0.9, "color3": 0.02, "color4": 0.03}
    })

    colors = ["color1", "color2", "color3", "color4"]
    painters = [painting_maker1, painting_maker2, painting_maker3, painting_maker4]
    current_painter = random.choice(painters)
    start_color = random.choice(colors)

    current_painter.paint_artwork(start_color)

if __name__ == "__main__":
    main()