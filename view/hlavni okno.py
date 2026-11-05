from tkinter import Tk, Frame, Canvas


class HlavniOknoFrme(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.herni_deska = Canvas(self, width=400, height=400, bg="white")
        self.herni_deska.pack()
        self.herni_deska.create_rectangle(0, 0, 50, 50, fill="black")

        velikost = 50
        for radek in range(8):
            for sloupec in range(8):
                x1 = sloupec * velikost
                y1 = radek * velikost
                x2 = x1 + velikost
                y2 = y1 + velikost
                if (radek + sloupec) % 2 == 0:
                    barva = "white"
                else:
                    barva = "brown"
                self.herni_deska.create_rectangle(x1, y1, x2, y2, fill= barva)


        for sloupec in range(8):
            stred_x = sloupec * velikost + velikost / 2

            self.herni_deska.create_text(
                stred_x, 1 * velikost + velikost / 2,
                    text="♟", font=("Arial", 24), fill="black"
            )

            self.herni_deska.create_text(
                stred_x, 6 * velikost + velikost / 2,
                text="♙", font=("Arial", 24), fill="pink"
            )

if __name__ == "__main__":
    root = Tk()
    view = HlavniOknoFrme(root)
    view.pack()
    root.mainloop()