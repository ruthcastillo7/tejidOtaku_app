import reflex as rx

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
            )
        )
    )