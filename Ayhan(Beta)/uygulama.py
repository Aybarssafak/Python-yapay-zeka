import json
from fuzzywuzzy import process

def veri_tabani_yukle():
    with open('C:\\Users\\Aybars\\Documents\\Yapay Zeka\\Ayhan(Beta)\\veritabanı.json', 'r', encoding='utf-8') as dosya:
        return json.load(dosya)
    
def veritabanina_yaz(veriler):
    with open('C:\\Users\\Aybars\\Documents\\Yapay Zeka\\Ayhan(Beta)\\veritabanı.json', 'w', encoding='utf-8') as dosya:
        json.dump(veriler, dosya, indent=2, ensure_ascii=False)

def yakin_sonuc_bul(soru, sorular):
    eslesen = process.extractOne(soru, sorular, scorer=process.fuzz.token_set_ratio)
    return eslesen[0] if eslesen and eslesen[1] >= 60 else None

def cevabini_bul(soru, veritabani):
    for soru_cevaplar in veritabani["sorular"]:
        if soru_cevaplar["soru"] == soru:
            return soru_cevaplar["cevap"]
    return None

def chat_bot():
    veritabani = veri_tabani_yukle()
    
    while True:
        soru = input("Siz: ")
        
        if soru.lower() == "çık":
            break
        
        gelen_sonuc = yakin_sonuc_bul(soru, [soru_cevaplar["soru"] for soru_cevaplar in veritabani["sorular"]])
        
        if gelen_sonuc:
            verilecek_cevap = cevabini_bul(gelen_sonuc, veritabani)
            print(f"Bot: {verilecek_cevap}")
        else:
            print("Bot: Bunu nasıl cevaplayacağımı bilmiyorum. Öğretir misiniz?")
            yeni_cevap = input("Öğretmek için yazabilir veya 'geç' diyebilirsiniz: ")
            
            if yeni_cevap.lower() != 'geç':
                veritabani["sorular"].append({
                    "soru": soru,
                    "cevap": yeni_cevap
                })
                veritabanina_yaz(veritabani)
                print("Teşekkürler, sayenizde yeni bir şey öğrendim.")

if __name__ == '__main__':
    chat_bot()
