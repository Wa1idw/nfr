#__________________________

link = "http://aminoapps.com/p/liwx72"


sid = "AnsiMSI6IG51bGwsICIwIjogMiwgIjMiOiAwLCAiMiI6ICI4MDQxNmViNy1kZTViLTQ4MmUtYTc3Ni0zNmFkYTRjYjcwOGIiLCAiNSI6IDE2NjY5NTMwMjgsICI0IjogIjgwLjgzLjMwLjE2NiIsICI2IjogMTAwfcXoSPsTDBt5wSp6jETJer5DQ5uX"

e = "wallid11@mentonit.net"
p = "wallid23"

#__________________________

 

import os
import time
import aminofix
import urllib.request
from random import choice
from gtts import gTTS
from threading import Thread as T
clint=aminofix.Client()
x=open("sp.txt").read()
p = x.split(  '\n'  )
clint.login(email="wallid11@mentonit.net",password="wallid23")
print("login")
o=clint.get_from_code(link)
j=o.objectId
com=o.path[1:o.path.index(  '/' )]



def Countdown(s,user,dictList):
 while s:
  mins, secs = divmod(s, 60)
  hour, mins = divmod(mins, 60)
  timer = '{}:{}:{}'.format(hour, mins, secs)
  dictList[user]=timer
  time.sleep(1)
  s -= 1
 del dictList[user]

Dict = {}




clint.join_community(com)
subclint=aminofix.SubClient(comId=com,profile=clint.profile)
point = []
subclint.join_chat(j)
@clint.event('on_group_member_join')
def on_group_member_join(data: aminofix.objects.Event):
	userId = data.message.author.userId
	chatId = data.message.chatId
	nm = data.message.author.nickname
	ttf = data.message.createdTime
	subclint.send_message(chatId=data.message.chatId  ,message=f"""
[C]
[bC]منور/ة〈 <${data.message.author.nickname}$>  〉
[C]

[C]
""",embedId=data.message.author.userId  ,embedTitle= f"{nm}",embedLink="ndc://g/user-profile/"+userId,embedImage=urllib.request.urlopen(data.message.author.icon),mentionUserIds=[data.message.author.userId])

m = 0
@clint.event('on_group_member_leave')
def on_group_member_leave(data: aminofix.objects.Event):
 chatId = data.message.chatId
 msgG = """[BC]  خسرنا عضو متفاعل 
[BC]الله يكثر الراحلين """
 
 subclint.send_message(chatId=chatId, message=msgG)
