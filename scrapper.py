import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'INSERT_URL_YANG_MAU_DISCRAPPING'

headers = {"User-Agent": 'SEARCH_GOOGLE_USER-AGENT_MY_COMPUTER'} 
#contoh user-agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36 OPR/62.0.3331.116

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser') 
    #fungsi html.parser berguna untuk mempermudah kita untuk membaca code

    title = soup.h1.get_text() 
    #kita harus inspect element dan klik bagian judul nya, jadi tiap e-commerce yang digunakan bisa berbeda-beda

    price = float(soup.find("span", itemprop="price").get_text())
    #inspect element dan klik bagian harganya

    print(title.strip())
    print(price)
    
    #Jika barang dibawah 300k maka akan mengirim email menggunakan method send_mail()
    if(price < 300000):
        send_mail()
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587) #587 adalah port
    #disini saya menggunakan smtp gmail, apabila kalian tidak menggunakan gmail silahkan cari saja di google smtp list
    
    #disini peran TCP 3-Way Handshake Process mulai bergerak
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('EMAIL', 'PASSWORD')
    #saya sarankan gunakan fitur Google App Password, karena ada fitur Two-Factor Authentication
    
    subject = "Barang sedang diskon!!"
    body = "Cek barangnya di [insert URL]"
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'PENGIRIM_EMAIL',
        'PENERIMA_EMAIL',
        msg
    )
    
    print("Email sudah terkirim")
    server.quit()


check_price()