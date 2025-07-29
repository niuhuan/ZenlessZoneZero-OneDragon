import flet as ft

from home import Home
from og import OG
from settings import Settings

home = Home()
og = OG()
settings = Settings()

class App(ft.Container):
    def __init__(self, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        
        # 创建页面列表
        self.pages = [home, og, settings]
        self.current_page_index = 0
        
        # 创建导航栏
        self.nav = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=80,
            min_extended_width=80,
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME,
                    label="仪表盘",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.BOOKMARK_BORDER,
                    selected_icon=ft.Icons.BOOKMARK,
                    label="游戏",
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                    selected_icon=ft.Icons.SETTINGS,
                    label="设置",
                ),
            ],
            on_change=self.nav_change,
        )
        
        # 创建主内容区域
        self.main_content = ft.Container(
            content=self.pages[0],
            expand=True,
        )
        
        self.content = ft.Row(
            [
                self.nav,
                ft.VerticalDivider(width=1, thickness=1),
                self.main_content,
            ],
            expand=True,
        )
        self.expand = True
        self.page.update()
    
    def nav_change(self, e):
        # 获取选中的页面索引
        self.current_page_index = e.control.selected_index
        
        # 更新主内容区域
        self.main_content.content = self.pages[self.current_page_index]
        
        # 更新页面
        self.page.update()


def main(page: ft.Page):
    page.title = "ZZZOD"
    page.add(
        App(
            page=page
        )
    )


ft.app(main)
