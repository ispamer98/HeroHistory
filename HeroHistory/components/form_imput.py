import reflex as rx

def form_register_input(
        name="",
        placeholder="",
        size="3",
        required=True,
        margin_top="1em",
        margin_left="1em",
        margin_right="1em",
        margin_bottom="1em",
        value="",
        on_change=None,
        type="text",
        border=None,
        border_radius=None
    ) -> rx.Component:
    
    return rx.input(
        name=name,
        placeholder=placeholder,
        size=size,
        required=required,
        border=border,
        border_radius=border_radius,
        margin_left=margin_left,
        margin_top=margin_top,
        margin_bottom=margin_bottom,
        margin_right=margin_right,
        value=value,
        on_change=on_change,
        type=type)