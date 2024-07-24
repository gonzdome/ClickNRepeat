import ctypes
import time

lastPosition = None

# Defining the structure for capturing mouse position
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def getMousePosition():
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

def isLeftButtonPressed():
    return ctypes.windll.user32.GetAsyncKeyState(0x01) & 0x8000 != 0

def getClickCoordinates():
    try:
        while True:
            if isLeftButtonPressed():
                position = getMousePosition()
                if lastPosition != position:
                    return position
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Interrupted by user.")
