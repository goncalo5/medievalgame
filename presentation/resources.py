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
        for n, resource in enumerate(self.village.resources):
            Label(self.root, text=resource.name).grid(row=row_i, column=column_i + 1 + n)
            resource.l_total = Label(self.root, text=resource.total)
            resource.l_total.grid(row=row_i + 1, column=column_i + n + 1)
            resource.l_per_s = Label(self.root, text=resource.per_s)
            resource.l_per_s.grid(row=row_i + 2, column=column_i + n + 1)

        self.updating()

    def update(self, resource):
        resource.l_total['text'] = int(resource.total)
        resource.l_per_s['text'] = int(resource.per_s)

    def update_all(self):
        for resource in self.village.resources:
            self.update(resource)

    def updating(self):
        if self.village.run:
            self.update_all()
            # always use after method in Tkinter
            self.root.after(1000, self.updating)
