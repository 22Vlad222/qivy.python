from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty
Window.size = (300, 500)
Window.clearcolor = (0, 0.5, 0, 1)


class Delivery(Widget):
    order = ObjectProperty()
    adress = ObjectProperty()
    number = ObjectProperty()

    def press(self):
        order = self.order.text
        adress = self.adress.text
        number = self.number.text

        print(order, adress, number)

        f = open("text.txt", "a")
        f.write(order + "" + adress + " " + number + "\n")
        f.close()

        self.order.text = ""
        self.adress.text = ""
        self.number.text = ""

class FiguresApp(App):
    def build(self):
        return Delivery()


FiguresApp().run()

