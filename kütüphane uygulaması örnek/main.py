from tablolar import Kutuphane,Kisi,Kitap,Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///kutuphane_takip_sistemi.db")
Base.metadata.bind = engine

DbSession = sessionmaker(bind = engine)
Session = DbSession()

kisiler = Session.query(Kisi).all()
print("\n\n")
print("******************* ÜYELER **************************")
for kisi in kisiler:
    print("Üye adı: {} Üye soyadı: {}\nÜye TC: {}\nÜye doğum tarihi: {}\nÜye olduğu kütüphane: {}".format(kisi.kisi_ad,kisi.kisi_soyad,kisi.kisi_tc,kisi.kisi_dogum_tarihi,kisi.kutup_id.kutup_isim))
    print("*****************************************************")

print("\n\n")

kitaplar = Session.query(Kitap).all()
print("****************** KİTAPLAR *************************")

for kitap in kitaplar:
    print("Kitap adı: {}\nKitap yazarı: {}\nKitap ID: {}\nKitap sayfa sayısı: {}\nKitabın bulunduğu kütüphane: {}".format(kitap.kitap_ad,kitap.kitap_yazar,kitap.kitap_id,kitap.kitap_sayfa_sayisi,kitap.kutup_id.kutup_isim))
    print("*****************************************************")

print("\n\n")
kutuphaneler = Session.query(Kutuphane).all()
print("**************** KÜTÜPHANELER ***********************")

for kutuphane in kutuphaneler:
    print("Kütüphane adı: {}\nKütüphane ID: {}\nKütüphane adresi: {}\nKütüphane telefon no: {}".format(kutuphane.kutup_isim,kutuphane.kutup_id,kutuphane.kutup_adres,kutuphane.kutup_telefon_no))
    print("*****************************************************")

print("\n\n")