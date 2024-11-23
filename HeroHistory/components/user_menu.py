import reflex as rx
from HeroHistory.utils.states import User_menuState as menu_state


def user_menu() -> rx.Component:
    return rx.drawer.root(
        # Botón que abre el menú
        rx.drawer.trigger(
            rx.text(
                "Menu",  # Texto del "botón"
                border_top="1px solid gray",  # Separador arriba
                border_bottom="1px solid gray",  # Separador abajo
                padding="0.5em",  # Espaciado alrededor del texto
                on_click=menu_state.toggle_menu,  # Evento para alternar el menú
                cursor="pointer",  # Hacer que el texto sea clickeable
            )
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.drawer.close(
                        rx.box(
                            rx.button(
                                rx.image(
                                    "/close2.png",
                                    weight="4em",  # Tamaño inicial
                                    height="4em",  # Tamaño inicial
                                    margin_top="3em",
                                    margin_rigth="3em", 
                                    on_click=menu_state.toggle_menu, 
                                    object_fit="contain",
                                    _hover={  # Estilo cuando el ratón pase por encima
                                        "padding": "0.5em",
                                        
                                    },
                                ),
                                background="transparent",  # Sin fondo
                                border="none",  # Sin bordes
                                padding="0",  # Sin padding
                                box_shadow="none",  # Sin sombra
                            ),
                            justify_content="rigth",
                            weight="100%",
                            
                        ),
                    ),
                    rx.vstack(
                        rx.spacer(margin_top="4em"),
                        rx.link(
                            "Personajes",
                            href="/characters",
                            on_click=menu_state.toggle_menu,
                            color="gray.300",
                            padding="0.5em",
                            width="100%",
                            text_align="center",
                            border_bottom="1px solid gray",
                        ),
                        rx.link(
                            "Gestionar Cuenta",
                            href="/user_dashboard",
                            on_click=menu_state.toggle_menu,
                            color="gray.300",
                            padding="0.5em",
                            width="100%",
                            text_align="center",
                            border_bottom="1px solid gray",
                        ),

                        margin_left="4em",
                    ),
                    weight="100%",
                ),
                height="100%",
                width="15em",
                background_image="url(/menu_background.png)",  # Ruta de tu imagen
                background_size="cover",
                background_position="center",
                background_opacity=0.7,
                justify_content="center",
                place="right",
                position="fixed",  # Fija el menú
                right="0",  # Lo coloca en la parte derecha de la pantalla
                top="0",  # Lo coloca en la parte superior de la pantalla
                border_right="3px solid #333333",  
                border_radius="0 4em 4em 0",  # Solo borde redondeado en el lado derecho
            ),
        ),
        direction="left",  # Cambié de 'left' a 'right'
        side="rigth", #
    )
