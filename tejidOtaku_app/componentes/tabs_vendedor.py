import reflex as rx

def tabs_vendedor()->rx.Component:
     return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Home", value="tab1",color="#3d1d0b"),
            rx.tabs.trigger("Actualizar descripción", value="tab2",color="#3d1d0b"),
            rx.tabs.trigger("Ordenar / tipo de tejido", value="tab3",color="#3d1d0b"),
            rx.tabs.trigger("Actualizar medios de pago", value="tab4",color="#3d1d0b"),
        ),
        rx.tabs.content(
            rx.text("Home",color="#3d1d0b"),
            value="tab1",
        ),
        rx.tabs.content(
            rx.text("Actualizar descripción",color="#3d1d0b"),
            value="tab2",
        ),
        rx.tabs.content(
            rx.text("Ordenar / tipo de tejido",color="#3d1d0b"),
            value="tab3",
        ),
        rx.tabs.content(
            rx.text("Actualizar medios de pago",color="#3d1d0b"),
            value="tab4",
        ),
        background="#e8ca61"
     )