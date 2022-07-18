from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Iterable, DefaultDict


class Size:

    def __init__(self, *args, dim=None):
        if isinstance(args[0], Iterable):
            self._value = tuple(args[0])
        elif dim:
            if len(args) > 0:
                raise ValueError("Can not set dim and multiple values")
            self._value = tuple(args * dim)
        else:
            self._value = tuple(args)

    def __add__(self, other: "Size"):
        return Size(a + b for a, b in zip(self, other))

    def __sub__(self, other):
        return Size(a - b for a, b in zip(self, other))

    def __getitem__(self, item):
        return self._value[item]

    def __len__(self):
        return len(self._value)

    def __iter__(self):
        return iter(self._value)

    def __repr__(self):
        return f"<{','.join(map(str, self._value))}>"

    def __hash__(self):
        return hash(self._value)

    def __eq__(self, other: "Size"):
        return hash(self) == hash(other)

    def __lt__(self, other: "Size"):
        for v1, v2 in zip(self, other):
            if v1 >= v2:
                return False
        return True

    def __le__(self, other):
        for v1, v2 in zip(self, other):
            if v1 > v2:
                return False
        return True

    def __gt__(self, other: "Size"):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)


class Item:

    def __init__(self, size: Size):
        self._size = size
        self._dim = len(self._size)

    @property
    def dim(self):
        return self._dim

    @property
    def size(self):
        return self._size

    def __repr__(self):
        return f"<Item, size: {repr(self.size)} >"


class Bin:

    def __init__(self, size: Size):
        self._size: Size = size
        self._empty_space: Size = size
        self._dimension: int = len(size)
        self._items: List[Item] = list()
        self._size_count: DefaultDict[Size, int] = defaultdict(lambda: 0)

    def add_item(self, item: Item):
        if not self.has_spot(item):
            raise ValueError("Bin does not have enough space for this item. You should call has_spot method first")
        self._empty_space -= item.size
        self._items.append(item)
        self._size_count[item.size] += 1

    def has_spot(self, item: Item) -> bool:
        return item.size <= self._empty_space

    @property
    def size(self):
        return self._size

    @property
    def empty_space(self):
        return self._empty_space

    @property
    def dimension(self):
        return self._dimension

    @property
    def packed_items(self):
        return list(self._items)

    @property
    def size_count(self):
        return dict(self._size_count)

    def __repr__(self):
        sizes = []
        for size, value in self._size_count.items():
            sizes.append(f"{size} : {value}")
        items = ",\n".join(sizes)
        return f"[Bin: \n{items}\n]"





