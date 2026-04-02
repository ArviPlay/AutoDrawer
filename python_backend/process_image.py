from PIL import Image
import argparse

def process(img_path: str, output_path: str, start_x: int, start_y: int, end_x: int, end_y: int, is_invert: bool):
    image = Image.open(img_path.strip('"'))
    gray_img = image.convert("L")
    if is_invert == True:
        bw_img = gray_img.point(lambda x: 255 if x < 128 else 0, '1')
    else:
        bw_img = gray_img.point(lambda x: 0 if x < 128 else 255, '1')
    final_img = bw_img.resize((end_x-start_x, end_y-start_y))
    final_img.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("img_path", str)
    parser.add_argument("output_path", str)
    parser.add_argument("start_x", int)
    parser.add_argument("start_y", int)
    parser.add_argument("end_x", int)
    parser.add_argument("end_y", int)
    parser.add_argument("is_invert", bool)
    args = parser.parse_args()
    process(args.img_path, args.output_path, args.start_x, args.start_y, args.end_x, args.end_y, args.is_invert)