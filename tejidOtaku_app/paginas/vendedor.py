import reflex as rx

@rx.page(route="/vendedor")
def vendedor()->rx.Component:
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
                rx.input(
                    placeholder="Ingrese nombre del negocio",
                    name="ingrese_nombre_del_negocio",
                ),
                rx.input(
                    placeholder="Ingrese sus medios de pago",
                    name="ingrese_sus_medios_de_pago",
                ),
                rx.button("CONTINUAR", type="continuar")
            ),
        ),
    align="center",
    justify="center",
    background="#f3e5ab",
    height="100vh"
    )