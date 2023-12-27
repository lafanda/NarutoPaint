from pygame import *
from random import randint, choice
from math import*
#from tkinter import *
#from tkinter.filedialog import askopenfilename
#from tkinter.filedialog import asksaveasfilename
#------------------------------------------------------------------
#Random Variables
WIDTH,HEIGHT= 1200,900
screen=display.set_mode((WIDTH,HEIGHT))
RED=(255,0,0)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
WHITE = (255,255,255)
ORANGE = (255,155,0)
col = WHITE
font.init()
tool="no tool"
text = ""
text2 = ""
text3 = ""
omx,omy = (0,0)
size = 15 
stick = 0
sx,sy=0,0
sz = 0
i = 0
#root = Tk()
#root.withdraw()
fileName = 0
#----------------------------------------------------------------------
#Rects for tools
pencilRect = Rect(20,400,60,60) 
eraserRect = Rect(100,400,60,60)
brushRect = Rect(20,480,60,60)
highlightRect = Rect(100,480,60,60)
fillRect = Rect(20,560,60,60)
stickerRect = Rect(20,650,140,140)
stickerRectDown = Rect(20,790,70,20)
stickerRectUp = Rect(90,790,70,20)
sprayRect = Rect(100,560,60,60)
canvasRect = Rect(200,10,990,800)
paletteRect = Rect (7, 130, 180, 230)
eyeRect = Rect(1050,820,60,60)
clearRect = Rect(1130,820,60,60)
lineRect = Rect(970,820,60,60)
rectRect = Rect(890,820,60,60)
circleRect = Rect(810,820,60,60)
defineRect = Rect(20,820,200,60)
polygonRect = Rect(730,820,60,60)
undoRect = Rect(650,820,60,60)
redoRect = Rect(570,820,60,60)
saveRect = Rect(490,820,60,60)
openRect = Rect(410,820,60,60)
#------------------------------------------------------------------------
#Wallpaper and palette
wallpaper = image.load("Wallpapers/wallpaper.jpg")
screen.blit(wallpaper,(0,0)) 
wheel = image.load("Tools/paletteRect.png")
screen.blit(wheel,(7,130)) 
#----------------------------------------------------------------------
#Title
draw.rect(screen,WHITE,canvasRect)
draw.rect(screen,WHITE,(2,10,190,80))
Fonts = font.SysFont("Algerian",50)
words = ["Naruto"]
word = choice(words)
picword = Fonts.render(word,True,ORANGE)
screen.blit(picword,(33,10))

Fonts = font.SysFont("Algerian",50)
words = [" Paint"]
word = choice(words)
picword = Fonts.render(word,True,ORANGE)
screen.blit(picword,(38,50))
#-------------------------------------------------------------------
#loading stckers
narutoTeen = image.load("Stickers/NarutoOld.png") 
naruto = image.load("Stickers/naruto.png")
sasukeTeen = image.load("Stickers/sasukeOld.png")
sasuke = image.load("Stickers/sasuke.png")
kakashi = image.load("Stickers/Kakashi.png")
sakura = image.load("Stickers/Sakura.png")
itachi = image.load("Stickers/itachi.png")
narutoTeen2 = image.load("Stickers/NarutoOld2.png") 
naruto2 = image.load("Stickers/naruto2.png")
sasukeTeen2 = image.load("Stickers/sasukeOld2.png")
sasuke2 = image.load("Stickers/sasuke2.png")
kakashi2 = image.load("Stickers/Kakashi2.png")
sakura2 = image.load("Stickers/Sakura2.png")
itachi2 = image.load("Stickers/itachi2.png")

stickers = [narutoTeen,naruto,sasukeTeen,sasuke,kakashi,sakura,itachi] #putting srickers into a list
stickers2 = [narutoTeen2,naruto2,sasukeTeen2,sasuke2,kakashi2,sakura2,itachi2]

#songs = load("music/OP 03 - Blue Bird.ogg")
#------------------------------------------------------------------------------------------------------ 
undo = []
redo = []
points= []


