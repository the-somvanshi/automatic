import pyautogui as pg
import time as t
x=994
y=326
qty="1"
pname="alok"
item="EVRON"
pg.click(x,y)
pg.typewrite(item)
#pg.click(882,254)
#t.sleep(0.5)
#pg.click(914,185)
pg.typewrite(['enter','enter'])
pg.typewrite(qty)
pg.typewrite(['enter','esc'])
t.sleep(2)
pg.press(['numlock'])
pg.keyDown("left")
pg.keyUp("left")
