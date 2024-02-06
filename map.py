import cv2
import numpy as np
import os

def load_images_from_folder(folder):
    """Load all images from a folder into a list."""
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def stitch_images(images):
    """Stitch images together to create a panoramic view of the room."""
    # Initialize the OpenCV stitcher class and stitch the images
    stitcher = cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        print("Images stitched successfully.")
        return stitched
    else:
        print("Image stitching failed.")
        return None

def save_image(image, path):
    """Save the stitched image to a file."""
    cv2.imwrite(path, image)

# Main process
folder_path = 'path/to/your/images'
output_path = 'path/to/output/panorama.jpg'

# Load images
images = load_images_from_folder(folder_path)

# Stitch the images together
panorama = stitch_images(images)

# Save the result
if panorama is not None:
    save_image(panorama, output_path)
    print(f"Panorama saved to {output_path}")
else:
    print("Failed to create a panorama.")
