import base64
with open("tortuga_bg.gif", "rb") as bg_gif:
    encoded_string = base64.b64encode(bg_gif.read())
print(encoded_string)

with open("tortuga_bg.py", "w") as bg_py:
    bg_py.write(f"tortuga_bg = {encoded_string}")
