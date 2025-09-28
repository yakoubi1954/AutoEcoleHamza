cat > main.py <<'PY'
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label

class MenuScreen(Screen):
    pass

class AutoEcoleApp(App):
    def build(self):
        sm = ScreenManager()
        scr = MenuScreen(name="menu")
        scr.add_widget(Label(text="Menu AutoEcole — test OK"))
        sm.add_widget(scr)
        return sm

if __name__ == "__main__":
    AutoEcoleApp().run()
PY
python main.py
