from PIL import Image
import pyautogui
import keyboard
import argparse

def paint(img_path: str, start_x: int, start_y: int, delay: float):
    """
    draws a black and white image at the specified coordinates
    """
    image = Image.open(img_path)

    pyautogui.PAUSE = delay
    stop_flag = False
    for x in range(image.width):
        if stop_flag: break
        for y in range(image.height):
            if keyboard.is_pressed('esc'):
                stop_flag = True
                break
            if image.getpixel((x, y)) == 255:
                pyautogui.click(start_x+x, start_y+y)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Painter")
    parser.add_argument("img_path", str)
    parser.add_argument("start_x", int)
    parser.add_argument("start_y", int)
    parser.add_argument("delay", float)
    args = parser.parse_args()
    paint(args.img_path, args.start_x, args.start_y, args.delay)