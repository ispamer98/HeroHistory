#models.py

import reflex as rx
from sqlalchemy import Column, Integer, String, Boolean, DateTime, LargeBinary
from datetime import datetime
import pytz
from HeroHistory.db import Base
import bcrypt  # Librería para encriptar las contraseñas

# Definimos el modelo User, que es el que manejará la tabla de datos de los usuarios
class User(Base):
    __tablename__ = "user"  # Nombre de la tabla en la base de datos
    __table_args__ = {"sqlite_autoincrement": True}  # Permitimos que se autoincremente la primary key

    id = Column(Integer, primary_key=True)  # Id único para cada usuario
    username = Column(String(50), nullable=False, unique=True)  # Definimos longitud máxima para MySQL
    pasw = Column(String(100), nullable=False)  # Contraseña, con longitud máxima
    email = Column(String(100), nullable=False, unique=True)  # Usuario nunca vacío y único
    age = Column(Integer, nullable=False)  # Edad al momento de registrarse
    # Capturará la fecha y hora de registro del usuario en la zona horaria de Madrid
    creation_date = Column(DateTime, default=lambda: datetime.now(pytz.timezone('Europe/Madrid')))
    verify = Column(Boolean, nullable=False)  # Columna que indicará si el correo electrónico ha sido verificado
    avatar = Column(String(255), nullable=True)
    admin=Column(Boolean, nullable=False,default=False)
    
    avatars=["/avatar1.png", "avatar2.png", "/avatar3.png", "/avatar4"]
   

    def __init__(self, username, pasw, email, birthday, verify=False, avatar=None, admin=False):
        self.username = username  # Definimos el usuario
        self.pasw = bcrypt.hashpw(pasw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.email = email  # Definimos el correo
        # Calculamos la edad según la fecha de nacimiento proporcionada en el registro por el usuario
        self.age = self.calculate_age(birthday)
        self.verify = verify
        self.admin = admin

        if avatar is None:
            self.avatar = "/avatar_default.png"
        
        elif avatar in self.avatars:
            self.avatar = avatar
        else:
            self.avatar = "/avatar_default.png"


    def __str__(self):
        return f"User(username={self.username}, email={self.email}, verified={self.verify})"

    # Creamos una función que se encargará de calcular la edad del usuario mediante la fecha proporcionada en el registro
    def calculate_age(self, birthday):
        # Convertimos la fecha de nacimiento en un objeto de tiempo con un formato específico
        birthday_obj = datetime.strptime(birthday, "%d/%m/%Y")
        # Ajustamos la fecha a la zona horaria de Madrid
        birthday_obj = pytz.timezone('Europe/Madrid').localize(birthday_obj)
        # Calculamos la edad restando la fecha obtenida con la fecha actual de Madrid
        age = datetime.now(pytz.timezone('Europe/Madrid')) - birthday_obj
        # Dividimos los días obtenidos entre 365 que son los que tiene un año
        age_years = age.days // 365
        return age_years  # Y devolvemos el valor obtenido
