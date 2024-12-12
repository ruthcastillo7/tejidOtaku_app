import reflex as rx
from ..componentes.imag_desc_cli import imag_desc_cli
def tabs_cliente()->rx.Component:
     return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Home", value="tab1",color="#3d1d0b"),
            rx.tabs.trigger("Amigurumis", value="tab2",color="#3d1d0b"),
            rx.tabs.trigger("Prendas", value="tab3",color="#3d1d0b"),
            rx.tabs.trigger("Accesorios", value="tab4",color="#3d1d0b"),
        ),
        rx.tabs.content(
            imag_desc_cli(),
            value="tab1",
        ),
        rx.tabs.content(
            value="tab2",
        ),
        rx.tabs.content(
            value="tab3",
        ),
        rx.tabs.content(
            value="tab4",
        ),
        background="#e8ca61"
     )