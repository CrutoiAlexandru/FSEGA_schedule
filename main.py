import json
import coms    
import datetime   
from os.path import exists
import days_of_the_week.monday as monday
# import days_of_the_week.tuesday as tuesday
# import days_of_the_week.wednesday as wednesday
# import days_of_the_week.thursday as thursday
# import days_of_the_week.friday as friday


if __name__ == '__main__':
    if not exists("config.json"):
        coms.init_json()

    coms.std_data()

    with open("config.json", "r") as file:
        config = json.load(file)

    day = datetime.datetime.today().weekday()

    if day == 0:
        monday.monday(config["GROUP"], config["LANG"], config["SEMIG"])
    if day == 1:
        tuesday.tuesday(config["GROUP"], config["LANG"], config["SEMIG"])
    if day == 2:
        wednesday.wednesday(config["GROUP"], config["LANG"], config["SEMIG"])
    if day == 3:
        thursday.thursday(config["GROUP"], config["LANG"], config["SEMIG"])
    if day == 4:
        friday.friday(config["GROUP"], config["LANG"], config["SEMIG"])