from ..types import Bin, Item, Size
from typing import List


class FirstFit:

    def __init__(self, bin_size: Size):
        self._bin_size = bin_size
        self._bins: List[Bin] = list()

    def pack_item(self, item: Item):
        assert item.size <= self._bin_size
        packed = False
        for bin in self._bins:
            if bin.has_spot(item):
                bin.add_item(item)
                packed = True
                break

        if not packed:
            new_bin = Bin(self._bin_size)
            new_bin.add_item(item)
            self._bins.append(new_bin)

    @property
    def cost(self):
        return len(self._bins)

    @property
    def solution(self):
        return list(self._bins)
