# DESCRIPTION
A Mass media downloader for Windows, powered with [youtube-dl](https://github.com/ytdl-org/youtube-dl) and [Ffmpeg](https://ffmpeg.zeranoe.com/builds/)
# HOW TO INSTALL/BUILD
Everything required to run the prepackaged executable version of Grabbit can be found in [Executables, dependencies](https://github.com/TrashRat/Grabbit/raw/master/EXECUTABLE%20VERSION%2C%20DEPENDENCIES.zip). If you'd like to build the executable yourself, `pip install pyinstaller` and open a command prompt in the folder with **Grabbit!.pyw** and **grabbitbunny.ico**. Then,
`pyinstaller --onefile --noconsole --icon=grabbitbunny.ico Grabbit.pyw`. the **Dist** file will have the executable, all other generated files & folders can be deleted. Make sure **Grabbit!.exe** is in the same root folder as **youtube-dl.exe**, **ffmpeg.exe**, & **grabbitbunny.ico**, otherwise it will not run. To convert **updater.py**, `pyinstaller --onefile --noconsole updater.py` and delete everything except the executable, same as before.
# HOW TO USE
SDSDASDGASDGSADF
# DEPENDENCIES
Grabbit relies on [Youtube-dl.exe](https://yt-dl.org/latest/youtube-dl.exe) and [ffmpeg.exe](https://drive.google.com/uc?export=download&id=1EeMqfcI8w5rfU7wCIJEKgxO1waXgnvdb) for converting into mp4s/mp3s. 
Updater.exe/.py is not needed for normal use, but if you wish to update Grabbit.exe through the program instead of github, it is required.
