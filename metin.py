import requests
from bs4 import BeautifulSoup

# Site URL'sini belirleyin
url = 'SİTENİZİN_URLSİ_BURAYA_GELECEK'

# Siteye GET isteği gönderin
response = requests.get(url)

# Sayfanın içeriğini analiz etmek için BeautifulSoup kullanın
soup = BeautifulSoup(response.text, 'html.parser')

# Tüm metinleri içeren bir liste oluşturun
metinler = []

# Tüm metinleri bulmak için sayfa içinde dolaşın
for metin in soup.stripped_strings:
    metinler.append(metin)

# Metinleri metin.txt dosyasına yazın
with open('metin.txt', 'w', encoding='utf-8') as file:
    for metin in metinler:
        file.write(metin + '\n')

# İşlem tamamlandı mesajı
print("Metinler başarıyla kaydedildi.")
