import json

groups = ['1','2','3','4','5']
langs  = {
    '1':'english',
    '2':'german',
    '3':'italian',
    '4':'french',
    '5':'spanish'
}
semigs = ['1','2']
optional_classes = {
    '1':'doctrine',
    '2':'management',
    '3':'fiscalitate',
    '4':'none'
}

def init_json():
    config = {
        "GROUP":"none",
        "LANG":"none",
        "SEMIG":"none",
        "OPTIONAL":"none"
    }

    with open("config.json", "w") as file:
        json.dump(config, file)

def std_group(group):
    group = str(group)

    with open("config.json", "r") as file:
        config = json.load(file)
    
    config["GROUP"] = group
    with open("config.json", "w") as file:
        json.dump(config, file)
    
def std_lang(lang):
    lang = str(lang)

    with open("config.json", "r") as file:
        config = json.load(file)

    config["LANG"] = lang
    with open("config.json", "w") as file:
        json.dump(config, file)

def std_semig(semig):
    semig = str(semig)

    with open("config.json", "r") as file:
        config = json.load(file)

    config["SEMIG"] = semig
    with open("config.json", "w") as file:
        json.dump(config, file)

def std_optional(optional):
    optional = str(optional)

    with open("config.json", "r") as file:
        config = json.load(file)
    
    config["OPTIONAL"] = optional
    with open("config.json", "w") as file:
        json.dump(config, file)