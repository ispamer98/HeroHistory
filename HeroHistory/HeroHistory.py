#HeroHistory.py

import reflex as rx
from rxconfig import config
from HeroHistory.pages.register import register
from HeroHistory.pages.index import index as index
from .views.background_style import BACKGROUND_STYLE
from .db import first_start as first_start

app = rx.App(
        style=BACKGROUND_STYLE
        )

first_start()
