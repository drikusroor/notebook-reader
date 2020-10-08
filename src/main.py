import cv2
import numpy as np
from scene_text import AllWordsRecognizer

img = cv2.imread("images/test.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold image
ret, thresh = cv2.threshold(imgray, 150, 255, 0)
cv2.imwrite("images/thresh.jpg", thresh)

# edge contours
contours, hierarchy = cv2.findContours(thresh, 1, 2)

pipeline = AllWordsRecognizer()

# read an image
img = cv2.imread("images/thresh.jpg")

# detect and recognize all words in the image
words, boxes = pipeline.get_all_words(img)

counter = 1

# loop over the bounding boxes
for box in boxes:
    
		height, width = np.shape(img)

    X, y = box[:, 0], box[:, -1]

    minX = int(np.min(X))
    maxX = int(np.max(X))
    minY = int(np.min(y))
    maxY = int(np.max(y))

		if minX > 5:
			minX -= 5
		else:
			minX = 0

		if minY > 5:
			minY -= 5
		else:
			minY = 0

		if maxX <= width - 5:
			maxX +=5
		else
			maxX = width

		if maxY <= height - 5:
			maxY += 5
		else:
			maxY = height

    crop_img = img[minY:maxY, minX:maxX]
    cv2.imwrite("boxes/crop-{0}.jpg".format(counter), crop_img)

    counter += 1
