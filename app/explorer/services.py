from os import walk

from .domain import Folder

class ExplorerService:

    @staticmethod
    def getDirectoryItems(path):
        f = []
        d = []
        for (dirpath, dirnames, filenames) in walk(path):
            f.extend(filenames)
            d.extend(dirnames)
            break
        #return Folder(path, d, f)
        return {
            "path" : path,
            "folders" : d,
            "files" : f,
        }
