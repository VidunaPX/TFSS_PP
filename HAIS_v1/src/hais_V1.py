
print("Starting HAIS GUI...")

import tkinter as tk  # noqa: E402
from tkinter import scrolledtext, Button, Label, END, DISABLED, NORMAL, BOTH, WORD  # noqa: E402
from main import set_open_api_key, get_myModel  # noqa: E402

#API Setup
set_open_api_key()

isRequestERROR = False

"""
if isConnected:
    print("API Key has been set successfully.")
else
    print("ER004: Failed to set API Key.")
    exit(1)
"""
#get_bot_response = ''
def isERROR(response):
    if "HAIS-ERROR:" in response:
        global isRequestERROR
        isRequestERROR = True
        print("Error Occurred; Send Button is Disabled")
        SendButton["state"] = DISABLED
        DisplayText.config(state=NORMAL)
        DisplayText.insert(END, "\n*** ALERT ***\nAn error has occurred, please try to resolve mentioned errors.\nSession has been terminated.\nClick Exit\n********************************\n")
        DisplayText.config(state=DISABLED)
# Function to get AI response from the model
def SendText():
    UserInput = InputText.get("1.0", END).strip()
    if UserInput:
        DisplayText.config(state=NORMAL)
        DisplayText.tag_configure("HAIS_response", foreground="Dark Blue")
        DisplayText.insert(END, "You: " + UserInput + "\n")
        get_bot_response = get_myModel(UserInput)
        DisplayText.insert(END, "\nHAIS: " + get_bot_response + "\n", "HAIS_response")
        DisplayText.config(state=DISABLED)
        DisplayText.see(END)
        InputText.delete("1.0", END)
        isERROR(get_bot_response)

def my_exit():
    DisplayText.config(state=NORMAL)
    DisplayText.insert(END, "\nIt was fun talking to you! \nHave a nice day! \nGoodbye!")
    DisplayText.config(state=DISABLED)
    root.after(3000, root.quit)

def my_exit():
    DisplayText.config(state=NORMAL)
    DisplayText.insert(END, "\nIt was fun talking to you! \nHave a nice day! \nGoodbye!")
    DisplayText.config(state=DISABLED)
    #await asyncio.sleep(5)
    root.after(10000, root.quit())
    #root.quit()
    #wait()

def enter_pressed(event):
    SendText()
    #print("Enter key pressed")



# GUI Setup
root = tk.Tk()
root.title("HAIS - AI Chatbot")
root.geometry("800x600")  # Increased width
root.minsize(500, 400)  # Set minimum size

print("Creating header...")
AppHeader = Label(root, text="HAIS", relief="flat", font=("Georgia", 20), bg="chartreuse4", fg="White", highlightthickness=0, borderwidth=0)
AppHeader.pack(fill=tk.X, pady=10)
print("Header created and packed.")

print("Creating display text...")
DisplayText = scrolledtext.ScrolledText(root, relief="flat", font=("Georgia", 13), bg="White", fg="Black", state=DISABLED, wrap=WORD, bd=0, highlightthickness=0)
DisplayText.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
print("Display text created and packed.")

# Similar debug prints for other widgets

# Input Text
InputText = scrolledtext.ScrolledText(root, relief="flat", font=("Georgia", 13), bg="Dark Grey", fg="Black", wrap=WORD, bd=0, highlightthickness=0, height=5)
InputText.pack(fill=tk.X, padx=10, pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, padx=10, pady=10)

SendButton = Button(button_frame, text="Send", bg="Green", font=("Georgia", 12), command=SendText)
SendButton.pack(side='right', padx=5)

#KeyBinding
root.bind("<Return>", enter_pressed)

ExitButton = Button(button_frame, text="Exit", bg="darkred", fg="black", font=("Georgia", 12), command=my_exit)
ExitButton.pack(side='left', padx=5)
root.mainloop()
print("HAIS GUI closed.")

#if not isRequestERROR:

#else:
   #SendButton.state = DISABLED
   # print("ERROR: Unable to set up the API.\n")
    
