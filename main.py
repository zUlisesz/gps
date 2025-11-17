import flet as ft

from views.main_view import main_view
from views.result_view import result_view
from views.settings_view import settings_view


def main(page: ft.Page):
    page.title = "Ruta Inteligente"
    page.theme_mode = "dark"
    page.window_width = 950
    page.window_height = 550

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    controls=[main_view(
                        go_results=lambda data: page.go("/result"),
                        go_settings=lambda: page.go("/settings")
                    )],
                    can_pop=False,
                )
            )

        elif page.route == "/result":
            page.views.append(
                ft.View(
                    route="/result",
                    controls=[result_view(
                        go_back=lambda: page.go("/")
                    )]
                )
            )

        elif page.route == "/settings":
            page.views.append(
                ft.View(
                    route="/settings",
                    controls=[settings_view(
                        go_back=lambda: page.go("/")
                    )]
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


ft.app(target=main)
