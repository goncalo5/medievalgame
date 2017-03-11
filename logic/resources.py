import constants


class Resources(object):
    def __init__(self):
        self.list = []
        self.dictionary = {}
        self.n = None
        self.create_resources_objects()

    def create_resources_objects(self):
        for resource in constants.RESOURCES:
            self.add_resource(resource)
        self.n = len(self.list)

    def add_resource(self, resource):
        self.list.append(Resource(**resource))
        new = self.list[-1]
        self.__dict__[new.name] = new
        self.dictionary[new.name] = new

    def __iter__(self):
        return iter(self.list)


class Resource(object):
    def __init__(self, index, name, total, per_s=None, rate_per_s=None):
        self.index, self.name, self.total, self.per_s, self.rate_per_s =\
            index, name, total, per_s, rate_per_s

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
