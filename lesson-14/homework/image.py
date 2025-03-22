from PIL import Image
import numpy as np

image = Image.open("images/birds.jpg")
image_array = np.array(image)

def flip_image(img_array):
    return np.flip(img_array, axis=(0, 1))  

def add_noise(img_array):
    noise = np.random.randint(-50, 50, img_array.shape, dtype=np.int16)
    noisy_image = np.clip(img_array + noise, 0, 255).astype(np.uint8)
    return noisy_image

def brighten_channels(img_array, value=40):
    brightened_image = np.clip(img_array + value, 0, 255).astype(np.uint8)
    return brightened_image

def apply_mask(img_array):
    masked_image = img_array.copy()
    h, w, _ = masked_image.shape
    center_x, center_y = w // 2, h // 2
    masked_image[center_y-50:center_y+50, center_x-50:center_x+50] = [0, 0, 0]
    return masked_image

flipped = flip_image(image_array)
noisy = add_noise(image_array)
brightened = brighten_channels(image_array)
masked = apply_mask(image_array)

Image.fromarray(flipped).save("images/birds_flipped.jpg")
Image.fromarray(noisy).save("images/birds_noisy.jpg")
Image.fromarray(brightened).save("images/birds_brightened.jpg")
Image.fromarray(masked).save("images/birds_masked.jpg")

print("Image manipulations completed.")
