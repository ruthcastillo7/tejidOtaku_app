import reflex as rx
from ..componentes.tabs_cliente import tabs_cliente
from ..componentes.navbar_cli import navbar_cli
@rx.page(route="/homecliente")
def home_ven_add()->rx.Component:
    return rx.vstack(
      navbar_cli(),
      tabs_cliente(),
      background="#e8ca61",
      weigth="100vw",
      height="100vh"
    )