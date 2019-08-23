# Tokopedia Price Tracker
Kali ini saya akan memberikan tutorial cara Track Harga dan saya akan menggunakan *e-commerce* Tokopedia sebagai contoh, tapi kalian bebas mau menggunakannya untuk *e-commerce* apapun. Cara kita untuk Track Harga adalah menggunakan teknik Web Scrapping, tujuan dari Web Scrapping ini adalah untuk monitoring harga barang yang kita inginkan dan apabila barang yang kita inginkan sedang diskon harganya, secara otomatis akan mengirimkan notifikasi pesan ke email kita.

Saya menggunakan **Jupyter Notebook** sebagai editor saya. Alasan saya menggunakan **Jupyter Notebook** kita tidak perlu install Library lagi, karena sudah disediakan langsung oleh **Jupyter Notebook**

Library yang digunakan:
* requests
* BeautifulSoup
* smtplib

Menggunakan Library smtplib karena kita akan mengirim pesan ke email kita. Dan proses yang digunakan adalah TCP 3-Way Handshake Process.

### Untuk User-Agent kita tinggal Search di Google

Documentation for [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/ "BeautifulSoup") 
