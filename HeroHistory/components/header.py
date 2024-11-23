import reflex as rx
from HeroHistory.components.header_tittle import header_tittle
from HeroHistory.components.header_login import header_login
from HeroHistory.utils.states import LoginState as state

def header() -> rx.Component:
    # Hacer que el contenido de header_login no altere los márgenes
    return rx.hstack(  # Contenedor principal de todo el header
        rx.box(  # Mantener header_tittle en su posición
            header_tittle(),
            margin_left=["0em", "25%"],  # Sin margen en pantallas pequeñas, 25% en pantallas grandes
            margin_top="3em",  # Ajuste para adaptarse mejor en pantallas grandes
        ),
        rx.box(  # En lugar de usar cond aquí, mantenemos un solo box para header_login
            header_login(),  # Mantener header_login y dejar que solo cambie su contenido
            margin_top="0em",  # Ajuste del margen en el box
            width="auto",  # Dejar que el ancho se ajuste dinámicamente
            padding="0.5em",  # Mantener un padding constante para que no cambien de tamaño de forma brusca
        ),
        justify_content="space-between",  # Centrado en móviles, espacio entre elementos en pantallas grandes
        flex_direction=["column", "row"],  # En móviles se apila, en pantallas grandes se coloca en fila
        width="100%",  # Ancho completo
        padding="1em",  # Espaciado global
        gap="1em",  # Espaciado entre elementos
        height="20em"
    )
