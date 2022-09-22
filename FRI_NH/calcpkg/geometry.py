class Geo:
    def __init__(self, *argm):
        self.width = argm[0]
        self.height = argm[1]
        self.radius = argm[0]

    def tri_area(self):
        return self.width * self.height / 2

    def rect_area(self):
        return self.width * self.height

    def circle_area(self):
        return self.radius**2 * 3.14