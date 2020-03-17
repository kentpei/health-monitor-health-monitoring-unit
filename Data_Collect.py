def data_collect(dict):
    # description: Receive in-time data (Pulse, Blood Pressure and Oxygen Level)
    #              and handle exception, return in time data
    # INPUT:    Python Dictionary in time generated (value of items can be int or float)
    # OUTPUT:   Python Dictionary data after exception handle
    # EXAMPLE:  data1 = {'Pulse' : 75, 'BP' : 120, 'OL' : 340}
    #               data_collect(data1) -> {'Pulse' : 75, 'BP' : 120, 'OL' : 340}
    #           data2 = {'Pulse' : None, 'BP' : 120, 'OL' : 340}
    #               data_collect(data2) -> {'Pulse' : None, 'BP' : 120, 'OL' : 340}

    # Check if data keys in dict, if not, give None value
    if "Pulse" not in dict.keys():
        dict["Pulse"] = None
    if "BP" not in dict.keys():
        dict["BP"] = None
    if "OL" not in dict.keys():
        dict["OL"] = None

    pulse = dict['Pulse']
    bp = dict['BP']
    ol = dict['OL']

    parse = {}

    # data type check
    data = [pulse, bp, ol]

    for key in dict.keys():
        value = dict[key]
        # wrong data type -> set None
        if value is not None and not isinstance(value, int) and not isinstance(value, float):
            parse[key] = None
        # negative value -> set None
        elif (isinstance(value, int) and value < 0) or (isinstance(value, float) and value < 0):
            parse[key] = None
        # else just parse
        else:
            parse[key] = value
    # print(parse)
    return parse

def test_data_collect():
    data1 = {'Pulse': None, 'BP': 120, 'OL': 340} # int parse
    data2 = {'Pulse': 75, 'BP': 120.0, 'OL': 340} # float parse
    data3 = {'Pulse': "wrong type test", 'BP': 120, 'OL': 340} # wrong type exception
    data4 = {'Pulse': "wrong type test", 'BP': -120, 'OL': 340} # negative number exception
    assert data_collect(data1) == {'Pulse': None, 'BP': 120, 'OL': 340}
    assert data_collect(data2) == {'Pulse': 75, 'BP': 120.0, 'OL': 340}
    assert data_collect(data3) == {'Pulse': None, 'BP': 120, 'OL': 340}
    assert data_collect(data4) == {'Pulse': None, 'BP': None, 'OL': 340}

# test_data_collect()
