from PIL import Image
import pyautogui
import keyboard, mouse
import time, os

path = input("Image path: ")
image = Image.open(path.strip('"'))
gray_img = image.convert("L")

is_invert = input("invert image? (1 - yes, default - no): ")
if is_invert == "1":
    bw_img = gray_img.point(lambda x: 255 if x < 128 else 0, '1')
else:
    bw_img = gray_img.point(lambda x: 0 if x < 128 else 255, '1')


upper_left = list()
lower_right = list()
print("click the upper left corner of the area")
while(True): #setting the upper left corner coordinate
    coordinates_text = f"X: {pyautogui.position().x}; Y: {pyautogui.position().y}"
    print(f"{coordinates_text:<50}", end="\r", flush=True)
    if (mouse.is_pressed(button='left')):
        while mouse.is_pressed(button='left'): time.sleep(0.01)
        upper_left.append(pyautogui.position().x)
        upper_left.append(pyautogui.position().y)
        break

print("click the lower right corner of the area")
while(True): #setting the lower right corner coordinate
    coordinates_text = f"X: {pyautogui.position().x}; Y: {pyautogui.position().y}"
    print(f"{coordinates_text:<50}", end="\r", flush=True)
    if (mouse.is_pressed(button='left')):
        while mouse.is_pressed(button='left'): time.sleep(0.01)
        lower_right.append(pyautogui.position().x)
        lower_right.append(pyautogui.position().y)
        break

final_img = bw_img.resize((lower_right[0]-upper_left[0], lower_right[1]-upper_left[1])) #resizing image

between_clicks_delay = 0.003
between_clicks_delay_input = input("between clicks delay in seconds (default: 0.003): ")
if between_clicks_delay_input: between_clicks_delay = float(between_clicks_delay_input) #setting delay

os.system('cls')
print(f"start X: {upper_left[0]}; start Y: {upper_left[1]}")
print(f"size X: {lower_right[0]-upper_left[0]}; size Y: {lower_right[1]-upper_left[1]}") #printing information
print(f"delay: {between_clicks_delay}")
print("escape - break")
print("press enter to start...")
keyboard.wait('enter')

pyautogui.PAUSE = between_clicks_delay
stop_flag = False
for x in range(final_img.width):
    if stop_flag: break
    for y in range(final_img.height):
        if keyboard.is_pressed('esc'):
            stop_flag = True
            break
        if final_img.getpixel((x, y)) == 255:
            pyautogui.click(upper_left[0]+x, upper_left[1]+y) #clicking
print("completed")