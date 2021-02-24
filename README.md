# Le Pixelkov

## Description
This program uses two Markov chains—one for color transition probabilities and another for layer transition probabilities—to paint a painting. The color used to paint each pixel and line relies on the color Markov chain, which has 4 colors, each of which are randomly generated for each painting. The layer being painted relies on the layer Markov chain, which has 2 states (lines or pixels). There are only 2 layers painted per painting so the system will yield a painting with pixels only, a painting with lines only, or a painting with lines overlaid on a pixel background.

## How to Set Up and Run the Code
1. Open the terminal.
2. Install the Python modules necessary to run the code: numpy and PIL (random and itertools are built-in already). If you already use pip, you can install them with the following commands.  
```
$ pip install numpy  
$ pip install Pillow
```
3. Change your directory to the folder you want to store this code in.  
```
$ cd Documents/GitHub
```
4. Clone this repository onto your computer with the following line.  
```
$ git clone https://github.com/nicolenigro/a-markov-distinction.git
```
5. Change your directory to the folder for this project.  
```
$ cd a-markov-distinction
```
6. Type and enter the following line into the terminal to run the program.  
```
$ python markov_artist.py
```

## Reflection
**Describe how the system is personally meaningful to you…**  
In freshman year, I took an art history class and when using the elements of art to analyze artworks, professors emphasized focus on form, which I didn’t find nearly as interesting or aesthetically pleasing as color. This system is personally meaningful to me because I had the creative power to place emphasis on the element of art that I enjoy the most—color. Growing up, when asked my favorite color, I would always respond "rainbow!”; my love of color is why I wanted to have my system use enough colors to fully explore this element while also not using too many to the point of chaos. By using a new palette of randomly generated RGB tuples for each painting, I am always excited and curious to see the new painting created by my system and the ways that different colors and their placements complement each other. Also, given that the system creates art that is saved as an image on the computer, I find meaning from the point of view I have as a viewer looking at my art on the screen and how the my interpretation can change when I zoom in and out. I’ve always appreciated art, whether it be in museum galleries or posted on Instagram, and being able to create a system that painted a vision I had in my mind was empowering; what I might not be able to create with my own two hands on canvas I was able to create with a program.

**Explain how working on it genuinely challenged you as a computer scientist.**  
Based off of my experiences this past year, I would describe my comfort zone in computer science as coding in Java, working collaboratively in groups or with a partner, and asking for help from professors, TAs, and friends when struggling to find a solution. I pushed myself outside of my comfort zone by working in Python (which felt kind of rusty as I haven’t written a program in it since summer 2019…I would catch myself planning a for loop with Java syntax in mind), trusting my own abilities, and testing my patience working independently. There was a 3 day period when I wasn’t able to successfully debug my program to produce the output I envisioned, and I got very antsy. But, instead of relying on others for help, I kept testing print statements and reading articles about Python functions and modules online to push myself to work through it and I ultimately persevered. In addition to pushing myself outside of my comfort zone, I made an effort to avoid the bad habit of procrastinating and rushing to turn in code that just works. I made sure to start early and wrote down a plan with some pseudocode I had in mind before starting to code. This helped focus both my research on Python functions and modules as well as my coding. Since I had time to review and polish my work, I made edits like replacing a nested for loop with a `for x, y in product` loop that I learned existed by doing research online as well as creating the `paint_pixels` and `paint_lines` functions instead of just keeping all the code in the `paint_artwork` function to make the code easier to read. These were important challenges because they helped me establish good habits and confidence in Python and working alone, which make me feel more prepared for future work in the class. The next steps going forward include exploring new Python modules and learning how to use other mathematical models to build creative systems.

**Include a discussion of whether you believe your system is creative (and why or why not).**  
Based on this class’s first definition of creativity—a creative system is both novel and valuable—I believe that my system fulfills the novel component of creativity in that each time it is run, it creates a new piece of art using a unique color palette, pixel/line placement, and combination of layers based off of Markov probabilities. However, I’m not certain my system is valuable. The pixel layer that my system creates is vaguely similar to mainstream art I have seen on album covers (["A Different Arrangement" by Black Marble](http://images.genius.com/5731bdda8a5e9407c8d29bd5275cb39d.1000x1000x1.jpg), ["Real Love Baby" single by Father John Misty](https://media.pitchfork.com/photos/5929f6440c2bba1b7de038d6/1:1/w_500/691e31e5.jpg)) as well as clothing ([Paloma Wool Puerto pants](https://cdn.shopify.com/s/files/1/0412/0952/8474/products/puerto-elastic-high-waist-knitted-pants-black-01_912x.jpg?v=1602859144)). Meanwhile, the line layer somewhat resembles some of [Sol LeWitt’s wall drawings](https://i.pinimg.com/originals/30/12/25/3012252ef6cb598bc4660554e5c7a6ae.jpg). If patterns/art similar to my pixel and line layers are associated with popularity/success (in streams for the songs using the album art, financially for the sold out pants, critical acclaim for LeWitt), does that make my system valuable? I’m not really sure. Ventura’s “How To Build A CC System” considers value as “the importance, worth, or usefulness of something; this would typically be ascribed by practitioners of the domain in question.” So I guess the question of if my system is valuable remains unanswered until the artists themselves judge. Furthermore, Ventura’s definition of a computationally creative agent expands on the class’s definition with the inclusion of intentionality. I believe that my system is intentional because my output is correlated with the process as the layers based on the Markov chain are visible in the output. In conclusion, I think that my system is novel and intentional, but am unsure of its value, fulfilling 1/2 of the components of the class’s definition of creativity and 2/3 of the components of Ventura’s definition. Aside from formal definitions, I think my system is a good start for a creative system, but there’s even more I can do in the future to make it more creative.


## Sources
* Professor Harmon's markov_musician.py sample code
* https://docs.python.org/3/library/random.html
* https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
* https://www.geeksforgeeks.org/python-pil-putpixel-method/
* https://www.rapidtables.com/web/color/RGB_Color.html
* https://www.youtube.com/watch?v=mWPWTy7quYU
