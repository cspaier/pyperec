## PyPerec

This project aim at answering a simple game from [Georges Perec](https://en.wikipedia.org/wiki/Georges_Perec):

You take 2 words of 5 letters. You must go from the first to the latter by changing one letter each step.
You can only use words from the dictionary. You canot use Capital name.

This is a fun game to kill time with a sheet of paper and a pen. Not easy.


This define what we will call the "Perec distance" in a dictionary: The smallest path between 2 connected words with the above rules.

This raise quite some questions on the dictionary graph structure:

- Is the dictionary connexe? In other words are all the words connected?
- If not, how many stack of connected words do we have?

Appart from answering those questions, the idea is to offer an interective graph visualisation tool and some game modes.

## So what?

The code is inside the `pyperec.py` file.

So far we are using a very naive algorythme in `build_graph` using the [igraph python library](https://igraph.org/python/). Exmples are provided in the `french` directory with a 22000 french words containing 2401 5-letters words. This graph is saved in dot, graphml and pickle. You can view an interactive rendering of this exemple clicking the above picture.

[![grpah_png](https://github.com/cspaier/pyperec/raw/master/french/Pyperec-test-2.png)]( https://plot.ly/~cspaier/4/pyperec-test-2/)
