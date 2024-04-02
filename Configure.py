import os
import configparser as cp
from FileHandling import FileHandler as fh

class Settings:
    def __init__(self):
        self.config = cp.ConfigParser()
        setting = self.getConfig()
        self.cropText = setting.get("Paths", "cropText")
        self.Translated = setting.get("Paths", "Translated")
    def createConfig(self):
        file = fh()
        self.config.add_section("Paths")
        if file.find_directory("cropText"):
            # found the directory
            self.config.set("Paths", "cropText", file.find_directory("cropText"))
        else:
            # not found -> create a new directory
            path = os.path.join(os.getcwd(),"cropText")
            os.mkdir(path)
            self.config.set("Paths", "cropText", path)
        if file.find_directory("Translated"):
            # found the directory
            self.config.set("Paths", "Translated", file.find_directory("Translated"))
        else:
            # not found -> create a new directory
            pathT = os.path.join(os.getcwd(),"Translated")
            os.mkdir(pathT)
            self.config.set("Paths", "Translated", pathT)
        with open("settings.ini", "w") as setting:
            self.config.write(setting)
    def getConfig(self):
            if not os.path.exists("settings.ini"):
                self.createConfig()
            self.config = cp.ConfigParser()
            self.config.read("settings.ini")
            return self.config
    def updateSetting(self, section, setting, value):
            self.config = self.getConfig()
            self.config.set(section, setting, value)
            with open("settings.ini", "w") as updated:
                self.config.write(updated)
    def getUpdateInfo(self):
            self.cropText = self.config.get("Paths", "cropText")
            self.Translated = self.config.get("Paths", "Translated")
            