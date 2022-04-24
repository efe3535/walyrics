from os import getlogin

wallpaper = "YOUR WALLPAPER DIRECTORY"

fontcolor = "#4b526d"

fontpath = '/usr/share/fonts/TTF/iosevka-medium.ttf'
envpath = 'YOUR ENV FILE PATH'

persist_wallpapers = True # False by default.
persistent_wallpapers_dir = f'/home/{getlogin()}/.walyrics/' # if you get an error saying .walyrics folder is not found then simply create it using mkdir.

thumbsize = 150 # Thumbnail size
fontsize = 14 # Font size for lyrics
offset_x = 25 # X axis offset
offset_y = 25 # Y axis offset
randlimit = 1000 # Random limit for temporary pictures
charlimit = (1366 // fontsize) * (768 // fontsize) # You can replace 1366 with your screen width and 768 with your screen height.
