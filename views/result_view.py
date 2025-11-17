# views/result_view.py
import flet as ft

def result_view(go_back):

    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        controls=[
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        on_click=lambda _: go_back()
                    ),
                    ft.Text("Resultado de la ruta", size=22, weight="bold")
                ]
            ),

            ft.Container(height=20),

            ft.Text("Ruta sugerida:", size=18, weight="bold"),
            ft.Text("Plaza Central → Hospital → Universidad"),

            ft.Container(height=20),

            ft.Text("Distancia total:", size=18, weight="bold"),
            ft.Text("3.8 km"),

            ft.Container(height=20),

            ft.Text("Tiempo estimado:", size=18, weight="bold"),
            ft.Text("12 min (Tráfico moderado)"),

            ft.Container(height=20),

            ft.Text("Flujo de tránsito:", size=18, weight="bold"),
            ft.ProgressBar(value=0.55),

            ft.Container(height=30),

            ft.FilledButton(
                "Finalizar",
                icon=ft.Icons.CHECK,
                width=200,
                on_click=lambda _: go_back()
            )
        ]
    )
