

class QuantityException(Exception):
    """ Класс исключения для обработки ситуации нулевого количества товаров в категории. """

    def __init__(self, message=None):
        self.message = message if message else "Обнаружен товар с нулевым количеством."

    def __str__(self):
        return self.message
