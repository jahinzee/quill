import tkinter
from tkinter import scrolledtext
from tkinter.constants import BOTTOM, DISABLED, FLAT, LEFT, NW, SE, SW, TOP, W, WORD
from tkinter import IntVar, StringVar

qTracker = 0
qList = [
    ["1", "Enter your Tax File Number (TFN)", "See the Privacy note on the ATO website", "ol", ""],
    ["2", "Are you an Australian resident?", "", "sc", "Yes", "No"],
    ["3", "Enter your full name", "Format: Title Surname, Given Name", "ol", ""],
    ["4", "Have any part of your name changed since completing your last tax return?", "", "sc", "Yes", "No"],
    ["5", "Enter your postal address", "Print the address where you want your mail sent.", "fr", ""],
    ["6", "Has your address changed since completing your last tax return?", "", "sc", "Yes", "No"],
    ["7", "Is your home address different from your postal address?", "", "sc", "Yes", "No"],
    ["8", "Your contact details", "Enter your phone number.\n\nYour contact details may be used by the ATO:\n- to advise you of tax return lodgment options\n- to correspond with you with regards to your taxation and superannuation affairs\n- to issue notices to you, or\n- to conduct research and marketing.", "ol", ""],
    ["9", "Your contact details", "Enter your email address.\n\nYour contact details may be used by the ATO:\n- to advise you of tax return lodgment options\n- to correspond with you with regards to your taxation and superannuation affairs\n- to issue notices to you, or\n- to conduct research and marketing.", "ol", ""],
    ["10", "Will you need to lodge an Australian tax return in the future?", "", "sc", "Yes", "No", "Don't Know"],
    ["11", "Enter your date of birth", "If you were under 18 years old on 30 June 2020 you must complete the A1 Under 18 form.\n\nFormat: dd/mm/yyyy", "ol", ""],
    ["12", "Electronic funds transfer (EFT)", "We need your financial institution details to pay any refund owing to you, even if you have provided them to us\nbefore.\n\nEnter your BSB number (must be six digits)", "ol", ""],
    ["13", "Electronic funds transfer (EFT)", "We need your financial institution details to pay any refund owing to you, even if you have provided them to us\nbefore.\n\nEnter your account number (must be nine digits)", "ol", ""],
    ["14", "Electronic funds transfer (EFT)", "We need your financial institution details to pay any refund owing to you, even if you have provided them to us\nbefore.\n\nEnter your account name (for example, Rick Astley.\nDo not show the account type, such as cheque, savings, mortgage offset)", "ol", ""],
    ["15", "Form complete.", "Thank you for completing Part I of the Tax Return for Individuals form.", ""],
]


class Styles:
    fTitleText = ("Segoe UI", 14)
    fSymbol = ("Segoe UI Symbol", 11)
    fMain = ("Segoe UI", 11)
    fAccent = ("Segoe UI", 11, "bold")
    cMainBackground = "#FFE8D1"
    cHighlightBackground = "#AC5600"
    xPadX = 5
    xPadY = 20

window = tkinter.Tk()
window.title("Tax Return for Individuals (Demo) - Quill")
window.geometry("800x600")
window.configure(bg = Styles.cMainBackground)
window.iconbitmap('favicon.ico')

