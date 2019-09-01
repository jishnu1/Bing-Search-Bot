import webbrowser
import time

url = "https://www.bing.com/search?q="
ch = 'A'
# 150 pts
for i in range(0, 30):
    webbrowser.open(url+ch, new=0)
    # webbrowser.open(url+ch+ch, new=0)     | uncomment for days
    # time.sleep(1)                         | with double points
    ch = chr(ord(ch) + 1)
    time.sleep(1)
    
