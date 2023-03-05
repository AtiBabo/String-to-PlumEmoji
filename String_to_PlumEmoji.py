import clipboard
import tkinter
import tkinter.font

alphabetList = list("qwertyuiopasdfghjklzxcvbnm ")
supportList = list("qwertyuiopasdfghjklzxcvbnm 1234567890")
nomList = list("123467890")
nomEngList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]#이거 .split()으로 안 했다고 뭐라 하지마세요

window=tkinter.Tk()
window.title("String to Plum Emoji [0.0.3v]")
window.geometry("640x100")
window.resizable(False, False)

heheFont = tkinter.font.Font(family="맑은 고딕", size=15) 

def copyDef(event):
    iptcom = ""
    iptSt = list(entry.get())
    
    for i in range(0, len(iptSt)):
        if iptSt[i].lower() in supportList:
            if iptSt[i].lower() in alphabetList:
                if iptSt[i] == " ":
                    iptcom = iptcom + "  "
                else:
                    iptcom = iptcom + ":" + iptSt[i].upper() + "_: "
            elif str(iptSt[i]) in nomList:
                iptcom = iptcom + ":" + nomEngList[int(iptSt[i])] + ": "
        else:
            print("지원하지 않는 글자가 포함되어 있습니다.")
            infoLabel.config(text="지원하지 않는 글자가 포함되어 있습니다.", font=heheFont)
            break
    
    if iptSt[i].lower() in supportList:
        print(iptcom)
        infoLabel.config(text=iptcom, font=heheFont)
        clipboard.copy(iptcom)

entry=tkinter.Entry(window, width=70)
infoLabel=tkinter.Label(window)

entry.bind("<Return>", copyDef)

entry.pack()
infoLabel.pack()

window.mainloop()
