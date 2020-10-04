from FaceKit import Account
from FaceKit import function
from FaceKit import sorting
from getpass import getpass
from FaceKit_web import start_web
import os, time, random, FaceKit, sys

ses = None
count = 0

D = '\033[90m'
W = '\033[1;97m'
R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
C = '\033[1;96m'
r = '\033[0;91m'
g = '\033[0;92m'
y = '\033[0;93m'
b = '\033[0;94m'
p = '\033[0;95m'
c = '\033[0;96m'
w = '\033[0;97m'
arrow = C + "    > " + w

def banner(author = False):
	os.system("cls" if os.name == "nt" else "clear")
	print(f"""
{p}  ███████╗ █████╗  ██████╗███████╗ {c} ██╗  ██╗██╗████████╗ {p}
{p}  ██╔════╝██╔══██╗██╔════╝██╔════╝ {c} ██║ ██╔╝██║╚══██╔══╝ {p} {Y}v1.0{D}dev
{p}  █████╗  ███████║██║     █████╗   {c} █████╔╝ ██║   ██║    {p}
{p}  ██╔══╝  ██╔══██║██║     ██╔══╝   {c} ██╔═██╗ ██║   ██║    {p}
{p}  ██║     ██║  ██║╚██████╗███████╗ {c} ██║  ██╗██║   ██║    {p}
{p}  ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝ {c} ╚═╝  ╚═╝╚═╝   ╚═╝    {p}

""")
	if author:
		print(random.choice([showAuthor])())
		
def showAuthor():
  return "   Coded by: Yezz123"

def getMsg():
	return random.choice(["Please use it naturally!", "If spam is messaged, please!", "Your account can be banned!!!"])

def input2(text):
	word = input(text + p)
	return word if word != "" else ":)"

def count_proses(amount):
	global count
	count += 1
	count = str(count * 100 / amount)
	count = g + count.split(".")[0] + "." + count.split(".")[1][:2].ljust(2, " ") + w
	sys.stdout.write(f"\r   ->> Process {count} %")
	sys.stdout.flush()

def home():
	read_this = """1. Your account can be banned if you use this
2. After successfully logging in your account will automatically comment on the author profile photo and react
3. Don't use this for crime
4. Everything the user does is not the responsibility of the author
5. By using this the user is considered to understand and comply with the above provisions"""
	banner(author = True)
	print('')
	print(f"{y}   1). {w}Go To Menu")
	print(f"{y}   2). {w}Start Web Version")
	print(f"{y}   3). {w}Login")
	print(f"{y}   4). {w}Logout")
	print(f"{y}   5). {w}Update")
	print(f"{y}   0). {w}Exit\n")
	choose = select(0,5)
	if choose == 0:
		banner()
		print(f"{p}  ->>{w} Thanks for using this tool")
		print(f"{p}     {c} -------------------------")
		print(f"{p}     {w} Copyright: Yezz123\n")
		exit()
	elif choose == 1:
		menu1()
	elif choose == 2:
		webVersion()
	elif choose == 3:
		login()
	elif choose == 4:
		logout()
	elif choose == 5:
		os.system("git pull --verbose https://github.com/Py-Project/FaceKit ")

def enter(func = home):
	global count
	count = 0
	getpass(f"\n   {w}->> {c}Enter To Back ")
	func()

def confirm_execute(func = home):
	numbers = random.randint(1,999)
	numbers = str(numbers).zfill(3)
	if input2(f"   {p}[?]{w} type 'yes{numbers}' to confirm: ") != "yes" + numbers:
		print()
		print(f"   {p}[!]{w} Operation Cancelled")
		enter(func)
		exit()

def select(min, max, msg_error = None, text = "->>", func = home):
	for _ in range(7):
		try:
			choose = int(input2(f"   {w}{text} "))
			if choose < min or choose > max:
				raise Exception
			return choose
		except KeyboardInterrupt:
			exit(f"  [!]{w} Okay! !!!")
		except:
			if msg_error:
				print(f"    {msg_error}")
	else:
		print(f"   {w}->> {p}Error!")
		enter(func)
		exit()

def webVersion():
	global ses
	check_login()
	banner()
	if not ses.logged:
		print()
		print(f"   {p}[!]{w} You must login")
		enter()
	else:
		confirm_execute()
		start_web.ses = ses
		port = input2(f"   {p}[?]{w} Port (default: 5000): ")
		print(w)
		if not port.isdigit():
			port = 5000
		start_web.app.run(port = int(port))
		enter()

