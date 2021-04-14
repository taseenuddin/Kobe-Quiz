import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen


class FrontScreen(Screen):
    pass


class Question1(Screen):
    pass


class Screenlist(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        return kv


kv = Builder.load_file("my.kv")
if __name__ == "__main__":
    MyApp().run()
