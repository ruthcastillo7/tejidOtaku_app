import reflex as rx

def imag_desc_ven()->rx.Component:
    return rx.hstack(
        rx.card(
            rx.button(
                rx.hstack(
                rx.icon(tag="plus"),
                justify="end",
                spacing="5",
                
                ),background="#A0581D",
                size="4"
            ),
        ),
        
        rx.card(
            rx.inset(
                rx.box(rx.image(
                    src="/https://images4-f.ravelrycache.com/uploads/eirehscrochet/854412995/Untitled_design__3__small2.png",
                    width="100%",
                    height="auto",
                )
                ),
                side="top",
                pb="current",
            ),
            rx.box(
                rx.heading("LUFFY",size="2",color="#3d1d0b"),
                rx.text(
                    "S/. 40 - Amigurumi de 15 cm de altura",size="2",color="#3d1d0b"
                    ),
            width="10vw",
        ),
            size="1"
        ),
    )