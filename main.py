import json
import acces_zoom as az

groups = ['1','2','3','4','5']
langs  = {
    '1':'english',
    '2':'german',
    '3':'italian',
    '4':'french',
    '5':'spanish'
}
semig = ['1','2']

def reset():
    with open("config.json", "r") as file:
        config = json.load(file)

    config["GROUP"] = 'none' 
    config["LANG"]  = 'none'
    config["SEMIG"] = 'none'

    with open("config.json", "w") as file:
                json.dump(config, file)

def std_data():
    with open("config.json", "r") as file:
        config = json.load(file)
    
    if config["GROUP"] == "none":
        print("Choose your group from: " + str(groups))
        inp = input()

        if inp in groups:
            config["GROUP"] = inp
            with open("config.json", "w") as file:
                json.dump(config, file)
        else:
            std_data()
    
    if config["LANG"] == "none":
        print("Choose your language from: " + str(langs))
        inp = input()

        if inp in langs:
            config["LANG"] = inp
            with open("config.json", "w") as file:
                json.dump(config, file)
        else:
            std_data()

    if config["SEMIG"] == "none":
        print("Choose your semigroup from: " + str(semig))
        inp = input()

        if inp in semig:
            config["SEMIG"] = inp
            with open("config.json", "w") as file:
                json.dump(config, file)
        else:
            std_data()

if __name__ == '__main__':
    reset()
    std_data()

    with open("config.json", "r") as file:
        config = json.load(file)
        
    az.acces(config["GROUP"], config["LANG"], config["SEMIG"],)
