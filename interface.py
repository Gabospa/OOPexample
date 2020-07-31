

#clase tipo caja
class Box:
    #metodo para añadir cualquier numero de items a la caja
    def add(self, *items):
        raise NotImplementedError()
    #empty debe sacar todos los elementos de la caja y retornarlos como una lista
    def empty(self):
        raise NotImplementedError()
    # metodo que cuenta el numero de los elementos en la caja 
    def count(self):
        raise NotImplementedError()

#clase tipo item
class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, *items):
        self._items.extend(items)

    def empty(self):
        items = self._items
        self._items = []
        return items

    def count(self):
        return len(self._items)


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(dict((i.name, i) for i in items))

    def empty(self):
        items = list(self._items.values())
        self._items = {}
        return items

    def count(self):
        return len(self._items)


def repack_boxes(*boxes):
    items = []

    for box in boxes:
        items.extend(box.empty())

    while items:
        for box in boxes:
            try:
                box.add(items.pop())
            except IndexError:
                break

box1 = ListBox()
box1.add(Item(str(i), i) for i in range(20))

box2 = ListBox()
box2.add(Item(str(i), i) for i in range(9))

box1 = DictBox()
box1.add(Item(str(i), i) for i in range(5))

repack_boxes(box1, box2, box3)

print(box1.count())
print(box2.count())
print(box3.count())