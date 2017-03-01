from header import Header
from fill import Fill


class Buildings(object):
    def __init__(self, root, village, resources, row_i, column_i):
        self.root = root
        self.village = village

        self.header = Header(self.root, village, row_i, column_i)
        self.fill = Fill(self.root, village, resources, self.header, row_i + self.header.n_rows, column_i)
