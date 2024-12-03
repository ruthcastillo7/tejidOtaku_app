import reflex as rx
#from .componentes.
@rx.page(route="/homevenvedor")
def home_ven_add()->rx.Component:
    return rx.hstack(
      rx.hstack(
        rx.icon(tag="shopping-cart"),
        rx.heading("TejidOtaku",size="6",weight="bold"),
      ),
      rx.hstack(
        rx.input(
            placeholder="Buscar",
            name="buscar",width="50em",background="#F8F0CD"
            ),
        ),
        rx.button(
          rx.hstack(
            rx.icon(tag="bell-dot"),
            justify="end",
            spacing="5"
          ),background="#A0581D"
        ),
        rx.button(
          rx.hstack(
            rx.icon(tag="user"),
            justify="end",
            spacing="5"
          ),background="#A0581D"
        ),
   
        
      justify="between",
      align_items="center",
      padding="1em",
      width="100%",
      background="#e8ca61"
      )