import configparser #https://zetcode.com/python/configparser/#:~:text=ConfigParser%20is%20a%20Python%20class,customized%20by%20end%20users%20easily.

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password
