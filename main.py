#ll Now code ll#
import pip
try:
    from pyrogram import Client, filters
except:
    print("#ll Installing Pyrogram.")
    package = "pyrogram"
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
    print("\n"*100 + "#ll Pyrogram installed!" + "\n"*10)
from datetime import datetime
try:
    from config import *
except Exception as e:
    print("#ll Could't find config!")
    exit()
    
    
try: 
    app = Client(
        session_name,
        api_id=app_id,
        api_hash=app_hash,
        device_model = f"Lzokn Logger {lzokn_version}",
        app_version = "MeowMew",
        system_version = "I love lzokn <3")
except Exception as e:
      print("#ll Invalid API!")
      os.remove("user.py")
      exit()
      
print(lzokn_info)

if not os.path.exists(f"logs/lzokn_logger_v{lzokn_version}"):
    app.run(login(app))
    os.mkdir("logs")
    open(f"logs/lzokn_logger_v{lzokn_version}", "w").close()
print("#ll Program started ll#")


@app.on_message(filters.command(["help"], "/") & filters.me)
def resp_help(_, msg):
    msg.edit(help_txt)
    

@app.on_message(filters.command(["add", "del", "delete", "nels", "unnels"], "/") & filters.me)
def database_manage(_, msg):
    tg = Helper()
    chat_id = str(msg.chat.id)
    com = msg.command[0]
    white_list = tg.white_check()
    
    if com == "delete":
        white_list.clear()
        tg.logg("ChatS deleted.", msg)
    if com == "add":
        if chat_id not in white_list:
            white_list.append(chat_id)
        tg.logg("Chat added.", msg)
    if com == "del":
            if chat_id in white_list:
                white_list.remove(chat_id)
            tg.logg("Chat deleted.", msg)
    if com == "nels":
        if "lznell" not in white_list:
            white_list.append("lznell")
        tg.logg("Channels added.", msg)
    if com == "unnels":
        if "lznell" in white_list:
            white_list.remove("lznell")
        tg.logg("Channels deleted.", msg)
        
    tg.white_write(white_list)
            
        
@app.on_message(filters.private & ~filters.bot)
def lzokn_logg(_, msg):
    tg = Helper()
    user = app.get_users(msg.chat.id)
    logg_text = "Unknown"
    dir = f"logs/private/{msg.chat.username} ({msg.chat.id})/"
    if not os.path.exists(dir):
        os.makedirs(dir)
    if msg.media:
        logg_text = tg.load(msg, dir)
    if msg.text:
        logg_text = msg.text
    tg.write(msg, dir, logg_text, [user.first_name, user.username])
    
   
@app.on_message(filters.group)
def lzokn_logg(_, msg):
    tg = Helper()
    chat_id = msg.chat.id
    white_list = tg.white_check()
    title = str(msg.chat.title)
    for i in ['/', ':', '*', '?'  '<', '>', '|', '"']:
        title = title.replace(i, " ")        
    if str(chat_id) in white_list:
        dir = f"logs/groups/{msg.chat.username} ({chat_id}) [{title}]/"
        if not os.path.exists(dir):
            os.makedirs(dir)  
        if msg.media:
            tg.write(msg, dir, tg.load(msg, dir), [title, msg.chat.username])
        elif msg.text:
            tg.write(msg, dir, msg.text, [title, msg.chat.username])            
    else:
        dir = f"logs/NOT LOGGING/{msg.chat.username} ({chat_id}) [{title}]/"
        if not os.path.exists(dir):
            os.makedirs(dir)

app.run()
