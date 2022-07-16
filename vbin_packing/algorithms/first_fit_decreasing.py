from operator import itemgetter
from typing import List

from ..types import Size, Item, Bin
from .first_fit import FirstFit


class FirstFitDecreasing:
    KEY_DIM = 1

    def __init__(self, size: Size, sigma: List[Item]):
        self._bin_size = size
        self.sigma = sigma
        self.first_fit = None

    def solve(self, strategy, **kwargs):
        if strategy == self.__class__.KEY_DIM:
            dim = kwargs.pop("dim")
            sorted_sigma = sorted(self.sigma, key=self.key_dim_sort_key(dim), reverse=True)
        else:
            raise NotImplementedError

        self.first_fit = FirstFit(self._bin_size)
        for item in sorted_sigma:
            self.first_fit.pack_item(item)

    @property
    def cost(self):
        return self.first_fit.cost

    @property
    def solution(self):
        return self.first_fit.solution

    @staticmethod
    def key_dim_sort_key(dim):
        def func(item: Item):
            return item.size[dim]
        return func


