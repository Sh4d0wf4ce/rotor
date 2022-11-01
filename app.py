import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
import socket

def client(data):
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    client_socket.send(data.encode())

    client_socket.close()


Builder.load_string('''
<MainWidget>:
    BoxLayout:
        size: root.size
        orientation: 'vertical'

        Label:
            id: circular_progress
            text: str(root.angle)
            
            size_hint: None, None
            width: 200
            height: 200
            
            progress: 0
            
            pos_hint: {'center_x':.5, 'center_y':.6}
            
            canvas.before:
                # Main ellipse as background
                Color:
                    rgba: (0,0,1,1)
                Ellipse:
                    size: self.size
                    pos: self.pos
                
                # Pie Chart ellipse as progress
                Color:
                    rgba: (1,0,0,1)
                Ellipse:
                    size: self.size
                    pos: self.pos
                    angle_end: self.progress
                
                # small ellipse that cover the center of progress
                Color:
                    rgba: (0,0,0,1)
                Ellipse:
                    size: [self.width - 30 ,self.height - 30]
                    pos: [(self.center_x - (self.width - 30)/2), (self.center_y - (self.height - 30)/2)]
        
        GridLayout:
            cols: 2

            Button:
                text: 'left'
                on_press: root.changeAngle('left')
            
            Button:
                text: 'right'
                on_press: root.changeAngle('right')
            
''')


class MainWidget(BoxLayout): 
    angle = NumericProperty()

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)

    def changeAngle(self, direction):
        if direction == "right":
            self.angle = 0 if self.angle == 359 else self.angle + 1 
        elif direction == "left":
            self.angle = 359 if self.angle == 0 else self.angle - 1

        self.ids.circular_progress.progress = self.angle
        client(direction)

class MyApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    MyApp().run()
