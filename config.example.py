from os import getlogin

wallpaper = "YOUR WALLPAPER DIRECTORY" # your wallpaper path

fontcolor = "#4b526d" # text color

fontpath = '/usr/share/fonts/TTF/iosevka-medium.ttf' # your font's path
envpath = 'YOUR ENV FILE PATH' # your env file path: required for genius lyrics api

persist_wallpapers = False # False by default. ENABLE IF YOU WILL USE A DE RATHER THAN FEH.
persistent_wallpapers_dir = f'/home/{getlogin()}/.walyrics/' # if you get an error saying .walyrics folder is not found then simply create it using mkdir.

marquee = True # True by default
marquee_pixels = 15 # pixels to move lyrics up
marquee_sleep = 0.7 # seconds to sleep

show_thumbs = True # Show thumbs by default
thumbsize = 150 # Thumbnail size

fontsize = 14 # Font size for lyrics

cinnamon = False # Cinnamon DE support

offset_x = 25 # X axis offset
offset_y = 25 # Y axis offset

randlimit = 1000 # Random limit for temporary pictures
charlimit = (1366 // fontsize) * (768 // fontsize) # You can replace 1366 with your screen width and 768 with your screen height.
