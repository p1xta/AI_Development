from skimage import data
import matplotlib.pyplot as plt
import cv2


# canny parameters
THRESHOLD1 = 150
THRESHOLD2 = 200
# hough parameters
DP = 1
MIN_DIST = 20
PARAM1 = 50
PARAM2 = 30
MIN_RADIUS = 10
MAX_RADIUS = 50

def load_image(img_path = None):
    # if no path was passed, returns an image of coins
    if img_path is None:
        return data.coins()
    
    try:
       image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    except Exception as e:
        print(f"Could not load image: {e}")

    return image

def save_image(image, img_output_path = "image_with_circles.png"):
    try:
        cv2.imsave(img_output_path, image)
    except Exception as e:
        print(f"Could not save image: {e}")

def find_circles(image):
    # find edges on the image
    image_with_edges = cv2.Canny(image, threshold1=THRESHOLD1, threshold2=THRESHOLD2) 

    # find circles with hough algorithm
    circles = cv2.HoughCircles(image_with_edges, cv2.HOUGH_GRADIENT, \
                                dp=DP, minDist=MIN_DIST, \
                                param1=PARAM1, param2=PARAM2, \
                                minRadius=MIN_RADIUS, maxRadius=MAX_RADIUS)
    if circles is None:
        print("No circles found on the image")
        return image
    circles = circles.astype(int)

    # broadcast to 3 channels, so we can draw colorful circles 
    result_image = cv2.merge([image, image, image])
    # draw circles
    for i in circles[0,:]:
        cv2.circle(result_image,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(result_image,(i[0],i[1]),2,(255,0,0),3)

    print(f"{len(circles[0])} circles found.")
    return result_image


if __name__ == "__main__":
    image = load_image()
    print(f"Coins image shape: {image.shape}")

    image_with_circles = find_circles(image)
    save_image(image=image_with_circles)