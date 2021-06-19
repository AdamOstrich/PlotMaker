#!usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.config import Config
from kivy.uix.popup import Popup

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')

class Picture(Widget):
    root = "wykres.jpg"

class MyGrid(Widget):
    """
    We will use MyGrid to make app looks nice.
    """
    # These variables will be needed to make program run as it should.
    function_str = ObjectProperty(str)
    start_range = ObjectProperty(float)
    end_range = ObjectProperty(float)
    x_axis = ObjectProperty(str)
    y_axis = ObjectProperty(str)
    title = ObjectProperty(str)
    legend = ObjectProperty(bool)

    def calculate(self):
        """
        Here program interprets the string with function and makes a plot and return plot pic to app
        :return: 0
        """
        print(self.function_str.text)
        legend = self.function_str.text
        try:
            self.function_str.text = self.function_str.text.replace("^", "**")
            self.function_str.text = self.function_str.text.replace("sin", "np.sin")
            self.function_str.text = self.function_str.text.replace("cos", "np.cos")
            self.function_str.text = self.function_str.text.replace("tan", "np.tan")
            self.function_str.text = self.function_str.text.replace("sqrt", "np.sqrt")
            self.function_str.text = self.function_str.text.replace("e", "np.e")
            self.function_str.text = self.function_str.text.replace("pi", "np.pi")
            self.function_str.text = self.function_str.text.replace("log", "np.log")

            # Making a plot:
            x = np.linspace(float(self.start_range.text), float(self.end_range.text), 100)
            try:
                f = eval("lambda x: " + self.function_str.text)
                y = f(x)
                plt.plot(x,y)
                print("funkcja: ", self.function_str.text)
                plt.title(self.title.text)
                plt.xlabel(self.x_axis.text)
                plt.ylabel(self.y_axis.text)
                plt.legend([legend])
                plt.savefig("wykres.jpg")
                show_plot()
            except:
                self.function_str.text = "bad data"
        except ValueError:
            self.function_str.text = "bad data"


    def write_function(self, value):
        """
        Function add what we click in app window to string with function
        :param value: string from clicked button
        :return: 0
        """
        self.function_str.text += value
        print(self.function_str.text)

class MyApp(App):
    """
    Here starts kivy app.
    """
    def build(self):
        return MyGrid()

def show_plot():
    #print("inside show_plot")
    show = Picture()
    #print("inside show_plot")
    popupWindow = Popup(title="Plot", content=show, size_hint=(None, None), size=(500, 500))
    #print("inside show_plot")
    popupWindow.open()


if __name__ == "__main__":
    """Here starts the program"""
    MyApp().run()