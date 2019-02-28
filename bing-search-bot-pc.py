import webbrowser
import time

url = "https://www.bing.com/search?q="
ch = 'A'

for i in range(0, 30):
    webbrowser.open(url+ch, new=0)
    ch = chr(ord(ch) + 1)
    time.sleep(1)
