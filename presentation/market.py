from Tkinter import *

class Market(object):
    def __init__(self, world, village, root, resources, row_i=0, column_i=0):
        # logic attributes
        self.world = world
        self.village = village
        # presentation attributes
        self.root = root
        self.resources = resources
        self.row_i = row_i
        self.column_i = column_i
        # find offers
        Label(self.root, text='I want').grid(row=self.row_i + 1, column=self.column_i)
        Label(self.root, text="I'm offering").grid(row=self.row_i + 2, column=self.column_i)
        for i, resource in enumerate(self.village.resources):
            Label(self.root, text=resource.name).grid(row=self.row_i, column=self.column_i + 1 + i)