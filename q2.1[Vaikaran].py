import time
from PIL import Image, ImageDraw
import os
import pandas as pd

def generate_number():
    the_time = int(time.time())
    generated_number = (the_time % 100) + 50
    if generated_number % 2 == 0:
        generated_number += 10
    print("The Generated Number (n) is:", generated_number)
    return generated_number

def set_img(img_direct):
    try:
        return Image.open(img_direct)
    except FileNotFoundError:
        print(f"Error: image doc '{img_direct}' not found.")
        return None

def modify_pixels(image, generated_number):
    width, height = image.size
    img_px = image.load()
    coordinates = []
    pixels = []
    red_pixel_sum = 0

    for x in range(width):
        for y in range(height):
            rgb = img_px[x, y]
            coordinates.append([x, y])
            modified_pixel = (
                min(255, rgb[0] + generated_number),
                min(255, rgb[1] + generated_number),
                min(255, rgb[2] + generated_number),
            )
            pixels.append(modified_pixel)
            red_pixel_sum += modified_pixel[0]

    return coordinates, pixels, red_pixel_sum

def save_modified_image(image, coordinates, pixels, output_path):
    img_out = Image.new("RGB", image.size)
    draw = ImageDraw.Draw(img_out)

    for coord, pixel in zip(coordinates, pixels):
        draw.point(coord, pixel)

    img_out.save(output_path)
    print(f"New image saved at: {output_path}")

def main():
    # Exact path to the Downloads directory
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

    # Setting the image with the path
    image_filename = "chapter1.png"
    image_path = os.path.join(downloads_dir, image_filename)

    generated_number = generate_number()

    # Load the image
    original_image = set_img(image_path)

    if original_image:
        # Pixel modification
        coordinates, pixels, red_pixel_sum = modify_pixels(original_image, generated_number)

        # Save the modified image
        new_image_path = os.path.join(downloads_dir, "chapter1out.png")
        save_modified_image(original_image, coordinates, pixels, new_image_path)

        # Print the sum of red pixel values
        print("Sum of Red Pixel Values:", red_pixel_sum)

if __name__ == "__main__":
    main()
