import tkinter
import json

def update_needshelp(data_index: int, button: tkinter.Button) -> None:
    # Update the data
    data[data_index]['NEEDSHELP'] = 0
    # Save back to JSON
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    # Remove the button
    button.destroy()

def refresh_gui():
    global data, frame
    # Reload data
    with open('data.json', 'r') as f:
        data = json.load(f)
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()
    # Recreate buttons
    for i, item in enumerate(data):
        if item['NEEDSHELP'] == 1:
            button = tkinter.Button(frame, text=f"Name: {item['NAME']}")
            button.config(command=lambda idx=i, btn=button: update_needshelp(idx, btn))
            button.pack(anchor='w')



m = tkinter.Tk()

# Load data from data.json
with open('data.json', 'r') as f:
    data = json.load(f)

# Create a frame for the data display
frame = tkinter.Frame(m)
frame.pack(pady=10)

# Dynamically add buttons for items where NEEDSHELP == 1
for i, item in enumerate(data):
    if item['NEEDSHELP'] == 1:
        button = tkinter.Button(frame, text=f"Name: {item['NAME']}")
        button.config(command=lambda idx=i, btn=button: update_needshelp(idx, btn))  # Proper closure
        button.pack(anchor='w')

m.mainloop()