```.py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.textinput import TextInput

class Que(MDScreen):
    pass
class qeso(MDApp):
    def build(self):
        return
test = qeso()
test.run()
```
```.kv
ScreenManager:
    Que:
        name:"Que"
<Que>:

    MDBoxLayout:
        id: bck

        md_bg_color: "#FFFFFF"
        orientation: "vertical"
        pos_hint: {"center_x":.5, "center_y":.9}
        spacing: dp(10)

        MDLabel:

            text:"""Tic Tac Toe by Mina :  it's X turn \n"""
            
            halign: "center"
            font_style:"H5"
            color: "#222222"
            multiline:True




    MDFloatLayout:


        MDGridLayout:
            size_hint: .5, .5
            pos_hint: {'center_x': .5, 'center_y': .5}
            cols: 3
            rows: 3


            Button:
                id: btn1
                text: "O"
                font_size: "45sp"
                background_color:(200, 60, 0, 1)



            Button:
                id: btn2
                text: ""
                font_size: "45sp"
                background_color:(0, 121, 0, 0.7)



            Button:
                id: btn3
                text: ""
                font_size: "45sp"
                background_color:(0, 121, 0, 0.7)


            Button:
                id: btn4
                text: "X"
                font_size: "45sp"
                background_color:(225, 0, 0, 1)

            Button:
                id: btn5
                text: ""
                font_size: "45sp"
                background_color:(0, 121, 0, .7)

            Button:
                id: btn6
                text: ""
                font_size: "45sp"
                background_color:(0, 121, 0, .7)

            Button:
                id: btn7
                text: ""
                font_size: "45sp"
                background_color:(0,121, 0, .7)

            Button:
                id: btn8
                text: ""
                font_size: "45sp"
                background_color:(0, 121, 0, .7)

            Button:
                id: btn9
                text: ""
                font_size: "45sp"
                background_color:(0, 121, 0, .7)


```
