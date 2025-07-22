from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainWidget(BoxLayout):
    def on_button_press(self):
        self.ids.label_resultado.text = '¡Botón presionado!'

class MiApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MiApp().run()