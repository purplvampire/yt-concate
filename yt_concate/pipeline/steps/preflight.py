from .step import Step


# 繼承Step class
class Preflight(Step):
    def process(self, data, inputs, utils):
        print('Processing Preflight...\n')
        utils.create_dirs()
