import cv2
import numpy as np
from scene_text import AllWordsRecognizer

img = cv2.imread('images/test.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold image
ret, thresh = cv2.threshold(imgray, 150, 255, 0)
cv2.imwrite('thresh.jpg', thresh)

# edge contours
contours, hierarchy = cv2.findContours(thresh, 1, 2)

pipeline = AllWordsRecognizer()

# read an image
img = cv2.imread('thresh.jpg')

# detect and recognize all words in the image
words, boxes = pipeline.get_all_words(img)

# loop over the bounding boxes
for box in boxes:
	# TODO
	# Figure out how to use boxes to make crops of words
	# that I can use to apply text recognition on
	print(box)