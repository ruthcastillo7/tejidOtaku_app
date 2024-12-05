import reflex as rx
from ..componentes.tabs_vendedor import tabs_vendedor
from ..componentes.navbar import navbar
@rx.page(route="/homevendedor")
def home_ven_add()->rx.Component:
    return rx.vstack(
      navbar(),
      tabs_vendedor(),
      background="#e8ca61",
      weigth="100vw",
      height="100vh"
    )