### 
            ScreenManager:
            id:scr_manager

            IntroScreen:
                name:"IntroScreen"
            DarkMood:
                name:"DarkMood"
        <IntroScreen>
                size:500,500
                MDBoxLayout:
                    id:second_box

                    halign:"center"
                    orientation: "horizontal"

                    MDLabel:
                        id:counter_label
                        text: "Your Name"
                        font_size: 60
                        color: "#283618"

                        halign:"center"
                    MDRaisedButton:

                        id:add_btn
                        text:"Dark mode"
                        halign:"right"

                        on_press:root.parent.current ="DarkMood"
            <DarkMood>
                MDBoxLayout:
                    id: DarkMood
                    md_bg_color:"00000"
                    MDLabel:
                        text:"Your Name"
                        color:"ffff0"
                        font_size:"60"
                        halign:"center"



