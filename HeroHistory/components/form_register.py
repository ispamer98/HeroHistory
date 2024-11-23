import reflex as rx
from HeroHistory.db import db_session as session
from HeroHistory.models import User as User
from HeroHistory.utils.states import LoginState as state
from HeroHistory.utils.states import RegisterState as RegisterState
from HeroHistory.utils.states import RegisterAdminState as RegisterAdminState
from HeroHistory.components.form_imput import form_register_input as finput
def form_register() -> rx.Component:
    return rx.grid(
        rx.box(
            rx.heading("Registro de Usuario", size="lg", mb=4),
            rx.flex(
                rx.card(
                    rx.text("Usuario", align="center", margin_top="1em"),
                    finput(
                        name="username",
                        placeholder="Nombre",
                        size="3",
                        required=True,
                        margin_top="1em",
                        margin_left="1em",
                        margin_right="1em",
                        value=rx.cond(RegisterState.username, RegisterState.username, ""),
                        on_change=RegisterState.set_username,
                        type="username"
                    ),
                    rx.text("Contraseña", align="center", margin_top="1em"),
                    finput(
                        name="password",
                        placeholder="Contraseña",
                        type="password",
                        size="3",
                        required=True,
                        margin_top="1em",
                        margin_left="1em",
                        margin_right="1em",
                        value=rx.cond(RegisterState.password, RegisterState.password, ""),
                        on_change=RegisterState.set_password,
                    ),
                    finput(
                        name="password",
                        placeholder="Confirmar contraseña",
                        type="password",
                        size="3",
                        required=True,
                        margin_top="1em",
                        margin_left="1em",
                        margin_right="1em",
                        value=RegisterState.confirm_password,
                        on_change=RegisterState.set_confirm_password,
                    ),
                    width="50%",
                    margin_left="2em",
                    margin_right="2em",
                    margin_top="2em",
                    margin_bottom="2em",
                    height="400px",
                ),
                rx.card(
                    rx.text("Correo Electronico", align="center", margin_top="1em"),
                    finput(
                        placeholder="Correo electrónico",
                        type="email",
                        size="3",
                        margin_top="1em",
                        margin_left="1em",
                        margin_right="1em",
                        value=RegisterState.email,
                        on_change=RegisterState.set_email,
                        required=True,  # Campo obligatorio
                    ),
                    finput(
                        placeholder="Confirmar correo electrónico",
                        type="email",
                        size="3",
                        margin_top="1em",
                        margin_left="1em",
                        margin_right="1em",
                        value=RegisterState.confirm_email,
                        on_change=RegisterState.set_confirm_email,
                        required=True,  # Campo obligatorio
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.text("Fecha de Nacimiento", 
                                    align="center", 
                                    margin_top="2em",
                                    margin_left="2em",),
                            rx.divider(width="100%",
                            margin_top="2em",
                            ),
                            finput(
                                type="date",
                                size="3",
                                placeholder="Fecha",
                                margin_top="0em",
                                margin_left="1em",
                                margin_right="0.5em",
                                value=RegisterState.date,
                                on_change=RegisterState.set_date,
                                required=True,  # Campo obligatorio
                            ),
                        ),
                        rx.vstack(
                                rx.text("¿Conoces la AdminPasw?", align="center", margin_top="2em",margin_left="1.5em"),
                                rx.vstack(
                                    rx.switch(
                                    checked=RegisterAdminState.switch_value,
                                    on_change=RegisterAdminState.toggle_switch,
                                    label="Activar contraseña admin",
                                    margin_left="5em",
                                    width="150px",
                                ),
                                rx.divider(width="100%"),
                                rx.cond(
                                RegisterAdminState.switch_value,
                                # Si el switch está en True, mostrar el input
                                    rx.box(
                                        finput(
                                        size="3",
                                        margin_top=0,
                                        margin_left="1em",
                                        margin_right="1em",
                                        placeholder="Contraseña admin",
                                        type="password",
                                        value=RegisterState.admin_password,
                                        on_change=RegisterState.set_admin_password,
                                        ),
                                        margin_top=0,
                                        width="100%"
                                    )
                                    
                                )
                            ),
                            margin_left="2em",

                            
                        
                    )
                    
                    ),
                    margin_left="2em",
                    margin_right="2em",
                    margin_top="2em",
                    margin_bottom="2em",
                    width="50%",
                ),
            ),
            rx.button("Registrar", on_click=RegisterState.register, mt=4),
            rx.text(RegisterState.error_message, color="red", mt=4),
            spacing=4,
            border="1px solid #ddd",
            padding=4,
            border_radius="8px",
            box_shadow="lg",
            width="1200px",
        ),
        justify_content="space-between",
        margin_left="4em",

        margin_bottom="2em",
        width="70%",
    )