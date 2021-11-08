import time
import webbrowser
import teachers as t

tm = time.localtime()

def monday(GROUP, LANG, SEMIG):
    # if (tm.tm_hour >= 7 or tm.tm_hour >= 8) and (tm.tm_hour <= 9 and tm.tm_min <= 30):
    #     if GROUP == '1':
    #         webbrowser.open(t.teachers[""])
    #     if GROUP == '2':
    #         webbrowser.open(t.teachers[""])
    #     if GROUP == '3':
    #         webbrowser.open(t.teachers[""])
    #     if GROUP == '4':
    #         webbrowser.open(t.teachers[""])
    #     if GROUP == '5':
    #         webbrowser.open(t.teachers[""])
    elif ((tm.tm_hour >= 9 and tm.tm_min >= 39) or tm.tm_hour >= 10) and ((tm.tm_hour < 11) or (tm.tm_hour <= 11 and tm.tm_min <= 10)):
        if GROUP == '1':
            webbrowser.open(t.teachers["cuceu"])
        if GROUP == '2':
            webbrowser.open(t.teachers["cuceu"])
        if GROUP == '3':
            webbrowser.open(t.teachers["cuceu"])
        if GROUP == '4':
            webbrowser.open(t.teachers["cuceu"])
        if GROUP == '5':
            webbrowser.open(t.teachers["cuceu"])
    elif ((tm.tm_hour >= 11 and tm.tm_min >= 19) or tm.tm_hour >= 12) and (tm.tm_hour < 13):
        if GROUP == '1':
            webbrowser.open(t.teachers["silaghi"])
        if GROUP == '2':
            webbrowser.open(t.teachers["silaghi"])
        if GROUP == '3':
            webbrowser.open(t.teachers["silaghi"])
        if GROUP == '4':
            webbrowser.open(t.teachers["silaghi"])
        if GROUP == '5':
            webbrowser.open(t.teachers["silaghi"])
    elif (tm.tm_hour >= 13) and (tm.tm_hour <= 14 or (tm.tm_hour <= 15 and tm.tm_min <= 40)):
        if GROUP == '1':
            webbrowser.open(t.teachers[""])
        if GROUP == '2':
            webbrowser.open(t.teachers[""])
        if GROUP == '3':
            webbrowser.open(t.teachers[""])
        if GROUP == '4':
            webbrowser.open(t.teachers[""])
        if GROUP == '5':
            webbrowser.open(t.teachers[""])
    elif ((tm.tm_hour >= 15 and tm.tm_min >= 39) or tm.tm_hour >= 16) and (tm.tm_hour < 17 or (tm.tm_hour <= 17 and tm.tm_min <= 10)):
        if GROUP == '1':
            webbrowser.open(t.teachers[""])
        if GROUP == '2':
            webbrowser.open(t.teachers[""])
        if GROUP == '3':
            webbrowser.open(t.teachers[""])
        if GROUP == '4':
            webbrowser.open(t.teachers[""])
        if GROUP == '5':
            webbrowser.open(t.teachers[""])
    elif ((tm.tm_hour >= 17 and tm.tm_min >= 19) or tm.tm_hour >= 18) and (tm.tm_hour < 18 or (tm.tm_hour <= 18 and tm.tm_min <= 30)):
        if GROUP == '1':
            webbrowser.open(t.teachers[""])
        if GROUP == '2':
            webbrowser.open(t.teachers[""])
        if GROUP == '3':
            webbrowser.open(t.teachers[""])
        if GROUP == '4':
            webbrowser.open(t.teachers[""])
        if GROUP == '5':
            webbrowser.open(t.teachers[""])
    elif ((tm.tm_hour >= 18 and tm.tm_min >= 59) or tm.tm_hour >= 19) and (tm.tm_hour <= 21):
        if GROUP == '1':
            webbrowser.open(t.teachers[""])
        if GROUP == '2':
            webbrowser.open(t.teachers[""])
        if GROUP == '3':
            webbrowser.open(t.teachers[""])
        if GROUP == '4':
            webbrowser.open(t.teachers[""])
        if GROUP == '5':
            webbrowser.open(t.teachers[""])
    else:
        tm.sleep(30)
        get_to_class(GROUP, LANG, SEMIG)