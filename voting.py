#!/usr/bin/env python

from Tkinter import *
import ttk
from PIL import ImageTk as imtk, Image
import pickle

'''
TODO:
1) Intro screen
2) Sample candidate buttons updating vote in log file
3) Autosave
4) Outro window with 2 minute cooldown.
'''


class VotingSystem(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.state('zoom')
        self.geometry('1020x700')
        self.wm_title('Student Council Elections 2017-18')

        icon = imtk.PhotoImage(Image.open(
            'logo.ico'))
        self.call('wm', 'iconphoto', self._w, icon)

        # Program can now only be exited through task manager.
        # self.protocol("WM_DELETE_WINDOW", self.__callback)

        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (intropage, Headboy, Headgirl, D_Headboy, D_Headgirl, outropage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(intropage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    @staticmethod
    def __callback():
        return


class intropage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.intro_img = imtk.PhotoImage(Image.open(
            'beaconhouse.jpg').resize((1024, 705), Image.ANTIALIAS))
        self.intro_img_label = Label(self, image=self.intro_img)
        self.intro_img_label.place(x=0, y=0, relwidth=1, relheight=1)

        testB = ttk.Button(self, text='Start',
                           command=lambda: controller.show_frame(Headboy))

        testB.pack(side=BOTTOM, pady=150)


class Headboy(Frame):

    hb_votes = {
        'candidate1': 0,
        'candidate2': 0,
        'candidate3': 0,
        'candidate4': 0,
        'candidate5': 0,
        'candidate6': 0,
        'candidate7': 0,
        'candidate8': 0,
        'candidate9': 0,
        'candidate11': 0,
        'candidate12': 0,
        'candidate13': 0,
        'candidate14': 0,
        'candidate15': 0,
        'candidate16': 0,
        'candidate17': 0,
        'candidate18': 0,
    }

    def __init__(self, parent, controller):

        self.controller = controller

        Frame.__init__(self, parent)

        self.intro_img = imtk.PhotoImage(Image.open(
            r'backgrounds/headboy.jpg').resize((1024, 705), Image.ANTIALIAS))
        self.intro_img_label = Label(self, image=self.intro_img)
        self.intro_img_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Test candidate1
        candidate1_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate1_button = Button(self, text='Test candidate 1', image=candidate1_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate1'))
        candidate1_button.image = candidate1_img
        candidate1_button.grid(padx=22, pady=30, row=0, column=0)

        # Test candidate2
        candidate2_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate2_button = Button(self, text='Test candidate 2', image=candidate2_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate2'))
        candidate2_button.image = candidate2_img
        candidate2_button.grid(padx=22, pady=30, row=0, column=1)

        # Test candidate3
        candidate3_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate3_button = Button(self, text='Test candidate 3', image=candidate3_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate3'))
        candidate3_button.image = candidate3_img
        candidate3_button.grid(padx=22, pady=30, row=0, column=2)

        # Test candidate4
        candidate4_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate4_button = Button(self, text='Test candidate 4', image=candidate4_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate4'))
        candidate4_button.image = candidate4_img
        candidate4_button.grid(padx=22, pady=30, row=0, column=3)

        # Test candidate5
        candidate5_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate5_button = Button(self, text='Test candidate 5', image=candidate5_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate5'))
        candidate5_button.image = candidate5_img
        candidate5_button.grid(padx=22, pady=30, row=0, column=4)

        # Test candidate6
        candidate6_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate6_button = Button(self, text='Test candidate 6', image=candidate6_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate6'))
        candidate6_button.image = candidate6_img
        candidate6_button.grid(padx=22, pady=30, row=0, column=5)

        # Test candidate7
        candidate7_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate7_button = Button(self, text='Test candidate 7', image=candidate7_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate7'))
        candidate7_button.image = candidate7_img
        candidate7_button.grid(padx=22, pady=30, row=1, column=0)

        # Test candidate8
        candidate8_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate8_button = Button(self, text='Test candidate 8', image=candidate8_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate8'))
        candidate8_button.image = candidate8_img
        candidate8_button.grid(padx=22, pady=30, row=1, column=1)

        # Test candidate9
        candidate9_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate9_button = Button(self, text='Test candidate 9', image=candidate9_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate9'))
        candidate9_button.image = candidate9_img
        candidate9_button.grid(padx=22, pady=30, row=1, column=2)

        # Test candidate10
        candidate10_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate10_button = Button(self, text='Test candidate 10', image=candidate1_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate10'))
        candidate10_button.image = candidate10_img
        candidate10_button.grid(padx=22, pady=30, row=1, column=3)

        # Test candidate11
        candidate11_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate11_button = Button(self, text='Test candidate 11', image=candidate11_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate11'))
        candidate11_button.image = candidate11_img
        candidate11_button.grid(padx=22, pady=30, row=1, column=4)

        # Test candidate12
        candidate12_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate12_button = Button(self, text='Test candidate 12', image=candidate12_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate12'))
        candidate12_button.image = candidate12_img
        candidate12_button.grid(padx=22, pady=30, row=1, column=5)

        # Test candidate13
        candidate13_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate13_button = Button(self, text='Test candidate 13', image=candidate13_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate13'))
        candidate13_button.image = candidate13_img
        candidate13_button.grid(padx=22, pady=30, row=2, column=0)

        # Test candidate14
        candidate14_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate14_button = Button(self, text='Test candidate 14', image=candidate14_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate14'))
        candidate14_button.image = candidate14_img
        candidate14_button.grid(padx=22, pady=30, row=2, column=1)

        # Test candidate15
        candidate15_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate15_button = Button(self, text='Test candidate 15', image=candidate15_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate15'))
        candidate15_button.image = candidate15_img
        candidate15_button.grid(padx=22, pady=30, row=2, column=2)

        # Test candidate16
        candidate16_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate16_button = Button(self, text='Test candidate 16', image=candidate16_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate16'))
        candidate16_button.image = candidate16_img
        candidate16_button.grid(padx=22, pady=30, row=2, column=3)

        # Test candidate17
        candidate17_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate17_button = Button(self, text='Test candidate 17', image=candidate17_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate17'))
        candidate17_button.image = candidate17_img
        candidate17_button.grid(padx=22, pady=30, row=2, column=4)

        # Test candidate18
        candidate18_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate18_button = Button(self, text='Test candidate 18', image=candidate18_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate18'))
        candidate18_button.image = candidate18_img
        candidate18_button.grid(padx=22, pady=30, row=2, column=5)

    # Vote tally
    def voteCount(self, name):
        Headboy.hb_votes[name] += 1
        print Headboy.hb_votes
        self.controller.show_frame(Headgirl)
        # with open('Headboy Votes.txt', 'r+') as f:
        #     pickle.dump(Headboy.votes, f)


class Headgirl(Frame):

    hg_votes = {
        'candidate1': 0,
        'candidate2': 0,
        'candidate3': 0,
        'candidate4': 0,
        'candidate5': 0,
        'candidate6': 0,
        'candidate7': 0,
        'candidate8': 0,
        'candidate9': 0,
        'candidate11': 0,
        'candidate12': 0,
        'candidate13': 0,
        'candidate14': 0,
        'candidate15': 0,
        'candidate16': 0,
        'candidate17': 0,
        'candidate18': 0,
    }

    def __init__(self, parent, controller):
        self.controller = controller

        Frame.__init__(self, parent)

        self.intro_img = imtk.PhotoImage(Image.open(
            r'backgrounds/headgirl.jpg').resize((1024, 705), Image.ANTIALIAS))
        self.intro_img_label = Label(self, image=self.intro_img)
        self.intro_img_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Test candidate1
        candidate1_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate1_button = Button(self, text='Test candidate 1', image=candidate1_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate1'))
        candidate1_button.image = candidate1_img
        candidate1_button.grid(padx=22, pady=30, row=0, column=0)

        # Test candidate2
        candidate2_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate2_button = Button(self, text='Test candidate 2', image=candidate2_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate2'))
        candidate2_button.image = candidate2_img
        candidate2_button.grid(padx=22, pady=30, row=0, column=1)

        # Test candidate3
        candidate3_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate3_button = Button(self, text='Test candidate 3', image=candidate3_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate3'))
        candidate3_button.image = candidate3_img
        candidate3_button.grid(padx=22, pady=30, row=0, column=2)

        # Test candidate4
        candidate4_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate4_button = Button(self, text='Test candidate 4', image=candidate4_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate4'))
        candidate4_button.image = candidate4_img
        candidate4_button.grid(padx=22, pady=30, row=0, column=3)

        # Test candidate5
        candidate5_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate5_button = Button(self, text='Test candidate 5', image=candidate5_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate5'))
        candidate5_button.image = candidate5_img
        candidate5_button.grid(padx=22, pady=30, row=0, column=4)

        # Test candidate6
        candidate6_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate6_button = Button(self, text='Test candidate 6', image=candidate6_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate6'))
        candidate6_button.image = candidate6_img
        candidate6_button.grid(padx=22, pady=30, row=0, column=5)

        # Test candidate7
        candidate7_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate7_button = Button(self, text='Test candidate 7', image=candidate7_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate7'))
        candidate7_button.image = candidate7_img
        candidate7_button.grid(padx=22, pady=30, row=1, column=0)

        # Test candidate8
        candidate8_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate8_button = Button(self, text='Test candidate 8', image=candidate8_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate8'))
        candidate8_button.image = candidate8_img
        candidate8_button.grid(padx=22, pady=30, row=1, column=1)

        # Test candidate9
        candidate9_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate9_button = Button(self, text='Test candidate 9', image=candidate9_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate9'))
        candidate9_button.image = candidate9_img
        candidate9_button.grid(padx=22, pady=30, row=1, column=2)

        # Test candidate10
        candidate10_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate10_button = Button(self, text='Test candidate 10', image=candidate1_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate10'))
        candidate10_button.image = candidate10_img
        candidate10_button.grid(padx=22, pady=30, row=1, column=3)

        # Test candidate11
        candidate11_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate11_button = Button(self, text='Test candidate 11', image=candidate11_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate11'))
        candidate11_button.image = candidate11_img
        candidate11_button.grid(padx=22, pady=30, row=1, column=4)

        # Test candidate12
        candidate12_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate12_button = Button(self, text='Test candidate 12', image=candidate12_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate12'))
        candidate12_button.image = candidate12_img
        candidate12_button.grid(padx=22, pady=30, row=1, column=5)

        # Test candidate13
        candidate13_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate13_button = Button(self, text='Test candidate 13', image=candidate13_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate13'))
        candidate13_button.image = candidate13_img
        candidate13_button.grid(padx=22, pady=30, row=2, column=0)

        # Test candidate14
        candidate14_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate14_button = Button(self, text='Test candidate 14', image=candidate14_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate14'))
        candidate14_button.image = candidate14_img
        candidate14_button.grid(padx=22, pady=30, row=2, column=1)

        # Test candidate15
        candidate15_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate15_button = Button(self, text='Test candidate 15', image=candidate15_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate15'))
        candidate15_button.image = candidate15_img
        candidate15_button.grid(padx=22, pady=30, row=2, column=2)

        # Test candidate16
        candidate16_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate16_button = Button(self, text='Test candidate 16', image=candidate16_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate16'))
        candidate16_button.image = candidate16_img
        candidate16_button.grid(padx=22, pady=30, row=2, column=3)

        # Test candidate17
        candidate17_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate17_button = Button(self, text='Test candidate 17', image=candidate17_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate17'))
        candidate17_button.image = candidate17_img
        candidate17_button.grid(padx=22, pady=30, row=2, column=4)

        # Test candidate18
        candidate18_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate18_button = Button(self, text='Test candidate 18', image=candidate18_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate18'))
        candidate18_button.image = candidate18_img
        candidate18_button.grid(padx=22, pady=30, row=2, column=5)

    # Vote tally
    def voteCount(self, name):
        Headgirl.hg_votes[name] += 1
        print Headboy.hb_votes
        self.controller.show_frame(D_Headboy)
        # with open('Headboy Votes.txt', 'r+') as f:
        #     pickle.dump(Headboy.votes, f)


class D_Headboy(Frame):

    d_hb_votes = {
        'candidate1': 0,
        'candidate2': 0,
        'candidate3': 0,
        'candidate4': 0,
        'candidate5': 0,
        'candidate6': 0,
        'candidate7': 0,
        'candidate8': 0,
        'candidate9': 0,
        'candidate11': 0,
        'candidate12': 0,
        'candidate13': 0,
        'candidate14': 0,
        'candidate15': 0,
        'candidate16': 0,
        'candidate17': 0,
        'candidate18': 0,
    }

    def __init__(self, parent, controller):
        self.controller = controller

        Frame.__init__(self, parent)

        self.intro_img = imtk.PhotoImage(Image.open(
            r'backgrounds/dheadboy.jpg').resize((1024, 705), Image.ANTIALIAS))
        self.intro_img_label = Label(self, image=self.intro_img)
        self.intro_img_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Test candidate1
        candidate1_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate1_button = Button(self, text='Test candidate 1', image=candidate1_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate1'))
        candidate1_button.image = candidate1_img
        candidate1_button.grid(padx=22, pady=30, row=0, column=0)

        # Test candidate2
        candidate2_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate2_button = Button(self, text='Test candidate 2', image=candidate2_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate2'))
        candidate2_button.image = candidate2_img
        candidate2_button.grid(padx=22, pady=30, row=0, column=1)

        # Test candidate3
        candidate3_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate3_button = Button(self, text='Test candidate 3', image=candidate3_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate3'))
        candidate3_button.image = candidate3_img
        candidate3_button.grid(padx=22, pady=30, row=0, column=2)

        # Test candidate4
        candidate4_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate4_button = Button(self, text='Test candidate 4', image=candidate4_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate4'))
        candidate4_button.image = candidate4_img
        candidate4_button.grid(padx=22, pady=30, row=0, column=3)

        # Test candidate5
        candidate5_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate5_button = Button(self, text='Test candidate 5', image=candidate5_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate5'))
        candidate5_button.image = candidate5_img
        candidate5_button.grid(padx=22, pady=30, row=0, column=4)

        # Test candidate6
        candidate6_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate6_button = Button(self, text='Test candidate 6', image=candidate6_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate6'))
        candidate6_button.image = candidate6_img
        candidate6_button.grid(padx=22, pady=30, row=0, column=5)

        # Test candidate7
        candidate7_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate7_button = Button(self, text='Test candidate 7', image=candidate7_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate7'))
        candidate7_button.image = candidate7_img
        candidate7_button.grid(padx=22, pady=30, row=1, column=0)

        # Test candidate8
        candidate8_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate8_button = Button(self, text='Test candidate 8', image=candidate8_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate8'))
        candidate8_button.image = candidate8_img
        candidate8_button.grid(padx=22, pady=30, row=1, column=1)

        # Test candidate9
        candidate9_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate9_button = Button(self, text='Test candidate 9', image=candidate9_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate9'))
        candidate9_button.image = candidate9_img
        candidate9_button.grid(padx=22, pady=30, row=1, column=2)

        # Test candidate10
        candidate10_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate10_button = Button(self, text='Test candidate 10', image=candidate1_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate10'))
        candidate10_button.image = candidate10_img
        candidate10_button.grid(padx=22, pady=30, row=1, column=3)

        # Test candidate11
        candidate11_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate11_button = Button(self, text='Test candidate 11', image=candidate11_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate11'))
        candidate11_button.image = candidate11_img
        candidate11_button.grid(padx=22, pady=30, row=1, column=4)

        # Test candidate12
        candidate12_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate12_button = Button(self, text='Test candidate 12', image=candidate12_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate12'))
        candidate12_button.image = candidate12_img
        candidate12_button.grid(padx=22, pady=30, row=1, column=5)

        # Test candidate13
        candidate13_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate13_button = Button(self, text='Test candidate 13', image=candidate13_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate13'))
        candidate13_button.image = candidate13_img
        candidate13_button.grid(padx=22, pady=30, row=2, column=0)

        # Test candidate14
        candidate14_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate14_button = Button(self, text='Test candidate 14', image=candidate14_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate14'))
        candidate14_button.image = candidate14_img
        candidate14_button.grid(padx=22, pady=30, row=2, column=1)

        # Test candidate15
        candidate15_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate15_button = Button(self, text='Test candidate 15', image=candidate15_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate15'))
        candidate15_button.image = candidate15_img
        candidate15_button.grid(padx=22, pady=30, row=2, column=2)

        # Test candidate16
        candidate16_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate16_button = Button(self, text='Test candidate 16', image=candidate16_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate16'))
        candidate16_button.image = candidate16_img
        candidate16_button.grid(padx=22, pady=30, row=2, column=3)

        # Test candidate17
        candidate17_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate17_button = Button(self, text='Test candidate 17', image=candidate17_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate17'))
        candidate17_button.image = candidate17_img
        candidate17_button.grid(padx=22, pady=30, row=2, column=4)

        # Test candidate18
        candidate18_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate18_button = Button(self, text='Test candidate 18', image=candidate18_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate18'))
        candidate18_button.image = candidate18_img
        candidate18_button.grid(padx=22, pady=30, row=2, column=5)

    # Vote tally
    def voteCount(self, name):
        D_Headboy.d_hb_votes[name] += 1
        print D_Headboy.d_hb_votes
        self.controller.show_frame(D_Headgirl)
        # with open('Headboy Votes.txt', 'r+') as f:
        #     pickle.dump(Headboy.votes, f)


class D_Headgirl(Frame):

    d_hg_votes = {
        'candidate1': 0,
        'candidate2': 0,
        'candidate3': 0,
        'candidate4': 0,
        'candidate5': 0,
        'candidate6': 0,
        'candidate7': 0,
        'candidate8': 0,
        'candidate9': 0,
        'candidate11': 0,
        'candidate12': 0,
        'candidate13': 0,
        'candidate14': 0,
        'candidate15': 0,
        'candidate16': 0,
        'candidate17': 0,
        'candidate18': 0,
    }

    def __init__(self, parent, controller):
        self.controller = controller

        Frame.__init__(self, parent)

        self.intro_img = imtk.PhotoImage(Image.open(
            r'backgrounds/dheadgirl.jpg').resize((1024, 705), Image.ANTIALIAS))
        self.intro_img_label = Label(self, image=self.intro_img)
        self.intro_img_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Test candidate1
        candidate1_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate1_button = Button(self, text='Test candidate 1', image=candidate1_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate1'))
        candidate1_button.image = candidate1_img
        candidate1_button.grid(padx=22, pady=30, row=0, column=0)

        # Test candidate2
        candidate2_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate2_button = Button(self, text='Test candidate 2', image=candidate2_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate2'))
        candidate2_button.image = candidate2_img
        candidate2_button.grid(padx=22, pady=30, row=0, column=1)

        # Test candidate3
        candidate3_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate3_button = Button(self, text='Test candidate 3', image=candidate3_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate3'))
        candidate3_button.image = candidate3_img
        candidate3_button.grid(padx=22, pady=30, row=0, column=2)

        # Test candidate4
        candidate4_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate4_button = Button(self, text='Test candidate 4', image=candidate4_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate4'))
        candidate4_button.image = candidate4_img
        candidate4_button.grid(padx=22, pady=30, row=0, column=3)

        # Test candidate5
        candidate5_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate5_button = Button(self, text='Test candidate 5', image=candidate5_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate5'))
        candidate5_button.image = candidate5_img
        candidate5_button.grid(padx=22, pady=30, row=0, column=4)

        # Test candidate6
        candidate6_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate6_button = Button(self, text='Test candidate 6', image=candidate6_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate6'))
        candidate6_button.image = candidate6_img
        candidate6_button.grid(padx=22, pady=30, row=0, column=5)

        # Test candidate7
        candidate7_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate7_button = Button(self, text='Test candidate 7', image=candidate7_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate7'))
        candidate7_button.image = candidate7_img
        candidate7_button.grid(padx=22, pady=30, row=1, column=0)

        # Test candidate8
        candidate8_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate8_button = Button(self, text='Test candidate 8', image=candidate8_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate8'))
        candidate8_button.image = candidate8_img
        candidate8_button.grid(padx=22, pady=30, row=1, column=1)

        # Test candidate9
        candidate9_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate9_button = Button(self, text='Test candidate 9', image=candidate9_img,
                                   padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate9'))
        candidate9_button.image = candidate9_img
        candidate9_button.grid(padx=22, pady=30, row=1, column=2)

        # Test candidate10
        candidate10_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate10_button = Button(self, text='Test candidate 10', image=candidate1_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate10'))
        candidate10_button.image = candidate10_img
        candidate10_button.grid(padx=22, pady=30, row=1, column=3)

        # Test candidate11
        candidate11_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate11_button = Button(self, text='Test candidate 11', image=candidate11_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate11'))
        candidate11_button.image = candidate11_img
        candidate11_button.grid(padx=22, pady=30, row=1, column=4)

        # Test candidate12
        candidate12_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate12_button = Button(self, text='Test candidate 12', image=candidate12_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate12'))
        candidate12_button.image = candidate12_img
        candidate12_button.grid(padx=22, pady=30, row=1, column=5)

        # Test candidate13
        candidate13_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate13_button = Button(self, text='Test candidate 13', image=candidate13_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate13'))
        candidate13_button.image = candidate13_img
        candidate13_button.grid(padx=22, pady=30, row=2, column=0)

        # Test candidate14
        candidate14_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate14_button = Button(self, text='Test candidate 14', image=candidate14_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate14'))
        candidate14_button.image = candidate14_img
        candidate14_button.grid(padx=22, pady=30, row=2, column=1)

        # Test candidate15
        candidate15_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate15_button = Button(self, text='Test candidate 15', image=candidate15_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate15'))
        candidate15_button.image = candidate15_img
        candidate15_button.grid(padx=22, pady=30, row=2, column=2)

        # Test candidate16
        candidate16_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate16_button = Button(self, text='Test candidate 16', image=candidate16_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate16'))
        candidate16_button.image = candidate16_img
        candidate16_button.grid(padx=22, pady=30, row=2, column=3)

        # Test candidate17
        candidate17_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate17_button = Button(self, text='Test candidate 17', image=candidate17_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate17'))
        candidate17_button.image = candidate17_img
        candidate17_button.grid(padx=22, pady=30, row=2, column=4)

        # Test candidate18
        candidate18_img = imtk.PhotoImage(Image.open(
            'sample.jpg').resize((100, 100), Image.ANTIALIAS))
        candidate18_button = Button(self, text='Test candidate 18', image=candidate18_img,
                                    padx=10, pady=10, compound=TOP, command=lambda: self.voteCount('candidate18'))
        candidate18_button.image = candidate18_img
        candidate18_button.grid(padx=22, pady=30, row=2, column=5)

    # Vote tally
    def voteCount(self, name):
        D_Headgirl.d_hg_votes[name] += 1
        print D_Headgirl.d_hg_votes
        self.controller.show_frame(outropage)
        # with open('Headboy Votes.txt', 'r+') as f:
        #     pickle.dump(Headboy.votes, f)


class outropage(Frame):

    def __init__(self, parent, controller):
        self.controller = controller

        Frame.__init__(self, parent)

        self.intro_img = imtk.PhotoImage(Image.open(
            'outro.jpg').resize((1024, 705), Image.ANTIALIAS))
        self.intro_img_label = Label(self, image=self.intro_img)
        self.intro_img_label.place(x=0, y=0, relwidth=1, relheight=1)

        show_startpage = ttk.Button(self, text='Retrurn to start page',
                                    command=lambda: self.controller.show_frame(intropage), state='disabled')
        show_startpage.pack(side=BOTTOM)
        show_startpage.after((1000 * 30), lambda: show_startpage.config(state='enabled'))


app = VotingSystem()
app.mainloop()
