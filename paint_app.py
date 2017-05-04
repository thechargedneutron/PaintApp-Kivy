from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.properties import BooleanProperty
 
foreground_red=1
foreground_green=1
foreground_blue=1
previous_x=0
previous_y=0
prev_x=0
prev_y=0
linewidth=1
class DrawStraight(Widget):
    straight_active=BooleanProperty(True)
    def on_touch_down(self, touch):
        global foreground_red, foreground_green, foreground_blue, previous_x, previous_y
        print foreground_red, foreground_blue, foreground_green
        if not self.straight_active:
            print "Hii!!"
            return
        with self.canvas:
            Color(foreground_red,foreground_green,foreground_blue,1)
            touch.ud["line"]=Line(points=(touch.x,touch.y),width=linewidth)
        touch.ud["line"].points+=(touch.x, touch.y)
        previous_x=touch.x
        previous_y=touch.y
    def on_touch_move(self, touch):
        global previous_x, previous_y
        if 'line' in touch.ud:
            touch.ud["line"].points.remove(previous_x)
	    touch.ud["line"].points.remove(previous_y)
            touch.ud["line"].points += (touch.x, touch.y)
            previous_x=touch.x
            previous_y=touch.y
    def on_touch_up(self, touch):
        if 'line' in touch.ud:
            print "Love!!"
            touch.ud["line"].points+= [touch.x,touch.y]

class UseRubber(Widget):
    rubber_active=BooleanProperty(True)
    def on_touch_down(self, touch):
	if not self.rubber_active:
	    print "rubber inactive"
	    return
	with self.canvas:
	    Color(0,0,0,1)
	    touch.ud["rubber"]=Line(points = (touch.x, touch.y),width=10)
    def on_touch_move(self, touch):
	if 'rubber' in touch.ud:
	    touch.ud["rubber"].points += [touch.x, touch.y]

class DrawRectangle(Widget):
    rectangle_active=BooleanProperty(True)
    global foreground_red,foreground_green,foreground_blue,prev_x,prev_y
    def on_touch_down(self, touch):
	global prev_x,prev_y
	if not self.rectangle_active:
	    return
        with self.canvas:
	    print touch.x,touch.y
	    Color(foreground_red,foreground_green,foreground_blue,1)
	    touch.ud["rect"]=Line(points=(touch.x,touch.y),width=linewidth)
	    #touch.ud["rect"].points+=(touch.x,touch.y)
	    prev_x=touch.x
	    print "Working"
	    prev_y=touch.y
	    print prev_x, prev_y
    def on_touch_up(self, touch):
	global prev_x,prev_y
	#print prev_x, prev_y, touch.x,  touch.y
	if 'rect' in touch.ud:
	    print "Yes"
	    touch.ud["rect"].points += (prev_x,touch.y)
	    touch.ud["rect"].points += (touch.x, touch.y)
	    touch.ud["rect"].points += (touch.x, prev_y)
	    touch.ud["rect"].points += (prev_x, prev_y)


 
class DrawPencil(Widget):
    pencil_active=BooleanProperty(True)
    def on_touch_down(self, touch):
        if not self.pencil_active:
            print "Wassup?"
            return
        with self.canvas:
	    Color(foreground_red,foreground_green,foreground_blue,1)
            print "random being drawn"
            touch.ud["line1"] = Line( points = (touch.x, touch.y), width=linewidth)
    def on_touch_move(self, touch):
        if 'line1' in touch.ud:
            print "random shit!!"
            touch.ud["line1"].points += [touch.x, touch.y]
 
class MainScreen(Screen):
    def give_yellow(self, *args):
        global foreground_red, foreground_green, foreground_blue
	print "yellow"
        foreground_red=1
        foreground_green=1
        foreground_blue=0
        print foreground_red, foreground_green, foreground_blue
    def give_orange(self, *args):
        global foreground_red, foreground_green, foreground_blue
        foreground_red=1
        foreground_green=0.5
        foreground_blue=0
        print foreground_red, foreground_green, foreground_blue
    def give_red(self, *args):
	global foreground_red, foreground_green, foreground_blue
        foreground_red=1
        foreground_green=0
        foreground_blue=0
        print foreground_red, foreground_green, foreground_blue
    def give_green(self, *args):
	global foreground_red, foreground_green, foreground_blue
        foreground_red=0
        foreground_green=1
        foreground_blue=0
        print foreground_red, foreground_green, foreground_blue
    def give_white(self, *args):
	global foreground_red, foreground_green, foreground_blue
        foreground_red=1
        foreground_green=1
        foreground_blue=1
        print foreground_red, foreground_green, foreground_blue
    def give_violet(self, *args):
	global foreground_red, foreground_green, foreground_blue
        foreground_red=0.62
        foreground_green=0
        foreground_blue=1
        print foreground_red, foreground_green, foreground_blue
    def give_blue(self, *args):
	global foreground_red, foreground_green, foreground_blue
        foreground_red=0
        foreground_green=0
        foreground_blue=1
        print foreground_red, foreground_green, foreground_blue
    def set_width_1(self, *args):
	global linewidth
	linewidth=1
    def set_width_5(self, *args):
	global linewidth
	linewidth=5
    def set_width_10(self, *args):
	global linewidth
	linewidth=10


class ScreenManagement(ScreenManager):
    pass
 
presentation = Builder.load_file("main.kv")
 
class PaintApp(App):
    def build(self):
        return presentation
 
if __name__=="__main__":
    PaintApp().run()
