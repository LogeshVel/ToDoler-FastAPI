
class NegativeNumberException(Exception):
    def __init__(self, neg_id):
        self.negative_id = neg_id

