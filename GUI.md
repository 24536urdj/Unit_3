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
