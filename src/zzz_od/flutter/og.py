import flet as ft

class OG(ft.Container):

    def __init__(self): 
        super().__init__()
        # 设置容器的内容
        self.content = self.build()
        # 设置容器填充整个可用空间
        self.expand = True
    
    def before_update(self):
        pass

    def build(self):
        return ft.Column(
            spacing=10,
            controls= [
                ft.Text("游戏页面", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(
                    content=ft.Text(value="OG Content 1"),
                    alignment=ft.alignment.center,
                    width=200,
                    height=60,
                    bgcolor=ft.Colors.BLUE_100,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Container(
                    content=ft.Text(value="OG Content 2"),
                    alignment=ft.alignment.center,
                    width=200,
                    height=60,
                    bgcolor=ft.Colors.GREEN_100,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Container(
                    content=ft.Text(value="OG Content 3"),
                    alignment=ft.alignment.center,
                    width=200,
                    height=60,
                    bgcolor=ft.Colors.PURPLE_100,
                    border_radius=ft.border_radius.all(10),
                ),
            ],
        )