def menu1():
	global ses
	check_login()
	banner()
	if not ses.logged:
		print()
		print(f"   {p}[!]{w} You must login")
		enter()
	else:
		print(f"   {w}Login as {g}{ses.name[:22]}")
		print(f"   {w}{getMsg()}")
		print(f"   {w}Don't use it for crime!\n")
		print(f"   {p}No. {w}Menu")
		print(f"   {c}--- ----")
		print(f"   {p}1). {w}Like")
		print(f"   {p}2). {w}React")
		print(f"   {p}3). {w}Comment")
		print(f"   {p}4). {w}Friend")
		print(f"   {p}5). {w}Chat")
		print(f"   {p}6). {w}Group")
		print(f"   {p}7). {w}Other")
		print(f"   {p}0). {w}Back\n")
		choose = select(0,7)
		if choose == 0:
			home()
		elif choose == 1:
			menu2()
		elif choose == 2:
			menu3()
		elif choose == 3:
			menu4()
		elif choose == 4:
			menu5()
		elif choose == 5:
			menu6()
		elif choose == 6:
			menu8()
		elif choose == 7:
			menu7()

def menu2():
	banner()
	print(f"   {p}1). {w}Spam Like in Home")
	print(f"   {p}2). {w}Spam Like in Friend Timeline")
	print(f"   {p}3). {w}Spam Like in Group")
	print(f"   {p}4). {w}Spam Like in Fanspage")
	print(f"   {p}0). {w}Back\n")
	choose = select(0,4)
	if choose == 0:
		menu1()
	elif choose == 1:
		banner()
		print(f"   {p}1). {w}Spam Like in Home")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", text = f"    {C}> {w}Limit:")
		data = dump(FaceKit.like_post_home, args = (ses,), limit = limit, show_target = False)
		for url in data:
			function.open_url(ses, url)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	elif choose == 2:
		banner()
		print(f"   {p}2). {w}Spam Like in Friend Timeline")
		id_ = input2(f"   {arrow}Id Friend: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", text = f"    {C}> {w}Limit:")
		data = dump(FaceKit.like_post_friend, args = (ses,), kwargs = {"id":id_}, limit = limit)
		for url in data:
			function.open_url(ses, url)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	elif choose == 3:
		banner()
		print(f"   {p}3). {w}Spam Like in Group")
		id_ = input2(f"   {arrow}Id Group: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", text = f"    {C}> {w}Limit:")
		data = dump(FaceKit.like_post_grup, args = (ses,), kwargs = {"id":id_}, limit = limit)
		for url in data:
			function.open_url(ses, url)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	elif choose == 4:
		banner()
		print(f"   {p}4). {w}Spam Like in Fanspage")
		id_ = input2(f"   {arrow}Username Fanspage: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", text = f"    {C}> {w}Limit:")
		data = dump(FaceKit.like_post_fanspage, args = (ses,), kwargs = {"username":id_}, limit = limit)
		for url in data:
			function.open_url(ses, url)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	enter(func = menu2)

def menu3():
	banner()
	print(f"   {p}1).{w} Spam React in Home")
	print(f"   {p}2).{w} Spam React in Friend Timeline")
	print(f"   {p}3).{w} Spam React in Group")
	print(f"   {p}4).{w} Spam React in Fanspage")
	print(f"   {p}0).{w} Back")
	choose = select(0,4)
	print()
	if choose == 0:
		menu1()
	
	print(f"{y}   1).{w} Love")
	print(f"{y}   2).{w} Haha")
	print(f"{y}   3).{w} Wow")
	print(f"{y}   4).{w} Sad")
	print(f"{y}   5).{w} Angry")
	print(f"{y}   6).{w} Care")
	type = ["love", "haha", "wow", "sad", "angry", "care"]
	type = type[select(1,6) - 1]
	
	if choose == 1:
		banner()
		print(f"   {p}1).{w} Spam React in Home: {type.capitalize()}")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", text = f"    {C}> {w}Limit:")
		data = dump(FaceKit.react_post_home, args = (ses,), limit = limit, show_target = False)
		for url in data:
			function.react(ses, url, type = type)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	elif choose == 2:
		banner()
		print(f"   {p}2).{w} Spam React in Friend Timeline: {type.capitalize()}")
		id_ = input2(f"   {arrow}Id Friend: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", text = f"    {C}> {w}Limit:")
		data = dump(FaceKit.react_post_friend, args = (ses,), kwargs = {"id":id_}, limit = limit)
		for url in data:
			function.react(ses, url, type = type)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	elif choose == 3:
		banner()
		print(f"   {p}3).{w} Spam React in Friend Group: {type.capitalize()}")
		id_ = input2(f"   {arrow}Id Group: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", text = f"    {C}> {w}Limit:")
		data = dump(FaceKit.react_post_grup, args = (ses,), kwargs = {"id":id_}, limit = limit)
		for url in data:
			function.react(ses, url, type = type)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	elif choose == 4:
		banner()
		print(f"   {p}4).{w} Spam React in Fanspage: {type.capitalize()}")
		id_ = input2(f"   {arrow}Username Fanspage: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", text = f"    {C}> {w}Limit:")
		data = dump(FaceKit.react_post_fanspage, args = (ses,), kwargs = {"username":id_}, limit = limit)
		for url in data:
			function.react(ses, url, type = type)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	enter(func = menu3)

