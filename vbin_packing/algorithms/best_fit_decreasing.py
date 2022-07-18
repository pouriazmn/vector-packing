from typing import List

from ..types import Size, Item, Bin
from .best_fit import BestFit
from .first_fit_decreasing import FirstFitDecreasing


class BestFitDecreasing(FirstFitDecreasing):

    def __init__(self, size: Size, sigma: List[Item]):
        super().__init__(size, sigma)

    def solve(self, strategy, **kwargs):
        sorted_sigma = self.sorted_sigma(strategy, **kwargs)
        self.packing_alg = BestFit(self._bin_size)
        for item in sorted_sigma:
            self.packing_alg.pack_item(item)