def draw(content):
    for widget in window.winfo_children():
        widget.destroy()

    titleText = tkinter.StringVar(window, value=content[1])
    descriptionText = tkinter.StringVar(window, value=content[2])

    tkinter.Frame(window).pack(side=TOP, anchor=NW, pady=Styles.xPadX*2, padx=Styles.xPadY)

    questionHeader = text = tkinter.Label(
        window,
        bg=Styles.cMainBackground,
        fg=Styles.cHighlightBackground,
        font=Styles.fAccent,
        relief=FLAT,
        text="QUESTION "+content[0]
    ).pack(side=TOP, anchor=NW, pady=Styles.xPadX/2, padx=Styles.xPadY)


    title = tkinter.Label(
        window,
        bg=Styles.cMainBackground,
        fg="#000000",
        font=Styles.fTitleText,
        relief=FLAT,
        justify=LEFT,
        textvariable=titleText,
    ).pack(side=TOP, anchor=NW, pady=Styles.xPadX, padx=Styles.xPadY)

    if content[2] != "":
        text = tkinter.Label(
            window,
            bg=Styles.cMainBackground,
            fg="#000000",
            font=Styles.fMain,
            relief=FLAT,
            justify=LEFT,
            textvariable=descriptionText
        ).pack(side=TOP, anchor=NW, pady=Styles.xPadX, padx=Styles.xPadY)

    tkinter.Frame(window).pack(side=TOP, anchor=NW, pady=Styles.xPadX*2, padx=Styles.xPadY)

    if content[3] == "sc":
        choice = IntVar(window)
        for i in range (4, len(content)):
            tkinter.Radiobutton(
                window,
                bg=Styles.cMainBackground,
                fg="#000000",
                font=Styles.fMain,
                variable=choice,
                value=i-2,
                width=50,
                anchor=W,
                text=content[i]
            ).pack(side=TOP, anchor=NW, pady=Styles.xPadX, padx=Styles.xPadY)

    if content[3] == "mc":
        choice = {}
        for i in range (4, len(content)):
            choice[i] = IntVar(window)
            tkinter.Checkbutton(
                window,
                bg=Styles.cMainBackground,
                fg="#000000",
                font=Styles.fMain,
                variable=choice[i],
                width=50,
                anchor=W,
                text=content[i]
            ).pack(side=TOP, anchor=NW, pady=Styles.xPadX, padx=Styles.xPadY)

    if content[3] == "ol":
        response = StringVar(window, value=content[4])
        a = tkinter.Entry(
            window,
            bg="#FFFFFF",
            fg="#000000",
            font=Styles.fMain,
            textvariable=response,
            width=50,
        ).pack(side=TOP, anchor=NW, pady=Styles.xPadX, padx=Styles.xPadY)

    if content[3] == "fr":
        a = scrolledtext.ScrolledText(
            window,
            wrap=WORD,
            bg="#FFFFFF",
            fg="#000000",
            font=Styles.fMain,
            width=50,
            height=10
        ).pack(side=TOP, anchor=NW, pady=Styles.xPadX, padx=Styles.xPadY)

    # Footer
    currentPage = qTracker + 1
    totalPages = len(qList)

    tkinter.Frame(window).pack(side=BOTTOM, pady=Styles.xPadX, padx=Styles.xPadY)

    tkinter.Button(
        window,
        bg=Styles.cMainBackground,
        fg="#000000",
        font=Styles.fMain,
        relief=FLAT,
        justify=LEFT,
        text=str(currentPage) + " out of " + str(totalPages) + "  —  Quill Prototype Demo (created 17th July 2021)",
        state=DISABLED
    ).pack(side=BOTTOM, anchor=SW, pady=Styles.xPadX, padx=Styles.xPadY)

    f = tkinter.Button(
        window,
        bg=Styles.cMainBackground,
        fg="#000000",
        font=Styles.fMain,
        relief=FLAT,
        justify=LEFT,
        text="    Next ",
        command=lambda: nextItem(None)
    ).pack(side=BOTTOM, anchor=SW, pady=Styles.xPadX, padx=Styles.xPadY)

    b = tkinter.Button(
        window,
        bg=Styles.cMainBackground,
        fg="#000000",
        font=Styles.fMain,
        relief=FLAT,
        justify=LEFT,
        text="    Back ",
        command=lambda: prevItem(None)
    ).pack(side=BOTTOM, anchor=SW, pady=Styles.xPadX, padx=Styles.xPadY)

draw(qList[0])

def nextItem(event):
    global qTracker
    try:
        qTracker = qTracker + 1
        draw(qList[qTracker])
    except IndexError:
        print(None)
        qTracker = len(qList)
    window.update()

def prevItem(event):
    global qTracker
    try:
        qTracker = qTracker - 1
        draw(qList[qTracker])
    except IndexError:
        print(None)
        qTracker = 0
    window.update()


window.bind('<Return>', nextItem)
window.mainloop()
