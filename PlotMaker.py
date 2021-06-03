#!usr/bin/env python3

import matplotlib
import requests
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')

class MyGrid(Widget):
    function_str = ObjectProperty(str)
    start_range = ObjectProperty(float)
    end_range = ObjectProperty(float)
    #function_str = ""

    def calculate(self):
        print(self.function_str.text)

    def write_function(self, value):
        self.function_str.text += value
        print(self.function_str.text)



class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()