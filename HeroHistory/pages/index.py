#index.py

import reflex as rx
from HeroHistory.components.header import header as header
from HeroHistory.components.navbar import navigation_bar as navbar

@rx.page(route="/", title="Hero History")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        header(),
        navbar(),
    )