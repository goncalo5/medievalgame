from Tkinter import *


class Buildings(object):
    def __init__(self, root, village, resources, row_i, column_i):
        self.root = root
        self.village = village

        self.header = BuildingsHeader(self.root, village, row_i, column_i)
        self.fill = BuildingsFill(self.root, village, resources, self.header, row_i + self.header.n_rows, column_i)


class BuildingsHeader(object):
    def __init__(self, root, village, row_i, column_i):
        self.root = root
        # initiate village
        self.village = village

        self.l = row_i  # upper Header row
        self.c = column_i  # initial Header column
        self.n_rows = 2
        Label(self.root, text='Building').grid(row=self.l, column=self.c, rowspan=2)
        Label(self.root, text='Level').grid(row=self.l, column=self.c + 1, rowspan=2)

        # initial costs column
        self.c_costs = self.c + 2
        Label(self.root, text='evolving cost'). \
            grid(row=self.l, column=self.c_costs, columnspan=len(self.village.resources))
        for n, resource in enumerate(self.village.resources):
            # costs
            Label(self.root, text=resource.name).grid(row=self.l + 1, column=self.c_costs + n)
        # Column of construction times
        self.c_t = self.c_costs + len(self.village.resources)
        Label(self.root, text='Time'). \
            grid(row=self.l, column=self.c_t, rowspan=2)
        # evolving column
        self.c_evol = self.c_t + 1
        Label(self.root, text='Evolve').\
            grid(row=self.l, column=self.c_evol, rowspan=2)


class BuildingsFill(object):
    def __init__(self, root, village, resources, header, row_i, column_i):
        self.root = root
        # initiate village
        self.village = village
        self.resources = resources
        self.header = header

        for n, building in enumerate(self.village.buildings):
            l = row_i + n
            Label(self.root, text=building.name). \
                grid(row=l, column=column_i)
            # Level
            building.l_lv = Label(self.root, text=building.level)
            building.l_lv.grid(row=l, column=column_i + 1)
            # evolving cost
            building.l_cost = {}
            for i, resource in enumerate(self.village.resources):  # r = resource name
                text = building.cost[i]
                building.l_cost[i] = Label(self.root, text=int(text))
                building.l_cost[i].grid(row=l, column=column_i + i + 2)
            building.l_t = Label(self.root, text=int(building.time))
            building.l_t.grid(row=l, column=column_i + 2 + len(self.village.resources))
            # evolving

        self.updating()

        # create buttons
        l = self.header.l + 2
        self.b_buildings = []
        for i, building in enumerate(self.village.buildings):
            self.b_buildings.append(
                Button(self.root, text=building.kind, command=lambda b=building: self.evolve_building(b)))
            self.b_buildings[-1].grid(row=l + i, column=self.header.c_evol)

        self.resources.updating()

    def evolve_building(self, building):
        self.village.evolve_building(building)
        self.update(building)

    def update(self, building):
        self.fill.update(building)
        self.resources.update_all()

    def quit(self):
        self.village.save()
        self.village.metal.total = 40
        self.village.run = False
        self.root.destroy()

    def update(self, building):
        building.l_lv['text'] = int(building.level)
        for i, resource in enumerate(self.village.resources):  # r = resource name
            building.l_cost[i]['text'] = building.cost[i]
            #getattr(building.l_cost, r)['text'] = int(getattr(building.cost, r))
        building.l_t['text'] = int(building.left)

    def update_all(self):
        for building in self.village.buildings:
            self.update(building)

    def updating(self):
        self.update_all()
        self.root.after(1000, self.updating)