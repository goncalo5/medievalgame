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
        self.want = StringVar()
        self.offer = StringVar()
        for i, resource in enumerate(self.village.resources):
            Label(self.root, text=resource.name).grid(row=self.row_i, column=self.column_i + i + 1)
            self.b_want = Radiobutton(self.root, variable=self.want, value=resource.name)
            self.b_want.grid(row=self.row_i + 1, column=self.column_i + i + 1)
            self.b_offer = Radiobutton(self.root, variable=self.offer, value=resource.name)
            self.b_offer.grid(row=self.row_i + 2, column=self.column_i + i + 1)

        header = ['Receive', 'for', 'player', 'Duration', 'Ratio', 'Availability', 'Accept']
        for i, name in enumerate(header):
            Label(self.root, text=name).grid(row=self.row_i + 4, column=self.column_i + i)
        self.button = Button(self.root, text='accept', command=self.accept)
        self.button.grid(row=self.row_i + 5, column=self.column_i + 6)

    def accept(self):
        if self.want.get() != self.offer.get():
            print 'ok'
