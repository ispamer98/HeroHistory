import reflex as rx
import reflex as rx
from HeroHistory.models import User  # Tu modelo de usuario
from HeroHistory.db import db_session as session  # La conexión a la base de datos
import re
from datetime import datetime
import bcrypt

class RegisterAdminState(rx.State):
    admin_password: str = ""
    switch_value: bool = False

    @rx.event
    def set_admin_password(self, value: str):
        """Actualizar la contraseña admin."""
        self.admin_password = value

    @rx.event
    def toggle_switch(self):
        """Actualizar el estado del switch."""
        self.switch_value = not self.switch_value



class User_menuState(rx.State):
    is_open : bool = False
    
    @rx.event
    def toggle_menu(self):
        self.is_open = not self.is_open

    




class RegisterState(rx.State):
    """Estado de la página de registro."""
    username: str = ""
    password: str = ""
    confirm_password: str = ""
    email: str = ""
    confirm_email: str = ""
    date : str = ""
    admin_password: str = ""
    error_message: str = ""

    admin_pasw = "12345"  # Contraseña de administrador oculta

    def set_date(self, value: str):
            """Establecer la fecha ingresada por el usuario."""
            self.date = value

    def register(self):
        """Validar los datos e intentar registrar al usuario."""
        # Limpiar mensajes de error
        self.error_message = ""

        # Validar campos
        if not self.username:
            self.error_message = "El nombre de usuario no puede estar vacío."
            return
        if not re.match(r"^[a-zA-Z0-9]{5,20}$", self.username):
            self.error_message = "El usuario debe tener entre 5 y 20 caracteres alfanuméricos."
            return
        if session.query(User).filter_by(username=self.username).first():
            self.error_message = "El usuario ya existe."
            return

        if not self.password:
            self.error_message = "La contraseña no puede estar vacía."
            return
        if not any(c.isupper() for c in self.password):
            self.error_message = "La contraseña debe tener al menos una letra mayúscula."
            return
        if len(self.password) < 8:
            self.error_message = "La contraseña debe tener al menos 8 caracteres."
            return
        if self.password != self.confirm_password:
            self.error_message = "Las contraseñas no coinciden."
            return

        if not self.email:
            self.error_message = "El correo electrónico no puede estar vacío."
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            self.error_message = "El formato del correo electrónico no es válido."
            return
        if session.query(User).filter_by(email=self.email).first():
            self.error_message = "El email ya existe."
            return
        if self.email != self.confirm_email:
            self.error_message = "Los correos electrónicos no coinciden."
            return

        if not self.date:
            self.error_message = "La fecha de nacimiento es obligatoria."
            return
        




                # Convertir la fecha a formato adecuado para la base de datos
        try:
            # La fecha se recibe como "yyyy-mm-dd"
            valid_date = datetime.strptime(self.date, "%Y-%m-%d").strftime("%d/%m/%Y")  # Cambiar al formato requerido por la base de datos
        except ValueError:
            self.error_message = "La fecha ingresada no es válida."
            return

        # Validar si es administrador
        is_admin = self.admin_password == self.admin_pasw
        print(f"admin pasw = {self.admin_pasw}")
        # Crear usuario
        new_user = User(
            username=self.username,
            pasw=self.password,
            email=self.email,
            birthday=valid_date,
            admin=is_admin,
        )
        print(f"Is_admin = {is_admin}")
        print(f"Usuario.admin = {new_user.admin}")
        print(f"contraseña introducida = {self.admin_password}")

        session.add(new_user)
        session.commit()
        self.clear_entries()
        return [rx.toast.success(f"Bienvenido {new_user.username}"),
                
                ]
                
        # Limpiar el formulario
        

    def clear_entries(self):
        """Limpiar los campos del formulario."""
        self.username = ""
        self.password = ""
        self.confirm_password = ""
        self.email = ""
        self.confirm_email = ""
        self.date = ""
        self.admin_password = ""
        


class LoginState(rx.State):
    username: str = ""
    password: str = ""
    login_state: bool = False
    user_logged: dict = {}  # Cambiar a un tipo más específico
    admin_logged: dict = {}  # Cambiar a un tipo más específico
    # Si prefieres mantener un dict, puedes especificar su tipo
    user_logged: dict = {
        "username": "",
        "id": 0,
        "email": "",
        "age": 0,
        "creation_date": "",
        "verify": False,
        "avatar": ""  # Asegúrate de que avatar sea siempre una cadena
    }
        

    @rx.event
    def set_avatar(self,avatar : str):
        self.user_logged["avatar"] = avatar  # Asignar el avatar al usuario logueado en el estado

        user= session.query(User).filter_by(username=self.user_logged["username"]).first()  # Buscar el usuario en la base de datos
        if user : 
            user.avatar = avatar
            session.commit()
            session.close()

    @rx.event
    def login(self,user_logged : dict):
        self.user_logged = user_logged  # Asignar el usuario logueado al estado
        """Log in the self.user if the credentials are correct."""
        try: 
            user = session.query(User).filter_by(username=self.username).first()  # Buscar el usuario en la base de datos

            if user:
                # Comparar la contraseña en hexadecimal
                if bcrypt.checkpw(self.password.encode('utf-8'), user.pasw.encode('utf-8')):
                    self.login_state = True  # Usuario autenticado
                    if user.admin == True:
                        self.admin_logged = {
                            "username": user.username, 
                            "id": user.id, 
                            "email": user.email, 
                            "age": user.age,
                            "creation_date": user.creation_date.strftime("%Y-%m-%d %H:%M:%S"),  # Formato de la fecha
                            "verify": user.verify,
                            "avatar": str(user.avatar),
                            "admin": user.admin
                        }
                        return rx.toast.success(f"Bienvenido Admin {user.username}")
                    
                    else:

                        self.user_logged = {
                            "username": user.username, 
                            "id": user.id, 
                            "email": user.email, 
                            "age": user.age, 
                            "creation_date": user.creation_date.strftime("%Y-%m-%d %H:%M:%S"),  # Formato de la fecha
                            "verify": user.verify,
                            "avatar": str(user.avatar)
                        }
                        return rx.toast.success(f"Bienvenido {user.username}")
                else:
                    self.password = ""
                    self.login_state = False  # Contraseña incorrecta
                    return rx.toast.error("Contraseña incorrecta")
            else:
                self.password = ""
                self.username = ""  # Si no encuentra al usuario, vacía el campo de username
                self.login_state = False
                return rx.toast.error("Usuario no encontrado")
        except Exception as e:
            print(f"Error en la consulta a la base de datos: {e}")
            return rx.toast.error("Error de conexión con la base de datos.")
        
    @rx.event
    def log_out(self):
        self.user_logged = {}  # Reiniciar a un diccionario vacío
        self.login_state = False  # Asegurar que el estado de autenticación se actualice
        self.password = ""
