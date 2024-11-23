import reflex as rx
from HeroHistory.utils.states import LoginState as state

def navigation_bar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.button(
                "Home",
            ),
            href="/",
        ),
        rx.button(
            "About",
        ),
        rx.link(
        rx.button(
            "Prueba"),
            on_click=state.log_out
        ),
        width="70%",             # Haz que el contenedor cubra todo el ancho disponible
        height="4em",             # Ajusta la altura del contenedor
        padding="1em",            # Añade espacio interno
        margin_left= "4em",          # Centra el hstack horizontalmente
        margin_top= "0em",
        bg="rgba(255, 255, 255, 0.7)",  # Fondo blanco con opacidad
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",  # Sombra para dar profundidad
        align_items="center",     # Centra los botones verticalmente
        justify_content="space-around",  # Espacia los botones uniformemente
        border_radius="10px",  # Redondea las esquinas
        border="3px solid rgba(0, 0, 0, 0.2)",  # Borde azulado
    )