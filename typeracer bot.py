'''This is an auto-type-racer bot'''

import pyautogui

input = '''Books are the treasured wealth of the world and the fit inheritance of generations and nations. Books, the oldest and the best, stand naturally and rightfully on the shelves of every cottage. They have no cause of their own to plead, but while they enlighten and sustain the reader his common sense will not refuse them. Their authors are a natural and irresistible aristocracy in every society, and, more than kings or emperors, exert an influence on mankind. '''
pyautogui.sleep(2)
print("Typing...")
pyautogui.write(input,interval=0.1)
print("Successfully Typed!\n")


pyautogui.sleep(100)
from selenium import webdriver

web = webdriver.Chrome(executable_path=r"D:\Apps\chromedriver.exe")
web.get("https://play.typeracer.com/")
pyautogui.sleep(4)
pyautogui.click(x=254, y=557)
pyautogui.sleep(2)

input1 = web.find_elements_by_id("hwRestgwt-uid-14")
input2 = web.find_elements_by_id("hwRestgwt-uid-15")
# pyautogui.sleep(10)
output = web.find_element_by_class_name("txtInput")
output.send_keys(input1[0].text)
pyautogui.write(input2,interval=0.2)

