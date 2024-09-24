import configparser  # this is used to read the data from ini file

config = configparser.RawConfigParser()  # creating an object for  RawConfigParser()
config.read("/home/manikrishna/Pycharm/Python_Automation//configarations/config.ini")


# here im creating one class for fetching the data from an imi file

class Read_config:
    @staticmethod  # we need to crate static method
    def get_admin_page_url():  # this is a static method for calling url
        url = config.get('admin login info',
                         'admin_page_url')  # here with config we need to call get inside that we need to pass ini section name, after that we need to pass key , it will return value
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('admin login info', 'invalid_username')
        return invalid_username

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('admin login info', 'invalid_password')
        return invalid_password

    @staticmethod
    def get_product():
        iphone = config.get('admin login info', 'iphone')
        return iphone
