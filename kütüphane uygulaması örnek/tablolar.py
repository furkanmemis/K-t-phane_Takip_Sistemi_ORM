from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Kutuphane(Base):

    __tablename__ = "kutuphane"

    kutup_id = Column(Integer,primary_key = True,nullable = False)
    kutup_isim = Column(String(70),nullable = False)
    kutup_adres = Column(String(150))
    kutup_telefon_no = Column(String(11),nullable = False)


class Kisi(Base):

    __tablename__ = "kisi"

    kisi_tc = Column(String(11),primary_key = True,nullable = False)
    kisi_ad = Column(String(20),nullable = False)
    kisi_soyad = Column(String(20),nullable = False)
    kisi_dogum_tarihi = Column(String(11))

    kutup = Column(Integer,ForeignKey("kutuphane.kutup_id"))
    kutup_id = relationship(Kutuphane,backref = "kisi")


class Kitap(Base):

    __tablename__ = "kitap"

    kitap_id = Column(Integer,primary_key = True,nullable = False)
    kitap_ad = Column(String(50),nullable = False)
    kitap_yazar = Column(String(60),nullable = False)
    kitap_sayfa_sayisi = Column(Integer,nullable = False)

    kutup = Column(Integer,ForeignKey("kutuphane.kutup_id"))
    kutup_id = relationship(Kutuphane,backref = "kitap")


engine = create_engine("sqlite:///kutuphane_takip_sistemi.db")
Base.metadata.create_all(engine)