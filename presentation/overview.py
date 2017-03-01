from Tkinter import *


class Overview(object):
    def __init__(self, root, village, row_i, column_i):
        self.player = ['Player', 'points', 'position']
        self.villages = ['Villages', 'coordinates', 'fields', 'temperature']
        self.all = self.player + self.villages
        for i, l in enumerate(self.all):
            Label(root, text=l).grid(row=row_i + i, column=column_i)
