# -*- coding: utf-8 -*- 
from tkinter import *
from tkinter import messagebox, colorchooser
from grafika import *
from dialogs import *

class MyApp:
    def __init__(self, parent):
        self.color_fg = 'black'
        self.color_bg = '#bce0a8'
        self.x = 100
        self.y = 100
        self.r_x = 100
        self.r_y = 100
        self.objects = []
        self.obj = None
        self.roads = []
        self.road= None
        self.dict_road = {
            "x0": 100,
            "y0": 100,
            "x": 200,
            "y": 200
        }
        self.status = 0
        self.index = -1
        self.dicts = 0
        self.active = []
        self.action = ""
        self.parent = parent
        self.drawWidgets()

    def drawWidgets(self):
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        self.container = Frame(self.parent, width=screen_width, height=100, bg="gray")
        self.canvas = Canvas(self.parent, width=screen_width - 200, height=screen_height - 200, bg=self.color_bg)
        self.canvas.pack(fill=BOTH,expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.canvas.bind("<ButtonPress-3>", self.button3_press)
        self.canvas.bind("<B3-Motion>", self.button3_move_press)

        
        button_circle = Button(self.container, text="Přidat město", command=self.add_city)
        button_circle.pack(side=LEFT)
        button_road = Button(self.container, text="Přidat silnici", command=self.add_road)
        button_road.pack(side=LEFT)
        button_info = Button(self.container, text="O aplikaci", command=self.info_box)
        button_info.pack(side=RIGHT)
        self.container.pack(fill=BOTH)

        self.canvas.focus_set()

        menu = Menu(self.parent)
        self.parent.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='Soubor',menu=filemenu)
        filemenu.add_command(label='Konec',command=self.parent.destroy)     
        canvasmenu = Menu(menu)
        menu.add_cascade(label='Plátno',menu=canvasmenu)
        canvasmenu.add_command(label='Vyčistit plátno',command=self.delete_objects)
        citymenu = Menu(menu)
        menu.add_cascade(label='Obec', menu=citymenu)
        citymenu.add_command(label='Počet obyvatel', command=self.city_population)
        coordinatesmenu = Menu(menu)
        menu.add_cascade(label='Souřadnice', menu=coordinatesmenu)
        coordinatesmenu.add_command(label='Náhled', command=lambda: self.coordinates(screen_width, screen_height))

        self.canvas.create_line(0,50,100,200, fill="#d1d106", width=10)

    def coordinates(self, screen_width, screen_height):
        self.rows = 9
        self.cols = 16
        self.dif = 120
        self.x0 = self.dif
        self.y0 = self.dif
        while self.rows > 0:
            self.canvas.create_line(0, self.y0, screen_width, self.y0)
            self.y0 += self.dif
            self.rows -= 1

        while self.cols > 0:
            self.canvas.create_line(self.x0, 0, self.x0, screen_height)
            self.x0 += self.dif
            self.cols -= 1      

    def city_population(self):
        dialog = CityDialog(self.parent, self.obj)
        self.parent.wait_window(dialog.top)
        self.redraw_canvas()
   
    def add_city(self):
        self.obj = City(self.x, self.y)
        self.objects.append(self.obj)
        self.action = "new"

    def add_road(self):
        self.road = Road(self.r_x, self.r_y, self.x, self.y)
        self.roads.append(self.dict_road)
        self.action = "new"
        self.index += 1

    def delete_objects(self):
        self.canvas.delete("all")
        self.objects = []
        self.roads = []

    def clear_canvas(self):
        self.canvas.delete("all")

    def redraw_canvas(self):     
        self.clear_canvas()
        for obj in self.objects:
            obj.draw(self.canvas)
        while self.dicts < len(self.roads):    
            self.active = self.roads[self.index].values()
            self.canvas.create_line(self.active[0], self.active[1], self.active[2], self.active[3], fill="#d1d106", width=10)
            self.dicts += 1
            self.index += 1
        


    def info_box(self):
        messagebox.showinfo('Info', 'Převelice primitivní editor map')
   
    # Mouse events
    
    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        point = Point(self.start_x, self.start_y)
        self.action == ""
        for s in self.objects:
            if s.detect_cursor(point): 
                self.obj = s
                self.old_x = self.obj.x
                self.old_y = self.obj.y
                self.action = "edit"

    def on_move_press(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        if (self.action == "new"):
            self.obj.x = self.start_x if self.start_x <= cur_x else cur_x
            self.obj.y = self.start_y if self.start_y <= cur_y else cur_y
            self.obj.width = abs(self.start_x - cur_x)
            self.obj.height = abs(self.start_y - cur_y)

        if (self.action == "edit"):
            self.obj.x = cur_x - self.start_x + self.old_x
            self.obj.y = cur_y - self.start_y + self.old_y
        
        self.redraw_canvas()

    def on_button_release(self, event):
        self.action = ""

    def button3_move_press(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        if (self.action == "next"):
            self.road.x = self.canvas.canvasx(event.x)
            self.road.y = self.canvas.canvasx(event.y)
            self.dict_road["x"] = self.canvas.canvasx(event.x)
            self.dict_road["y"] = self.canvas.canvasx(event.y)
            print(self.road.x)
            print(self.road.y)
            #print(self.roads[1].values())
            self.redraw_canvas()

    def button3_press(self, event):
        self.r_x = self.canvas.canvasx(event.x)
        self.r_y = self.canvas.canvasy(event.y)
        if (self.action == "new"):
            self.road.x0 = self.r_x
            self.road.y0 = self.r_y
            self.dict_road["x0"] = self.r_x
            self.dict_road["y0"] = self.r_y
            self.action = "next"
        



root = Tk()
myapp = MyApp(root)
root.mainloop()