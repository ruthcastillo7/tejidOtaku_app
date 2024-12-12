import reflex as rx

def imag_desc_cli()->rx.Component:
    return rx.vstack(
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
                rx.heading("LUFFY",color="#3d1d0b"),
                rx.text(
                    "S/. 40 - Amigurumi de 15 cm de altura",color="#3d1d0b"
                    ),
            width="10vw",
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
                rx.heading("GOKU",color="#3d1d0b"),
                rx.text(
                    "S/. 45 - Amigurumi de 15 cm de altura",color="#3d1d0b"
                    ),
            width="10vw",
        ),
),
)