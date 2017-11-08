import re


data = '''
           "MaxCapacity" = 4540
           "CurrentCapacity" = 2897
           "LegacyBatteryInfo" = {"Amperage"=18446744073709550521,"Flags"=4,"Capacity"=4540,"Current"=2897,"Voltage"=7283,"Cycle Count"=406}
           "DesignCapacity" = 6700
'''


def get_battery_level(data):
    data = data.split("\n")
    data_dict = {}
    for i in data:
        k = i.find('=')
        if k > 0:
            data_dict.update({re.sub('[\s+\"]', '', i[:k]) : i[k+2:]})
    level = float(data_dict["CurrentCapacity"])/float(data_dict["MaxCapacity"])
    return "{:.2%}".format(level)