import reflex as rx

def tabs_cliente()->rx.Component:
     return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Home", value="tab1",color="#3d1d0b"),
            rx.tabs.trigger("Amigurumis", value="tab2",color="#3d1d0b"),
            rx.tabs.trigger("Prendas", value="tab3",color="#3d1d0b"),
            rx.tabs.trigger("Accesorios", value="tab4",color="#3d1d0b"),
        ),
        rx.tabs.content(
            rx.text("Home",color="#3d1d0b"),
            value="tab1",
        ),
        rx.tabs.content(
            rx.text("Amigurumis",color="#3d1d0b"),
            value="tab2",
        ),
        rx.tabs.content(
            rx.text("Prendas",color="#3d1d0b"),
            value="tab3",
        ),
        rx.tabs.content(
            rx.text("Accesorios",color="#3d1d0b"),
            value="tab4",
        ),
        background="#e8ca61"
     )