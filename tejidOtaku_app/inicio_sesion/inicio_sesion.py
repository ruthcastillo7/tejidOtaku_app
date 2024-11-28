import reflex as rx
def index()->rx.Component:
  return rx.flex(
#      rx.hstack(
      rx.button("Iniciar sesion", disabled=True),
      rx.button("Registrarse", disabled=True),
      spacing="2"
#      ),
#    align="center"
  )
# app=rx.App()
# app.add_page(index)