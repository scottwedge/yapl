class TestConfig:
    '''
        Extend this Base class to avoid Re-writing most of the things

        example:
            class config(TestConfig):
                DATA_FILE = '../hsjdhfs/sdfjsk.zip'
                DEVICE = 'cpu'

            config = config()
            config.DEVICE
            config.BATCHSIZE
    '''
    
    OPTIMIZER = 0.0001
    DEVICE = 'cuda'

    BATCHSIZE = 32