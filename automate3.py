import pyautogui as pg
import time as t
#pname=input("enter name of petient :-")
#dname=input("enter name of doctor :-")
#item=input("enter name of medecine :-")
#qty=input("enter quantity of medicine :-")
item=['IVSET','IVC']
qty=['1','1']
def pdetail(p='ALOK',d='001'):
    x=958
    y=54
    pg.click(x,y)
    pg.typewrite(['enter','enter'])
    pg.typewrite(p)
    pg.typewrite(['enter','enter'])
    pg.typewrite(d)
    pg.typewrite(['enter','enter'])
def idetail(i,q):
    pg.typewrite(i)
    pg.typewrite(['enter','enter'])
    pg.typewrite(q)
    pg.typewrite(['enter','esc'])
pdetail()
for i in range(2):
    idetail(item[i],qty[i])   
for i in range(2):
    idetail(item[i],qty[i])   
