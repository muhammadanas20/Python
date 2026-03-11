from pathlib import Path
import cv2

# Build image path relative to this script
image_path = Path(__file__).resolve().parent / "assets" / "dog.jpg"
img = cv2.imread(str(image_path),-1)

if img is None:
    raise FileNotFoundError(f"Could not load image: {image_path}")
img = cv2.resize(img,(400,400))
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
# img = cv2.resize(img, (0,0),fx=0.5,fy=0.5) half the height
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()