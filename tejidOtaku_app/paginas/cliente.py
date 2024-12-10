import reflex as rx

@rx.page(route="/cliente")
def cliente()->rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Ingrese correo",
                    name="ingrese_correo",width="17%"
                ),
                rx.input(
                    placeholder="Ingrese contraseña",
                    name="ingrese_contraseña",width="17%"
                ),
                rx.button("CONTINUAR", type="continuar",width="17%",background="#A0581D",on_click=rx.redirect("/homecliente")),
            ),
            margin_left="34em",
        ),
    align="center",
    justify="center",
    background="#f3e5ab",
    height="100vh"
    )