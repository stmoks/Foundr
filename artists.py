# The code will cover the design of a platform where the artist can post items and the user can 
# search for artists.

import tkinter


window = tkinter.Tk()

window.title("Artist")
window.minsize(width=500,height=500)


# Label
artist_header = tkinter.Label(text="Artist interface",font = ("Arial",15,"bold"))
artist_header.grid(column=2,row=3)

artistname_label = tkinter.Label(text="Artist name",font = ("Arial",11))
artistname_label.grid(column=1,row=3)

# Button
def continue_button():
    artistname_label["text"] = "The button has been clicked"
    artist_header["text"] = input.get()

button = tkinter.Button(text="Continue",command=continue_button)
#button.pack(side="left")

# Entry
input = tkinter.Entry()
#input.pack(side="left")


window.mainloop()