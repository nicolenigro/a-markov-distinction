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

## Sources
* Professor Harmon's markov_musician.py sample code
* https://docs.python.org/3/library/random.html
* https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
* https://www.geeksforgeeks.org/python-pil-putpixel-method/
* https://www.rapidtables.com/web/color/RGB_Color.html
* https://www.youtube.com/watch?v=mWPWTy7quYU
