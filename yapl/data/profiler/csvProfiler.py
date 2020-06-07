import numpy as np
import pandas as pd

class ProfileCsv:
    def __init__(self, df, preprocess=False):
        self.df = df
        self.preprocess = preprocess

    def _preprocess(self):
        pass

    def show(self):
        if self.preprocess:
            self._preprocess()

        return self.df.describe()
