from typing import List
from math import prod

from ..types import Size, Item, Bin
from .first_fit import FirstFit


class FirstFitDecreasing:
    KEY_DIM = 1
    PROD = 2

    def __init__(self, size: Size, sigma: List[Item]):
        self._bin_size = size
        self.sigma = sigma
        self.packing_alg = None

    def sorted_sigma(self, strategy, **kwargs):
        if strategy == self.__class__.KEY_DIM:
            dim = kwargs.pop("dim")
            return sorted(self.sigma, key=self.key_dim_sort_key(dim), reverse=True)
        if strategy == self.__class__.PROD:
            return sorted(self.sigma, key=self.vector_production, reverse=True)
        else:
            raise NotImplementedError

    def solve(self, strategy, **kwargs):
        sorted_sigma = self.sorted_sigma(strategy, **kwargs)
        self.packing_alg = FirstFit(self._bin_size)
        for item in sorted_sigma:
            self.packing_alg.pack_item(item)

    @property
    def cost(self):
        return self.packing_alg.cost

    @property
    def solution(self):
        return self.packing_alg.solution

    @staticmethod
    def key_dim_sort_key(dim):
        def func(item: Item):
            return item.size[dim]
        return func

    @staticmethod
    def vector_production(item: Item):
        return prod(item.size)


