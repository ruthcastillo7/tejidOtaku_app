import reflex as rx

@rx.page(route="/cliente")
def cliente()->rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Ingrese correo",
                    name="ingrese_correo",
                ),
                rx.input(
                    placeholder="Ingrese contraseña",
                    name="ingrese_contraseña",
                ),
                rx.button("CONTINUAR", type="continuar")
            ),
        ),
    align="center",
    justify="center",
    background="#f3e5ab",
    height="100vh"
    )