#!usr/bin/env python3

import matplotlib
import requests
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '500')

class MyGrid(Widget):
    def calculate(self):
        pass

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()