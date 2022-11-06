import pgzrun
import random
import time
WIDTH=350
HEIGHT=600
bg=Actor('background')
bird=Actor('bird')
bar_down=Actor('bar_down')
bar_up=Actor('bar_up')
tree=Actor('tree')
tree2=Actor('tree 2')
tree3=Actor('tree 3')
#Gameover=Actor('GAMEOVER')
global score
score = 0

bird.x=50
bird.y=HEIGHT/2
bar_up.x=300
bar_up.y=0
bar_down.x=300
bar_down.y=600
tree.x=0
tree.y=515
tree2.x=150
tree2.y=515
tree3.x=300
tree3.y=515
def draw():
    bg.draw()   
    tree.draw()
    tree2.draw()
    tree3.draw()
    bird.draw()
    bar_up.draw()
    bar_down.draw()
    screen.draw.text(str(score),(30,30),fontsize=50,color='red')

def update():
    global score
    bird.y += 1
    bar_down.x-=3
    bar_up.x-=3
    tree.x-=3
    tree2.x-=3
    tree3.x-=3
    dy=random.randint(-100,100)
    if bar_up.x<0:
        bar_up.x=WIDTH
        bar_down.x=WIDTH
        score += 1
        print(score)
    if tree.x<-20:
        tree.x=600
    if tree2.x<-20:  
        tree2.x=600
    if tree3.x<-20: 
        tree3.x=600
    if bar_down.x<-20:
        bar_down.x=600
        bar_down.y+=dy
    if bar_up.x<-20:
        bar_up.x=600
        bar_up.y+=dy
    if bird.colliderect(bar_up) or bird.colliderect(bar_down) or bird.y<0:
        print('你输了!')
        exit()

def on_key_down():
    bird.y -= 50
    if bird.y<0:
        bird.y=0

pgzrun.go()