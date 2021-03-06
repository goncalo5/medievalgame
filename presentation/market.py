from Tkinter import *


class Market(object):
    def __init__(self, world, village, root, resources, row_i=0, column_i=0):
        # initiate_attributes
        # logic attributes
        self.world = world
        self.village = village
        # presentation attributes
        self.root = root
        self.resources = resources
        self.row_i = row_i
        self.column_i = column_i
        # null attributes
        self.b_want = self.b_offer = None
        self.ratio = None
        self.resource_send = {}
        self.resource_receive = {}
        self.l_receive = self.e_for = None
        self.b_barter = None
        # initial methods
        self.find_offers()

    # initial methods
    def find_offers(self):
        self.choose_resources2trade()
        #self.output_all_offers_wanted()

    def choose_resources2trade(self):
        Label(self.root, text='I want').grid(row=self.row_i + 1, column=self.column_i)
        Label(self.root, text="I'm offering").grid(row=self.row_i + 2, column=self.column_i)
        self.create_resources_option_to_choose()
        self.b_see_offers = Button(self.root, text="see offers", command=self.output_all_offers_wanted)
        self.b_see_offers.grid(row=self.row_i + 3, column=self.column_i)

    def create_resources_option_to_choose(self):
        self.resource_receive['name'] = StringVar()
        self.resource_receive['name'].set(self.village.resources.list[0].name)
        self.resource_send['name'] = StringVar()
        self.resource_send['name'].set(self.village.resources.list[1].name)
        for i, resource in enumerate(self.village.resources.list):
            Label(self.root, text=resource.name).grid(row=self.row_i, column=self.column_i + i + 1)
            self.b_want = Radiobutton(self.root, variable=self.resource_receive['name'], value=resource.name)
            self.b_want.grid(row=self.row_i + 1, column=self.column_i + i + 1)
            self.b_offer = Radiobutton(self.root, variable=self.resource_send['name'], value=resource.name)
            self.b_offer.grid(row=self.row_i + 2, column=self.column_i + i + 1)

    def output_all_offers_wanted(self):
        self.create_header_for_all_offers_wanted()
        self.add_entry_for()
        self.calculate_ratio_and_receive()
        self.add_label_receive()
        self.add_label_ratio()
        self.add_other_labels()
        self.add_button_barter()

    def create_header_for_all_offers_wanted(self):
        header = ['Receive', 'for', 'player', 'Duration', 'Ratio', 'Availability', 'Accept']
        for i, name in enumerate(header):
            Label(self.root, text=name).grid(row=self.row_i + 4, column=self.column_i + i)

    def add_entry_for(self):
        if self.e_for == None:
            self.e_for = Entry(self.root, width=7)
            self.e_for.insert(0, 500)
            self.e_for.grid(row=self.row_i + 5, column=self.column_i + 1)

    def calculate_ratio_and_receive(self):
        self.ratio = self.world.trader.calculate_ratio(self.resource_receive['name'].get(), self.resource_send['name'].get())
        self.receive = self.world.trader.calculate_receive(self.e_for.get(), self.ratio)

    def add_label_receive(self):
        if self.l_receive == None:
            self.l_receive = Label(self.root, text=int(self.receive))
            self.l_receive.grid(row=self.row_i + 5, column=self.column_i)
        else:
            self.calculate_ratio_and_receive()
            self.l_receive['text'] = int(self.receive)

    def add_label_ratio(self):
        self.l_ratio = Label(self.root, text=round(self.ratio, 3))
        self.l_ratio.grid(row=self.row_i + 5, column=self.column_i + 4)

    def add_other_labels(self):
        self.l_player = Label(self.root, text='Trader')
        self.l_player.grid(row=self.row_i + 5, column=self.column_i + 2)
        self.l_duration = Label(self.root, text=0)
        self.l_duration.grid(row=self.row_i + 5, column=self.column_i + 3)
        self.l_availability = Label(self.root, text='Unlimited')
        self.l_availability.grid(row=self.row_i + 5, column=self.column_i + 5)

    def add_button_barter(self):
        self.b_barter = Button(self.root, text='Barter', command=self.accept)
        self.b_barter.grid(row=self.row_i + 5, column=self.column_i + 6)

    #
    def accept(self):
        if self.resource_receive['name'].get() != self.resource_send['name'].get():
            self.add_label_receive()
            resource_send = {'name': self.resource_send['name'].get(), 'total': int(self.e_for.get())}
            resource_receive = {'name': self.resource_receive['name'].get(), 'total': int(self.l_receive['text'])}
            if self.village.resources.dictionary[resource_send['name']].total > resource_send['total']:
                self.village.resources.dictionary[resource_send['name']].total -= resource_send['total']
                self.village.resources.dictionary[resource_receive['name']].total += resource_receive['total']
