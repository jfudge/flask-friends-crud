from utilities import filter_input, format_name

class Friend:
    """
    This class defines a Friend.
    """
    def __init__(self, form):
        self.name = form.name.data
        self.image = form.image.data
        self.invited = form.invited.data

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = format_name(value)
        return self.__name

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = filter_input(value, r"([^a-zA-Z0-9_\-.]+)")
        return self.__image

    @property
    def invited(self):
        return self.__invited

    @invited.setter
    def invited(self, value):
        self.__invited = value
        return self.__invited
