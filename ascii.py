from PIL import Image


def image_to_ascii(image_path, output_path, width=100):
    img = Image.open(image_path)
    img = img.convert('L')
    aspect_ratio = img.height / img.width
    new_height = int(aspect_ratio * width * 0.55)
    img = img.resize((width, new_height))
    pixels = img.getdata()
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    ascii_str = "".join([chars[pixel // 25] for pixel in pixels])
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index: index + width] for index in range(0, ascii_str_len, width)])
    with open(output_path, "w") as f:
        f.write(ascii_img)


image_to_ascii('Image.png', 'output.txt')
