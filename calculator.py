#################################################################################
# author : Hamza Rafique                                                        #
#################################################################################

import pyautogui
import configparser

config_file = 'calculator.ini' 
pyautogui.PAUSE = 0.25


def test_size():
    width, height = pyautogui.size()

    return width, height


def minimize_windows():
    
    width, height = pyautogui.size()
    pyautogui.click(x=width-2, y=height-2, button = 'left')

def find_icon(icon_path):
    print(icon_path)
    try:
        x,y = pyautogui.locateCenterOnScreen(str(icon_path))
        return x,y
    except TypeError:
        print("Cannot find Excel file . Please Open the Excel File for the Bot.")

def click_and_write(loc,data):

    a,b = loc
    pyautogui.doubleClick(a, b, button = 'left')
    pyautogui.typewrite(str(data))
    #pyautogui.hotkey('tab')

def click(loc):
    a,b = loc
    pyautogui.click(a, b, button = 'left')

def doubleclick(loc, interval = 0):
    a,b = loc
    pyautogui.doubleClick(a, b, interval, button = 'left')

def get_control_cord(section):

    datatype = config.get(section,'datatype')

    if datatype == 'int':
        x = config.getint(section,'x')
        y = config.getint(section,'y')

        return x,y
    else:
        print('Data Type Error. Please enter pixel values in "int" format')
    
def main():



    print(config.sections())

    print(config.items('windows search'))

    print(config['windows search']['x'])
    x = int(config['windows search']['x'])
    print(type(x))

    main = config.getint('windows search','x')
    print(type(main))

    print('mmmmmmmmmmmmmmmmmmmmmm')

    # minimize windows
    minimize_windows()

    # search for calulator app
    windows_search = get_control_cord('windows search')
    click_and_write(windows_search,'calculator')

    # open app
    best_match = get_control_cord('best match')
    doubleclick(best_match,interval = 0.25)
    
    # maximize app
    pyautogui.hotkey('win', 'up')


    # Add two numbers
    one = get_control_cord('one')
    click(one)

    plus = get_control_cord('plus')
    click(plus)    
    
    two = get_control_cord('two')
    click(two)

    equals = get_control_cord('equals')
    click(equals)    





if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read(config_file)
    
    main()

#python calculator.py
