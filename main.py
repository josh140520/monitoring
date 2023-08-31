#Pillow version: 9.5

import kivy
from kivy.app import App
from kivy.properties import ListProperty, NumericProperty, DictProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import sp
from kivy.graphics import Rectangle


kivy.require("1.9.1")


class MainWindow(Screen): #Main screen

    #DESIGN - MainWindow Background
    app_name = StringProperty("MONITORING APP")
    app_name_color = ListProperty([1, 1, 1, 1])
    font_size_sp = NumericProperty(40)
    main_background_color = ListProperty([0.945, 0.937, 0.278, 0.7])
    app_background_color = ListProperty([0.9, 0.5, 0.9, 0.1])

    #DESIGN - Shared properties of button
    button_color = ListProperty([0, 1, 1, 0.3])
    button_text_color = ListProperty([0, 1, 0, 1])
    button_font_size_sp = NumericProperty(30)
    button_size_dp = ListProperty([200, 100])
    button_size_hint_dp = ListProperty([0.4, 0.4])

    #DESIGN - Button Name and position
    button_conn = StringProperty("Connection Page")

    button_status = StringProperty("Status Page")

    button_graph = StringProperty("Graph Page")



class ConnWindow(Screen): #1st window
    #DESIGN - ConnWindow Background
    app_name_conn = StringProperty("Connection Setup")
    app_name_color_conn = ListProperty([1, 1, 1, 1])
    font_size_dp_conn = NumericProperty(40)
    background_color_conn = ListProperty([0.1, 0.2, 0.4, 0.8])



class StatusWindow(Screen): #2nd window
    status_name = StringProperty("SENSOR STATUS")
    sensor1 = StringProperty("DS18B20 Temperature  Sensor")
    sensor2 = StringProperty("PZEM-015 Battery Meter")
    sensor3 = StringProperty("YF-S201 Water Flow Rate Sensor")
    sensor4 = StringProperty("Analog Water Pressure Sensor")
    sensor5 = StringProperty("Solar Power Pump")
class GraphWindow(Screen): #3rd window
    pass
class WindowManager(ScreenManager): #handle transition
    pass



class MonitoringApp(App):
    def build(self):
        return Builder.load_file("monitoring.kv")

    def exit_app(self):
        App.get_running_app().stop()

if __name__ == "__main__":
    MonitoringApp().run()