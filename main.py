from nuker import nuker

x = nuker("token here", prefix='>', invis=False, assignCmd=False)
x.assignCommand("masschannel", 'joe')
x.run()
