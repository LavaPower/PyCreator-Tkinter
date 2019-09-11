from tkinter import Menu, IntVar, TclError

from pycreator_tkinter.Core.Utils import replace_code, get_editor, add_begin_code, remove_begin_code


class CodeMenu(Menu):
    def __init__(self, window, menu):
        super(CodeMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.add_command(label="Informations")
        self.add_separator()
        self.add_command(label="Indenter", command=self.indenter)
        self.add_command(label="Désindenter", command=self.desindenter)
        self.add_command(label="Reformater")
        self.add_command(label="Commenter", command=self.comment)
        self.add_command(label="Décommenter", command=self.decomment)
        self.add_separator()
        self.add_command(label="Espaces -> Tabs", command=self.spacestotabs)
        self.add_command(label="Tabs -> Espaces", command=self.tabstospaces)

    def indenter(self):
        add_begin_code(self.window, "\t")

    def desindenter(self):
        remove_begin_code(self.window, "\t")

    def comment(self):
        add_begin_code(self.window, "#")

    def decomment(self):
        remove_begin_code(self.window, "#")

    def spacestotabs(self):
        replace_code(self.window, "    ", "\t")

    def tabstospaces(self):
        replace_code(self.window, "\t", "    ")
