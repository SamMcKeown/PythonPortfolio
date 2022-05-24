import pathlib
import tkinter as tk 
from tkinter import Label, filedialog, Text
import os, subprocess

## The parent window
root = tk.Tk() 

## Files selected will be stored here
files_to_open = [] 

## Before application is run
if os.path.isfile('saved_labels.txt'):
    with open('saved_labels.txt', 'r') as f:
        tempFiles = f.read()
        # Creates array
        tempFiles = tempFiles.split(',')
        # Removes whitespace
        files = [x for x in tempFiles if x.strip()]
        # Saved labels
        for file in files:
            files_to_open.append(file)
        
## Button command
def addFile():
    '''
    Attaches selected file to the frame of root canvas
    
    - Removes any duplicate labels from the frame before prompting the 
    user to select a file (of any filetype) from a specified directory
    - File is then appended to a list &  a label widget is created to
    display the file name text of the selected file
    '''
    for fileLabel in frame.winfo_children():
        fileLabel.destroy() 

    filetypes = ('all files', '*.*')
    filename = filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=[filetypes])
    files_to_open.append(filename)

    for file in files_to_open:  
        ## Label: widget to display text
        label = tk.Label(master=frame, text=file, bg='light blue')
        label.pack()

## Button commad
def runSelected():
    ''' Opens selected file(s) attached to the frame of the root canvas'''
    for file in files_to_open:
        subprocess.call(['open', file])

## Canvas: to place graphics, text, widgets or frames
canvas = tk.Canvas(master=root, height=500, width=500, bg='#FFA07A')
canvas.pack()

## Frame: to group/organise other widgets
frame = tk.Frame(master=root, background='white')
frame.place(relheight=0.6, relwidth=0.8, relx=0.1, rely=0.1)

## Button: widget to add button to the root canvas
openFile = tk.Button(master=root, text='Select File', padx=10, pady=5, fg='#FFA07A', command=addFile)
openFile.pack()

## Button: widget torun selected files
runFile = tk.Button(master=root, text='Run File(s)', padx=10, pady=5, fg='#FFA07A', command=runSelected)
runFile.pack()

## Displays text in specified colour if read directly from txt file
for files in files_to_open:
    label = tk.Label(frame, text=files, bg='light green')
    label.pack()

## Runs the application
root.mainloop() 

## Generates a txt file when the application is closed
with open('saved_labels.txt', 'w') as f:
    for files in files_to_open:
        f.write(files + ', ')