@clint.event('on_text_message')
def on_text_message(data: aminofix.objects.Event):
    mention = data.message.mentionUserIds
    content = data.message.content
    msgId = data.message.messageId
    chatId = data.message.chatId
    userId = data.message.author.userId
    author = data.message.author
    tui = data.message.author.level
    icon = data.message.author.icon
    y = data.message.createdTime
    ci = data.message.author.content
    nm = data.message.author.nickname
    print(content)
       
    if content=="ايدي":
    	subclint.send_message(chatId=chatId, message=userId, replyTo=msgId)
    
    
    if content.startswith("هههه") or content.startswith("😂"):
    	from random import choice
    	d7ka=["دُوم الضحكة عيوني","متضحكيش يا سافلة"]
    	g=choice(d7ka)
    	subclint.send_message(chatId=chatId, message=g, replyTo=msgId)
    if content.startswith("تتزوجني"):
    	from random import choice
    	io = ["مهري مليونين","كلٰخرا محد معبرك","هههههههههههههههه","موافق","ها اخوي؟","اها بفكر"]
    	g=choice(io)
    	subclint.send_message(chatId=chatId, message=g, replyTo=msgId)
	       	    	
    if content.startswith("مين انت"):
    	subclint.send_message(chatId=chatId, message="أأنت مين ؟", replyTo=msgId)
    if content.startswith("شلونك") or content.startswith("كيفك"):
    	subclint.send_message(chatId=data.message.chatId,message=f"بخير الحمد لله أحسن منك كمان ")
   
    	
    if content.startswith("قروش"):
    	subclint.send_message(chatId=chatId, message="مليونير ها  😂", replyTo=msgId)
    if content.startswith("اكرهك"):
    	subclint.send_message(chatId=chatId, message="و انا بعد  🌚", replyTo=msgId)
    
    
    
    if content.startswith("http") or content.startswith(".com") or content.startswith("t.me"):	   	
    	if content[0] == "رابط":
    		pass   		
    	subclint.delete_message(chatId=chatId,messageId=msgId)
    	subclint.send_message(chatId=chatId, message="لا ترسل روابط", replyTo=msgId)	       	    	
	       	    	
    
    if content.startswith("رابط"):
    	oo=content.replace('رابط','')
    	
    	id=clint.get_from_code(oo)
    	od = id.objectId
    	oo=clint.get_from_id(od,0).shortUrl
    	try:
    		link=clint.get_from_id(od,0,comId="118096603").shortUrl
    	except:
    		link = "-{ مو موجود داخل المنتدى}-"
    		pass
    	try:
    		lin=clint.get_from_id(od,0,comId="3434136").shortUrl
    	except:
    		lin = "-{ مو موجود داخل المنتدى}-"
    		pass
    	try:
    		li=clint.get_from_id(od,0,comId="215067101").shortUrl
    	except:
    		li = "-{ مو موجود داخل المنتدى}-"
    		pass
    	try:    		l=clint.get_from_id(od,0,comId="214924547").shortUrl
    	except:
    		l = "-{ مو موجود داخل المنتدى}-"
    		pass
    	tuio = f"""[BC]روابط بروفايله في المنتديات الثانيه
[C]_______________________
[C] بروفايل الرئيسي
[C]{oo}

[C] امبراطوريه
[C]{lin}

[C] محششين
[C]{li}

[C]حيدر و مريم
[C]{link}

[C] كيبوب
[C]{l}"""
    	subclint.send_message(chatId=chatId, message=tuio)
    	
    
    
    if content.startswith("join"):
    	tx=content.replace('join','')
    	gf=clint.get_from_code(tx)
    	yu=gf.objectId
    	comi= gf.comIdPost
    	try:
    		clint.join_community(comi)
    		time.sleep(0.5)
    		subclint.join_chat(yu)
    	except:
    		subclint.send_message(chatId=chatId, message="حدث خطاء", replyTo=msgId)
    		
    		
    if content.startswith("leave"):
    	tx=content.replace('leave','')
    	gf=clint.get_from_code(tx)
    	yu=gf.objectId
    	comi= gf.comIdPost
    	try:
    		clint.join_community(comi)
    		time.sleep(0.5)
    		subclint.leave_chat(yu)
    	except:
    		subclint.send_message(chatId=chatId, message="حدث خطاء", replyTo=msgId)
    		
    	
    	

    
    if content.startswith("انشر"):
    	xx=content.replace('انشر','')
    	subclint.post_blog(title=nm,content=xx)
    	time.sleep(1)
    	
    	subclint.send_message(chatId=chatId, message="نشرت منشور", replyTo=msgId)
    	
    	
    if content.startswith("ارسلي"):
    	xx=content.replace('ارسلي','')
    	subclint.start_chat(userId=userId, message=xx)
    	subclint.send_message(chatId=chatId, message="رسلت لك في الخاص", replyTo=msgId)
    	
    


    if content=="تاريخ":
    	subclint.send_message(chatId=chatId, message=y, replyTo=msgId)
    if content=="منشن":
    	chat_users=subclint.get_chat_users(chatId=chatId, start=0, size=100).userId
    	time.sleep(1)
    	subclint.send_message(chatId=chatId,message="<$@all$>", mentionUserIds=chat_users)
    	
    	
    if  content == "اونلاين":
        o=""
        q=subclint.get_online_users(start=0,size=1000)
        for uid in q.profile.nickname:
        	o=o+uid+"\n"
        subclint.send_message(chatId=data.message.chatId,message=f"""[BC]  الاعضاء الاونلاين
[C] ____________________
[C] {o}
[C] ____________________""")
        	

    
    if  content == "وليد":
    	    	 subclint.send_message(chatId=chatId, message="""[BC] وليد عمكم يا نوبات""")
	
    
    if  content == "مكالمة":
    	subclint.send_message(chatId=chatId, message='سيتم تشغيل المكالمة بعد 5 ثواني', replyTo=msgId)
    	time.sleep(5)
    	clint.start_vc(comId=com,chatId=data.message.chatId,joinType=1)
    	
    if  content == "اغلاق المكالمة":
    	subclint.send_message(chatId=chatId, message='سيتم اغلاق المكالمة بعد 5 ثواني', replyTo=msgId)
    	time.sleep(5)
    	clint.end_vc(comId=com,chatId=data.message.chatId,joinType=2)
    	
    if  content == "تحدي":
    	gt = """سوف ارسل ارقام
    	اول واحد يكتبه بسرعه هو الفائز  
    	سوف ارسل بعد خمس ثواني"""
    	subclint.send_message(chatId=chatId, message=gt)
    	time.sleep(5)
    	subclint.send_message(chatId=chatId, message="1")
    	time.sleep(1)
    	subclint.send_message(chatId=chatId, message="2")
    	time.sleep(1)
    	subclint.send_message(chatId=chatId, message="3")
    	from random import sample
    	you = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    	gx = sample(you,6)
    	Finish = "".join(gx)
    	time.sleep(1)
    	subclint.send_message(chatId=chatId, message=f"[CB] [[ {Finish} ]]")
      	
    if content.startswith("بصمة"):
    	xo=content.replace('بصمة','')
    	subclint.comment(message=xo,userId=data.message.author.userId)
    	subclint.send_message(chatId=chatId, message='اعطيتك بصمه في الحائط', replyTo=msgId)
    if content=="تحدي مميز":
    	from random import sample
    	you = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    	gx = sample(you,4)
    	Finish = "".join(gx)
    	subclint.send_message(chatId=chatId, message="سوف ارسل تسجيل  صوت  و رح اقول فيه ارقام اول واحد يكتبها هو الفائز")
    	time.sleep(4)
    	lan="ar"
    	name="ss.mp3"
    	gTTS(text=Finish,lang=lan,slow=False).save(name)
    	with open(name,"rb") as fff:
    		subclint.send_message(chatId=chatId,file=fff,fileType="audio")
    		os.remove(name)
    		
    	
    	
    	
		
		
   
    if content.startswith("قول"):
    	texxxt=content.replace('قول','')
    	lan="ar"
    	name="sssss.mp3"
    	gTTS(text=texxxt,lang=lan,slow=False).save(name)
    	with open(name,"rb") as fff:
    		subclint.send_message(chatId=chatId,file=fff,fileType="audio")
    		os.remove(name)
    if content.startswith("السلام عليكم") or content.startswith("هاي") or content.startswith("هلاو") :
    	subclint.send_message(chatId=chatId, message="منور", replyTo=msgId)
    
    
    if content.startswith('مشاهد'):
                for c in range(2):
                	try:
                		clint.join_video_chat_as_viewer(comId=com, chatId=chatId)
                	except:
                		subclint.send_message(chatId=chatId, message='حدث خطاء', replyTo=msgId)   
                subclint.send_message(chatId=chatId, message='[C] تم الدخول كمشاهد!', replyTo=msgId)
    
   
    
    if content=="روليت":
    	yi = """كل واحد يختار رقم من 1 الى20 
    	و عند ارسال كلمه[ ابدأ]سوف اختار الرقم عشوائي"""
    	subclint.send_message(chatId=chatId, message=yi)
    	
    if content=="ابدأ":
    	from random import choice
    	g=choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
    	
    	uiu = f"""تم اختيار عضو رقم : {g}"""
    	subclint.send_message(chatId=chatId,message=uiu)
    if content=="العاب":
    	fio = """[BC] الالعاب الحالية 

[C]____________________
[C]اكتب [ تحدي مميز ] لكي ابدا لعبة كتابه السريع بالصوت
[C]____________________
[C] اكتب [ تحدي ] لكي تبدا لعبة الكتابه السريعه
[C]____________________
[C] اكتب [ حظ ] لي تعرف كم انت محظوظ
[C]____________________
[C]اكتب [ روليت ] روليت لكي تبدأ لعبة الروليت"""
    	subclint.send_message(chatId=chatId,message=fio)
    	
    	
    
    if content=="بوت":
    	hh = """[BC]انا ليو بوت مساعد في كروب 
[BC]𝙞𝙣𝙛𝙞𝙣𝙞𝙩𝙮 𝙬𝙤𝙧𝙡𝙙 ∞

[C] _ _ _ _ _ _ _

[BCU] اكتب [ العاب ] لفتح قسم الالعاب

[C]اكتب [ انشر ]"مع الوصف" لكي انشر منشور باسمك
[C]__________________
[C]اكتب [ انضم ]"مع رابط القروب" لكي انضم للقروب
[C]__________________
[C]اكتب [ ارسل ]"مع الكلام" لكي ارسل لك في الخاص 
[C]__________________
[C] اكتب  [ معلوماتي ] لكي اعرض معلوماتك
[C]__________________
[C] اكتب [ بصمة ]"مع الرساله" لكي اعطيك بصمة في الحائط
[C]__________________
[C]اكتب [ منشن ] لكي ادعي جميع أعضاء القروب
[C]__________________
[C] اكتب [ مكالمة ] لكي اشغل مكالمه
[C]__________________
[C] اكتب [ اغلاق المكالمة ] لكي اغلق  الاتصال 
[C]__________________
[C] اكتب [ تاريخ ] لمعرفه وقت الحالي و وقت ارسال الرساله
[C]__________________
[C] اكتب [ مشاهد ] للدخول الي المشاهدة 
[C]__________________
[C] اكتب [ قول ]"و بعدها الكلمه" لكي ارسل تسجيل صوت 
[C]__________________
[C] اكتب [ اونلاين ] لمعرفه عدد أعضاء الاونلاين 
[C]__________________

[C] و انا لدي نظام خاص احذف الرسائل الغير اخلاقيه

[C] و ايضا لدي نظام مانع روابط

[C]  """
    	subclint.send_message(chatId=chatId,message=hh)
	
	   
    if content=="حظ":
    	from random import choice
    	g=choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    	
    	uiu = f"""من بين 1 الي 10
    	حصلت على -[ {g} ]-"""
    	subclint.send_message(chatId=chatId,message=uiu)
    	
    if content=="مجرة":
    	if userId not in Dict:
	    	aas = """
[B]⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀✦ ⠀ ⠀　　　　　　　　　　　　　　⠀⠀⠀⠀⠀* ⠀⠀⠀.　　　　　　　　　　. ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀.　　　　　　　　　　　　　.　　　ﾟ .　　　　　　　　　　　　　. 　　　　　　　　　　　　　　　✦ 　　　　　,　　　　　　　.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☀️
　　　　　　*　　　　　　　　　　　.
.　　　　　　　　　　　　　. 　　✦⠀　   　　　,　　　　　　　　　*
　　　　　⠀　　　　⠀　　, 🍃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.　　　　　 　　⠀　　　⠀.　
　　˚　　　⠀　⠀  　　,　　　　　　.
　　　　　　　　　　　　　.
　　　　　　*⠀　　⠀  　　　　　⠀✦⠀　
　　　　　　　　　　　　　　　　　　.
　　　　.　　　　.　　　⠀🌕
　　　　　　　　　　　.
　　　　　　　🚀
　　　˚　　　　　　　　ﾟ　　　　　.
　.⠀　　🌎⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀‍⠀, ⠀⠀✦ ⠀ ⠀　　　　　　　　　　　　　　⠀⠀⠀⠀⠀* ⠀⠀⠀.　　　　　　　　　　. ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀.　　　　　　　　　　　　　.　　　ﾟ .　　　　　　　　　　　　　. 　　　　　　　　　　　　　　　✦ 　　　　　,　　　　　　　.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☀️
　　　　　　*　　　　　　　　　　　.
.　

♡
˚  · .　　  ♡
✦  ˚ 　· 　　    .      ♡⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀✦ ⠀ ⠀ ⠀⠀⠀⠀⠀* ⠀⠀⠀. . ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀✦ ⠀ ⠀　　　　　　　　　　　　　　⠀⠀⠀⠀⠀* ⠀⠀⠀.　　　　　　　　　　. ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀✦⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☄️ ⠀ ⠀⠀⠀⠀⠀⠀.　　　　　　　　　　　　　.　　　ﾟ .　　　　　　　　　　　　　. 　　　　　　　　　　　　　　　✦ 　　　　　,　　　　　　　.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀☀️
　　　　　　*　　　　　　　　　　　.
.　　　　　　　　　　　　　. 　　✦⠀　   　　　,　　　　　　　　　*
　　　　　⠀　　　　⠀　　, 🍃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.　　　　　 　　⠀　　　⠀.　
　　˚　　　⠀　⠀  　　,　　　　　　.
　　　　　　　　　　　　　.
　　　　　　*⠀　　⠀  　　　　　⠀✦⠀　

　.⠀⠀
	    	"""
	
	    	for qq in range(10):
	    		subclint.send_message(chatId=chatId,message=aas)
	    		T(target=Countdown,args=(300,userId,Dict, )).start()
	    		
	    	else:
	    		subclint.send_message(chatId=chatId, message="لا يمكن استخدام الامر حاليا انتظر خمس دقائق", replyTo=msgId)
	    		

    if content.startswith("نفر"):
	       	    	from random import choice
	       	    	io = ["ها","عيوني","مو فاضي لك","انجب","شكو خير؟","قول"]
	       	    	g=choice(io)
	       	    	subclint.send_message(chatId=chatId, message=g, replyTo=msgId)
	       	    	
    if content.startswith("نكتة"):
	       	    	from random import choice
	       	    	nkta = ['فرحان تجوز زعلانة خلفو يا فرحة ما تمت ', 'محشش غمز لزوجته وقال : صرفي العيال من الغرفة صرخت زوجته: اللي ينام آعطيه 100 ريال نام زوجها أول واحد.', 'محشش وهندي طاحو من الطيارة المحشش مات والهندي ما مات سألو الهندي كيف مات المحشش قال :ياخي هذا نفر همار انا يقول افتح مظلة هو يقول:مافي مطر.', 'شرطي مسك محشش قاله انت وين ساكن؟ قال مع أخوي قال وأخوك وين ساكن؟ قال معي قال وأنت وأخوك وين ساكنين؟ قال مع بعض', 'مره واحد اشترى خاتم لخطيبته قالوله اهلها تعال لبسها الخاتم ضرب الطاوله قال خسارة ياليتني شريت لها سروال', 'فتاة تسأل حبيبها: هل ستظل تحبني بعد الزواج؟ فرد قائلاً: طبعاً حبيبتي إذا لم يمانع زوجك', 'مره واحد تزوج وحده حولا قال لها. ليش ما تتكلمي قالت مستحيه من الي جنبك ', 'قال لزوجته بالمطار البسي عباية واسعة، قالتله فديتك تغار علي، قالها موغيرة ولا شي طبقات كرشك كنها حزام ناسف لا تورطينا مع التفتيش', 'أم تسأل ولدها تعرف نيوتن؟، قال الولد: لا ما أعرفه، قالت له: لو تنتبه لدروسك كان عرفته!!، قال الولد: طيب أنتِ تعرفين خلود؟، قالت له: لا من هي؟، قال لها : لو تنتبهين لزوجك كان عرفتيها!!، المهم الولد حاليًا أسبوع عند أخواله وأسبوع عند عمامه', 'واحد تخانق مع زوجته قال لها: ما رح أشبهك بالحمار أخاف يزعل!، قالت له: كل شيء ولا زعلك عاد، يقولون إبليس دمعت عيونه وصفق لها', 'واحد سأل خطيبته في أحد مسك يدك؟، سكتت قال لها زعلتي، قالت له لا بس أعدهم', 'خروف بيسأل خروف مر عيدين وما ذبحوك، قاله مسجل بشهادة ميلادي حمار', 'سأل المدرس الطالب ايه الحاجة اللي لونها أسود في أصفر وبتعطينا عسل؟، رد الطالب وقاله أتوبيس المدرسة بتاع البنات', 'واحد أحول اجا ابوه من السفر ركض لعنده وباس الشنطة وشال أبوه', 'واحد غبي اشتغل في الصين سواق تكسي وكل ما حد يوقفه كان يقله ياعم أنا لسه منزلك قبل كدة أنت نسيت', 'مرة طاولة تجوزت طاولة خلفو كراسي', 'مرة واحد خلف 7عيال سمى نفسه سفن اب', 'واحد مشغول أتجوز واحدة مشغولة خلفوا عيل مش فاضيلهم', 'مرة واحدة قاعدة مع جوزها في جو رومانسى فالست قالت لجوزها قولي كلمة حلوة قالها بقلاوة قالت له لا كلمة تهزني قال لها مرجيحة قالت لا كلمة تحسسني إني مراتك قال لها أنتي طالق', 'واحد عايز ياخد حقه وهو على فراش الموت قال لمراته إذا مت أتجوزي جارنا محمود قلت ليه قالها لأنه مره باعلي بضاعة وغشني فيها','فيه واحد رجع في كلامه خبط اللي وراه','واحد مسطول صاحبه وقع في البير راح يستناه عند الحنفيه','مرة واحد ضاق خلقه أعطاه لأخوه','شو الفرق بين النّملة والفيل؟ الجواب الفيل رجله بتنمّل أمّا النملة رجلها ما بتفيِّل','قمة الوفاء بأنه نملة تزوّجت فيل، وبعد ما مات قضت كل عمرها تدفن فيه']
	       	    	g=choice(nkta)
	       	    	subclint.send_message(chatId=chatId, message=g, replyTo=msgId)

	

    if content=="معلوماتي":
    	user_info = subclint.get_user_info(userId=userId).json
    	description = user_info["content"]
    	gir = f"""[BC] معلوماتك
[C]_____________
[C] اسمك :{nm} 
[C]{y} : الوقت
[C]{tui} : لفل
[C] السيرة :{description} 
"""
    	subclint.send_message(chatId=chatId,message=gir)
    if content in p:
    	gt = f"عيب لا تسب {nm}"
    	subclint.delete_message(chatId=chatId,messageId=msgId)
    	subclint.send_message(chatId=chatId,message=gt)
    if content.startswith("احبك"):
	       	    	from random import choice
	       	    	io = ["حبتك حيه ","اعشقك","اموت فيك","عنجد؟"]
	       	    	g=choice(io)
	       	    	subclint.send_message(chatId=chatId, message=g, replyTo=msgId)	
    if content.startswith("سالي"):
	       	    	subclint.send_message(chatId=chatId, message="سَاليّ أحسن بنت بالطابة الارضية",replyTo=msgId) 

    if content.startswith("برهوم"):
	       	    	subclint.send_message(chatId=chatId, message="اكبر كشاش بالعالم لا تصدق ولا حرف منو ",replyTo=msgId)
   	    	         		       	    		       	    	 
    if content == "بروين":
	       	    	subclint.send_message(chatId=chatId, message="بروينننع يعني كولااااعععع يعني وسااع  ",replyTo=msgId)
    if content == "مافيا":
	       	    	subclint.send_message(chatId=chatId, message="مافيا خط احمر لحد يحتك فيه ",replyTo=msgId)
	
    if content == "سيزار":
	       	    	subclint.send_message(chatId=chatId, message="سيزارو احلا عالم حبيب القلب ",replyTo=msgId)
	       	    	
    if content.startswith('كل'):
	       	    	subclint.send_message(chatId=chatId, message="كول خرا ولاك",replyTo=msgId)
    if content == 'رورو':
	       	    	subclint.send_message(chatId=chatId, message="اكبر نصابة بالعالم لا تأمنو لها ",replyTo=msgId)
    if content == 'حلا':
	       	    	subclint.send_message(chatId=chatId, message=" تحب الفراشات يقولو انها فراشة ناعمة ",replyTo=msgId)
    if content == 'مرندي':
	       	    	subclint.send_message(chatId=chatId, message="غارق بأحضان نسوان اليونان ",replyTo=msgId)
	       	    	
    if content.startswith("سهيل"):
    	subclint.send_message(chatId=chatId, message="عضو",replyTo=msgId)
    	
    	
    if content.startswith("ودي اكتب"):
    	subclint.send_message(chatId=chatId, message="عن طيزك قصيدة",replyTo=msgId)
    if content.startswith("القلم عندي"):
    	subclint.send_message(chatId=chatId, message="لكن طيزك وين أصيده",replyTo=msgId)
    	
    if content.startswith("مسا"):
    	subclint.send_message(chatId=chatId, message="يسعدلي مساك/ي اللي زي الفل",replyTo=msgId)
    	
    if content.startswith("صباح"):
    	subclint.send_message(chatId=chatId, message="يسعدلي صباحك يقلبي فديت كلشي",replyTo=msgId)
    	
    if content.startswith("ارحب"):
    	subclint.send_message(chatId=chatId, message="البقى يا بعدي",replyTo=msgId)
    	
    	
    if content.startswith("تحبني"):
    	from random import choice
    	t7bni=["يمكن","بموت فيك","لا","مين انت حتى حبك","عيفني غازي كرامة ل الله ","خجلت"]
    	g=choice(t7bni)
    	subclint.send_message(chatId=chatId, message=g,replyTo=msgId)
    if content.startswith("ليش"):
    	from random import choice
    	lesh=["خلك فحالك","مدخلك","لأنك حريمة يا صديق ","أسأل نفسك   ","مدري","كيفي"]
    	g=choice(lesh)
    	subclint.send_message(chatId=chatId, message=g,replyTo=msgId)
    if content.startswith("تخليني"):
    	subclint.send_message(chatId=chatId, message="أخليك وأخلي أبوك",replyTo=msgId)
    if content.startswith("حجرة"):
    	from random import choice
    	ll3ba=["🪨","📄","✂️"]
    	g=choice(ll3ba)
    	subclint.send_message(chatId=chatId, message=g,replyTo=msgId)
    if content.startswith("ورقة"):
    	from random import choice
    	ll3ba=["🪨","📄","✂️"]
    	g=choice(ll3ba)
    	subclint.send_message(chatId=chatId, message=g,replyTo=msgId)
    if content.startswith("مقص"):
    	from random import choice
    	ll3ba=["🪨","📄","✂️"]
    	g=choice(ll3ba)
    	subclint.send_message(chatId=chatId, message=g,replyTo=msgId)
    if content.startswith("دوم"):
    	subclint.send_message(chatId=chatId, message="دام نبضك وعزك وغلاتك ودلالك يعمري",replyTo=msgId)
    if content.startswith("نورت"):
    	subclint.send_message(chatId=chatId, message="نورك",replyTo=msgId)
    if content.startswith("هلا"):
    	subclint.send_message(chatId=chatId, message="هَلَا بروحك يروحي",replyTo=msgId)
    if content.startswith("مرحبا"):
    	subclint.send_message(chatId=chatId, message="اهلين روحي",replyTo=msgId)
    if content.startswith("تسلم"):
    	subclint.send_message(chatId=chatId, message="ربي يسلمك ",replyTo=msgId)
    if content.startswith("نبضك"):
    	subclint.send_message(chatId=chatId, message="ونبضك",replyTo=msgId)
    if content.startswith("عزك"):
    	subclint.send_message(chatId=chatId, message="وعزك",replyTo=msgId)
    if content.startswith("اسمع"):
    	subclint.send_message(chatId=chatId, message="سم طال عمرك",replyTo=msgId)
    if content.startswith("مح"):
    	subclint.send_message(chatId=chatId, message="مٰمحححححح ",replyTo=msgId)
    if content.startswith("ابوس"):
    	subclint.send_message(chatId=chatId, message="أبوس طيبة قلبك",replyTo=msgId)
    if content.startswith("هلو"):
    	subclint.send_message(chatId=chatId, message="لا تقول هلو يا قي ",replyTo=msgId)
    if content.startswith("ابوك"):
    	subclint.send_message(chatId=chatId, message="أأبوك لحالك  ",replyTo=msgId)
    if content.startswith("حيوان"):
    	subclint.send_message(chatId=chatId, message="يركبك",replyTo=msgId)
    if content.startswith("جحش"):
    	subclint.send_message(chatId=chatId, message="ينط عليك",replyTo=msgId)
    if content.startswith("حئير"):
    	subclint.send_message(chatId=chatId, message="شو ئاسي",replyTo=msgId)
    if content.startswith("حقير"):
    	subclint.send_message(chatId=chatId, message="متوحش",replyTo=msgId)
    if content.startswith("كيوت"):
    	subclint.send_message(chatId=chatId, message="ابوك لكيوت",replyTo=msgId)
    if content.startswith("نوب"):
    	subclint.send_message(chatId=chatId, message="نطم محد غيرك نوب يلفرخ",replyTo=msgId)
    if content.startswith("اشلح"):
    	subclint.send_message(chatId=chatId, message="طوبز",replyTo=msgId)
    if content.startswith("فازلين"):
    	subclint.send_message(chatId=chatId, message="ابراهيم ارحمني",replyTo=msgId)
    if content.startswith("💔"):
    	from random import choice
    	ll3ba=["تع تع اشلح اعطيك ابرة تخفف وجعك 💉","تع افكعك تحميلة تطيب💊","يعقلبي خذ لزقة 🩹"]
    	g=choice(ll3ba)
    	subclint.send_message(chatId=chatId, message=g,replyTo=msgId)
    if content.startswith("حلو"):
    	subclint.send_message(chatId=chatId, message="عيونك الحلوة",replyTo=msgId)
    if content.startswith("الوان"):
    	subclint.send_message(chatId=chatId, message="رفرف يا كايدهم 🏳️‍🌈",replyTo=msgId)
    if content.startswith("باي"):
    	subclint.send_message(chatId=chatId, message="لا تبعد عني يا حبيبي ",replyTo=msgId)
    if content.startswith("بام"):
    	subclint.send_message(chatId=chatId, message="صديقة باو ",replyTo=msgId)
    if content.startswith("الحياة حلوة"):
    	subclint.send_message(chatId=chatId, message="كذاب بكندرة ",replyTo=msgId)
    if content.startswith("كم الساعة"):
    	subclint.send_message(chatId=chatId, message="ستين دقيقة",replyTo=msgId)
    if content.startswith("صح نفر"):
    	subclint.send_message(chatId=chatId, message="صح يكبتن ببصملك بالعشرة ",replyTo=msgId)
    if content.startswith("بوت "):
    	subclint.send_message(chatId=chatId, message="اذا تجيب سيرتي بالعاطل اشقك",replyTo=msgId)
    if content.startswith("ناروتو"):
    	subclint.send_message(chatId=chatId, message="ون بيس عمك",replyTo=msgId)
    if content.startswith("سيلاوي"):
    	subclint.send_message(chatId=chatId, message="حريمة دولي",replyTo=msgId)
    if content.startswith("ابعرها"):
    	subclint.send_message(chatId=chatId, message="كول هوا عيب البيت دا طاهر ",replyTo=msgId)
    if content.startswith("كفو"):
    	subclint.send_message(chatId=chatId, message="كَفوك",replyTo=msgId)
    if content.startswith("تم"):
    	subclint.send_message(chatId=chatId, message="تتم أفراحك",replyTo=msgId)
    	
    	
