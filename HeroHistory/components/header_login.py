#header_login.py



import reflex as rx
from HeroHistory.db import db_session as session
from HeroHistory.models import User as User
from HeroHistory.utils.states import LoginState as state
from HeroHistory.components.user_menu import user_menu
from HeroHistory.utils.get_avatars import get_avatars




def header_login() -> rx.Component:
    avatars=get_avatars()
    return rx.center(  # Centra el formulario dentro de la página
        rx.vstack(  # Usamos un solo vstack
            rx.cond(
                state.login_state,  # Si el usuario está autenticado
                rx.vstack(  # Mostrar avatar y botón de cerrar sesión
                    rx.hstack(
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.button(
                                    rx.image(
                                        rx.cond(
                                            state.admin_logged, 
                                            state.admin_logged["avatar"],
                                            state.admin_logged["avatar"],
                                        ),
                                        width="100%",
                                        height="100%",
                                    ),
                                    height="50px",  # Altura fija del botón
                                    width="50px",  # Ancho fijo del botón (debe coincidir con la altura para ser circular)
                                    border_radius="50%",  # Bordes redondeados al máximo (círculo perfecto)
                                    background="transparent",  # Sin fondo
                                    _hover={
                                        "border": "3px solid gray",  # Borde gris al pasar el ratón
                                    },
                                    padding="0",  # Sin relleno extra
                                    box_shadow="none",  # Sin sombra adicional
                                )
                            ),
                            rx.popover.content(
                                rx.inset(
                                    rx.flex(
                                        rx.foreach(
                                            avatars,
                                            lambda avatar: rx.image(
                                                src=avatar,  # Ruta de la imagen del avatar
                                                width="50px",
                                                height="50px",
                                                border_radius="50%",
                                                cursor="pointer",
                                                _hover={"border": "2px solid blue"},
                                                on_click=lambda avatar=avatar : state.set_avatar(avatar),  # Cambia el avatar
                                                    
                                            ),
                                        ),
                                        spacing="1em",
                                        flex_wrap="wrap",
                                        width="100%",
                                    )
                                )
                            ),
                        ),
                        rx.text(state.user_logged["username"]),
                        align="center",
                        justify="center",
                        
                    ),
                    
                    rx.hstack(
                            rx.text(
                                "Cerrar Sesión",
                                border_top="1px solid gray",  # Separador arriba
                                border_bottom="1px solid gray",  # Separador abajo
                                padding="0.5em",  # Espaciado alrededor del texto
                                on_click=state.log_out,  # Llama al evento log_out para cerrar sesión
                                cursor="pointer",  # Hacer que el texto sea clickeable

                            
                            ),
                            rx.spacer(
                                        "|",
                                      color="solid gray",
                                      margin_top="0.5em",
                                      ),

                            user_menu(),

                    ),
                    
                    
                    
                ),
                #Segunda condicion 
                rx.form(  # Utilizamos un formulario en lugar de un vstack para manejar el on_submit
                    rx.vstack(  # Mostrar formulario de login si no está autenticado
                        rx.text("Usuario", align="center", margin_top="1em"),
                        rx.input(
                            name="username",
                            placeholder="Nombre",
                            size="5",
                            required=True,
                            margin_top="1em",
                            margin_left="1em",
                            margin_right="1em",
                            value=rx.cond(state.username, state.username,""),
                            on_change=state.set_username,
                        ),
                        rx.text("Contraseña", align="center", margin_top="1em"),
                        rx.input(
                            name="password",
                            placeholder="Contraseña",
                            type="password",
                            size="5",
                            required=True,
                            margin_top="1em",
                            margin_left="1em",
                            margin_right="1em",
                            value=rx.cond(state.password, state.password,""),
                            on_change=state.set_password,
                        ),
                        rx.vstack(  # Hstack para envolver el botón
                            rx.button(
                                "Acceder",
                                type="submit",
                                bg="transparent",  # Color de fondo del botón
                                border_top="1px solid gray",  # Separador arriba
                                border_bottom="1px solid gray",  # Separador abajo
                                padding="0.5em",  # Espaciado alrededor del texto
                                border_radius="5px",  # Bordes redondeados al máximo (círculo perfecto)
                                _hover={"bg": "grey",
                                        "opacity": "0.9"},  # Borde azul al pasar el ratón
                                margin_left="5em",
                                margin_rigth="5em",  # Espacio a la izquierda del botón
                                align="center",  # Centrado horizontalmente
                                weight="2.5em",  # Tamaño inicial
                                height="2.5em",
                                
                            ),
                            rx.link(
                                rx.tooltip(
                                    rx.button("¿No tienes cuenta?",
                                            bg="transparent",  # Color de fondo del botón
                                                border_top="1px solid gray",  # Separador arriba
                                                border_bottom="1px solid gray",  # Separador abajo
                                                padding="0.5em",  # Espaciado alrededor del texto
                                                border_radius="5px",  # Bordes redondeados al máximo (círculo perfecto)
                                                _hover={"bg": "grey",
                                                        "opacity": "0.9"},  # Borde azul al pasar el ratón
                                                margin_left="2.5em",
                                                margin_rigth="5em",  # Espacio a la izquierda del botón
                                                align="center",  # Centrado horizontalmente
                                                weight="2.5em",  # Tamaño inicial
                                                height="2.5em",
                                            ),
                                            content="Regístrate aquí",
                                            side="bottom",
                                            delay_duration=5,
                                            bg="grey",

                                          ),
                
                                href="/register",
                                
                                
                            )
                        ),
                        

                    ),
                    
                    on_submit=state.login,  # Llama al método login directamente al enviar el formulario
                ),
            ),
            margin_top="1em",
            margin_right="1em",
            width="15em",
            height=rx.cond(state.login_state,
                           "10em",
                           "20em"),
            padding="1em",
            justify_content="center",  # Centrado vertical y horizontal
            align_items="center",  # Alineación de los elementos hijos en el contenedor
            style={
                "backgroundImage": "url('/card_background.png')",
                "backgroundSize": "cover",
                "backgroundPosition": "center",
                "opacity": "0.9",
                "border": "4px solid #0A122A",
                "borderRadius": "10px",
                "boxShadow": "0 10px 10px rgba(0.1, 0.1, 1, 0.7)",
            },
        ),
    )
