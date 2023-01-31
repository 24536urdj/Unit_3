###
      from kivymd.app import MDApp
      class quiz_40(MDApp):
          def build(self):
              return

          def change(self):
              amount = self.root.ids.text.text
              o=int(amount)
              p= round(o*12.56,2)

              self.root.ids.second_box.text = f"{p} jpy"

      test = quiz_40()
      test.run()
###
      Screen:
    size: 500, 500
    md_bg_color: "#a3b18a"

    MDBoxLayout:
        id:main_box
        text : "Convert from mad to jpy"
        orientation: "horizontal"
        size_hint: 1, .3
        pos_hint: {"center_x":.5, "center_y":.5}
        md_bg_color: "#ff0000"

        MDTextField:
            id:text
            hint_text: "enter an amount in mad"
            mode: "rectangle"
            size_hint: .7, .5
            md_bg_color: "ffffff"
            on_text: app.change()
        MDLabel:
            id:second_box



            text: "in jpy it is"


            md_bg_color:"fffff"
            on_text:app.change()
            mode:"rectangle"
            size_hint: .7, .5
            orientation: "vertical"



