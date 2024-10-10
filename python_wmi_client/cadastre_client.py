#import sections as sections
import wmi
import configparser
import os



# créer un nouvel objet wmi
c = wmi.WMI()

# créer un nouvel objet configuration
config = configparser.ConfigParser()
absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
config.read(path + '\\' + 'wmi.ini')


def get_network_interface():

    for os in c.Win32_OperatingSystem():
        print(os.Caption)


def get_wmi_object(section, processing_options, static_options):
    wmi_ojects = eval('c.'+section+'()')
    if ((config[section]['active']).lower()) == 'yes':
        for object in wmi_ojects:
            for key in config[section]:
                value = (config[section][key])
                if key.lower() != 'item':
                    try:
                        if key.lower() not in processing_options and key.lower() not in static_options:
                            print(key+' : '+eval(str('object.' + value)))
                        else:
                            print(key+' : '+value)
                    except:
                        print('No value find for : ' + key)

                else:
                    print('*********************************************')
                    print(value)
                    print('*********************************************')


def get_categories(options):
    for section in config.sections():
        if ((config[section]['active']).lower()) == 'yes':
            for key in config[section]:
                if key.lower() == 'category':
                    print((config[section][key]))
                    options.append((config[section][key]))


def main():
    processing_options = ['active']
    static_options = ['category']
    options = ['active']
    get_categories(options)
    for section in config.sections():
        get_wmi_object(section, processing_options, static_options)


class Item:
    def __init__(self, sub_items):
        self.sub_items = []
    
    def set_sub_items(self,sub_item):
        self.sub_items.append(sub_item)

class SubItem:
    def __init__(self,properties):
        self.properties = []


class Property:
    def __init__(self,key,value):
        self.key = key
        self.value = value



if __name__ == "__main__":
    main()