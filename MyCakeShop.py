import pyautogui as pa
from pynput.mouse import Controller, Button 
import keyboard as key
from time import sleep

mouse = Controller()

def detect():
    orders = []
    if pa.locateOnScreen("Assets\plain_cake.png",region = (307, 135, 1144, 254),grayscale = True,confidence=0.9):
        orders.append("plain_cake")
    if pa.locateOnScreen("Assets/plain_choco_cake.png",region = (307, 135, 1144, 254),grayscale = True,confidence=0.95):
        orders.append("plain_choco_cake")
    if pa.locateOnScreen("Assets/berry_choco_cake.png",region = (307, 135, 1144, 254),grayscale = True,confidence=0.95):
        orders.append("berry_choco_cake")
    if pa.locateOnScreen("Assets/straw_choco_cake.png",region = (307, 135, 1144, 254),grayscale = True,confidence=0.9):
        orders.append("straw_choco_cake")
    if pa.locateOnScreen("Assets/kiwi_choco_cake.png",region = (307, 135, 1144, 254),grayscale = True,confidence=0.9):
        orders.append("kiwi_choco_cake")
    if pa.locateOnScreen("Assets/plain_white_cake.png",region = (307, 135, 1144, 254),grayscale = True,confidence=0.95):
        orders.append("plain_white_cake")
    if pa.locateOnScreen("Assets/berry_white_cake.png",region = (307, 135, 1144, 254),grayscale = True,confidence=0.95):
        orders.append("berry_white_cake")
    if pa.locateOnScreen("Assets/straw_white_cake.png",region = (307, 135, 1144, 254),grayscale = True,confidence=0.9):
        orders.append("straw_white_cake")
    if pa.locateOnScreen("Assets/kiwi_white_cake.png",region = (307, 135, 1144, 254),grayscale = True,confidence=0.9):
        orders.append("kiwi_white_cake")
    if pa.locateOnScreen("Assets/coco_coffee.png",region = (307, 135, 1144, 254),grayscale = True,confidence=0.9):
        orders.append("coco_coffee")
    if pa.locateOnScreen("Assets/cream_coffee.png",region = (307, 135, 1144, 254),grayscale = True,confidence=0.9):
        orders.append("cream_coffee")
    if pa.locateOnScreen("Assets/plain_coffee.png",region = (263, 482, 434, 667),grayscale = True,confidence=0.8):
        orders.append("plain_coffee")
    if pa.locateOnScreen("Assets/check.png",region = (263, 482, 434, 667),grayscale = True,confidence=0.9):
        orders.append("take_out")
    return orders

def toping(name):
    if name == "berry":
        mouse.position = (718, 589)
        mouse.click(Button.left)
    elif name == "straw":
        mouse.position = (817, 587)
        mouse.click(Button.left)
    elif name == "kiwi":
        mouse.position = (917, 592)
        mouse.click(Button.left)

def flavor(name):
    if name == "white":
        mouse.position = (501, 609)
        mouse.click(Button.left)
    elif name == "choco":
        mouse.position = (609, 608)
        mouse.click(Button.left)
    elif name == "plain":
        mouse.position = (582, 480)
        mouse.click(Button.left)
        mouse.position = (774, 480)
        mouse.click(Button.left)
        mouse.position = (582, 380)
        mouse.click(Button.left)
        mouse.position = (774, 380)
        mouse.click(Button.left)

def coffee(name):
    if name == "plain":
        mouse.position = (1044, 476)
        mouse.click(Button.left)
        mouse.position = (997, 420)
        mouse.click(Button.left)
        mouse.position = (965, 372)
        mouse.click(Button.left)
    elif name == "coco":
        mouse.position = (1233, 485)
        mouse.click(Button.left)
    elif name == "cream":
        mouse.position = (1145, 515)
        mouse.click(Button.left)

def play(orders):
    orders = list(set(orders))
    mouse.position = (150, 353)
    mouse.click(Button.left)
    mouse.position = (150, 353)
    mouse.click(Button.left)
    if "take_out" in orders:
        mouse.position = (353, 543)
        mouse.click(Button.left)
        mouse.position = (370, 631)
        mouse.click(Button.left)
        mouse.position = (150, 353)
        mouse.click(Button.left)
        mouse.position = (150, 353)
        mouse.click(Button.left)
        mouse.position = (150, 353)
        mouse.click(Button.left)
    if "plain_cake" in orders:
        flavor("plain")
    if "plain_choco_cake" in orders:
        flavor("choco")
        flavor("plain")
    if "berry_choco_cake" in orders:
        flavor("choco")
        toping("berry")
        flavor("plain")
    if "straw_choco_cake" in orders:
        flavor("choco")
        toping("straw")
        flavor("plain")
    if "kiwi_choco_cake" in orders:
        flavor("choco")
        toping("kiwi")
        flavor("plain")
    if "plain_white_cake" in orders:
        flavor("white")
        flavor("plain")
    if "berry_white_cake" in orders:
        flavor("white")
        toping("berry")
        flavor("plain")
    if "straw_white_cake" in orders:
        flavor("white")
        toping("straw")
        flavor("plain")
    if "kiwi_white_cake" in orders:
        flavor("white")
        toping("kiwi")
        flavor("plain")
    if "coco_coffee" in orders:
        coffee("coco")
        coffee("plain")
    if "cream_coffee" in orders:
        coffee("cream")
        coffee("plain")
    if "plain_coffee" in orders:
        coffee("plain")

def main():
    while True:
        if key.is_pressed("s"):
            play(detect())
        elif key.is_pressed("w"):
            while True:
                play(detect())
                if key.is_pressed("z"):
                    break
        elif key.is_pressed("q"):
            break

if __name__ == "__main__":
    main()