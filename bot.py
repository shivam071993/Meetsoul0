import requests
import telebot,time
import time
from telebot import types
from gatet import Tele
import os
token = '7740049047:AAGPVttQ1hLSmhU62QKJ2QicdOPPnXFxgJ8:' #bottoken
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber = '6507575922'
allowed_users = ['6507575922']  #Your ID
@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "🚫 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 @")
        return
    bot.reply_to(message, "𝐒𝐞𝐧𝐝 𝐭𝐡𝐞 𝐭𝐱𝐭 𝐟𝐢𝐥𝐞 𝐧𝐨𝐰")
@bot.message_handler(commands=["add_user"])
def add_user(message):
    if str(message.chat.id) == '6507575922':  # Only bot owner can add new users
        try:
            new_user_id = message.text.split()[1]  # Extract new user ID from the command
            allowed_users.append(new_user_id)
            bot.reply_to(message, f"User {new_user_id} Has Been Added Successfully.✅")
        except IndexError:
            bot.reply_to(message, "Please provide a valid user ID. Example: /add_user 123456789")
    else:
        bot.reply_to(message, "You do not have permission to add users.🚫")
@bot.message_handler(content_types=["document"])
def main(message):
	if str(message.chat.id) not in allowed_users:
		bot.reply_to(message, "🚫 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 @")
		return
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @')
						os.remove('stop.stop')
						return
				try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
				except: pass
				try:
					brand = data['brand']
				except:
					brand = 'Unknown'
				try:
					card_type = data['type']
				except:
					card_type = 'Unknown'
				try:
					country = data['country_name']
					country_flag = data['country_flag']
				except:
					country = 'Unknown'
					country_flag = 'Unknown'
				try:
					bank = data['bank']
				except:
					bank = 'Unknown'
				
				start_time = time.time()
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "Gateway Error"
				if 'risk' in last:
					last='declined'
				elif 'Duplicate' in last:
					last='Approved'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				status = types.InlineKeyboardButton(f"• 𝐒𝐓𝐀𝐓𝐔𝐒  : {last} ", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝐀𝐏𝐏𝐑𝐎𝐕𝐄𝐃 ✅ : [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝐃 ❌ : [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝐓𝐎𝐓𝐀𝐋 🎉       :  [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 🚫 ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, stop)
				end_time = time.time()
				execution_time = end_time - start_time
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝐖𝐚𝐢𝐭 𝐟𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 
𝐁𝐲 ➜ <a href='t.me/Approved_Raven'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a> ''', reply_markup=mes)
				msg = f'''
<a href='t.me/Approved_Raven'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/Approved_Raven'>┏━━━━━━━⍟</a>			
<a href='t.me/Approved_Raven'>┃</a>𝐂𝐂: <code>{cc}</code>
<a href='t.me/Approved_Raven'>┗━━━━━━━━━━━⊛</a>
<a href='t.me/Approved_Raven'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Braintree Charge</code>		
<a href='t.me/Approved_Raven'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/Approved_Raven'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐲: <a href='t.me/Approved_Raven'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a> '''
				print(last)
				if 'success' in last or 'Payment method successfully added.' in last:
					live += 1
					bot.reply_to(message, msg)
				elif 'Nice! New payment method added' in last or 'Insufficient Funds' in last:
					msg = f'''
<a href='t.me/Approved_Raven'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/Approved_Raven'>┏━━━━━━━⍟</a>			
<a href='t.me/Approved_Raven'>┃</a>𝐂𝐂: <code>{cc}</code>
<a href='t.me/Approved_Raven'>┗━━━━━━━━━━━⊛</a>
<a href='t.me/Approved_Raven'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Braintree Charge</code>		
<a href='t.me/Approved_Raven'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/Approved_Raven'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝 </code>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/Approved_Raven'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>
<a href='t.me/Approved_Raven'>-</a> 𝐁𝐲: <a href='t.me/Approved_Raven'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a> '''
					live += 1
					bot.reply_to(message, msg)
				elif 'Approved ✅! Live' in last or 'Approved ✅! CVV' in last:
					msg = f'''𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
					
𝐂𝐂: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: <code>Braintree Charge</code>
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{last}</code>

𝐈𝐧𝐟𝐨 <code>{cc[:6]} - {dicr} - {typ}  </code>
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{cn} - {emj} </code>
𝐁𝐚𝐧𝐤: <code>{bank} </code>

𝐓𝐢𝐦𝐞: {"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝 
𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: @ 
𝐁𝐲: @ ''' #Declined
					live += 1
					bot.reply_to(message, msg)
				else:
					dd += 1
					time.sleep(1)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @ITS_BFC')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
logop = f'''━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⢖⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⠎⠀⠀⠹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⢿⣤⠴⠒⢦⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⠿⠛⠁⠸⡇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⣧⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⠂⠾⠿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣷⣤⡀⠈⠉⠑⠒⠤⢀⡀⠀⠀⠀⠀⣿⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠟⠿⠿⢿⣿⣿⣆⠀⠀⠀⠀⠀⠈⠑⢄⠀⠀⣿⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡏⡄⠀⠀⠀⠈⠻⣿⣧⠀⠀⠀⠀⠀⠀⠀⢳⠀⣿⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡀⣷⠄⠀⠀⠀⠀⠙⢿⣇⡀⠀⠀⠀⠀⠀⠀⣷⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⡿⠐⣁⣀⣀⢀⣾⣤⢤⣶⣿⣿⣦⡀⠀⠀⠀⠀⢸⠇⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣇⣾⣿⣿⣿⡇⠀⠻⣽⣿⣿⣿⡿⠿⣦⠀⠀⠀⡟⠀⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡟⣌⡻⠛⠁⢰⠸⡔⣤⣉⡩⠐⠁⠀⢸⡇⠀⢰⠃⠀⠀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣇⠀⠉⠀⠀⠀⠀⠀⠈⠙⠻⣶⢶⣶⣾⠇⢀⡏⠀⠀⠰⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⢋⣿⣿⣿⣿⣿⣿⣿⣷⠀⠤⠒⠒⠓⠘⠀⢴⢏⡟⠈⣿⠀⡞⠀⠀⢀⡇⠀⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⡿⠁⣸⣿⣿⣿⣿⣿⣿⣿⣿⠀⡰⠞⠛⠛⠛⠳⠶⠿⠁⣰⣿⣼⠃⠀⠀⡼⢿⣶⡀⡇⠀⢀⠔⠚⠛⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⣿⠟⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣿⠟⠋⠉⠉⠁⠀⠀⢠⣿⣿⠃⠀⠀⠰⠁⠘⢿⠔⢀⣠⠇⣶⣶⣶⢠⣆⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⣿⡟⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣏⠻⠖⠂⠈⠒⠂⢀⣠⣿⣿⠏⠀⠀⢀⣧⣶⡶⢖⣿⠇⡿⠀⣿⣿⠏⣸⣿⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⡟⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣏⠩⠭⣼⣿⣿⠏⠀⠀⠀⡼⠛⢉⣴⣿⠏⣸⡇⢀⣿⡏⠀⣿⣿⠇⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⠏⠀⠀⠀⡼⢁⣴⣿⡿⠁⣰⣿⠁⣸⣿⠀⢀⣿⡿⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠿⠛⢛⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⣰⣿⣿⡿⠋⠀⣰⣿⡟⢠⣿⡇⠀⣸⣿⠃⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⢠⣿⡿⠛⠁⠀⣼⣿⣿⣧⣿⣿⠁⢀⣿⡏⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠟⢻⠐⠉⠑⠤⣀⢠⣿⣿⠀⠀⢀⣾⣿⣿⣿⣿⣿⡟⠀⣼⣿⠁⠀⠀⣿⠀⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⢱⠹⠉⢉⠉⠓⠶⠤⠍⠛⢻⡄⣠⣿⣿⣿⣿⣿⣿⣿⣇⣼⣿⠃⠀⠀⢠⣿⡀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀
⢸⠀⠀⠀⠀⠀⠀⢀⣤⣴⡖⠤⣀⠀⠀⠀⣼⣿⣿⣿⠉⠉⠑⠛⠛⠛⠳⢄⣀⠈⢹⠤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣸⣿⣇⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠸⠋⠀⠀⠈⠢⣀⣼⣿⣿⡿⠉⡗⠒⠒⠶⠶⢤⣀⠃⠀⣰⢺⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢟⣷⣆⡀⠀⠘⢿⣿⣿⡣⠀⣓⣤⠤⣤⠀⡸⠓⢲⠞⠸⡀⢣⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⣸⣿⣿⣿⡇⠀⠀⢱⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢟⢿⣤⡀⠀⠹⣿⣧⣼⣿⠃⠀⠀⠻⣄⠀⠈⡆⠀⢇⠈⣼⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣰⣿⣿⣿⣿⣷⠀⠀⠈⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢽⢷⣄⠀⠀⠉⠛⡏⠀⠀⠀⠀⣽⣧⠀⢿⡄⢸⡀⡇⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⠀⠀⠀⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣷⣟⣷⡀⠀⠀⡟⠀⠀⠀⠀⣿⣿⣇⠘⣷⠈⠃⢈⠜⢿⣿⣿⣿⣿⣿⡇⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠸⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣷⣽⣷⡞⠀⠀⠀⠀⢠⣿⣿⣿⠀⠘⡀⡘⠙⢢⣈⠛⠋⢻⣿⣿⡇⠀⢰⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⢇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣦⣶⡗⢁⠤⠚⡡⠒⠒⡄⠙⢿⣧⣀⣼⣿⣿⣿⣿⣿⣿⠋⠀⠀⣀⡀⠀⠸⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣷⣤⣰⣏⠀⠑⠈⠂⠄⡉⠻⠿⣿⠻⠿⣿⡿⢃⣠⣶⣿⣿⣿⣦⠀⢇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡄⠀⠁⠢⣈⢣⠀⠀⠈⠙⠉⠉⢛⣛⠿⣿⠇⠘⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠙⡇⠀⠀⠀⠀⠀⠀⢻⣧⡰⣦⣤⡐⠄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⡀⢂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⡀⠀⣸⣿⣿⣿⣿⣿⣿⠀⡜
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⣼⠁⢰⣿⣿⣿⣿⣿⣿⡟⢠⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⢠⣾⠇⢠⣿⣿⣿⣿⣿⣿⣿⠇⡜⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⢀⣰⣿⡟⢀⣿⣿⣿⣿⣿⣿⣿⡟⢠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢀⣤⣾⣿⣿⢁⣾⣿⣿⣿⣿⣿⣿⣿⠁⣼⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⡏⢠⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⣾⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣸⣿⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣿⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣾⣿⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠟⠉⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⡟⠁⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿⠋⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠿⠶⠶⠤⠤⠶⠶⠒⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
print(logop)
bot.polling()
