import os

class FileHandler:
    def __init__(self):
        self.baseDir = self.findBase()
        os.chdir(self.baseDir)
    # Find the base directory of the project
    def findBase(self):
        directory = os.getcwd()
        if "DichTruyen" not in directory:
            directory = self.find_directory("DichTruyen")
        return directory
    # Find the directory of the folder
    def find_directory(self, folderName):
        for r,d,f in os.walk(os.getcwd()):
            for folder in d:
                if folder == folderName:
                    return os.path.join(r,folder)
    # Delete files in the directory
    def deleteFiles(self, directory):
        for r,d,f in os.walk(directory):
            for file in f:
                os.remove(directory+"\\{}".format(file))
