#chatbot
from datetime import datetime
import webbrowser
hello = ["hi","hello","hey","hey buddy","hie"]
bye = ["bye","bie","tata","see you later"]
date=["date","show me the date","date please"]
time=["time","show me the time","time please"]
while True:
    msg = input("Enter a Message : ").lower()
    if msg in hello:
        print("Hi...")
        
    elif msg in date:
        currdate=datetime.now()
        print(currdate.strftime("%d/%m/%y,%a"))
        
    elif msg in time:
        currtime=datetime.now()
        print(currtime.strftime("%l:%M:%S,%p"))
        
    elif msg.startswith("open"):
        msg=msg.split()[-1]
        webbrowser.open(f"https://www.{msg}.com/")
        
    elif msg in bye:
        print("Bye...")
        break
