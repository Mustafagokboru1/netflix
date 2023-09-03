import requests
import time

# Kullanıcıdan link girmesini isteyin
target_url = input("İzlenme göndermek istediğiniz linki girin: ")
num_views = int(input("Kaç izlenme göndermek istersiniz: "))  # Kullanıcıdan bir sayı girmesini isteyin

for i in range(num_views):
    response = requests.get(target_url)
    print(f"Izlenme {i + 1}: {response.status_code}")
    time.sleep(10)  # Her istek arasında 10 saniye beklemek için, bu süreyi ihtiyaca göre ayarlayabilirsiniz.
