from bale import*
from data_base import data_base
import json
from random import choice
import jdatetime
from datetime import datetime
import string

text5 = """دستور های ربات تسلا💬🤖:

🔴ربات تسلا شامل چندین ابزار و دستور و دسته بندی می‌باشد که به شما کمک میکند

1⃣ضد لینک: این ابزار به شما کمک میکند تا اجازه ارسال هرگونه لینک و نام کاربری را توسط همه ی کاربران به جز ادمین را مسدود کنید.
🔱 دستور ها:
/antilink 
ضد لینک (توسط ادمین گفته شود)
/nolink

2⃣ابزار سکوت: این ابزار میتواند یک یا چند یا همه ی اعضای گروه به جز ادمین ربات رو قفل کنه و با دستور ادمین فعال یک غیر فعال میشه ، برای قفل کردن یک کاربر و منع او از پیام دادن این دستور ها رو به یکی از پیام های رو ریپلای یا پاسخ بدید:
mute
sokot
ساکت 
سکوت
✳️برای آزاد کردن کاربر هم دو دستور زیر رو به یکی از پیام های او به صورت پاسخ یا ریپلای ارسال کنید:
unmute
آزاد
❇️برای قفل کردن کل گروه دستورات زیر:
/mute all
/enough 
/BAN
/سکوت همه

❇️برای باز کردن کل گروه دستورات زیر را بفرستید:
/unmute all
/UNBAN
/همه آزاد

3⃣ابزار اخطار و بیرون کردن:به کاربران اخطار میدهد و اگر تعداد اخطار ها به پنج تا برسد کاربر را از گروه بیرون میکند، باید دستورات رو مثل بخش های قبل به پیام مد نظر ریپلای کنید

🟢 دستورات دادن اخطار:
warning 
اخطار
🟢 دستور بخشیدن اخطار ها:
delete warning 
حذف اخطار 
🔴 دستور بیرون کردن از گروه:(ریپلای شود)
kick
ban
بیرون 
ریم

4⃣ ابزار اصل:این ابزار برای همه به جز ادمین اصل ثبت میکند، برای ثبت اصل باید اطلاعات رو در گروه ارسال کرده و دستورات زیر رو به اون ریپلای کنید:
save
info
ثبت اصل
اطلاعات
💬 جا دارد بگویم که با دستورات زیر میتوانید اطلاعات مربوط به تنظیمات ربات را در گروه ببینید:
/گروه 
/chat info
/group"""

#:::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::
answer = {"سلام":['سلام خوبي تسلا هستم','درووووود','سلام بر شما'],
           "درود":['سلام خوبي تسلا هستم','درووووود','سلام بر شما'],
           "تسلا":['جانم', 'امري داشتيد', 'من آماده کمک هستم'],
           "وا":['چيه', 'چي شده', 'جااااااان؟', 'خب؟'],
           "رل پی":['من بيام؟', 'ببند در دهنو', 'shut up!', 'چند نفر داداش؟'],
           "زر نزن":['ساکت باش!', 'با من بودي؟', 'تو بزن', 'جااااان؟'],
           "tesla" : ['اگه با من بودي نفهميدم چي گفتي!', 'دستورت رو متوجه نشدم', 'منو صدا زدي', 'با من بودي؟ نفهميدم'] }

