class Animal():
    """A class for characterizing animal."""
    def __init__(self, feet, food, lay_eggs):
        self.feet = feet
        self.food = food
        self.lay_eggs = lay_eggs

    def __str__(self):
        return u'No. of feet:%s, Food:%s, Lay Eggs:%s' % (self.feet, self.food, self.lay_eggs)
