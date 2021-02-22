"""
Mission 3: A Markov Distinction
Nicole Nigro
2/21/21

This program uses a Markov chain to paint a painting where the color used to paint each pixel relies
on the Markov chain probabilities.

Dependencies: random, numpy, PIL
"""

import random
import numpy as np
from PIL import Image

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
        """Paints the entire painting pixel by pixel and then saves it.
            Args:
                current_color (str): the current color being used to paint.
        """
        width = 800
        height = 600
        img = Image.new('RGB', (width,height), (255,255,255)) #using RGB scale for colors

        for y in range(height):
            for x in range(width):
                next_color = self.get_next_color(current_color)
                img.putpixel((x, y), RGB_VALUES[next_color])
                current_color = next_color  
        
        img.save('exampleArt.png') #change the string before .png ('exampleArt') to change the name the painting is saved under

        return img


def main():
    painting_maker = MarkovArtist({
        "color1": {"color1": 0.3, "color2": 0.2, "color3": 0.2, "color4": 0.3},
        "color2": {"color1": 0.6, "color2": 0.2, "color3": 0.1, "color4": 0.1},
        "color3": {"color1": 0.1, "color2": 0.2, "color3": 0.2, "color4": 0.5},
        "color4": {"color1": 0.2, "color2": 0.4, "color3": 0.1, "color4": 0.3}
    })

    colors = ["color1", "color2", "color3", "color4"]

    painting_maker.paint_artwork(random.choice(colors))

if __name__ == "__main__":
    main()