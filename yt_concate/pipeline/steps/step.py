from abc import ABC
from abc import abstractmethod


# 建立抽象類別
class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs):  # 用字典把要用的參數打包起來(inputs)
        pass


class StepException(Exception):
    pass
