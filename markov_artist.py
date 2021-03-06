"""
Le Pixelkov
Mission 3: A Markov Distinction
Nicole Nigro
2/24/21

This program uses Markov chains to paint a painting where the color used to paint each pixel and 
line relies on one Markov chain's probabilities while the layer being painted (lines or pixels)
depends on another Markov chain's probabilities.

Dependencies: random, numpy, PIL, itertools
"""

import random
import numpy as np
from PIL import Image, ImageDraw
from itertools import product

#painting will use 4 colors, each is a randomly generated RGB tuple
RGB_VALUES = {
    "color1": (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 
    "color2": (random.randint(0,255),random.randint(0,255),random.randint(0,255)),
    "color3": (random.randint(0,255),random.randint(0,255),random.randint(0,255)),
    "color4": (random.randint(0,255),random.randint(0,255),random.randint(0,255))
}

#create 800x600 image with a randomly generated background color
WIDTH = 800
HEIGHT = 600
background_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
img = Image.new('RGB', (WIDTH,HEIGHT), background_color)

class MarkovArtist:
    def __init__(self, color_transition_matrix, layer_transition_matrix):
        """Simulates an artist that relies on one Markov chain for colors and another
        Markov chain for layers.
            Args:
                color_transition_matrix (dict): color transition probabilities
                layer_transition_matrix (dict): layer transition probabilities
        """
        self.color_transition_matrix = color_transition_matrix
        self.colors = list(color_transition_matrix.keys())
        self.layer_transition_matrix = layer_transition_matrix
        self.layers = list(layer_transition_matrix.keys())

    def get_next_color(self, current_color):
        """Decides which color to use next based on the current color.
            Args: 
                current_color (str): the current color being used to paint.
        """
        return np.random.choice(
            self.colors,
            p=[self.color_transition_matrix[current_color][next_color] for next_color in self.colors]
        )
    
    def get_next_layer(self, current_layer):
        """Decides which type of layer to paint next based on the current layer.
            Args:
                current_layer (str): the current layer being painted.
        """
        return np.random.choice(
            self.layers,
            p=[self.layer_transition_matrix[current_layer][next_layer] for next_layer in self.layers]
        )
    
    def paint_pixels(self, current_color):
        """Paints an entire layer, pixel by pixel, using the color probabilities from
        the color Markov chain.
            Args:
                current_color (str): the current color being used to paint.
        """
        for x, y in product(range(WIDTH), range(HEIGHT)):
            next_color = self.get_next_color(current_color)
            img.putpixel((x, y), RGB_VALUES[next_color])
            current_color = next_color
        
    def paint_lines(self, current_color):
        """Paints a series of lines connected to each other, using the color probabilities
        from the color Markov chain.
            Args:
                current_color (str): the current color being used to paint.
        """
        counter = 0

        #randomly set a max for how many lines are drawn
        maximum = random.randint(0,1400)

        #randomly choose start and end coordinates for the first line
        start_x = random.uniform(0, WIDTH)
        start_y = random.uniform(0, HEIGHT)
        end_x = random.uniform(0, WIDTH)
        end_y = random.uniform(0, HEIGHT)

        while counter < maximum:
            lines = ImageDraw.Draw(img)

            next_color = self.get_next_color(current_color)
            lines.line((start_x, start_y, end_x, end_y), RGB_VALUES[next_color], width=1, joint="curve")
            current_color = next_color

            #update the coordinates so the next line starts where the previous line ended
            start_x = end_x
            start_y = end_y
            end_x = random.uniform(0, WIDTH)
            end_y = random.uniform(0, HEIGHT)

            counter = counter + 1

    def paint_artwork(self, current_color, current_layer):
        """Paints the painting, layer by layer using the probabilities from the layer
        Markov chain, and then saves it.
            Args:
                current_color (str): the current color being used to paint.
                current_layer (str): the current layer being painted.
        """
        iteration = 0

        while (iteration < 2):
            if (current_layer == "pixels"):
                self.paint_pixels(current_color)

                next_layer = self.get_next_layer(current_layer)
                current_layer = next_layer

                iteration = iteration + 1

            elif (current_layer == "lines"):
                self.paint_lines(current_color)
                
                next_layer = self.get_next_layer(current_layer)
                current_layer = next_layer

                iteration = iteration + 1

        img.show()
        
        img.save('exampleArt.png') #change 'exampleArt' to change the name the painting is saved under

        return img


def main():
    painting_maker = MarkovArtist({
        "color1": {"color1": 0.3, "color2": 0.2, "color3": 0.2, "color4": 0.3},
        "color2": {"color1": 0.6, "color2": 0.2, "color3": 0.1, "color4": 0.1},
        "color3": {"color1": 0.1, "color2": 0.2, "color3": 0.2, "color4": 0.5},
        "color4": {"color1": 0.2, "color2": 0.4, "color3": 0.1, "color4": 0.3}    
        }, 
        {
        "pixels": {"pixels": 0.5, "lines": 0.5},
        "lines": {"pixels": 0.5, "lines": 0.5}
    })

    #randomly choose 1 of the 4 colors as the start color
    colors = ["color1", "color2", "color3", "color4"]
    start_color = random.choice(colors)

    #randomly choose "pixels" or "lines for the start layer"
    layers = ["pixels", "lines"]
    start_layer = random.choice(layers)

    painting_maker.paint_artwork(start_color, start_layer)

if __name__ == "__main__":
    main()