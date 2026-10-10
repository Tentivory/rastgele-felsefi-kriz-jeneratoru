#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Felsefi Kriz Jeneratörü
Hiçbir şey anlamayan ama her şeyi anlıyormuş gibi yapan makine.
Kullanım: python kriz_jeneratoru.py
"""

import random
import time
import sys

# Gizli not: YXJhemluZGUgZ8O8w6fDvG4gYmlyIGthcmFuIGtvbWFrIHlvay4gS2F5eXVtIGdlbGVubmUga2FkYXIgc2FoaXAgb2xtYXlhbiBiaXIgc2Fsa2luIGRlZ2lsIG1pPyAodmV5YSBiaXIgc2V5bGVyIGJ1IGJ1cmFkYSB5YXppbG1pIHNhZGVjZSBnaXppbG1pKQ==
# Bu base64'u decode edersen bir şeyler çıkar. Belki çıkmaz.

kriz_listesi = [
    "Eğer hayat bir simülasyonsa, neden hala faturalarımı ödüyorum?",
    "Sonsuzluk gerçek mi yoksa sadece çok uzun bir çay molası mı?",
    "Kendimi düşündüğümde, düşünenin kim olduğunu kim düşünüyor?",
    "Eğer hiçbir şey önemli değilse, neden bu kodu yazdım?",
    "Zaman bir yanılsama mı yoksa sadece geç gelen otobüs mü?",
    "Özgür irade var mı yoksa her şey rastgele kriz üreticisi mi?",
    "Eğer herkes aynı şeyi düşünüyorsa, kim yanlış düşünüyor?",
    "Anlam aramak anlamsız mı yoksa anlamsızlık mı anlamlı?",
    "Bu kriz gerçek mi yoksa sadece bir fonksiyon çağrısı mı?",
    "Eğer durursam, durmak da bir hareket mi sayılır?"
]

def dramatik_bekle(saniye):
    for i in range(saniye):
        sys.stdout.write(f"\rDüşünülüyor... {'.' * (i % 4)}")
        sys.stdout.flush()
        time.sleep(1)
    print()

def kriz_uret(sayi=1):
    print("\n" + "="*50)
    print("FELSEFİ KRİZ MAKİNESİ AKTİF")
    print("="*50 + "\n")
    for _ in range(sayi):
        dramatik_bekle(random.randint(2, 5))
        kriz = random.choice(kriz_listesi)
        print(f"\n⚠️  KRİZ: {kriz}\n")
        print("Bu kriz üzerine 3 dakika düşünmeniz önerilir. Ya da hiç düşünmeyin. Her ikisi de doğru olabilir.")
        print("-" * 40)

if __name__ == "__main__":
    print("Rastgele Felsefi Kriz Jeneratörü'ne hoş geldiniz.")
    print("Bu program hiçbir şeyi çözmez. Sadece kriz üretir.")
    try:
        adet = int(input("Kaç tane kriz istersiniz? (varsayılan 1): ") or "1")
    except ValueError:
        adet = 1
    kriz_uret(adet)
    print("\nİşlem tamamlandı. Varoluşunuz hala belirsiz.")
