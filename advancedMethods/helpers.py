import re
import random
import time
import os

def modify_input_for_multiple_files(bike, image):
    return {
        'bike': bike,
        'image': image
    }

def multiple_image_adding_function(image):
    n, ext = os.path.splitext(image.name)
    timestamp = int(time.time())
    filename = f"{''.join(random.choice(n) for _ in range(10))}{timestamp}{ext}"
    image.name = filename
    binary_image = image.read()
    return {"binary_image":binary_image, "image_name":filename}