# Le Pixelkov

## Description
This program uses two Markov chains—one for color transition probabilities and another for layer transition probabilities—to paint a painting. The color used to paint each pixel and line relies on the color Markov chain, which has 4 colors, each of which are randomly generated for each painting. The layer being painted relies on the layer Markov chain, which has 2 states (lines or pixels). There are only 2 layers painted per painting so the system will yield a painting with pixels only, a painting with lines only, or a painting with lines overlaid on a pixel background.

## How to Set Up and Run the Code
1. Open the terminal.
2. Install the Python modules necessary to run the code: numpy and PIL (random and itertools are built-in already). If you already use pip, you can install them with the following commands.  
```
pip install numpy  
pip install Pillow
```
3. Change your directory to the folder you want to store this code in.  
```
cd Documents/GitHub
```
4. Clone this repository onto your computer with the following line.  
```
git clone https://github.com/nicolenigro/a-markov-distinction.git
```
5. Change your directory to the folder for this project.  
```
cd a-markov-distinction
```
6. Type and enter the following line into the terminal to run the program.  
```
python markov_artist.py
```

## Reflection
**Describe how the system is personally meaningful to you…**  
In freshman year, I took an art history class and when using the elements of art to analyze artworks, professors emphasized focus on form, which I didn’t find nearly as interesting or aesthetically pleasing as color. This system is personally meaningful to me because I had the creative power to place emphasis on the element of art that I enjoy the most—color. Growing up, when asked my favorite color, I would always respond "rainbow!”; my love of color is why I wanted to have my system use enough colors to fully explore this element while also not using too many to the point of chaos. By using a new palette of randomly generated RGB tuples for each painting, I am always excited and curious to see the new painting created by my system and the ways that different colors and their placements complement each other. Also, given that the system creates art that is saved as an image on the computer, I find meaning from the point of view I have as a viewer looking at my art on the screen and how the my interpretation can change when I zoom in and out. I’ve always appreciated art, whether it be in museum galleries or posted on Instagram, and being able to create a system that painted a vision I had in my mind was empowering; what I might not be able to create with my own two hands on canvas I was able to create with a program.

**Include a discussion of whether you believe your system is creative (and why or why not).**  
Based on this class’s first definition of creativity—a creative system is both novel and valuable—I believe that my system fulfills the novel component of creativity in that each time it is run, it creates a new piece of art using a unique color palette, pixel/line placement, and combination of layers based off of Markov probabilities. However, I’m not certain my system is valuable. The pixel layer that my system creates is vaguely similar to mainstream art I have seen on album covers ("A Different Arrangement" by Black Marble, "Real Love Baby" single by Father John Misty) as well as clothing (Paloma Wool Puerto pants). Meanwhile, the line layer somewhat resembles some of Sol LeWitt’s wall drawings. If patterns/art similar to my pixel and line layers are associated with popularity/success (in streams for the songs using the album art, financially for the sold out pants, critical acclaim for LeWitt), does that make my system valuable? I’m not really sure. Ventura’s “How To Build A CC System” considers value as “the importance, worth, or usefulness of something; this would typically be ascribed by practitioners of the domain in question.” So I guess the question of if my system is valuable remains unanswered until the artists themselves judge. Furthermore, Ventura’s definition of a computationally creative agent expands on the class’s definition with the inclusion of intentionality. I believe that my system is intentional because my output is correlated with the process as the layers based on the Markov chain are visible in the output. In conclusion, I think that my system is novel and intentional, but am unsure of its value, fulfilling 1/2 of the components of the class’s definition of creativity and 2/3 of the components of Ventura’s definition. Aside from formal definitions, I think my system is a start for creativity, but there’s more I can do to make it even more creative.

![Image of A Different Arrangement album artwork]
(http://images.genius.com/5731bdda8a5e9407c8d29bd5275cb39d.1000x1000x1.jpg)

![Image of Real Love Baby album artwork]
(https://media.pitchfork.com/photos/5929f6440c2bba1b7de038d6/1:1/w_500/691e31e5.jpg)

![Image of Puerto Pants]
(https://cdn.shopify.com/s/files/1/0412/0952/8474/products/puerto-elastic-high-waist-knitted-pants-black-01_912x.jpg?v=1602859144)

![Image of Sol Lewitt Wall Drawing]
(https://i.pinimg.com/originals/30/12/25/3012252ef6cb598bc4660554e5c7a6ae.jpg)

## Sources
* Professor Harmon's markov_musician.py sample code
* https://docs.python.org/3/library/random.html
* https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
* https://www.geeksforgeeks.org/python-pil-putpixel-method/
* https://www.rapidtables.com/web/color/RGB_Color.html
* https://www.youtube.com/watch?v=mWPWTy7quYU
