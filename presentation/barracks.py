from Tkinter import *


class Barracks(object):
    def __init__(self, village, root, resources, row_i, column_i):
        # logic attributes
        self.village = village
        # presentation attributes
        self.root = root
        self.resources = resources
        self.row_i = self.row_aval = row_i
        self.column_i = column_i

        self.unit_being_trained = False
        text = "Barracks (level %i)" % self.village.buildings_dict['barracks'].level
        Label(self.root, text=text).grid(row=self.row_i, column=self.column_i)
        if self.unit_being_trained:
            self.create_units_being_trained()
        self.create_units4training()
        self.create_units_not_available()

    # 1
    # 1
    # 1
    def create_units_being_trained(self):
        Label(self.root, text="Recruitment").\
            grid(row=self.row_i + 2, column=self.column_i, columnspan=2)
        header = ['Training', 'Duration', 'Completion', 'Cancel']
        for i, h in header:
            Label(self.root, text=h).\
                grid(row=self.row_i + 3, column=self.column_i * i, columnspan=2)

    # 2
    # 1
    # 1
    def create_units4training(self):
        print 'create_units4training'
        self.create_header_unit4training()
        self.create_all_unit_available()

    # 2
    # 1
    def create_header_unit4training(self):
        self.row_aval = self.row_i + 6 * self.unit_being_trained + 1
        Label(self.root, text='Unit').\
            grid(row=self.row_aval, column=self.column_i)
        self.create_requirements()
        Label(self.root, text='In the \nvillage/total'). \
            grid(row=self.row_aval,
                 column=self.column_i + self.village.n_resources + 2,
                 rowspan=2)
        Label(self.root, text='Recruit'). \
            grid(row=self.row_aval,
                 column=self.column_i + self.village.n_resources + 3,
                 columnspan=2)

    # 2
    def create_requirements(self):
        Label(self.root, text='Requirements'). \
            grid(row=self.row_aval, column=self.column_i + 1,
                 columnspan=self.village.n_resources + 1)  # + 1, because of time
        for i, resource in enumerate(self.village.resources):
            Label(self.root, text=resource.name). \
                grid(row=self.row_aval + 1, column=self.column_i + i + 1)
        Label(self.root, text='time').\
            grid(row=self.row_aval + 1,
                 column=self.column_i + self.village.n_resources + 1)

    # create_units4training
    def create_all_unit_available(self):
        print 'create all unit aval', self.village.units
        for i, unit in enumerate(self.village.units):
            print unit.name
            self.create_n_available_type(i, unit, self.village.units[unit])

    # create_all_unit_available()
    def create_n_available_type(self, i, unit, n_units):
        print unit.name
        Label(self.root, text=unit.name).grid(row=self.row_aval + i + 2, column=self.column_i)
        print unit.costs
        for j, cost in enumerate(unit.costs):
            Label(self.root, text=cost).grid(row=self.row_aval + i + 2, column= self.column_i + j + 1)
        Label(self.root, text=unit.time).grid(row=self.row_aval + i + 2, column=self.column_i + self.village.n_resources + 1)

    # 3
    # 1
    def create_units_not_available(self):
        pass

