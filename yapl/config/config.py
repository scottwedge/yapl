import yaml

class Config:

    def __init__(self, FILE_LOC):
        self.FILE = FILE_LOC
        self._loaddata()

    def _loaddata(self):
        with open(self.FILE, 'r') as infile:
            try:
                self.__dict__.update(yaml.safe_load(infile))
            except yaml.YAMLError as errors:
                raise errors.InvalidPackageListFormat("Invalid YAML in package list: %s" % str(ex))