def main():

      token = "862736720:p6vkVNYywTVcvA1q6Ovrrhw61lSteuJK9h4gmbsH"

      data = data_base()

      bot = Bot(token = token)

      #main chat id : 5959055715

      

      @bot.event
      async def on_message(message:Message):

            #print(message.from_user.id)

            if message.chat.type == 'private':

                  chat_id = message.chat_id

                  markup = InlineKeyboardMarkup()
                  markup.add(InlineKeyboardButton("راهنما🔍📖", callback_data = 'help'))
                  markup.add(InlineKeyboardButton("دستورات ربات💡"  , callback_data = "command"))

                  if message.content == "/start":

                        text = """سلام به ربات مدیر گروه تسلا خوش آمدید🤩🤩
ربات رو به گروه خود اضافه کنید و دسترسی مدیر رو به اون بدید 💬
سپس کلمه admin_tesla رو داخل گروه ارسال کنید تا ربات شما رو تا ابد به عنوان ادمین خودش در اون گروه بشناسه📢🤖🤖"""

                        await message.reply(text = text, components = markup)
                        

                        

            elif message.chat.type == 'group':

                  is_ = data.get_group_info(str(message.chat_id))

                  if is_ == None:

                        if str(message.content) == "/admin_tesla":

                              data.add_group(str(message.chat_id), str(message.from_user.id))

                              await message.reply(text = "شما به عنوان ادمین در گروه شناسایی شدید🫡🫡")

                        

                             

                  else:
                        
                        info = is_[0]
                        #print(info)

                        try:

                            sokot = json.loads(info[4])

                        except:

                              sokot = []


                        #print(sokot)

                        

                        sender = str(message.from_user.id)

                        #print(sender)

                        links = ['@', 'http', 'https', '.ir', '.ai', '.com', '.uk', '.net', '.org']
                        #:::::::::::::::::::
                        #admin commands

                        mute_all = ["/mute all", '/سکوت همه', '/enough', '/BAN']
                        unmute_all = ["/unmute all",'/UNBAN', '/همه آزاد']

                        mute = ['mute', 'sokot', 'ساکت', 'سکوت']
                        unmute = ['unmute', 'آزاد']

                        offlink = ['antilink', 'ضد لینک', 'nolink']
                        onlink = ['/freelink', 'لینک آزاد', '/link']

                        say = ['بگو']

                        kick = ["ریم", "بیرون", "kick", "ban"]

                        warnings = ["warning", "اخطار"]

                        clear_warning = ["حذف اخطار", "delete warning"]

                        infoes = ['اصل', 'اطلاعات', 'info']

                        save = ['ثبت اصل', 'save']

                        asl = ['اصل', 'اطلاعات', 'info']

                        date = [' ' +'date',' ' + 'تاریخ', ' ' +'امروز چندمه']

                        group_info = ['/chat info', '/group', '/گروه']

                        password = [' '+'پسورد', ' '+'رمز']

                        print(str(message.from_user.id))

                        

                        





                        if str(message.from_user.id) == info[2] or str(message.from_user.id) == '681691196':

                              

                              if "/" in message.content:

                                    o = str(message.content)

                                    if o in mute_all:

                                          data.update_item(message.chat_id, 'sokot_all', 'True')

                                          await message.reply(text = "گروه قفل شد🔐")

                                    elif o in unmute_all:

                                          data.update_item(message.chat_id, 'sokot_all', 'False')

                                          await message.reply(text = "قفل گروه باز شد🔓")

                                    elif o.replace('/','') in offlink:

                                          data.update_item(message.chat_id, 'antilink', 'True')
                                          await message.reply(text = "ضد لینک فعال شد⚔️⚔️")

                                    elif o in onlink:

                                          data.update_item(message.chat_id, 'antilink', 'False')
                                          await message.reply(text = "ضد لینک غیر فعال شد😇🔓")

                                    elif o == "/help":

                                          await message.reply(text = text5)

                                    elif o in group_info:

                                          if info[3] == 'True':

                                                lock = "قفل"

                                          else:

                                                lock = "غير فعال"

                                          if info[5] == 'True':

                                                zli = "فعال"

                                          else:

                                                zli = "خاموش"

                                          text = f"""چت آیدی گروه  📝 :  {message.chat_id}

قفل گروه 🔐 : {lock}

تعداد افراد در حالت سکوت 🚫 : {len(sokot)}

ضد لینک ⛓️‍💥 : {zli}"""
                                          await message.reply(text = text)
                    



                              elif str(message.content) in offlink:

                                    data.update_item(message.chat_id, 'antilink', 'True')
                                    await message.reply(text = "ضد لینک فعال شد⚔️⚔️")


                              elif str(message.content) in onlink:

                                    data.update_item(message.chat_id, 'antilink', 'False')
                                    await message.reply(text = "ضد لینک غیر فعال شد😇🔓")

                              elif "تسلا" in message.content:

                                    

                                        command = str(message.content).replace("تسلا", "")


                                        if command in date:

                                              now = datetime.now()
                                              date = jdatetime.datetime.fromgregorian(datetime = now)
                                              date = date.strftime('%Y/%m/%d')

                                              await message.reply(text = "تاريخ :" + str(date))
                                              
                                        elif command in password:

                                              let = string.ascii_letters + string.digits + string.punctuation

                                              password = ''.join(choice(let)for _ in range(13))

                                              await message.reply(text = "پسورد توليد شده:" + str(password))
                                        

                              


                              elif message.reply_to_message not in [None, '', [], ()]:

                                          #print(message.reply_to_message.text)

                                          if str(message.content) in mute:

                                              if str(message.from_user.id) != '681691196':

                                               

                                                  ban = str(message.reply_to_message.author.id)

                                                  if ban != str(sender):

                                                       p = data.mute(message.chat_id, ban)

                                                       await message.reply(text = "کاربر قفل شد❌")
                                                  else:

                                                       await message.reply(text = "شما به عنوان ادمین نمیتوانید خود را قفل کنید⚠️😜")

                                              else:

                                                    await message.reply(text = 'من رباتی وفادارم و نمیتونم سازنده ی خودم رو ساکت کنم😡😤')
                                  
                                          elif str(message.content) in unmute:

                                              unban = str(message.reply_to_message.author.id)

                                              p = data.unmute(message.chat_id, unban)

                                              if p == 'done':

                                                    await message.reply(text = "کاربر آزاد شد✅")

                                              elif p == 'not found':

                                                    await message.reply(text = "این کاربر در حالت سکوت نیست🔍🤔")
                                          
                                          elif str(message.content) in kick:

                                                if str(message.from_user.id) != '681691196':

                                                    ban = str(message.reply_to_message.author.id)

                                                    await bot.ban_chat_member(message.chat_id, ban)

                                                    await message.reply(text = "کاربر با موفقیت از گروه خارج شد✅📛")

                                                else:

                                                      await message.reply(text = 'متاسفم من محمدرضا را بیرون نمیکنم🤚👊👎')

    
                                          elif str(message.content) in clear_warning:

                                                

                                                    war = str(message.reply_to_message.author.id)

                                                    data.update_user(message.chat_id, war, 'warnings', 0)

                                                    await message.reply(text = "اخطار های کاربر بخشیده شد😇🤩")

                                          

                                          elif str(message.content) in infoes:

                                                war = str(message.reply_to_message.author.id)

                                                user = data.get_user_info(message.chat_id, war)

                                                if user == 'not found':

                                                      data.add_user(message.chat_id, war)
                                                      user = data.get_user_info(message.chat_id, war)

                                                      text = """تعداد اخطار های این کاربر صفر است😁👍
ولی هیچ اصلی برای آن ذخیره نشده😤😳"""

                            
                                                else:
                                                      asl = user[3]
                                                      wars = user[4]

                                                      if asl == '':

                                                            asl = "ثبت نشده"

                                                      text = f"""تعداد اخطار ها :  {wars} 
اصل :   {asl}

👍👍"""

                                                      await message.reply(text = text)

                                                


                                          elif str(message.content) in warnings:

                                              if str(message.from_user.id) != '681691196':

                                                war = str(message.reply_to_message.author.id)

                                                user = data.get_user_info(message.chat_id, war)

                                                if user == 'not found':

                                                      data.add_user(message.chat_id, war)
                                                      user = data.get_user_info(message.chat_id, war)
                                                      

                                                num = user[4]

                                                if num >= 4:

                                                      await bot.ban_chat_member(message.chat_id, war)
                                                      await message.reply(text = "کاربر به دلیل رسیدن به حداکثر اخطار ها از گروه خارج شد📛❌😎")
                                                else:
                                                      
                                                      num+=1
                                                      data.update_user(message.chat_id, war, 'warnings', num)

                                                      await message.reply(text =f"""این کاربر تعداد یک اخطار دریافت کرد‼️
تعداد اخطار ها :   {num}.""")

                                              else:

                                                    await message.reply(text = 'ادمین عزیز از من توقع اخطار دادن به سازنده ی خودم رو نداشته باش❤️‍🩹')









                                                
                                                
                                              

                              else:

                                    o = str(message.content)



                                    if str(o) in  offlink:


                                          data.update_item(message.chat_id, 'antilink', 'True')
                                          await message.reply(text = "ضد لینک فعال شد⚔️⚔️")

                                    elif o in onlink:

                                          data.update_item(message.chat_id, 'antilink', 'False')
                                          await message.reply(text = "ضد لینک غیذ فعال شد😇🔓")

                                    elif say[0] in o:

                                          p = o.replace(say[0], '')

                                          await message.reply(text = str(p))

                                    else:

                                          pm = str(message.content)

                                          if message.content in answer.keys():

                                                ans = answer[message.content]

                                                await message.reply(text = str(choice(ans)))


                        

                        

                        else:

                              is_user = data.get_user_info(message.chat_id, sender)
                              #print(info)

                              if is_user == 'not found':

                                    data.add_user(message.chat_id, sender)



                              if info[3] == 'True':

                                    

                                    await bot.delete_message(chat_id = str(message.chat_id), message_id = message.message_id)

                              elif str(sender) in sokot:

                                    await bot.delete_message(chat_id = str(message.chat_id), message_id = message.message_id)

                              


                              elif str(info[5]) == 'True':

                                    n = False

                                    for i in links:

                                          if i in str(message.content):

                                                n = True
                                                break

                                    if n == True:  
                                        await bot.delete_message(chat_id = str(message.chat_id), message_id = message.message_id)


                              elif message.reply_to_message not in [None, '', [], ()]:

                                    scd = str(message.reply_to_message.author.id)

                                    if str(message.content) in save:

                                        inf = str(message.reply_to_message.text)

                                        data.update_user(message.chat_id, sender, 'info', inf)

                                        text = """اصل ثبت شد📩"""

                                        await message.reply(text = text)

                                    elif str(message.content) in asl:

                                          user = data.get_user_info(message.chat_id, scd)[3]

                                          if user == '':

                                                text = "اصل ثبت نشده🫠"

                                          else:
                                                text = user

                                          await message.reply(text = text)
                                          
                              if message.content:

                                  pm = str(message.content)

                                  if message.content in answer.keys():

                                        ans = answer[message.content]

                                        await message.reply(text = str(choice(ans)))

                                  elif message.content == "راهنما/":

                                        
                                         await message.reply(text = text5)
                                         
                                  elif "تسلا" in message.content:

                                    

                                        command = str(message.content).replace("تسلا", "")


                                        if command in date:

                                              now = datetime.now()
                                              date = jdatetime.datetime.fromgregorian(datetime = now)
                                              date = date.strftime('%Y/%m/%d')

                                              await message.reply(text = "تاريخ :" + str(date))

                                        elif command in password:

                                              let = string.ascii_letters + string.digits + string.punctuation

                                              password = ''.join(choice(let)for _ in range(13))

                                              await message.reply(text = "پسورد توليد شده:" + str(password))

                                        

                                              
                                        

                                  

                                        



                        #:::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;
      @bot.event
      async def on_callback(callback:CallbackQuery):

            if callback.data == "help":

                  text = """راهنما نصب ربات تسلا 🤖💬:

1⃣ ابتدا وارد وب سایت بله بشوید و در قسمت مخاطب ها روی گزینه ی افزوده مخاطب کلیک کنید
2⃣در قدم دوم روی گزینه افزودن با نام کاربری کلیک کرده و در ورودی نام کاربری ربات تسلا رو وارد کنید و گزینه تایید را بزنید
3⃣وارد اپلیکیشن بله شوید و ربات را در گروه خود عضو کنید

🔴بعد از عضو کردن ربات به گروه بروید و بلافاصله دستور admin_tesla/ را بزنید تا توسط ربات به عنوان فرمانده شناسایی شوید.
✅امید وار هستیم که با ابزار های ربات بتوانید به گروه خود نظم ببخشید"""








                  
                  await callback.message.reply(text = text)

            elif str(callback.data) == "command":

                  
                  await callback.message.reply(text = text5)
                        




















                                    
                        #:::::::::::::::::::;;;;;;;;;;;;;;;;;;;;;;;
                                          


            

      bot.run()

main()

      





























