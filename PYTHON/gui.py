
from guizero import App, Text, PushButton


app = App(title="MattyPi", width=1900, height=200, layout="grid")

button1 = PushButton(app, text="Relay1", grid=[1,0])
button2 = PushButton(app, text="Relay2", grid=[1,1])

app.display()