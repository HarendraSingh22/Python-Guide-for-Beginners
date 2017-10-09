import socket

## Paramètre du serveur
host="irc.domaine.org" # Serveur IRC
port=6667 # Port de connexion sur le serveur
channel=b"#NameOfTheChannel" # paramètre du channel
nickname = "username" #Mon ID

## Connexion
bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Création du socket
bot.connect((host,port)) # connexion avec les paramètres précédents.

bot.send(b"NICK "+nickname+"\r\n")
bot.send(b"USER "+nickname+" "+host+" domaine")
bot.send(b"JOIN "+channel)

#ginpong() # Take care of "PING" "PONG"
bot.send(b"ping")

## Votre code à envoyer au bot IRC
bot.send(b"hello world")

## DEFINITION DE FONCTIONS UTILES

def ginpong():
    while 1:
        junk=b""
        junk=bot.recv(7000)
        print(junk)
        beg=junk.find(b"PING") # Get the index of "PING"
        if beg>-1:             # If PING is captured
            junk=junk[beg:]
            if junk[5:].find(b" ")>0: # Check if there is a data sent after "PING"
                junk=junk[:(junk[5:].find(b" "))+4]+b"\r\n" # If TRUE, strip the data
                                                            # to obtain only "PING" message
            junk=junk.replace(b"PING",b"PONG") # raplace "PING" with "PONG"
            bot.send(junk) # send back the "PONG" message
            bot.send(junk) # do it more than once to make sure it's received
            bot.send(junk)
            break