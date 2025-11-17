import flet as ft

def settings_view(go_back):

    return ft.Column(
        spacing=20,
        controls=[
            ft.Text("Configuración", size=26, weight="bold"),

            ft.Switch(label="Modo Oscuro"),

            ft.ElevatedButton(
                "Volver",
                icon=ft.Icons.ARROW_BACK,
                on_click=lambda _: go_back()
            )
        ]
    )
