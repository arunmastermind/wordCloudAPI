from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# %matplotlib inline
matplotlib.rcParams['figure.figsize'] = (16.0, 9.0)

'''
class wordcloud.WordCloud(font_path=None, width=400, height=200, margin=2, ranks_only=None, prefer_horizontal=0.9, mask=None, scale=1, color_func=None, max_words=200, min_font_size=4, stopwords=None, random_state=None, background_color='black', max_font_size=None, font_step=1, mode='RGB', relative_scaling='auto', regexp=None, collocations=True, colormap=None, normalize_plurals=True, contour_width=0, contour_color='black', repeat=False, include_numbers=False, min_word_length=0)
'''

# script = open("batman.txt").read()
# stopwords = set(STOPWORDS)
# batman_mask = np.array(Image.open("test.jpg"))
#
# # Custom Colormap
# from matplotlib.colors import LinearSegmentedColormap
# colors = ["#000000", "#111111", "#101010", "#121212", "#212121", "#222222"]
# cmap = LinearSegmentedColormap.from_list("mycmap", colors)
#
# wc = WordCloud(background_color="white", stopwords=stopwords, mask=batman_mask,
#                width=1987, height=736, colormap=cmap)
# wc.generate(script)
# plt.figure()
# plt.imshow(wc, interpolation="bilinear")

dataset = open("batman.txt", "r").read()
def create_word_cloud(string):
   maskArray = np.array(Image.open("test.jpg"))
   # cloud = WordCloud(background_color = "black", min_font_size=5, mask = maskArray, stopwords = set(STOPWORDS))
   cloud = WordCloud(font_path=None, width=400, height=200, margin=2, ranks_only=None, prefer_horizontal=0.9, mask=None, scale=1, color_func=None, max_words=200, min_font_size=4, stopwords=None, random_state=None, background_color='black', max_font_size=None, font_step=1, mode='RGB', relative_scaling='auto', regexp=None, collocations=True, colormap=None, normalize_plurals=True, contour_width=0, contour_color='black', repeat=False, include_numbers=False, min_word_length=0)
   cloud.generate(string)
   cloud.to_file("wordCloud.png")
   plt.plot()
   plt.imshow(cloud)


dataset = dataset.lower()
create_word_cloud(dataset)