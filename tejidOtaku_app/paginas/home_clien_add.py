import reflex as rx
from ..componentes.tabs_cliente import tabs_cliente
from ..componentes.navbar_cli import navbar_cli
from ..componentes.imag_desc_cli import imag_desc_cli
@rx.page(route="/homecliente")
def home_clien_add()->rx.Component:
    return rx.vstack(
      navbar_cli(),
      tabs_cliente(),
      #imag_desc_cli(),
      background="#e8ca61",
      weigth="100vw",
      height="100vh"
    )