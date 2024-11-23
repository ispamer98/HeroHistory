import reflex as rx
import os
def get_avatars():
    
    
    """Devuelve una lista de rutas de imágenes que comiencen con 'avatar'."""
    avatar_path = os.path.join(os.path.dirname(__file__), "../../assets")  # Ajusta la ruta según la estructura
    avatar_path = os.path.abspath(avatar_path)  # Convierte a una ruta absoluta
    avatar_list= [
        f"/{file}"
        for file in os.listdir(avatar_path)
        if file.startswith("avatar")
    ]
    return avatar_list
