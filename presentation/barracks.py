from Tkinter import *


class Barracks(object):
    def __init__(self, village, root, resources, row_i, column_i):
        # logic attributes
        self.village = village
        # presentation attributes
        self.root = root
        self.resources = resources
        self.i = row_i
        self.j = column_i

        self.unit_being_trained = False
        text = "Barracks (level %i)" % self.village.buildings_dict['barracks'].level
        Label(self.root, text=text).grid(row=self.i, column=self.j)
        if self.unit_being_trained:
            self.create_units_being_trained()
        self.create_units4training()
        self.create_units_not_available()

    def create_units_being_trained(self):
        Recruitment(root=self.root, i=2, j=0)

    def create_units4training(self):
        Available(village=self.village, root=self.root, i=6, j=0)

    def create_units_not_available(self):
        pass


class Recruitment(object):
    def __init__(self, root, i, j):  # i(row), j(column)
        Label(root, text="Recruitment").\
            grid(row=i + 2, column=j, columnspan=2)
        header = ['Training', 'Duration', 'Completion', 'Cancel']
        for i, h in header:
            Label(root, text=h).\
                grid(row=i + 3, column=j * i, columnspan=2)


class Available(object):
    def __init__(self, village, root, i, j):
        self.village = village
        self.root = root
        self.i = i
        self.j = j
        self.create_header_unit4training()
        self.create_all_unit_available()

    def create_header_unit4training(self):
        self.i = 6
        Label(self.root, text='Unit').\
            grid(row=self.i, column=self.j)
        self.create_requirements()
        Label(self.root, text='In the \nvillage/total'). \
            grid(row=self.i,
                 column=self.j + self.village.n_resources + 2,
                 rowspan=2)
        Label(self.root, text='Recruit'). \
            grid(row=self.i,
                 column=self.j + self.village.n_resources + 3,
                 columnspan=2)

    def create_requirements(self):
        Label(self.root, text='Requirements'). \
            grid(row=self.i, column=self.j + 1,
                 columnspan=self.village.n_resources + 1)  # + 1, because of time
        for i, resource in enumerate(self.village.resources):
            Label(self.root, text=resource.name). \
                grid(row=self.i + 1, column=self.j + i + 1)
        Label(self.root, text='time').\
            grid(row=self.i + 1,
                 column=self.j + self.village.n_resources + 1)

    def create_all_unit_available(self):
        print 'create all unit aval', self.village.units
        for i, unit in enumerate(self.village.units):
            print unit.name
            self.create_n_available_type(i, unit, self.village.units[unit])

    def create_n_available_type(self, i, unit, n_units):
        print unit.name
        Label(self.root, text=unit.name).grid(row=self.i + i + 2, column=self.j)
        print unit.costs
        for j, cost in enumerate(unit.costs):
            Label(self.root, text=cost).grid(row=self.i + i + 2, column= self.j + j + 1)
        Label(self.root, text=unit.time).grid(row=self.i + i + 2, column=self.j + self.village.n_resources + 1)
