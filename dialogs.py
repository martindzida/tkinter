from tkinter import *
        
class CityDialog:
    def __init__(self, parent, shape):
        self.shape = shape
        top = self.top = Toplevel(parent)
        top.title("Počet obyvatel")
        top.transient(parent)
        # Zablokuje práci v hlavním okně aplikace - modální okno
        top.grab_set()
        # Nastaví zaměření na dialog
        top.focus_set()
        x = parent.winfo_x()
        y = parent.winfo_y()
        top.geometry("%dx%d+%d+%d" % (400, 100, x + 100, y + 50))
        # Proměnné pro vkládání parametrů okna
        spin_d_value = StringVar()
        spin_d_value.set(self.shape.d)
        # Kontejner pro pozici objektu
        container1 = Frame(top, width=400, pady=10, padx=10)
        label_pozice = Label(container1, text="Počet obyvatel", pady=5)
        label_pozice.pack()
        label_d = Label(container1, text="Počet obyvatel v tis. (max. 500) :")
        label_d.pack(side=LEFT)
        self.spinbox_d = Spinbox(container1, from_=0, to=parent.winfo_width(), textvariable=spin_d_value)
        self.spinbox_d.pack(side=LEFT, padx=30)
        container1.pack(fill=BOTH)

        button_ok = Button(top, text="OK", command=self.ok)
        button_ok.pack(side=LEFT, padx=10, pady=5, fill=BOTH, expand=True)
        button_cancel = Button(top, text="Zrušit", command=self.cancel)
        button_cancel.pack(side=LEFT, padx=10, pady=5, fill=BOTH, expand=True)

    def ok(self, event=None):
        if  float(self.spinbox_d.get()) < 501:
            self.shape.d = float(self.spinbox_d.get())
            self.top.destroy()

    def cancel(self, event=None):
        self.top.destroy()     