from data import *
from tkinter import *
from datetime import date
import requests
import json
import locale

locale.setlocale(locale.LC_TIME, "fi_FI")

now = date.today()
rest_nro = 164 #Sodexo ravintolan nro
url = "https://www.sodexo.fi/ruokalistat/output/daily_json/"+str(rest_nro) + "/" + str(now)
formtd_day = now.strftime("%A %d. ").capitalize() + now.strftime("%B").capitalize()
bg_color = "#EAFFE5"#"lightgrey"

def menu(data, nro):
    try:
        theJSON = json.loads(data)
        if "dietcodes" in theJSON["courses"][str(nro)]:
            return theJSON["courses"][str(nro)]["title_fi"]+"\n"+theJSON["courses"][str(nro)]["dietcodes"]+"\n"+theJSON["courses"][str(nro)]["price"]
        return theJSON["courses"][str(nro)]["title_fi"]+"\n"+theJSON["courses"][str(nro)]["price"]
    except:
        return 1
        
def get_content():
    try:
        r = requests.get(url)
        return r.content
    except:
        return "Error on request"

def main():
    lunch = []
    root = Tk()
    root.title("Ruokalista")
    root.geometry("480x360+680+240")
    root.configure(bg=bg_color)

    day = Label(root, text= formtd_day + "\n", font="Arial 18 bold", bg=bg_color)
    day.pack()

    if menu(get_content(), 1) != 1:
        for i in range(4):
            lunch.append(Label(root, text=str(menu(get_content(), i+1))+ "\n", font="Arial 12",bg=bg_color))
            lunch[i].pack()
    else:         
        err_msg = Label(root, text="Tänään ei lounasta", font="Arial 12",bg=bg_color)
        err_msg.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
