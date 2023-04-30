import socket
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "0.0.0.0"
port = 2345
server_config = (host, port)

s.bind(server_config)


print("server running:")
mousedown = 0

# single_click_count = 0

while True:
    data, addr = s.recvfrom(15)
    data = data.decode()
    coord = data.split(":")
    x = coord[0]
    y = coord[1]
    z = coord[2]

    if z == '0':
        # if single_click_count == 0:
        # pyautogui.moveTo(int(y), int(x))
        # single_click_count = single_click_count+1
        mousedown = 0
        pyautogui.mouseUp()
    # else:
        # single_click_count = 0

    if z == '1':
        pyautogui.click(button='left')

    if z == '2':
        pyautogui.doubleClick(button='left')
    if z == '3':
        pyautogui.click(button='right')
    if z == '4':
        pyautogui.moveTo(int(y), int(x))

    if z == '5' or z == '6':
        pyautogui.dragTo(int(y), int(x), button='left')

        # if mousedown != 1:
        #     pyautogui.mouseUp()
        #     pyautogui.moveTo(int(y), int(x))
        #     mousedown = 1
        #     pyautogui.mouseDown()
        # pyautogui.moveTo(int(y), int(x))
        # else:
        #     mousedown = 0

    print(data)
