from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
class IntroScreen(MDScreen):
    pass
class MysteryPageA(MDScreen):
    pass
class MysteryPageB(MDScreen):

    pass
class mystery(MDApp):
    def build(self):
        return
text = mystery()
text.run()
'''
  ScreenManager:
    IntroScreen:
        name:"IntroScreen"
    MysteryPageA:
        name:"MysteryPageA"
    MysteryPageB:
        name:"MysteryPageB"
<IntroScreen>
    size:500,500
    MDBoxLayout:
        id:second_box

        halign:"center"
        orientation: "horizontal"

        MDLabel:
            id:counter_label2
            text: "WELCOME"
            font_size: 60
            color: "#283618"

            halign:"center"
            MDRaisedButton:

                id:add_btn
                text:"NEXT PAGE"
                halign:"right"
                on_press:root.parent.current ="MysteryPageA"
<MysteryPageA>
    size:500,500
    MDBoxLayout:
        id:box

        halign:"center"
        orientation: "horizontal"

        MDLabel:
            id:counter_label
            text: "This is mystery page A you pressed the button"
            font_size: 40
            color: "#283618"

            halign:"center"
            MDRaisedButton:

                id:add_btn
                text:"Next Page"
                halign:"right"
                on_press:root.parent.current ="MysteryPageB"

<MysteryPageB>
    size:500,500
    MDBoxLayout:
        id:box1

        halign:"center"
        orientation: "horizontal"

        MDLabel:
            id:counter_label1
            text: "This is mystery page B you pressed the button"
            font_size: 40
            color: "#283618"

            halign:"center"
            MDRaisedButton:

                id:sub_btn
                text:"Previous Page"
                halign:"right"
                on_press:root.parent.current ="MysteryPageA"
'''