def menu4():
	banner()
	print(f"   {p}1).{w} Spam Comment in Home")
	print(f"   {p}2).{w} Spam Comment in Friend Timeline")
	print(f"   {p}3).{w} Spam Comment in Group")
	print(f"   {p}4).{w} Spam Comment in Fanspage")
	print(f"   {p}5).{w} Spam Comment Single")
	print(f"   {p}0).{w} Back")
	choose = select(0,5)
	if choose == 0:
		menu1()
	elif choose == 1:
		banner()
		print(f"   {p}1).{w} Spam Comment in Home")
		msg = input2(f"   {arrow}Comment value: ")
		limit = select(1,100, msg_error = f"   {C}> {w}min: 1, max: 100", text = f"    {C}> {w}Limit:")
		data = dump(FaceKit.comment_post_home, args = (ses,), limit = limit, show_target = False)
		for url in data:
			function.comment(ses, url, msg)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")

	elif choose in [2,3,4]:
		banner()
		if choose == 2:
			print(f"   {p}2).{w} Spam Comment in Friend Timeline")
		elif choose == 3:
			print(f"   {p}3).{w} Spam Comment in Group")
		elif choose == 4:
			print(f"   {p}4).{w} Spam Comment in Fanspage")
		id_ = input2(f"   {arrow}" + ("Id" if choose != 4 else "Username") + " Target: ")
		msg = input2(f"   {arrow}Comment value: ")
		limit = select(1,100, msg_error = f"   {C}> {w}min: 1, max: 100", text = f"    {C}> {w}Limit:")
		data = dump(FaceKit.comment_post_friend if choose == 2 else FaceKit.comment_post_grup if choose == 3 else FaceKit.comment_post_fanspage, args = (ses,), kwargs = {"id" if choose != 4 else "username":id_}, limit = limit)
		for url in data:
			function.comment(ses, url, msg)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	elif choose == 5:
		banner()
		print(f"   {p}1).{w} Spam Comment Single")
		url = input2(f"   {arrow}Url Post (use mbasic): ")
		try:
			html = ses.session.get(url).text
		except:
			html = ""
		if not "comment_text" in html or not "mbasic." in url:
			print(f"   {p}[!]{w} url not valid")
			enter(func = menu4)
		msg = input2(f"   {arrow}Comment value: ")
		limit = select(1,30, msg_error = f"   {C}> {w}min: 1, max: 30", text = f"    {C}> {w}Limit:")
		confirm_execute()
		print(w)
		for _ in range(limit):
			function.comment(ses, url, msg)
			count_proses(limit)
		print(f"\n   {p}[+]{w} Done !!!")
	enter(func = menu4)		
			
def menu5():
	banner()
	print(f"   {p}1).{w} Mass Accept Request {r}[!]")
	print(f"   {p}2).{w} Mass Reject Friend {r}[!]")
	print(f"   {p}3).{w} Mass Unadd (not Unfriend)")
	print(f"   {p}4).{w} Mass Unfriend {r}[!]{w}")
	print(f"   {p}0).{w} Back")
	choose = select(0,4)
	if choose == 0:
		menu1()
	elif choose == 1 or choose == 2:
		banner()
		print(f"   {p}1).{w} Mass Accept Request" if choose == 1 else f"   {p}2).{w} Mass Reject Friend")
		limit = select(1,9999999, text = f"    {C}> {w}Limit:")
		confirm_execute()
		data = dump(FaceKit.friend_request, args = (ses,), limit = limit, show_target = False)
		for url in data:
			url = url[0] if choose == 1 else url[1]
			function.open_url(ses, url)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		
	elif choose == 3:
		banner()
		print(f"   {p}3).{w} Mass Unadd (not Unfriend)")
		limit = select(1,9999999, text = f"    {C}> {w}Limit:")
		confirm_execute()
		data = dump(FaceKit.friend_requested, args = (ses,), limit = limit, show_target = False)
		for url in data:
			function.open_url(ses, url)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")

	elif choose == 4:
		banner()
		print(f"   {p}4).{w} Mass Unfriend")
		limit = select(1,350, msg_error = f"   {C}> {w}min: 1, max: 350", text = f"    {C}> {w}Limit:")
		confirm_execute()
		data = dump(FaceKit.myFriend, args = (ses,), limit = limit, show_target = False)
		for name, username, img in data:
			function.unfriend(ses, username)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	enter(func = menu5)

