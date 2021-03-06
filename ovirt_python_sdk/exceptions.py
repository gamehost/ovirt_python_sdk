class OvirtException(Exception):
    pass


class TooManyItemsException(OvirtException):
    def __init__(self, count: int):
        self.count = count

    def __str__(self) -> str:
        return f'Ожидался 1 элемент, получено {self.count}'


class NotEnoughMemoryException(OvirtException):
    def __init__(self, free: int, excepted: int):
        self.free = free
        self.excepted = excepted

    def __str__(self) -> str:
        return f'Ожидалось {self.excepted} Б, свободно {self.free}'


class ItemNotFoundException(OvirtException):
    def __init__(self, item_name: str):
        self.item_name = item_name

    def __str__(self) -> str:
        return f'Не найдено "{self.item_name}"'
