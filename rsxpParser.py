import yaml

def handle_per_band_conf(config: list):
    print(config)
    bandList = config['band'].replace(" ","").split(",")
    dlPortList = config['downlink'].replace(" ","").split(",")
    dlAttenList = ""
    if(isinstance(config['downlink_attenuation'], int)):
        dlAttenList = str(config['downlink_attenuation'])
    else:
        dlAttenList = config['downlink_attenuation'].replace(" ","").split(",")
    ulPortList = config['uplink'].replace(" ", "").split(",")
    ulAttenList = ""
    if (isinstance(config['uplink_attenuation'], int)):
        ulAttenList = str(config['uplink_attenuation'])
    else:
        ulAttenList = config['uplink_attenuation'].replace(" ", "").split(",")

    for dlPort in dlPortList:
        print(dlPort+", "+str(bandList)+","+str(dlPort in ulPortList))


with open(r'C:\Users\wan_f\PycharmProjects\pythonDemo\test_connection_setup.rsxp') as file:
    whole_list = yaml.load(file, Loader=yaml.FullLoader)
    #print(whole_list)
    content = whole_list['ConnectionSetup']
    #print(content)
    print('name: ' + content['name'])
    for key in content:
        if key!= "name":
            print(key, *content[key], sep=", ")
            handle_per_band_conf(content[key])

        # if item:
        #     # print(item, *FR1Content[item], sep=", ")
        #
