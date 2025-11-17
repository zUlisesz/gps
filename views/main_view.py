import flet as ft

def main_view(go_results, go_settings):

    title = ft.Text(
        "Planificador de Rutas",
        size=26,
        weight="bold"
    )

    # momentaneamente esto, debería ser el json
    lugares = [
        ft.dropdown.Option("Plaza Central"),
        ft.dropdown.Option("Hospital"),
        ft.dropdown.Option("Universidad"),
        ft.dropdown.Option("Estación Norte")
    ]

    dropdown_origen = ft.Dropdown(
        label="Lugar de salida",
        width=300,
        options=lugares,
    )

    dropdown_destino = ft.Dropdown(
        label="Lugar de llegada",
        width=300,
        options=lugares,
    )

    boton_calcular = ft.FilledButton(
        text="Calcular ruta",
        icon=ft.Icons.DIRECTIONS,
        width=200,
        on_click=lambda _: go_results(None)
    )

    mapa = ft.Container(
        content=ft.Image(
            src="assets/img.jpeg",
            width= 600,
            fit=ft.ImageFit.CONTAIN,
        ),
        expand=True,
        border_radius=10,
        padding=10,
        bgcolor=ft.Colors.GREY_200,
    )

    settings_button = ft.IconButton(
        icon=ft.Icons.SETTINGS,
        tooltip="Configuración",
        on_click=lambda _: go_settings()
    )

    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[title, settings_button]
            ),
            mapa,
            ft.Divider(),
            dropdown_origen,
            dropdown_destino,
            ft.Container(height=10),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[boton_calcular],
            )
        ]
    )
