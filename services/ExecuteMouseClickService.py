import ctypes
import time

# Mouse events
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# Structure for representing an input event
class INPUT(ctypes.Structure):
    class _MOUSEINPUT(ctypes.Structure):
        _fields_ = [("dx", ctypes.c_long), ("dy", ctypes.c_long), ("mouseData", ctypes.c_ulong), ("dwFlags", ctypes.c_ulong), ("time", ctypes.c_ulong), ("dwExtraInfo", ctypes.c_void_p)]
    
    _fields_ = [("type", ctypes.c_uint), ("mi", _MOUSEINPUT)]

# Defining the prototypes
sendInput = ctypes.windll.user32.SendInput
setCursorPosition = ctypes.windll.user32.SetCursorPos

# Function to simulate a mouse click
def mouseClick(x, y):
    setCursorPosition(x, y)

    inputDown = INPUT(
        type=0,
        mi=INPUT._MOUSEINPUT(dx=0, dy=0, mouseData=0, dwFlags=MOUSEEVENTF_LEFTDOWN, time=0, dwExtraInfo=0)
    )
    
    inputUp = INPUT(
        type=0,
        mi=INPUT._MOUSEINPUT(dx=0, dy=0, mouseData=0, dwFlags=MOUSEEVENTF_LEFTUP, time=0, dwExtraInfo=0)
    )
    
    # Send mouse event
    sendInput(1, ctypes.byref(inputDown), ctypes.sizeof(inputDown))
    sendInput(1, ctypes.byref(inputUp), ctypes.sizeof(inputUp))
