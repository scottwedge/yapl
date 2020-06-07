import tensorflow as tf


class Data:
    r"""
        Description: Define Data Retrival and logics here, 
                    like load from csv file or from folder
    """
    def __init__(self, location : str):
        self._location = location
        self._dataset = tf.data.Dataset

    def _loadFile(self):
        pass

    def _prepateData(self):
        self._loadFile()
        self._dataset.shuffle()

    def getData(self):
        # Only public function of class
        self._prepateData()

        return self._dataset
