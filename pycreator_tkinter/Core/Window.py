import tkinter as tk

from pycreator_tkinter.Core.Widgets import FilesWidget, TabEditorWidget
from pycreator_tkinter.Core.Menus import FileMenu, ExecuteMenu, CodeMenu, ParametersMenu

from pycreator_core import Config, Analyser


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.config = Config()
        self.analyser = Analyser(self.config)

        self.title("PyCreator")
        self.state("zoomed")

        self.menu = tk.Menu(self)
        self.filemenu = FileMenu(self, self.menu)
        self.executemenu = ExecuteMenu(self, self.menu)
        self.codemenu = CodeMenu(self, self.menu)
        self.parametersmenu = ParametersMenu(self, self.menu)
        self.filesview = FilesWidget(self)
        self.tabeditor = TabEditorWidget(self)

        self.setup_ui()

        self.mainloop()

    def setup_ui(self):
        self.menu.add_cascade(label="Fichier", menu=self.filemenu)
        self.menu.add_cascade(label="Executer", menu=self.executemenu)
        self.menu.add_cascade(label="Code", menu=self.codemenu)
        self.menu.add_cascade(label="Paramètres", menu=self.parametersmenu)

        self.config(menu=self.menu)

        self.filesview.grid(row=0, column=0, sticky='nesw')
        self.tabeditor.grid(row=0, column=1, sticky='nesw')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
