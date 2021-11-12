import json
import coms    
from os.path import exists
import gui.std_data_window as std_data_window
import gui.main_window as main_window


if __name__ == '__main__':
    if not exists("config.json"):
        coms.init_json()

    with open("config.json", "r") as file:
        config = json.load(file)

    if config["GROUP"] == "none" or config["LANG"] == "none" or config["SEMIG"] == "none":
        std_data_window.window()

    main_window.main_window()