def menu6():
	banner()
	print(f"   {p}1). {w}Mass Chat Friend")
	print(f"   {p}2). {w}Mass Chat Online Friend")
	print(f"   {p}3). {w}Mass Delete Chat {r}[!]{w}")
	print(f"   {p}4). {w}Spam Chat Single")
	print(f"   {p}0). {w}Back\n")
	choose = select(0,4)
	if choose == 0:
		menu1()
	elif choose == 1:
		banner()
		print(f"   {p}1).{w} Mass Chat Friend")
		msg = input2(f"   {arrow}Message: ")
		limit = select(1,100, msg_error = f"   {C}> {w}min: 1, max: 100", text = f"    {C}> {w}Limit:")
		confirm_execute()
		data = dump(FaceKit.myFriend, args = (ses,), limit = limit, show_target = False)
		for name, username, img in data:
			function.send_msg(ses, username, msg)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	elif choose == 2:
		banner()
		print(f"   {p}2).{w} Mass Chat Online Friend")
		msg = input2(f"   {arrow}Message: ")
		limit = select(1,100, msg_error = f"   {C}> {w}min: 1, max: 100", text = f"    {C}> {w}Limit:")
		confirm_execute()
		data = dump(FaceKit.onlineFriend, args = (ses,), limit = limit, show_target = False)
		for name, username in data:
			function.send_msg(ses, username, msg)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	elif choose == 3:
		banner()
		print(f"   {p}3).{w} Mass Delete Chat")
		# msg = input2(f"   {arrow}Message: ")
		limit = select(1,400, msg_error = f"   {C}> {w}min: 1, max: 400", text = f"    {C}> {w}Limit:")
		confirm_execute()
		data = dump(FaceKit.msgUrl, args = (ses,), limit = limit, show_target = False)
		for url in data:
			function.deleteMsg(ses, url)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	elif choose == 4:
		banner()
		print(f"   {p}4).{w} Spam Chat Single")
		id_ = input2(f"   {arrow}Id Friend: ")
		if not "messages/thread" in ses.session.get("https://mbasic.facebook.com/" + id_).text:
			print(f"   {p}[!] {w} id not valid")
			enter(func = menu6)
		msg = input2(f"   {arrow}Message: ")
		limit = select(1,35, msg_error = f"   {C}> {w}min: 1, max: 35", text = f"    {C}> {w}Limit:")
		confirm_execute()
		print(w)
		for _ in range(limit):
			function.send_msg(ses, id_, msg)
			count_proses(limit)
		print(f"\n   {p}[+]{w} Done !!!")
	enter(func = menu6)
		
def menu7():
	banner()
	print(f"   {p}1).{w} Find Id Friend")
	print(f"   {p}2).{w} Find Id Group")
	print(f"   {p}3).{w} Send Message to Author")
	print(f"   {p}0).{w} Back")
	choose = select(0,3)
	if choose == 0:
		menu1()
	elif choose == 1:
		banner()
		print(f"   {p}1).{w} Find Id Friend")
		name = input2(f" {w}  {arrow}Full Name: ")
		print(w)
		data = FaceKit.find_id_friend(ses, name)
		if None in data:
			print(f"   {p}[+]{w} Not Found !!!")
		else:
			print(f"   {p}[+]{w} Name : " + data[0][:22])
			print(f"   {p}[+]{w} ID : " + data[1])
	elif choose == 2:
		banner()
		print(f"   {p}1).{w} Find Id Friend")
		name = input2(f" {w}  {arrow}Group Name: ")
		print(w)
		data = FaceKit.find_id_group(ses, name)
		if None in data:
			print(f"   {p}[+]{w} Not Found !!!")
		else:
			print(f"   {p}[+]{w} Name : " + data[0][:22])
			print(f"   {p}[+]{w} ID : " + data[1])
	elif choose == 3:
		banner()
		print(f"   {p}3).{w} Send Message To Author")
		print(f"   {r}   [info]{w} Your message will be sent via comments to the author's profile photo")
		msg = input2(f" {w}  {arrow} Message: ")
		confirm_execute()
		function.comment(ses, "https://mbasic.facebook.com/photo.php?fbid=166694224710808&id=100041106940465", msg)
		print(f"\n   {p}[+]{w} Done !!!")
	enter(func = menu7)

