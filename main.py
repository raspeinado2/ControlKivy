from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.metrics import dp

class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            orientation='vertical',
            padding=dp(16),
            spacing=dp(24),
            **kwargs
        )

        # Fondo blanco + bisel gris de 2dp
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self._bg = Rectangle(pos=self.pos, size=self.size)
            Color(169/255, 169/255, 169/255, 1)  # DarkGray
            self._border = Line(
                rectangle=(self.x, self.y, self.width, self.height),
                width=dp(2)
            )
        self.bind(pos=self._update_canvas, size=self._update_canvas)

        # Fila de 5 ToggleButtons
        fila = BoxLayout(
            size_hint=(1, None),
            height=dp(50),
            spacing=dp(8)
        )
        self.add_widget(fila)

        # Colores exactos de Windows (hex convertidos a RGBA)
        self.active_colors = [
            (0, 1, 0, 1),            # #00ff00
            (0, 0, 1, 1),            # #0000ff
            (1, 1, 0, 1),            # #ffff00
            (128/255, 0, 128/255, 1),# #800080
            (1, 165/255, 0, 1)       # #ffa500
        ]
        self.default_color = (240/255, 240/255, 240/255, 1)  # #f0f0f0

        self.toggles = []
        for i, col in enumerate(self.active_colors):
            tb = ToggleButton(
                text=f"Botón {i+1}",
                size_hint=(1, 1),
                background_normal='',
                background_down='',
                background_color=self.default_color
            )
            tb.color_active = col
            tb.bind(state=self.on_toggle)
            fila.add_widget(tb)
            self.toggles.append(tb)

        # Fila inferior: recuadro rojo + botón Reset
        fila_inf = BoxLayout(
            size_hint=(1, None),
            height=dp(70),
            spacing=dp(16)
        )
        self.add_widget(fila_inf)
        fila_inf.add_widget(Widget())  # spacer izquierdo

        # Recuadro rojo (oculto inicialmente)
        self.red_box = Widget(
            size_hint=(None, None),
            size=(dp(50), dp(50))
        )
        with self.red_box.canvas:
            Color(1, 0, 0, 1)
            self._r = Rectangle(pos=self.red_box.pos, size=self.red_box.size)
        self.red_box.bind(pos=self._upd_red, size=self._upd_red)
        self.red_box.opacity = 0
        fila_inf.add_widget(self.red_box)

        # Botón Reset
        reset = Button(
            text="R",
            size_hint=(None, None),
            size=(dp(60), dp(60)),
            background_normal='',
            background_down='',
            background_color=(211/255, 211/255, 211/255, 1)  # lightgray
        )
        reset.bind(on_press=self.on_reset)
        fila_inf.add_widget(reset)
        fila_inf.add_widget(Widget())  # spacer derecho

    def _update_canvas(self, *args):
        self._bg.pos = self.pos
        self._bg.size = self.size
        self._border.rectangle = (self.x, self.y, self.width, self.height)

    def _upd_red(self, widget, _):
        self._r.pos = widget.pos
        self._r.size = widget.size

    def on_toggle(self, instance, state):
        # Aplica color activo o default al botón
        instance.background_color = instance.color_active if state == 'down' else self.default_color
        # Muestra u oculta el recuadro rojo si todos están activos
        self.red_box.opacity = 1 if all(tb.state == 'down' for tb in self.toggles) else 0

    def on_reset(self, _):
        # Reinicia todos los toggles y oculta el recuadro rojo
        for tb in self.toggles:
            tb.state = 'normal'
            tb.background_color = self.default_color
        self.red_box.opacity = 0

class ControlApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    ControlApp().run()
