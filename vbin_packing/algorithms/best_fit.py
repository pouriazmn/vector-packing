from ..types import Bin, Item, Size
from typing import List


class BestFit:

    def __init__(self, bin_size: Size):
        self._bin_size = bin_size
        self._bins: List[Bin] = list()

    def pack_item(self, item: Item):
        assert item.size <= self._bin_size
        best_bin, bb_empty_space = None, self._bin_size
        for bin in self._bins:
            if bin.has_spot(item) and bin.empty_space < bb_empty_space:
                best_bin = bin
                bb_empty_space = bin.empty_space

        if best_bin:
            best_bin.add_item(item)
        else:
            new_bin = Bin(self._bin_size)
            new_bin.add_item(item)
            self._bins.append(new_bin)

    @property
    def cost(self):
        return len(self._bins)

    @property
    def solution(self):
        return list(self._bins)