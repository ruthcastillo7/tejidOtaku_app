import reflex as rx

def navbar()->rx.Component:
    return rx.hstack(
      rx.hstack(
        rx.icon(tag="shopping-cart",color="#3d1d0b"),
        rx.heading("TejidOtaku",size="6",weight="bold",color="#3d1d0b"),
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
          ),background="#A0581D",
          #margin_left="20em"
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