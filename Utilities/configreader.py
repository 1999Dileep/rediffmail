from configparser import ConfigParser


def ConfigReader(section, Key):
    config = ConfigParser()
    config.read("C:\\Users\\HP\\Desktop\\automation\\RediffMail\\ConfigurationData\\config.ini")
    return config.get(section, Key)