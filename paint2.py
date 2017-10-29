from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from random import random
from kivy.uix.colorpicker import ColorPicker 
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
sline = False
clr=[1,1,0.5,1]
pre_clr=clr
xs=0
ys=0
xboun=0
yboun=0
rect=False
press=0
width=5
def reset():
    global rect, ell, sline
    rect=ell=sline=False
def retclr():
    return clr

def incanvasxy(self,x,y):
    if x > 0.15* self.width and y >0.2 *self.height and x < self.width*0.75 and y < self.height*0.8:
        return True


class Painter(Widget):
    
    col = ListProperty(clr)
    def save(self):
        self.export_to_png("image.png")    
     

    def on_touch_down(self, touch):
        #print "down"
        global xs,ys,xboun,yboun,press
        press = 1
        if incanvasxy(self,touch.x,touch.y):   
            
            self.col= retclr()
            if Widget.on_touch_down(self, touch):
                xs=touch.x
                ys=touch.y    
                return True

            with self.canvas:
                Color(*self.col)
                #d = 30
                #Ellipse(pos=(touch.x - d / 2,touch.y - d / 2), size=(d,d))
                touch.ud['line'] = Line(points=(touch.x, touch.y),width=5)
                #if sline:
                xs=touch.x
                ys=touch.y
        else:
            xs=touch.x
            ys=touch.y
    def on_touch_move(self, touch):
        #print "move"
        global xs,ys,xboun,yboun
        if incanvasxy(self,touch.x,touch.y) and incanvasxy(self,xs,ys) :
            self.col= retclr()
            if sline:
                if Widget.on_touch_move(self, touch):
                    return True
                with self.canvas.after:
                    self.canvas.after.clear()
                    #if skip > 5:
                     #   Color(*[0,0,0,1])
                      #  Line(points=(xp,yp,xs,ys),width=4)
                    Color(*self.col)
                    Line(points=(touch.x,touch.y,xs,ys),width=4)
                xboun=touch.x
                yboun=touch.y
            elif rect:
                if Widget.on_touch_move(self, touch):
                    return True
                with self.canvas.after:
                    self.canvas.after.clear()
                    Color(*self.col)
                    Line(rectangle=(xs, ys, touch.x-xs, touch.y-ys),width=4)
                xboun=touch.x
                yboun=touch.y
                    
            else:
                if incanvasxy(self,xs,ys):
                    touch.ud["line"].points += [touch.x, touch.y]

    def on_touch_up(self, touch):
        #print "up"
        global xs,ys,press
        
        if incanvasxy(self,xs,ys):
            if incanvasxy(self,touch.x,touch.y) :    
                
                if sline:
                    
                    self.col= retclr()
                    
                    if Widget.on_touch_down(self, touch):
                        return True
                    with self.canvas:
                        Color(*self.col)
                        Line(points=(touch.x,touch.y,xs,ys),width=4) 
                if rect:
                    
                    self.col= retclr()
                    
                    if Widget.on_touch_down(self, touch):
                        return True
                    with self.canvas:
                        Color(*self.col)
                        Line(rectangle=(xs, ys, touch.x-xs, touch.y-ys),width=4)         
            else:
                if press:
                    if sline :
                        with self.canvas:
                                if xboun:
                                    Color(*self.col)
                                    Line(points=(xboun,yboun,xs,ys),width=4)
                        self.canvas.after.clear()
                    if rect :
                        with self.canvas:
                                if xboun:
                                    Color(*self.col)
                                    Line(rectangle=(xs, ys, xboun-xs, yboun-ys),width=4)
                        self.canvas.after.clear() 

        press=0                     
class Cpicker(ColorPicker):
    pass

class popup(Popup):
    def hello (self, y):
        global clr,pre_clr
        pre_clr=clr    
        clr=y 
class popup2(Popup):
    def thick (self, w):
        global width 
        width =w

class MainScreen(Screen):
    
    def open_it1(self):
        popup().open()
    def open_it2(self):
        popup2().open()
    
    def eraser(self):
        global clr,pre_clr,sline
        reset()
        pre_clr = clr
        clr= [0,0,0,1]
    
    def pencil(self):
        global clr,pre_clr,sline
        clr=pre_clr
        reset()

    def sl(self):
        global sline,rect,pre_clr,clr
        reset()
        clr=pre_clr
        sline= True
        
    def rect(self):
        global rect,sline,pre_clr,clr
        reset()
        clr=pre_clr
        rect= True
                


class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("kvf.kv")

class painApp(App):
    def build(self):
        print "start"
        return presentation

if __name__== "__main__":
    painApp().run()