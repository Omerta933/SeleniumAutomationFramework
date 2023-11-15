from configparser import ConfigParser

config = ConfigParser()
config.read("..\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getAplicationURL():
        url = config.get('common_info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common_info', 'useremaile')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common_info', 'password')
        return password

