import os
from turtle import color
import flet as ft

from one_dragon.utils import os_utils

class Home(ft.Container):

    def __init__(self): 
        super().__init__()
        # 设置容器的内容
        self.content = self.build()
        # 设置容器填充整个可用空间
        self.expand = True
    
    def before_update(self):
        pass

    def build(self):
        index_banner_path = os.path.join(os_utils.get_path_under_work_dir('assets', 'ui'), 'index.png')
        
        # 启动按钮
        launch_button = ft.Container(
            content=ft.Text("🚀 启动一条龙", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
            alignment=ft.alignment.center,
            padding=ft.padding.all(15),
            bgcolor=ft.Colors.YELLOW_600,
            border_radius=ft.border_radius.all(25),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.BLACK26,
            ),
            # 设置按钮的固定宽度，防止扩展到容器大小
            width=200,
            height=50,
        )
        
        # 主内容区域
        main_content = ft.Column(
            spacing=10,
            controls=[
            ],
        )
        
        # 使用Stack来叠加背景图和内容
        return ft.Stack(
            controls=[
                # 背景图
                ft.Container(
                    content=ft.Image(
                        src=index_banner_path,
                        fit=ft.ImageFit.COVER,
                        expand=True,
                    ),
                    expand=True,
                    border_radius=ft.border_radius.all(20),
                ),
                # 主内容
                ft.Container(
                    content=main_content,
                    padding=ft.padding.all(20),
                    expand=True,
                ),
                # 右下角启动按钮
                ft.Container(
                    content=launch_button,
                    alignment=ft.alignment.bottom_right,
                    padding=ft.padding.only(bottom=30, right=20),
                    expand=True,
                ),
            ],
        )
