from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):

    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        self.result = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.result)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        # Add Facebook icon button
        facebook_button = Button(background_normal="facebook_icon.jpeg", size_hint=(None, None), size=(50, 50))
        facebook_button.bind(on_press=self.on_facebook_like)
        layout.add_widget(facebook_button)

        # Add Instagram icon button
        instagram_button = Button(background_normal="instagram_icon.jpeg", size_hint=(None, None), size=(50, 50))
        instagram_button.bind(on_press=self.on_instagram_like)
        layout.add_widget(instagram_button)

        # Add YouTube icon button
        youtube_button = Button(background_normal="youtube_icon.jpeg", size_hint=(None, None), size=(50, 50))
        youtube_button.bind(on_press=self.on_youtube_like)
        layout.add_widget(youtube_button)

        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)
        return layout

    # Other functions (on_button_press, on_solution) remain unchanged

    def on_facebook_like(self, instance):
        self.result.text = "Liked on Facebook!"

    def on_instagram_like(self, instance):
        self.result.text = "Liked on Instagram!"

    def on_youtube_like(self, instance):
        self.result.text = "Liked on YouTube!"

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
