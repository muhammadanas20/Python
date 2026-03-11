import cv2
import random
from pathlib import Path

# Build image path relative to this script
image_path = Path(__file__).resolve().parent / "assets" / "dog.jpg"
img = cv2.imread(str(image_path), -1)

if img is None:
    raise FileNotFoundError(f"Could not load image: {image_path}")

# Check image dimensions
h, w = img.shape[:2]
print(f"Image shape: {img.shape}")

# Extract a valid region from the image (adjust coordinates to fit actual image size)
# Use safer coordinates that are within bounds
y_start, y_end = min(100, h // 2), min(300, h)
x_start, x_end = min(100, w // 2), min(400, w)
dogFace = img[y_start:y_end, x_start:x_end].copy()  #copy

# Resize to match target paste dimensions (200, 300)
dogFace = cv2.resize(dogFace, (300, 200))  #resize to match target dimensions
img[100:300, 200:500] = dogFace  #paste
# cv2.imshow('dogImage',dogFace)
# cv2.waitKey(5)
# cv2.destroyAllWindows()
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()      