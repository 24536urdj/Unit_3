###
    Screen:
    size: 500, 500
    md_bg_color: "#a3b18a"

    MDBoxLayout:
        id:main_box
        orientation: "horizontal"
        size_hint: .3, .3
        pos_hint: {"center_x":.3, "center_y":.5}
        md_bg_color: "#ff0000"

        MDLabel:
            id:counter_label
            text: "Count 0"
            font_size: 34
            color: "#283618"
            size_hint: 1, .5
            pos_hint:{"center_x":1.5,"center_y":.5}
    MDBoxLayout:
        id:counter_lay

        orientation: "horizontal"
        size_hint:.3,.3
        pos_hint: {"center_x":.7, "center_y":.5}
        md_bg_color: "#ff0000"
        MDRaisedButton:
            id:counter
            text:"Add +1"
            font_size:34
            color: "#283618"
            size_hint:1,.5
            pos_hint:{"center_x":1.5,"center_y":.5}
            on_release:
                app.add()
###    
        from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class box(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0



    def add(self):
        self.count += 1
        self.root.ids.counter_label.text = f"Count is {self.count}"

    def build(self):
        return


test = box()
test.run()

