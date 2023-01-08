from tablolar import Kutuphane,Kisi,Kitap,Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///kutuphane_takip_sistemi.db")
Base.metadata.bind = engine

DbSession = sessionmaker(bind = engine)
Session = DbSession()


kutuphane1 = Kutuphane(kutup_id = 1,kutup_isim = "Zeynep Otu Kütüphanesi",kutup_adres = "İstanbul/Beylikdüzü",kutup_telefon_no = "02223443434")
Session.add(kutuphane1)
Session.commit()

kitap1 = Kitap(kitap_id = 1,kitap_ad = "kitap1",kitap_yazar = "kitap1 yazar",kitap_sayfa_sayisi = 100,kutup_id = kutuphane1)
kitap2 = Kitap(kitap_id = 2,kitap_ad = "kitap2",kitap_yazar = "kitap2 yazar",kitap_sayfa_sayisi = 10,kutup_id = kutuphane1)
kitap3 = Kitap(kitap_id = 3,kitap_ad = "kitap3",kitap_yazar = "kitap3 yazar",kitap_sayfa_sayisi = 160,kutup_id = kutuphane1)
kitap4 = Kitap(kitap_id = 4,kitap_ad = "kitap4",kitap_yazar = "kitap4 yazar",kitap_sayfa_sayisi = 230,kutup_id = kutuphane1)
kitap5 = Kitap(kitap_id = 5,kitap_ad = "kitap5",kitap_yazar = "kitap5 yazar",kitap_sayfa_sayisi = 540,kutup_id = kutuphane1)
kitap6 = Kitap(kitap_id = 6,kitap_ad = "kitap6",kitap_yazar = "kitap6 yazar",kitap_sayfa_sayisi = 110,kutup_id = kutuphane1)
kitap7 = Kitap(kitap_id = 7,kitap_ad = "kitap7",kitap_yazar = "kitap7 yazar",kitap_sayfa_sayisi = 151,kutup_id = kutuphane1)

Session.add_all([kitap1,kitap2,kitap3,kitap4,kitap5,kitap6,kitap7])
Session.commit()


kisi1 = Kisi(kisi_tc = "11111111111",kisi_ad = "Furkan",kisi_soyad = "Memiş",kisi_dogum_tarihi = "18/04/2001",kutup_id = kutuphane1)
kisi2 = Kisi(kisi_tc = "22222222222",kisi_ad = "Ahmet Akif",kisi_soyad = "Memiş",kisi_dogum_tarihi = "19/02/2016",kutup_id = kutuphane1)

Session.add_all([kisi1,kisi2])
Session.commit()

