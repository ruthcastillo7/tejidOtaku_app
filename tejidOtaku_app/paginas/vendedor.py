import reflex as rx

@rx.page(route="/vendedor")
def vendedor()->rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Ingrese correo",
                ),
                
            )
        )
    )