import reflex as rx
from HeroHistory.components.header import header
from HeroHistory.components.navbar import navigation_bar as navbar
from HeroHistory.components.form_register import form_register
from HeroHistory.models import User as User
from HeroHistory.db import db_session as session

@rx.page(route="/register", title="Registro")
def register() -> rx.Component:
    return rx.vstack(
        header(),
        navbar(),
        form_register()
    )