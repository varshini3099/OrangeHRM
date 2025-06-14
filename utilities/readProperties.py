import configparser

config = configparser.RawConfigParser()
config.read("..\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'loginURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
