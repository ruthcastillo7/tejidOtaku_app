import reflex as rx

def imag_desc_cli()->rx.Component:
    return rx.vstack(
        rx.card(
            rx.inset(
                rx.box(rx.image(
                    src="/reflex_banner.png",
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
                    "Amigurumi de Luffy de 15 cm de altura",color="#3d1d0b"
                    ),
            width="10vw",
        )
#         rx.card(
#             rx.link(
#                 rx.flex(
#                     rx.avatar(src="/https://images4-f.ravelrycache.com/uploads/eirehscrochet/854412995/Untitled_design__3__small2.png"),
#                     rx.box(
#                         rx.heading("LUFFY",color="#3d1d0b"),
#                         rx.text(
#                     "Amigurumi de Luffy de 15 cm de altura",color="#3d1d0b"
#                     ),
#                 ),
#             spacing="2",
#         ),
#     ),
#     as_child=True,
# )
),
)