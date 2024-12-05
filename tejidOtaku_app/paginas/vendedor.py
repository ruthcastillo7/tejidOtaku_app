import reflex as rx


@rx.page(route="/vendedor")
def vendedor()->rx.Component:
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
                rx.input(
                    placeholder="Ingrese nombre del negocio",
                    name="ingrese_nombre_del_negocio",width="17%"
                ),
                rx.input(
                    placeholder="Ingrese sus medios de pago",
                    name="ingrese_sus_medios_de_pago",width="17%"
                ),
                rx.button("CONTINUAR", type="continuar",width="17%",background="#A0581D",on_click=rx.redirect("/homevendedor")),
            ),
            margin_left="34em",
        ),
    justify="center",
    background="#f3e5ab",
    height="100vh",
    width="100vw"
    )