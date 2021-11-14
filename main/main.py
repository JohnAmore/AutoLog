# Course: CSC-107-A# Name: Daniel Bennett# ID: 0593616# E-mail: ddbennett@cn.edu# IMPORTSfrom tkinter import *from classes.jsonConvert import *from classes.webDrive import *# CONSTANTSTITLE = "AutoLog"WINDOW_SIZE = "1024x768"# JSON DATAdata = jsonConvert()loginJSON = data.loadJson()# Opens and logs into websitedef logToService(jsonFile, service):    service = service.lower()    url = jsonFile['websites'][service]['url']    user = jsonFile['websites'][service]['username']    pw = jsonFile['websites'][service]["password"]    htmlUser = jsonFile['websites'][service]['Login_Element']    htmlPw = jsonFile['websites'][service]['Password_Element']    htmlButton = jsonFile['websites'][service]['Login_Button']    web = webDrive()    web.login(url, user, pw, htmlUser, htmlPw, htmlButton)# GUI INITWindow = Tk()Window.title(TITLE)Window.geometry(WINDOW_SIZE)  # Creates GUI Object and sets window size and title.# DESIGNdef removeWidgets(label, button1, button2, currentState, button3=None, button4=None):    label.place_forget()    button1.place_forget()    button2.place_forget()    if button3 is not None:        button3.place_forget()    if button4 is not None:        button4.place_forget()    for i in range(2):        if currentState == 0:            start()            break        elif currentState == 1:            selectionMenu()            break        elif currentState == 2:            servicesMenu()            break        elif currentState == 3:            editLoginInfo()            break        elif currentState == 7:            editInfoScreen('netflix')        elif currentState == 8:            editInfoScreen('canvas')        else:            currentState -= 1# Updates JSON data and returns to selectionMenu (BUGGED WINDOWS)def getAndSet(service, title, user, pw, pwEnt, button, dataJSON=loginJSON, ):    inputVal = [user.get(), pwEnt.get()]    if service == 'netflix':        dataJSON['websites']['netflix']['username'] = inputVal[0]        dataJSON['websites']['netflix']['password'] = inputVal[1]    else:        dataJSON['websites']['canvas']['username'] = inputVal[0]        dataJSON['websites']['canvas']['password'] = inputVal[1]        data.dumpJson(dataJSON)    # Return to selection Menu    removeWidgets(title, user, pw, 1, button3=button, button4=pwEnt)# Design for the editing screendef editInfoScreen(serv):    title = Label(text="Username", pady=30)    title.configure(font=('Helvetica', 24))    user = Entry(width=40)    user.configure(font=('Helvetica', 24))    pw = Label(text="Password", pady=30)    pw.configure(font=('Helvetica', 24))    pwEnt = Entry(width=40)    pwEnt.configure(font=('Helvetica', 24))    submit = Button(text="Submit", font=('Helvetica', 24), pady=10, padx=15)    title.place(rely=.05, relx=.45)    user.place(relx=.225, rely=.2)    pw.place(rely=.3, relx=.45)    pwEnt.place(relx=.225, rely=.4)    submit.place(relx=.44, rely=.6)    submit.configure(        command=lambda a=serv, b=title, c=user, d=pw, e=pwEnt, f=submit: getAndSet(a, b, c, d, e, f))# Window for logging into specified servicesdef servicesMenu():    title = Label(text="Select the following: ", pady=30)    title.configure(font=('Helvetica', 24))    netflixButton = Button(text="Netflix", pady=20, padx=32,                           command=lambda file=loginJSON, service='netflix': logToService(file, service))    netflixButton.configure(font=('Helvetica', 24))    canvasButton = Button(text="Canvas", pady=20, padx=25,                          command=lambda file=loginJSON, service='canvas': logToService(file, service))    canvasButton.configure(font=('Helvetica', 24))    backSelect = Button(text="Back", pady=10, padx=15)    backSelect.configure(font=('Helvetica', 24),                         command=lambda a=title, b=netflixButton, c=canvasButton, e=backSelect, d=1: removeWidgets(a, b,                                                                                                                   c, d,                                                                                                                   e))    title.place(rely=.05, relx=.4)    netflixButton.place(relx=.425, rely=.3)    canvasButton.place(relx=.425, rely=.45)    backSelect.place(relx=.45, rely=.7)# Window for deciding to edit specified servicesdef editLoginInfo():    title = Label(text="Select the following: ", pady=30)    title.configure(font=('Helvetica', 24))    netflixEdit = Button(text="Netflix", pady=10, padx=32, )    netflixEdit.configure(font=('Helvetica', 24))    canvasEdit = Button(text="Canvas", pady=10, padx=25)    canvasEdit.configure(font=('Helvetica', 24))    backSelect = Button(text="Back", pady=10, padx=15)    backSelect.configure(font=('Helvetica', 24),                         command=lambda a=title, b=netflixEdit, c=canvasEdit, e=backSelect, d=1: removeWidgets(a, b, c,                                                                                                               d, e))    netflixEdit.configure(        command=lambda a=title, b=netflixEdit, c=canvasEdit, d=7, e=backSelect: removeWidgets(a, b, c, d, e))    canvasEdit.configure(        command=lambda a=title, b=netflixEdit, c=canvasEdit, d=8, e=backSelect: removeWidgets(a, b, c, d, e))    title.place(rely=.05, relx=.4)    netflixEdit.place(relx=.425, rely=.3)    canvasEdit.place(relx=.425, rely=.45)    backSelect.place(relx=.45, rely=.7)# Main Menu Windowdef selectionMenu():    title = Label(text="Select the following: ", pady=30)    title.configure(font=('Helvetica', 24))    serviceSelect = Button(text="Go to a service", pady=10, padx=15)    serviceSelect.configure(font=('Helvetica', 24))    editSelect = Button(text="Edit your service login information", pady=10, padx=15)    editSelect.configure(font=('Helvetica', 24))    backSelect = Button(text="Back", pady=10, padx=15)    backSelect.configure(font=('Helvetica', 24),                         command=lambda a=title, b=serviceSelect, c=editSelect, e=backSelect, d=0: removeWidgets(a, b,                                                                                                                 c, d,                                                                                                                 e))    serviceSelect.configure(        command=lambda a=title, b=serviceSelect, c=editSelect, e=backSelect, d=2: removeWidgets(a, b, c, d, e))    editSelect.configure(        command=lambda a=title, b=serviceSelect, c=editSelect, e=backSelect, d=3: removeWidgets(a, b, c, d, e))    title.place(rely=.05, relx=.4)    serviceSelect.place(relx=.4, rely=.3)    editSelect.place(relx=.3, rely=.5)    backSelect.place(relx=.45, rely=.7)# Start Menudef start():    title = Label(text="AutoLog", pady=40)  # Title Label    title.configure(font=('Helvetica', 36))    exitButton = Button(text='Exit', pady=10, padx=25, command=exit)    startButton = Button(text='Start', pady=10, padx=20)    startButton.configure(font=('Helvetica', 24),                          command=lambda a=title, b=startButton, c=exitButton, d=1: removeWidgets(a, b, c, d))    exitButton.configure(font=('Helvetica', 24))    title.place(relx=.45, rely=.05)    startButton.place(relx=.45, rely=.5)    exitButton.place(relx=.45, rely=.6)# Main Functiondef main():    start()    Window.mainloop()main()