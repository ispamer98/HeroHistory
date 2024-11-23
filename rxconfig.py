#rxconfig.py

import reflex as rx

config = rx.Config(
    app_name="HeroHistory",
    icon="/favicon.ico",
      # Usa el puerto correcto si lo estás personalizando.
    api_url="http://localhost:8000",
    cors_allow_origins=["https://herohistory.reflex.run",
                        "local://localhost:3000"],
)

