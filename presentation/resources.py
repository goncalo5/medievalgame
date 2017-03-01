from Tkinter import *


class Resources(object):
    def __init__(self, root, village, row_i, column_i):
        self.root = root
        # initiate village
        self.village = village

        # Available Resources
        # header
        Label(self.root, text='resource').grid(row=row_i, column=column_i)
        Label(self.root, text='Total').grid(row=row_i + 1, column=column_i)
        Label(self.root, text='per sec').grid(row=row_i + 2, column=column_i)
        for n, r in enumerate(self.village.resources):
            r = self.village.resources[r]
            Label(self.root, text=r.name).grid(row=row_i, column=column_i + 1 + n)
            r.l_total = Label(self.root, text=r.total)
            r.l_total.grid(row=row_i + 1, column=column_i + 1)
            r.l_per_s = Label(self.root, text=r.per_s)
            r.l_per_s.grid(row=row_i + 2, column=column_i + 1 + n)

        self.updating()

    def update(self, resource):
        resource.l_total['text'] = int(self.village.wood.total)
        resource.l_per_s['text'] = int(resource.per_s)

    def update_all(self):
        for r in self.village.resources:
            r = self.village.resources[r]
            self.update(r)

    def updating(self):
        if self.village.run:
            self.update_all()
            # always use after method in Tkinter
            self.root.after(1000, self.updating)
