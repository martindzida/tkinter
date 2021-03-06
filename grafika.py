class Point():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def clone(self):
        other = Point(self.x,self.y)
        other.config = self.config.copy()
        return other
                
    def getX(self): return self.x
    def getY(self): return self.y



class City():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = 50
        self.fill_color = "red"
        self.outline_color = "#c93c3c"
        self.outline_width = self.d / 10

    def draw(self, canvas):
       return canvas.create_oval(self.x, self.y, self.x + self.d / 2 + 10, self.y + self.d / 2 + 10, fill=self.fill_color, outline=self.outline_color, width=self.outline_width)

    def detect_cursor(self, point):
        return self.x <= point.x <= self.x + self.d / 2 + 10 and self.y <= point.y <= self.y + self.d / 2 + 10


class Road():
    def __init__(self, x0, y0, x, y):
        self.x0 = x0
        self.y0 = y0
        self.x = x
        self.y = y
        self.color = "#d1d106"
        self.width = 10

    def draw(self, canvas, r_x, r_y, x, y):
        return canvas.create_line(r_x, r_y, x, y, fill="#d1d106", width=10)
