import yaml

class Config:
    '''
        Extend this Base class to avoid Re-writing most of the things

        example:
            class config(Config):
                def __init__(self):
                    super().__init__()
                    self.EXPERIMENT = {
                        'NAME':"Exp1",
                        'DATE' : datetime.datetime.now(),
                    }
                    self.DATA_FILE = '../hsjdhfs/sdfjsk.zip'
                    self.DEVICE = 'cpu'

            config = config()
            config.DEVICE
            config.BATCHSIZE
    '''

    def __init__(self):
        self.DO_FINETUNE = True
        
        self.OPTIMIZER_RATE = 0.0001
        self.DEVICE = 'cuda'

        self.BATCH_SIZE = 32
        self.BUFFER_SIZE = 100
        self.EPOCHES = 5 

    def dumpconfig(self, location):
        with open(location, 'w') as dumpfile:
            yaml.dump(self.__dict__, dumpfile)

        return "you file has successfully saved"