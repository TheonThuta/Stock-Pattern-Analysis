import cv2
import numpy as np
from scipy.signal import find_peaks

def detect_patterns(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.Canny(img, 50, 150)
    coordinates = np.argmax(img!=0,axis=0) # black pixels are False and white is True, then get index of max value (True=1), which is the first instance per column
    mask = np.any(img!=0, axis=0) # columns that have no white at the top are False, otherwise True
    coordinates = coordinates.astype(float)
    coordinates = np.where(mask, coordinates, np.nan) # keep coordinate as 0 if white is at top, else change to -1
    inverted_coords = coordinates * -1
    print(find_peaks(coordinates, distance=50, prominence=15))
    print(find_peaks(inverted_coords, distance=50,  prominence=15))



detect_patterns('static/charts/AAPL.png')