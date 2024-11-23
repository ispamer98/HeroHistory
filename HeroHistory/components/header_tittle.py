import reflex as rx


def header_tittle() -> rx.Component:
    return rx.image(src="/image.png",
                    width="20em",
                    height="10em",
                    margin_left="1em",
                    min_width=["auto","250px"],
                    flex_shrink=0,
            )