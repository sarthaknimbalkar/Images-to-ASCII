from PIL import Image

def asciiConvert(image_path, output_type, output_path, scale):
    try:
        scale = int(scale)
        if scale <= 0:
            raise ValueError("Scale must be a positive integer")

        # Open and resize the image
        with Image.open(image_path) as img:
            img = img.resize((img.width // scale, img.height // scale))

            # Convert image to grayscale
            img = img.convert("L")

            # Define ASCII characters based on intensity
            ascii_chars = '@%#*+=-:. '

            # Convert pixels to ASCII art
            ascii_art = ''
            for pixel_value in img.getdata():
                ascii_art += ascii_chars[pixel_value // 25]

            # Split ASCII art into lines
            lines = [ascii_art[i:i+img.width] for i in range(0, len(ascii_art), img.width)]

        # Save ASCII art to file
        with open(output_path, 'w') as output_file:
            for line in lines:
                output_file.write(line + '\n')

        print("ASCII art saved to", output_path)

    except (IOError, ValueError) as e:
        print("Error:", e)

if __name__ == '__main__':
    asciiConvert("mona_lisa.jpg", "jpg", "mona_lisa.txt", "3")
