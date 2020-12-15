# nuker.py

Tiny, tiny, discord nuker lib in python.

## Before Setup ! Important !

1. Make sure you have a bot.
2. Go to your bot page in the discord developer portal, scroll down a bit and check every "privileged intent"

## Setup

1. Download nuker.py and requirements.txt
2. Install the requirements by using pip install -r requirements.txt
3. In your file, include the nuker lib using 
```py
from nuker import nuker
```
4. Well... Boom! You've successfully set it up.

## Docs

### Nuker Class

```py
myNuker = nuker("token here", prefix=prefix, invis=True / False, ownerid=yourownerid)
```

The token should be a bot token. If you do not supply a prefix, it will default to "!".
Invis will immediately set the bot's status to invisible when you run it if it is set to true. It also defaults to true.
Ownerid is the user id of the owner. With this set, the only person who will be able to use commands is the user with the id. If you do not set it, it will default to none.

### assignCommand

Now, how would you assign commands? You would use the assignCommand method.
```py
myNuker = nuker("token here", prefix=prefix, invis=True / False, ownerid=yourownerid)
myNuker.assignCommand(typeofcommand, nameofcommand)
```
Command types consist of "delchannels", "delroles", "masschannel", "massrole", "massnick", "masskick", and "massban".

You may also use the default set assignCmd command, which will be documented below. I will make this command configurable later.

### run

There are no parameters to this. This will simply load the bot.
```py
myNuker = nuker("token here", prefix=prefix, invis=True / False, ownerid=yourownerid)
myNuker.assignCommand(typeofcommand, nameofcommand)
myNuker.run()
```

## Commands

Command types: ***"delchannels", "delroles", "masschannel", "massrole", "massnick", "masskick", and "massban"***

Syntax for the commands.

### assignCmd

{prefix}assignCmd [nameofcommand, typeofcommand]

This will assign a certain command to a certain function. For example, if you were to send
"!assignCmd joe masschannel"
and then use
"!joe 10 rand"
It would create 10 random channels.

### delchannels

{prefix}delchannels [no args]

This will delete all channels. Pretty quickly, in fact!

### delroles

{prefix}delroles [no args]

This will delete all roles.

### masschannel

{prefix}masschannel [optional: amount, optional: name]

If no args are specified, it will do 100 random channels.
If no name is specified, it will do random names.
If the name value is "rand" it will random names.

### massrole

{prefix}massrole [optional: amount, optional: name]

If no args are specified, it will do 50 random roles.
If no name is specified, it will do random names.
If the name value is "rand" it will random names.

### massnick

{prefix}massnick [male/female/all, filter, nick]

The male/female/all arg is in case you wish for a random nick. If you do, "male" will use male names and "female" will use female names. Any other arg will use all nicknames.
The filter arg is if you only want to nick people who have a certain username. If you do, you would specify the username in that arg. Sadly, spaces are not supported as of now. If you do not wish to filter, just supply "*".
The nick arg is, well, what you want to nickname the people. If it is "rand", it will use names that you specified in the first argument.

### masskick

{prefix}masskick [optional: reason]

This command will kick everyone.

### massban

{prefix}massban [optional: reason]

This command will ban everyone.