running=True
click=False
bucketcol = WHITE
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            sx,sy = evt.pos
            click = True
            keys=key.get_pressed()
            if keys[K_LSHIFT]==1 or keys[K_RSHIFT]==1: #Checking if shift has been clicked
                fills=0 
            else:
                fills=5
            if tool == "line" or tool == "rect" or tool == "circle":
                sx,sy=evt.pos
                click=True
                screenCap=screen.subsurface(canvasRect).copy()
            if evt.button==4 and size < 50: #changing size
                size+=1
            if evt.button==5 and size > 1:
                size-=1
            if evt.button==1 and stickerRectUp.collidepoint((mx,my)): #changing sticker
                stick+=1
                if stick == 7:
                    stick = 0
            if evt.button==1 and stickerRectDown.collidepoint((mx,my)): #changing sticker
                stick-=1
                if stick == -1:
                    stick = 6
                    
            if tool == "polygon":
                try:
                    if canvasRect.collidepoint((mx,my)):
                        l = i+1
                        if evt.button ==1:
                            points.append((mx,my))
                        if len(points) > 1:
                            if evt.button ==1:
                                draw.line(screen,col,(points[i]),(points[l]),4)
                                i += 1
                            elif evt.button == 3:
                                draw.line(screen,col,(points[-1]),(points[0]),4)
                                points = []
                                i = 0
                except:
                    pass
                            
            if undoRect.collidepoint(mx,my):
                if len(undo) > 1:
                    redo.append(undo.pop())
                    screen.blit((undo[-1]),(canvasRect))
                    if len(undo) <= 0:
                           draw.rect(screen,bucketcol,canvasRect)
            if redoRect.collidepoint(mx,my):
                if len(redo) > 0:
                    screen.blit((redo[-1]),(canvasRect))
                    undo.append(redo.pop())
                

        if evt.type == MOUSEBUTTONUP:
            screenCap = screen.subsurface(canvasRect).copy()
            if saveRect.collidepoint(mx,my):
                fileName = asksaveasfilename(parent = root,title = "save the image as")
                if fileName != "":
                    image.save(screen.subsurface(canvasRect),"%s.png"%(fileName))
                    
            if openRect.collidepoint(mx,my):
                fileName = askopenfilename(parent=root,title = "open image")
                if fileName != "":
                    picture = image.load(fileName)
                    picture = transform.scale(picture,(990,800))
                    screen.set_clip(canvasRect)
                    screen.blit(picture,(200,10))
                    undo.append(screenCap)
                    screen.set_clip(None)

            if canvasRect.collidepoint(mx,my):
                screenCap1=screen.subsurface(canvasRect).copy()
                undo.append((screenCap1))
            screen.set_clip(canvasRect)
            if tool == "cicle" and  canvasRect.collidepoint((mx,my)) and mb[0] == 1:
                try:
                    screen.blit(screenCap,(canvasRect))
                    elleRect = Rect(sx,sy,mx-sx,my-sy)
                    elleRect.normalize()
                    draw.ellipse(screen,col,elleRect,fills)
                    screenCap=screen.subsurface(canvasRect).copy()
                except:
                    pass
                
            if tool == "rect" and canvasRect.collidepoint((mx,my)) and mb[0] == 1:
                screen.blit(screenCap,(canvasRect))
                for i in range(0,size):
                    if (mx-sx>0 and my-sy>0) or (mx-sx<0 and my-sy<0):
                        draw.rect(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),fills)
                    elif (mx-sx>0 and my-sy<0) and mb[0] ==1:
                        draw.rect(screen,col,(sx-i,sy+i,mx-sx+i*2,my-sy-i*2),fills)
                    else:
                        draw.rect(screen,col,(sx+i,sy-i,mx-sx-i*2,my-sy+i*2),fills)
                screenCap=screen.subsurface(canvasRect).copy()
            if tool == "line" and canvasRect.collidepoint((mx,my)) and mb[0] == 1:
                screen.blit(screenCap,(canvasRect))
                draw.line(screen,col,(sx,sy),(mx,my),size)
                screenCap=screen.subsurface(canvasRect).copy()
            if evt.button == 1 and tool == "sticker" and canvasRect.collidepoint((mx,my)):
                screen.blit(stickers[stick],(mx-100,my-100))
       
            screen.set_clip(None)
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

                                                                                    
    draw.rect(screen,col,fillRect) #background of tools
    draw.rect(screen,BLACK,pencilRect)
    draw.rect(screen,BLACK,eraserRect)
    draw.rect(screen,BLACK,brushRect)
    draw.rect(screen,BLACK,highlightRect)
    draw.rect(screen,BLACK,sprayRect)
    draw.rect(screen,BLACK,stickerRect)
    draw.rect(screen,BLACK,stickerRectUp)
    draw.rect(screen,BLACK,stickerRectDown)
    draw.rect(screen,BLACK,clearRect)
    draw.rect(screen,BLACK,lineRect)
    draw.rect(screen,BLACK,fillRect)
    draw.rect(screen,BLACK,rectRect)
    draw.rect(screen,BLACK,circleRect)
    draw.rect(screen,BLACK,undoRect)
    draw.rect(screen,BLACK,polygonRect)
    draw.rect(screen,BLACK,redoRect)
    draw.rect(screen,BLACK,saveRect)
    draw.rect(screen,BLACK,openRect)
    draw.rect(screen,WHITE,defineRect)
    draw.rect(screen,col,eyeRect)

    fonts2 = font.SysFont("Callibri",25)
    
    Fonts = font.SysFont("Algerian",20)
    words = ["  NEXT"]
    word = choice(words)
    picword = Fonts.render(word,True,ORANGE)
    screen.blit(picword,(stickerRectUp))

    Fonts = font.SysFont("Algerian",20)
    words = ["  BACK"]
    word = choice(words)
    picword = Fonts.render(word,True,ORANGE)
    screen.blit(picword,(stickerRectDown))

    Fonts = font.SysFont("Algerian",17)
    words = [" clear"]
    word = choice(words)
    picword = Fonts.render(word,True,ORANGE)
    screen.blit(picword,(1130,832))

    Fonts = font.SysFont("Algerian",17)
    words = ["   all"]
    word = choice(words)
    picword = Fonts.render(word,True,ORANGE)
    screen.blit(picword,(1130,845))


    pencil = image.load("Tools/pencil.png") #icons for tools
    screen.blit(pencil,(pencilRect))
    eraser = image.load("tools/eraser.png")
    screen.blit(eraser,(eraserRect))
    brush = image.load("Tools/brush.png")
    screen.blit(brush,(brushRect))
    brush = image.load("Tools/highlighter.png")
    screen.blit(brush,(highlightRect))
    spray = image.load("Tools/spray.png")
    screen.blit(spray,(sprayRect))
    fill = image.load("Tools/bucket.png")
    screen.blit(fill,(20,565,60,60))
    eye = image.load("Tools/Eyedropper.png")
    screen.blit(eye,(eyeRect))
    redopic = image.load("Tools/Redo.png")
    screen.blit(redopic,(redoRect))
    undopic = image.load("Tools/Undo.png")
    screen.blit(undopic,(undoRect))
    savepic = image.load("Tools/save.png")
    screen.blit(savepic,(495,823,60,60))
    openpic = image.load("Tools/open.png")
    screen.blit(openpic,(415,820,60,60))
    draw.line(screen,WHITE,(970,820),(1030,880),2)
    draw.rect(screen,WHITE,(900,830,40,40),2)
    draw.ellipse(screen,WHITE,(820,830,40,40),2)
    draw.polygon(screen,WHITE,[(740,830),(780,850),(740,870),(780,830),(740,830)],2)

    if paletteRect.collidepoint(mx,my) and mb[0]==1: #changing colour
        col=screen.get_at((mx,my))
            
    draw.rect(screen,GREEN,pencilRect,2) #tool squares
    draw.rect(screen,GREEN,eraserRect,2)
    draw.rect(screen,GREEN,brushRect,2)
    draw.rect(screen,GREEN,highlightRect,2)
    draw.rect(screen,GREEN,stickerRect,2)
    draw.rect(screen,GREEN,fillRect,2)
    draw.rect(screen,GREEN,sprayRect,2)
    draw.rect(screen,GREEN,stickerRectUp,2)
    draw.rect(screen,GREEN,stickerRectDown,2)
    draw.rect(screen,GREEN,eyeRect,2)
    draw.rect(screen,GREEN,clearRect,2)
    draw.rect(screen,GREEN,lineRect,2)
    draw.rect(screen,GREEN,rectRect,2)
    draw.rect(screen,GREEN,circleRect,2)
    draw.rect(screen,GREEN,undoRect,2)
    draw.rect(screen,GREEN,redoRect,2)
    draw.rect(screen,GREEN,saveRect,2)
    draw.rect(screen,GREEN,openRect,2)
    draw.rect(screen,GREEN,polygonRect,2)
    draw.rect(screen,col,(5,128,183,233),4)
    
    if pencilRect.collidepoint(mx,my):  #hovering over tool
        draw.rect(screen,BLUE,pencilRect,2)
        text = "draws thin line"
        text2 = ""
        text3 = ""
    elif eraserRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,eraserRect,2)
        text = "Eraser"
        text2 = "scroll wheel for size"
        text3 = ""
    elif brushRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,brushRect,2)
        text = "Brush"
        text2 = "scroll wheel for size"
        text3 = ""
    elif highlightRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,highlightRect,2)
        text = "Highlighter, transparent"
        text2 = "scroll wheel for size"
    elif fillRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,fillRect,2)
        text = "Bucket, fills area"
        text2 = ""
        text3 = ""
    elif sprayRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,sprayRect,2)
        text = "Spray"
        text2 = "scroll wheel for size"
        text3 = ""
    elif stickerRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,stickerRect,2)
        text = "stickers"
        text2 = ""
        text3 = ""
    elif stickerRectUp.collidepoint(mx,my):
        draw.rect(screen,BLUE,stickerRectUp,2)
        text = "next sticker"
        text2 = ""
        text3 = ""
    elif stickerRectDown.collidepoint(mx,my):
        draw.rect(screen,BLUE,stickerRectDown,2)
        text = "previous sticker"
        text2 = ""
        text3 = ""
    elif eyeRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,eyeRect,2)
        text = "Eyedropper"
        text2 = "reselects any colour"
        text3 = ""
    elif clearRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,clearRect,2)
        text = "clear all"
        text2 = ""
        text3 = ""
    elif openRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,openRect,2)
    elif saveRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,saveRect,2)
    elif lineRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,lineRect,2)
        text = "Straight line"
        text2 = "scroll wheel for size"
        text3 = ""
    elif rectRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,rectRect,2)
        text = "Perfect rectangle"
        text2 = "shift for fill"
        text3 = "scroll for size"
    elif circleRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,circleRect,2)
        text = "ellipse"
        text2 = "shift for fill"
        text3 = ""
    elif polygonRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,polygonRect,2)
        text = "polygon"
        text2 = "Click to add more points"
        text3 = "Right clck to connect all"
    elif undoRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,undoRect,2)
        text = "Undo"
        text2 = "Click to undo"
        text3 = ""
    elif redoRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,redoRect,2)
        text = "redo"
        text2 = "Click to redo"
        text3 = ""

    if mb[0]==1 and pencilRect.collidepoint(mx,my): #choosing the tool
        tool="pencil"  
    elif mb[0]==1 and eraserRect.collidepoint(mx,my):
        tool="eraser"
    elif mb[0]==1 and brushRect.collidepoint(mx,my):
        tool="brush"
    elif mb[0]==1 and highlightRect.collidepoint(mx,my):
        tool="highlighter"
    elif mb[0]==1 and fillRect.collidepoint(mx,my):
        tool="fill"
    elif mb[0]==1 and sprayRect.collidepoint(mx,my):
        tool="spray"
    elif mb[0]==1 and stickerRect.collidepoint(mx,my):
        tool="sticker"
    elif mb[0]==1 and eyeRect.collidepoint(mx,my):
        tool="eye"
    elif mb[0]==1 and clearRect.collidepoint(mx,my):
        tool="clear"
    elif mb[0]==1 and lineRect.collidepoint(mx,my):
        tool="line"
    elif mb[0]==1 and rectRect.collidepoint(mx,my):
        tool="rect"
    elif mb[0]==1 and circleRect.collidepoint(mx,my):
        tool="circle"
    elif mb[0]==1 and polygonRect.collidepoint(mx,my):
        tool="polygon"
        
    if tool == "pencil": #changing tool box colour if selected
        draw.rect(screen,RED,pencilRect,2)
    elif tool == "eraser":
        draw.rect(screen,RED,eraserRect,2)
    elif tool == "brush":
        draw.rect(screen,RED,brushRect,2)
    elif tool == "highlighter":
        draw.rect(screen,RED,highlightRect,2)
    elif tool == "fill":
        draw.rect(screen,RED,fillRect,2)
    elif tool == "spray":
        draw.rect(screen,RED,sprayRect,2)
    elif tool == "sticker":
        draw.rect(screen,RED,stickerRect,2)
    elif tool == "eye":
        draw.rect(screen,RED,eyeRect,2)
    elif tool == "line":
        draw.rect(screen,RED,lineRect,2)
    elif tool == "rect":
        draw.rect(screen,RED,rectRect,2)
    elif tool == "circle":
        draw.rect(screen,RED,circleRect,2)
    elif tool == "polygon":
        draw.rect(screen,RED,polygonRect,2)
   
    toolTitle =fonts2.render(text,True,BLACK)
    screen.blit(toolTitle,(defineRect))

    tooldescription = fonts2.render(text2,True,BLACK)
    screen.blit(tooldescription,(20,840,200,60))

    tooldescription2 = fonts2.render(text3,True,BLACK)
    screen.blit(tooldescription2,(20,860,200,60))
        
    if stick == 0 or stick == 2 or stick == 4:
        #print("hello")
        screen.blit(stickers2[stick],(50,650,140,140))
    if  stick == 3 or stick == 6:
        #print("hello")
        screen.blit(stickers2[stick],(25,660,140,140))
    if  stick ==5:
        #print("hello")
        screen.blit(stickers2[stick],(65,660,140,140))
    if stick == 1:
        #print("hello")
        screen.blit(stickers2[stick],(25,650,140,140))
        
    if tool == "clear":
        draw.rect(screen,WHITE,canvasRect)
        
    
    if mb[0]==1 and canvasRect.collidepoint(mx,my): #pencil tool
        screen.set_clip(canvasRect)
        if tool=="pencil":
            draw.line(screen,BLACK,(omx,omy),(mx,my),2)
        
        if tool=="eraser": #eraser
                dist=((my-omy)**2+(mx-omx)**2)**0.5
                if dist!=0: 
                    bx=(mx-omx)/dist
                    by=(my-omy)/dist
                    for i in range(int(dist)+1): 
                        draw.circle(screen,bucketcol,(int(omx+bx*i),int(omy+by*i)),size)
               

        elif tool == "brush": #brush
            dist=((my-omy)**2+(mx-omx)**2)**0.5
            if dist!=0: 
                bx=(mx-omx)/dist
                by=(my-omy)/dist
                for i in range(int(dist)+1): 
                    draw.circle(screen,col,(int(omx+bx*i),int(omy+by*i)),size) 

        elif tool == "highlighter" and col != (WHITE): #highlighter (doesnt work if white)
            col2 = col
            col2[3] = 5 #making transparent
            highlightertip=Surface((100,100),SRCALPHA) #highlighter surface
            draw.circle(highlightertip,(col2),(50,50),size)
            
            dist=((my-omy)**2+(mx-omx)**2)**0.5
            if dist!=0: 
                bx=(mx-omx)/dist
                by=(my-omy)/dist
                for i in range(int(dist)+1):  
                    screen.blit(highlightertip,(mx-50,my-50)) #blitting the highlighter surface

        elif tool == "spray": #spray
            for i in range(int(size**1.5)): #Getting a pos inside the thickness
                sx=randint(mx-size,mx+size) #Getting a random pos in a rect as large as the thickness
                sy=randint(my-size,my+size)
                if ((mx-sx)**2+(my-sy)**2)**0.5<=size: #Checking if the pos is within a cirlce 
                    draw.line(screen,col,(sx,sy),(sx,sy)) #drawing a line
                                        

        elif tool == "fill": #fill tool
            bucketcol = col
            draw.rect(screen,col,canvasRect)

        elif tool == "eye":
            col=screen.get_at((mx,my))
            
        elif tool == "line":
            screen.blit(screenCap,(canvasRect))
            draw.line(screen,col,(sx,sy),(mx,my),size)
                       
        elif tool == "rect":
            screen.blit(screenCap,(canvasRect))
            for i in range(0,size):
                if (mx-sx>0 and my-sy>0) or (mx-sx<0 and my-sy<0):
                    draw.rect(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),fills)
                elif (mx-sx>0 and my-sy<0):
                    draw.rect(screen,col,(sx-i,sy+i,mx-sx+i*2,my-sy-i*2),fills)
                else:
                    draw.rect(screen,col,(sx+i,sy-i,mx-sx-i*2,my-sy+i*2),fills)

        elif tool == "circle":
            try:
                screen.blit(screenCap,(canvasRect))
                elleRect = Rect(sx,sy,mx-sx,my-sy)
                elleRect.normalize()
                draw.ellipse(screen,col,elleRect,fills)
            except:
                pass
    screen.set_clip(None)     

    display.flip()
    omx = mx
    omy = my        
quit()

