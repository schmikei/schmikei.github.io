from PIL import Image
import argparse


def make_emote(img, name, size):
    img.thumbnail(size)
    img.save(name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("size", help="display a square of a given number",
                        type=int, default = 128)
    parser.add_argument("filename", help="display a square of a given number",
                    type=str)
    args = parser.parse_args()
    filename = args.filename
    size = (args.size, args.size)
    img = Image.open(filename)
    make_emote(img, filename, size)
