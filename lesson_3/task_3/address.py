class Address:
    def __init__(self, _postcode, _city, _street, _building, _appartment):
        self.postcode = _postcode
        self.city = _city
        self.street = _street
        self.building = _building
        self.appartment = _appartment

class Mailing:
    def __init__(self, _to, _from, _cost, _track):
        self.toPointB = _to
        self.fromPointA = _from
        self.cost = _cost
        self.track = _track