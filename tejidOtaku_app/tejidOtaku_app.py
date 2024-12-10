import reflex as rx
from .paginas.vendedor import vendedor
from .paginas.cliente import cliente
from .paginas.home_ven_add import home_ven_add
from .paginas.home_clien_add import home_clien_add

def index()->rx.Component:
  return rx.flex(
      rx.hstack(
        rx.vstack(
            rx.link(
              rx.card(
                rx.icon(tag="store",color="#3d1d0b"),
                size="5"
              ),
              href="/vendedor" ,
            ),
            rx.heading("Vendedor",color="#3d1d0b"),      
        ),
        rx.vstack(
           rx.link(
             rx.card(
               rx.icon(tag="shopping-cart",color="#3d1d0b"),
               size="5"
             ),
             href="/cliente" ,
           ),
           rx.heading("Cliente",color="#3d1d0b"),    
        ),
      ),
    align="center",
    justify="center",
    background="#f3e5ab",
    height="100vh"
  )
  
  
app=rx.App()
app.add_page(index)