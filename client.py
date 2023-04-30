import socket
from functools import partial
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty,ObjectProperty
from kivy.core.window import Window

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = '192.168.177.45'
server_port = 2345
server = (server_ip, server_port)


class Touch(Widget):

    count = NumericProperty(1)
    click_type = NumericProperty(0)
    right_click_event = ObjectProperty(0)

    def on_touch_down(self, touch):
        self.right_click_event =Clock.schedule_once(partial(self.right_click, touch), 1.5)
        if touch.is_double_tap:
            self.click_type = 1
            msg = str(round(touch.x))+":"+str(round(touch.y))+":"+str(self.click_type)
            print(msg)
            s.sendto(msg.encode(), server)
        elif touch.is_triple_tap:
            self.click_type = 2
            msg = str(round(touch.x))+":"+str(round(touch.y))+":"+str(self.click_type)
            print(msg)
            s.sendto(msg.encode(), server)
        else:
            self.click_type = 0
            msg = str(round(touch.x))+":"+str(round(touch.y))+":"+str(self.click_type)
            print(msg)
            s.sendto(msg.encode(), server)

    def on_touch_up(self, touch):
        self.click_type = 0
        Clock.unschedule(self.right_click_event)

    def on_touch_move(self, touch):
        Clock.unschedule(self.right_click_event)
        msg = str(round(touch.x))+":"+str(round(touch.y))+":"+str(self.click_type+4)
        print(msg)
        s.sendto(msg.encode(), server)

    def right_click(self, touch, count):
        self.click_type = 3
        msg = str(round(touch.x))+":"+str(round(touch.y))+":"+str(self.click_type)
        print(msg)
        s.sendto(msg.encode(), server)
        self.click_type = 0


class MyApp(App):
    def build(self):
        return Touch()


MyApp().run()
