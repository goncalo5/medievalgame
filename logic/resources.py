import constants


class Resources(object):
    def __init__(self):
        self.list = []
        self.dictionary = {}
        self.n = None
        self.create_resources_objects()

    def create_resources_objects(self):
        for resource in constants.RESOURCES:
            obj = self
            name = resource['name']
            value = Resource(**resource)
            setattr(obj, name, value)
            self.list.append(getattr(obj, name))
            self.__dict__[name] = getattr(obj, name)
        self.n = len(self.list)


class Resource(object):
    def __init__(self, index, name, total, per_s=None, rate_per_s=None):
        self.index = index
        self.name = name
        self.total = total
        self.per_s0 = self.per_s = per_s
        self.rate_per_s = rate_per_s

        # Null variables

        # initial methods

    # Data Base
    # GET
    def see_total_in_db(self):
        pass

    # PUT
    def save_total_in_db(self):
        pass

    def updating_total_in_db(self):
        pass
