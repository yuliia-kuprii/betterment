
### How to create an exe
To make a build, run
```pyinstaller --clean --onefile --windowed --noconfirm --icon "tortuga_icon.icns" gui_speedapp.py``` 

***
### How to update a background image 
The issue caused by the inability to find the background image with .gif extension after creating an exe file.
The following info is a way how to solve this issue about not opening an exe file on another computer.

If you want to change background, you have to convert the .gif file to base64.
For that there is a `convert_gif_to_base64.py` script that takes the `tortuga_bg.gif` image and
creates a `tortuga_bg.py` file with the image content. 
Then the `tortuga_bg.py` is used in the main `gui_speedapp.py` file as a background image.

So, you just change the image, rename it in the `convert_gif_to_base64.py` (if needed), and run
```python convert_gif_to_base64.py```

After new build the background image should be updated.
End user can run 'Tortuga Rapida' without python installation on its Mac. 
