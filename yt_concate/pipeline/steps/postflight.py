from .step import Step

# 繼承Step class
class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')