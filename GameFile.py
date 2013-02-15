#-------------------------------------------------------------------------------
# Name:        Game file Singleton
# Purpose:     This singleton stores game data, and can be accessed from anywhere
#
# Author:      Daniel
#
# Created:     15/02/2013
# Copyright:   (c) Daniel 2013
# Licence:     GPL
#-------------------------------------------------------------------------------

import Tkinter
from Tkinter import *
import tkFileDialog
import os
import Zipper

class GameFile:

    """ A python singleton """

    class __impl:
        Fname = ""
        Vars = list()
        obj = list()
        rooms = list()
        """ Implementation of the singleton interface """
        def load(self):
            self.cleartmp()
            self.Fname = tkFileDialog.askopenfilename(filetypes=[('Raspberry Pi Game','*.rpg;*.zip')])
            if self.Fname <> '':
                z= Zipper.zipper()
                z.openfile(os.path.dirname(__file__) + "/Project", self.Fname)
                self.opengame()

        def save(self):
            if self.Fname == "":
                self.Fname = tkFileDialog.asksaveasfilename(filetypes=[('Raspberry Pi Game','*.rpg')])
            if self.Fname <> ".rpg":
                z= Zipper.zipper()
                z.savefile(os.path.dirname(__file__) + "/Project", self.Fname+".rpg")

        def opengame(self):
            self.Vars = [line.strip() for line in open(os.path.dirname(__file__) + "/Project/vars")]
            self.objs = os.listdir(os.path.dirname(__file__)+ "/Project/objs")
            self.rooms = os.listdir(os.path.dirname(__file__)+ "/Project/rooms")

        def savevars(self):
            f = open(os.path.dirname(__file__) + "/Project/vars",'w')
            for a in self.Vars:
                f.write(a + '\n')

        def cleartmp(self):
            folder = os.path.dirname(__file__) + "/Project"
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception, e:
                print e

        def additm(self, item, Type):
            if Type == "room":
                self.rooms.append(item)
            elif Type == "var":
                self.Vars.append(item)
                self.savevars()
            elif Type == "obj":
                self.objs.append(item)

    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if GameFile.__instance is None:
            # Create and remember instance
            GameFile.__instance = GameFile.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = GameFile.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)
