from services.MouseClickCoordinatesService import getClickCoordinates
from services.ExecuteMouseClickService import mouseClick
from time import sleep

arr = [1, 2, 3, 4] # rpa simulation

x, y = getClickCoordinates()

for i in arr:
    mouseClick(x, y)
    sleep(3)