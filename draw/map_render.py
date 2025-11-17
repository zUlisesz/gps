import flet as ft

class MapRenderer:
    def __init__(
        self,
        map_image_path: str,
        nodes: dict,
        map_width: int = 600,
        map_height: int = 600,
    ):
        #nodos debe estar en el formato del diccionario del grafo

        self.map_image_path = map_image_path
        self.nodes = nodes
        self.map_width = map_width
        self.map_height = map_height

    def draw_route(self, route, route_color="#005CC5", node_color="red", show_labels=True):
        #route es la lista de nodos ["A", "B", "D"]
        

        canvas_shapes = []

        # Dibujar la línea de la ruta
        for i in range(len(route) - 1):
            n1 = self.nodes[route[i]]
            n2 = self.nodes[route[i + 1]]

            canvas_shapes.append(
                ft.canvas.Line(
                    n1["x"],
                    n1["y"],
                    n2["x"],
                    n2["y"],
                    paint=ft.Paint(
                        stroke_width=4,
                        color=route_color,
                        style=ft.PaintingStyle.STROKE,
                    ),
                )
            )

        # solo dibuja los nodos
        for node in route:
            n = self.nodes[node]

            # dibuja un punto como en java y el draw
            canvas_shapes.append(
                ft.canvas.Circle(
                    n["x"],
                    n["y"],
                    6,
                    paint=ft.Paint(
                        color=node_color,
                        style=ft.PaintingStyle.FILL,
                    )
                )
            )

            # asignala los labels
            if show_labels:
                canvas_shapes.append(
                    ft.canvas.Text(
                        n["x"] + 8,
                        n["y"] - 8,
                        node,
                        ft.TextStyle(size=14, color="black"),
                    )
                )

        # pegar los mapas,


        ###esto puedo que no funcione del todo
        return ft.Stack(
            [
                ft.Image(
                    src=self.map_image_path,
                    width=self.map_width,
                    height=self.map_height,
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Canvas(
                    shapes=canvas_shapes,
                    width=self.map_width,
                    height=self.map_height,
                )
            ],
            width=self.map_width,
            height=self.map_height,
        )
