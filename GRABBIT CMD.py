"""
A youtube downloader/ripper that uses youtube-dl.exe and ffmpeg.exe to convert and download video.
I know there's a youtube-dl python module and i don't have to pipe it to the terminal using subprocess,
but this is easier and i figured this one out first!
Hamfisted by your humble and gracious overlord, REED 2/19/19
"""

from subprocess import call
import colorama
from colorama import Fore, Back, Style
colorama.init()
commands = ["1","2","3","4","5"]
var = True

print(Style.BRIGHT + Fore.RED + """ _____              _      _      _  _    _
|  __ \            | |    | |    (_)| |  | |
| |  \/ _ __  __ _ | |__  | |__   _ | |_ | |   //
| | __ | '__|/ _` || '_ \ | '_ \ | || __|| |  ('>
| |_\ \| |  | (_| || |_) || |_) || || |_ |_|  /rr
 \____/|_|   \__,_||_.__/ |_.__/ |_| \__|(_) *\))_
"""+ Style.RESET_ALL)


while var == True:
    
    print(Style.BRIGHT + Fore.YELLOW +"""1. Download Video(.mp4)
2. Download Song(.mp3)
3. Download video playlist
4. Download music playlist
5. Help/Troubleshooting
6. Quit"""+ Style.RESET_ALL)

    
    print(Style.BRIGHT + Fore.RED + "Select Number"+ Style.RESET_ALL)
    command = input("")

    
    if command == "1":
        print(Style.BRIGHT + Fore.RED + "Input Video URL" + Style.RESET_ALL)
        link = input("")
        call(["youtube-dl","--retries","15","--format", "bestvideo+bestaudio[ext=m4a]/bestvideo+bestaudio/best","--merge-output-format", "mp4","-o","%(title)s.%(ext)s", link], shell=True)
  
    if command == "2":
        print(Style.BRIGHT + Fore.RED + "Input Song URL" + Style.RESET_ALL)
        link = input("")
        call(["youtube-dl","--retries", "15", "--extract-audio","--audio-format", "mp3", "-o", "%(title)s.%(ext)s", link], shell=True)
        
    if command == "3":
        print(Style.BRIGHT + Fore.RED + "Video playlist URL MUST contain" + Style.RESET_ALL + Style.BRIGHT + Fore.GREEN + " playlist?list=" + Style.RESET_ALL + Style.BRIGHT + Fore.RED +" to work properly" + Style.RESET_ALL)        
        link = input("")
        call(["youtube-dl","--retries","15","--format", "bestvideo+bestaudio[ext=m4a]/bestvideo+bestaudio/best","--merge-output-format", "mp4","-o","%(playlist_index)s-%(title)s.%(ext)s", link], shell=True)
        
    if command == "4":
        print(Style.BRIGHT + Fore.RED + "Music playlist URL MUST contain" + Style.RESET_ALL + Style.BRIGHT + Fore.GREEN + " playlist?list=" + Style.RESET_ALL + Style.BRIGHT + Fore.RED +" to work properly" + Style.RESET_ALL)         
        link = input("")
        call(["youtube-dl","--retries", "15", "--extract-audio","--audio-format", "mp3", "-o", "%(playlist_index)s-%(title)s.%(ext)s", link], shell=True)
        
    if command == "5":
        responses = ["1","2"]
        print(Style.BRIGHT + Fore.YELLOW + """1. Cant copy/paste into the console
2. First video/song in playlist is the only thing downloaded""")
        print(Style.BRIGHT + Fore.RED + "Select Number"+ Style.RESET_ALL)
        
        question = input("")
        if question == "1":
            print(Style.BRIGHT + Fore.CYAN + "Right-click console --> properties --> Under 'edit options', enable QuickEdit mode,\n Insert mode, and Enable Ctrl key shortcuts. If ctrl+v doesnt work, try right-clicking\n"+ Style.RESET_ALL)
            pass
        if question == "2":
            print(Style.BRIGHT + Fore.CYAN + "You need to make sure the playlist URL contains 'playlist?list=', you can get to this by clicking 'view full playlist' \nin search results, or on the playlist name.")
            print(Style.BRIGHT + Fore.CYAN + "GOOD URL: https://www.youtube.com/"+ Style.RESET_ALL+ Style.BRIGHT + Fore.GREEN +"playlist?list="+ Style.RESET_ALL + Style.BRIGHT + Fore.CYAN+"OLAK5uy_nVfY4cK802ME288AZBdeveHZZ6kJRwPdU")
            print(Style.BRIGHT + Fore.CYAN + "BAD URL: https://www.youtube.com/"+ Style.RESET_ALL + Style.BRIGHT + Fore.RED +"watch?v="+ Style.RESET_ALL + Style.BRIGHT + Fore.CYAN +"85QQlGuKGwo&list=OLAK5uy_nVfY4cK802ME288AZBdeveHZZ6kJRwPdU&index=1\n"+ Style.RESET_ALL)
            pass
        if question not in responses:
            print(Style.BRIGHT + Fore.RED + "invalid response, returning to options selection.." + Style.RESET_ALL)
            pass
        
    if command == "6":
        quit()
    
    if command not in commands:
        print(Style.BRIGHT + Fore.RED + '"%s"'%command + " is not an option..." )
        
    

    
    
