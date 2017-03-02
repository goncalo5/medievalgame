from Tkinter import *


class Fill(object):
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
            for i, r in enumerate(self.village.resources):  # r = resource name
                text = building.cost[r]
                building.l_cost[r] = Label(self.root, text=int(text))
                building.l_cost[r].grid(row=l, column=column_i + i + 2)
            #self.l_cost = LabelCost(self.village.forest.cost)
            #print '\n\n\n\n', self.l_cost.wood
            # evolving time
            building.l_t = Label(self.root, text=int(building.time))
            building.l_t.grid(row=l, column=column_i + 2 + self.village.n_resources)
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
        print building.name, building.level
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
        for i, r in enumerate(self.village.resources):  # r = resource name
            building.l_cost[r]['text'] = building.cost[r]
            #getattr(building.l_cost, r)['text'] = int(getattr(building.cost, r))
        building.l_t['text'] = int(building.left)

    def update_all(self):
        for building in self.village.buildings:
            self.update(building)

    def updating(self):
        self.update_all()
        self.root.after(1000, self.updating)
