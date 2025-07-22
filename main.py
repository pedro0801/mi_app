from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class MainWidget(BoxLayout):
    resultado_texto = StringProperty('')

    def presionar_boton(self):
        self.resultado_texto = '¡Botón presionado!'

class MiApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MiApp().run()

