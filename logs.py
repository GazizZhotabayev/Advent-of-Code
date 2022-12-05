class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __repr__(self):
        return f"{self.top}/{self.bottom}"

    def __ne__(self, other):
        ne_first_top = self.top * other.bottom
        ne_second_top = self.bottom * other.top
        return ne_first_top != ne_second_top

    def __eq__(self, other):

        if type(self) == type(other):
            first_top = self.top * other.bottom
            second_top = other.top * self.bottom
            return first_top == second_top
        else:
            return False