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


## Sources
* Professor Harmon's markov_musician.py sample code
* https://docs.python.org/3/library/random.html
* https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
* https://www.geeksforgeeks.org/python-pil-putpixel-method/
* https://www.rapidtables.com/web/color/RGB_Color.html
* https://www.youtube.com/watch?v=mWPWTy7quYU
