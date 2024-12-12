import reflex as rx
from ..componentes.imag_desc_ven import imag_desc_ven
def tabs_vendedor()->rx.Component:
     return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Home", value="tab1",color="#3d1d0b"),
            rx.tabs.trigger("Actualizar descripción", value="tab2",color="#3d1d0b"),
            rx.tabs.trigger("Ordenar / tipo de tejido", value="tab3",color="#3d1d0b"),
            rx.tabs.trigger("Actualizar medios de pago", value="tab4",color="#3d1d0b"),
        ),
        rx.tabs.content(
            imag_desc_ven(),
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