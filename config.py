#ll CONFIG FOR lzokn logger (main.py) ll#
try:
    from user import *
except:
    app_id = input("#ll Please, authorize on my.telegram.org/\n#ll api_id = ")
    app_hash = input("#ll api_hash = ")
    session_name = "lzokn"
    user_file = open("user.py", "w")
    user_file.write(f'app_id = "{app_id}"\napp_hash = "{app_hash}"\nsession_name = "{session_name}"')
    user_file.close()
    from user import *
import os
from time import sleep
#ll Free to use ll#
lzokn_name = "Pars-log.err"
lzokn_version = "1.4"
lzokn_status = "Success"
lzokn_info = f"{lzokn_name} made by lzokn. Now {lzokn_status} v{lzokn_version}"
#ll @lzokn for contact ll#

help_txt = f"Hi! {lzokn_name} {lzokn_version}\n/add - add group\n/del - delete group\n/delete - delete all groups\n/nels I unnels - not yet :("

extens = {
    "PHOTO" : ".png",
    "VOICE" : ".mp3",
    "VIDEO" : ".mp4",
    "VIDEO_NOTE" : ".mp4",
    "AUDIO" : ".mp3",
    "STICKER" : ".png",
    "ANIMATION" : ".mp4"}



async def login(app):
    async with app:
        await app.send_message("me", f'Hi! Now you are using "{lzokn_name}" v{lzokn_version}, based on pyrogram. My telegram is @lzokn. To learn more, write /help.')        
                        
class Helper():

        
    def load(self, msg, dir):
        date = str(msg.date)
        med_type = str(msg.media).split('.', maxsplit=1)[1]
        if not os.path.exists(dir + med_type):
            os.mkdir(dir + med_type)
        if med_type in extens:
            ext = extens[med_type]
        else:
            ext = ".none"
        loaded = False
        while not loaded:
            try:         
                msg.download(
                dir + med_type + "/" + f"{msg.from_user.username} [" + str(msg.date).replace(" ", "] ").replace(":", "-")[:-3] + ext)
                loaded = True
            except Exception as e:
                print(f"\n{e}")
            
        return f"*{med_type}*"
        
        
    def write(self, msg, dir, logg_text, cwith):
        path = dir + "log.txt"
        if os.path.exists(path):
            file = open(path, "a")
        else:
            file = open(path, "w")
            file.write(f'{lzokn_info}\nFile created at {msg.date}.\nChat "{cwith[0]}" (@{cwith[1]})\n\n\n')
        file.write(f"[{msg.date}] {msg.from_user.username}: {logg_text}\n")
        file.close()
        
        
    def white_check(self):
        file_name = "logs/white_list.txt"
        if not os.path.exists(file_name):
            open(file_name, "a").close()
        idss = open(file_name, "r")
        white_list = idss.read().split("\n")
        idss.close()
        return white_list


    def white_write(self, white_list):
        file = open("logs/white_list.txt", "w")
        white_ids = ""
        for id in self.clear(white_list):
            white_ids = white_ids + id + "\n"
        file.write(white_ids)
        file.close()
        
        
    def logg(self, text, msg):
        msg.edit(text)
        sleep(0.9)
        msg.delete()
    
    
    def clear(self, list):
        trash = ["", " "]
        for trash in trash:
            if trash in list:
                list.remove(trash)
        return list
