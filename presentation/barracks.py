from Tkinter import *


class Barracks(object):
    def __init__(self, village, root, resources, row_i, column_i):
        # logic attributes
        self.village = village
        # presentation attributes
        self.root = root
        self.resources = resources
        self.row_i = row_i
        self.column_i = column_i

        self.unit_being_trained = False
        text = "Barracks (level %i)" % self.village.buildings_dict['barracks'].level
        Label(self.root, text=text).grid(row=self.row_i)
        if self.unit_being_trained:
            self.create_units_being_trained()
        self.create_units4training()
        self.create_units_not_available()

    def create_units_being_trained(self):
        pass

    def create_units4training(self):
        pass

    def create_units_not_available(self):
        pass
