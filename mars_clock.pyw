import os
import threading
import time
import tkinter as tk
import tkinter.font as tkFont



def getMarsTime():

    millis = time.time()
    julianEpoch = 2440587.5 + (millis / 86400)
    terrestrialTime = julianEpoch + ((37 + 32.184) / 86400)
    since2kEpoch = terrestrialTime - 2451545
    marsSolDate = ((since2kEpoch - 4.5) / 1.027491252) + 44796 - 0.00096
    marsTime = (24 * marsSolDate) % 24
    return marsTime
    #print(time.strftime("%H:%M:%S", time.gmtime(marsTime * 3600)))


class MarsTimeWindow(tk.Frame):
    
    def __init__(self, master = None):

        # tk setup
        super().__init__(master)
        self.master = master

        self.createWidgets()
        

    def createWidgets(self):

        labelFrame = tk.Frame(self.master, width = 590, height = 161)
        # Create the label
        label = tk.Label(labelFrame)

        font = tkFont.Font(family = "Consolas", size = 100)
        label["text"] = "No time yet. Be patient nerd"
        label["font"] = font

        # Label frame configuration
        labelFrame.rowconfigure(0, weight = 1)
        labelFrame.columnconfigure(0, weight = 1)
        labelFrame.grid_propagate(0)

        labelFrame.grid(row = 1, column = 1)
        label.grid(sticky = "NESW")

        self.marsTimeLabel = label


        labelFrame = tk.Frame(self.master, width = 420, height = 80)
        # Create the label
        label = tk.Label()

        font = tkFont.Font(family = "Consolas", size = 20)
        label["text"] = "dims"
        label["font"] = font

        # Label frame configuration
        labelFrame.rowconfigure(0, weight = 1)
        labelFrame.columnconfigure(0, weight = 1)
        labelFrame.grid_propagate(0)

        # labelFrame.grid(row = 1, column = 1)
        # label.grid(sticky = "NESW")

        self.winDims = label


    def refresh(self, marsTime):
        
        self.marsTimeLabel["text"] = marsTime




root = tk.Tk()
root.title("Mars time")
# root.wm_minsize(1060, 640)
root.wm_maxsize(590, 161)
root.wm_minsize(590, 161)


timeWindow = MarsTimeWindow(root)






while True:




    # Refresh the window state
    timeWindow.refresh(time.strftime("%H:%M:%S", time.gmtime(getMarsTime() * 3600)))
    timeWindow.winDims["text"] = str(timeWindow.winfo_screenwidth()) + " x " + str(timeWindow.winfo_screenheight())

    # Force updates
    timeWindow.update_idletasks()
    timeWindow.update()


    # Console loop - deprecated
    """
    os.system("cls")
    print(time.strftime("%H:%M:%S", time.gmtime(getMarsTime() * 3600)))
    time.sleep(0.05)
    """