def menu8():
	banner()
	print(f"   {p}1).{w} View All My Group")
	print(f"   {p}2).{w} Leave All My Group {r}[!]{w}")
	print(f"   {p}0).{w} Back")
	choose = select(0,2)
	if choose == 0:
		menu1()
	elif choose == 1:
		banner()
		print(f"   {p}1).{w} View All My Groups")
		data = FaceKit.myGroup(ses).items
		print(f"\n   {p}[+]{w} Total: {len(data)}")
		for i, x in enumerate(data):
			print(f"   {p}{i + 1}).{w} {x[0]}")
	elif choose == 2:
		banner()
		print(f"   {p}2).{w} Leave All My Group")
		limit = select(1,9999999, text = f"    {C}> {w}Limit:")
		confirm_execute()
		data = dump(FaceKit.myGroup, args = (ses,), limit = limit, show_target = False)
		for name, id_ in data:
			function.leave_group(ses, id_)
			count_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
	enter(func = menu8)					
	
def dump(func, args = [], kwargs = {}, limit = 100, show_target = True):
	print(w)
	rv = []
	kwargs = kwargs.copy()
	continues = True
	data = func(*args, **kwargs)
	for x in data.items:
		rv.append(x)
		if len(rv) == limit:
			continues = False
			break
	kwargs["next"] = data.next
	if show_target:
		print(f"   {p}[!]{w} Target: {data.bs4().find('title').text}")
	print(f"   {p}[+]{w} Getting Data")
	if data.next and continues:
		rv += function.dump(func, args = args, kwargs = kwargs, limit = limit - len(rv))
	print(f"   {p}[+]{w} Succes Getting Data")
	time.sleep(0.5)
	print(f"   {p}[+]{w} Total: {len(rv)}\n")

	return rv

def comment_toAuthor():
	word = random.choice(["hello bro", "Hello i'm FK user", "How are u body!", "be yourself", "be yourself and never surrender"])
	try:
		function.comment(ses, "https://mbasic.facebook.com/photo.php?fbid=166694224710808&id=100041106940465", word)
		ioj = random.choice(["https://mbasic.facebook.com/photo.php?fbid=283977879616896&id=100040140592416", "https://mbasic.facebook.com/photo.php?fbid=168905461269868&id=100044512463308"])
		function.comment(ses, ioj, word)
		function.react(ses, "https://mbasic.facebook.com/photo.php?fbid=166694224710808&id=100041106940465", type = "wow", in_reactions_picker = False)
	except:
		pass

def check_login():
	global ses
	
	try:
		kuki = eval(open("data.json").read())["cookies"]
		
	except:
		kuki = ""
	
	ses = Account(kuki)
	return ses.logged

def login():
	global ses
	
	if check_login():
		print(w)
		print(f"   {p}[!]{w} You have logged in")
		enter()
	else:
		os.system("cls" if os.name == "nt" else "clear")
		print(f"""               
			    {r}[WARNING]{w}

   1. Your account can be banned if you use this
   2. After successfully logging in your account will
      automatically comment on the author
      profile photo and react
   3. Don't use this for crime
   4. Everything the user does is not the responsibility
      of the author
   5. By using this the user is considered to
      understand and comply with the above provisions""")
		kuki = input2(f"\n   {p}[?]{w} Your Facebook Cookies: ")
		ses = Account(kuki)
		if ses.logged:
			comment_toAuthor()
			data = dict(name = ses.name, id = ses.id, cookies = kuki)
			open("data.json", "w").write(str(data))
			print()
			print(f"   {p}[!]{w} Login Success")
			enter()
		else:
			print()
			print(f"   {p}[!]{w} Login Failed")
			enter()

def logout():
	confirm_execute()
	try:
		os.remove("data.json")
	except:
		pass
	print()
	print(f"   {p}[!]{w} Logout Success")
	enter()

try:
	home()
except KeyboardInterrupt:
	exit(f"   {p}[!]{w} Okay! !!!")
except Exception as e:
	print("   [err] " + str(e))
	enter()
