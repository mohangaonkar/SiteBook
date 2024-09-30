import  configparser

config = configparser.RawConfigParser()
config.read("Configurations/config.ini")


class readconfig():
    @staticmethod
    def appURL():
        return config.get('common info','baseURL')


    @staticmethod
    def Usernumber():
        return config.get('common info','usernumber')


    @staticmethod
    def Password():
        return config.get('common info','password')

    @staticmethod
    def get_quantity_exavation():
        return config.get('quotation details', 'quantity_exavation')

    @staticmethod
    def get_unit_exavation():
        return config.get('quotation details', 'unit_exavation')

    @staticmethod
    def get_rate_exavation():
        return config.get('quotation details', 'rate_exavation')