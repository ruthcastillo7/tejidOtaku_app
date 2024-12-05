import reflex as rx

def tabs_vendedor()->rx.Component:
     return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Tab 1", value="tab1"),
            rx.tabs.trigger("Tab 2", value="tab2"),
        ),
        rx.tabs.content(
            rx.text("item on tab 1"),
            value="tab1",
        ),
        rx.tabs.content(
            rx.text("item on tab 2"),
            value="tab2",
        ),
     )