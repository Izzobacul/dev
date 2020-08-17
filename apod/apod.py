#!/usr/bin/env python

import requests
import json
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk
from textwrap import wrap

with open('auth.json', 'r') as auth:
    key = json.load(auth)['api_key']

r = requests.get('https://api.nasa.gov/planetary/apod', params={'api_key':key})
data = json.loads(r.text)
exp = '\n'.join(wrap(data['explanation'], 40))

image = requests.get(data['url'])
img = Image.open(BytesIO(image.content))

root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}")
root['bg']="black"

render = ImageTk.PhotoImage(img)
panel = tk.Label(root, image = render, bg="black")
panel.pack(side = "left", fill = "both", expand = "yes")

explanation = tk.Label(root, text=exp, bg="black", fg="white", width=50, )
explanation.pack(side = "right", fill = "both", expand = "yes")

root.mainloop()
