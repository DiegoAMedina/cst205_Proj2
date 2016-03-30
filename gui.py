########## todo: add the "command = function" on line 38 to run the program when the button is pressed


#imports everything from Tkinter
from Tkinter import *


#main window
root = Tk()



########### FRAME

#top frame 
topFrame = Frame(root)
topFrame.pack()
#bottom frame
bottomFrame = Frame(root)
bottomFrame.pack()




########### PHOTOS

#creates a photo object
csumbPhoto = PhotoImage(file = "csumbLogo.png")
mozaicWordPhoto = PhotoImage(file = "mozaicGroupTxt.png")

#label with the photo object
csumbLabel = Label(topFrame, image = csumbPhoto)
csumbLabel.pack()

mozaicWordLabel = Label(topFrame, image = mozaicWordPhoto)
mozaicWordLabel.pack()





############ BUTTON

#mozaic button to compile
mozaicButton = Button(bottomFrame, width = 60, height = 5, text = "Start", fg = "navy", bg = "white", )
mozaicButton.bind()
mozaicButton.pack()



#infinite loop so the window will continue to display
root.mainloop()


