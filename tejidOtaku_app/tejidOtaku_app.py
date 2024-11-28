import reflex as rx


def index()->rx.Component:
  return rx.flex(
      rx.hstack(
        rx.vstack(
            rx.button(rx.image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSI3bgaDUpDBqs8nB8tKdfTQEPVTMIgJ0T7mQ&s"),size="5"),
            rx.heading("Vendedor"),      
        ),
         rx.vstack(
            rx.button(rx.image(src="https://img.freepik.com/vector-premium/ilustracion-dibujos-animados-lindo-chica-compras_274619-1042.jpg"),size="5"),
            rx.heading("Cliente"),      
        ),
      ),
    align="center",
    justify="center"
  )
app=rx.App()
app.add_page(index)