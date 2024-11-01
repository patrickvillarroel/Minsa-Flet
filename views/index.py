import flet as ft

from util import RolesEnum


def button_click(rol: RolesEnum):
    # TODO enviar a otra pagina
    pass


def view(page: ft.Page):
    page.window.min_width = 400
    page.window.min_height = 510
    page.scroll = None
    return ft.View(
        route="/",
        bgcolor=ft.colors.TRANSPARENT,
        controls=[
            ft.SafeArea(
                adaptive=True,
                expand=True,
                content=ft.Container(
                    image=ft.DecorationImage(
                        src="/images/fondo2.jpg",
                        fit=ft.ImageFit.COVER,
                    ),
                    bgcolor=ft.colors.TRANSPARENT,
                    expand=True,
                    margin=-10,
                    alignment=ft.alignment.center,
                    content=ft.Container(
                        bgcolor=ft.colors.WHITE,
                        height=500,
                        width=400,
                        border_radius=20,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "VACUNAS APP", color="black", size=35, weight=ft.FontWeight.BOLD
                                ),
                                ft.Image(src="/images/logo.png", width=150, height=150),
                                ft.ElevatedButton(
                                    text="Paciente",
                                    on_click=lambda e: button_click(RolesEnum.Roles.PACIENTE),
                                    width=220,
                                    height=40,
                                    style=ft.ButtonStyle(
                                        bgcolor={"": ft.colors.GREEN, "hovered": ft.colors.GREEN_600},
                                        color={"": ft.colors.WHITE, "hovered": ft.colors.WHITE70},
                                        shape=ft.RoundedRectangleBorder(radius=40),
                                        elevation={"": 2, "hovered": 6},
                                        text_style=ft.TextStyle(size=25)
                                    ),
                                    icon=ft.icons.PERSON,
                                ),
                                ft.ElevatedButton(
                                    text="Doctor",
                                    on_click=lambda e: button_click(RolesEnum.Roles.DOCTOR),
                                    width=220,
                                    height=40,
                                    style=ft.ButtonStyle(
                                        bgcolor={"": ft.colors.BLUE_ACCENT, "hovered": ft.colors.BLUE},
                                        color={"": ft.colors.WHITE, "hovered": ft.colors.WHITE70},
                                        shape=ft.RoundedRectangleBorder(radius=40),
                                        elevation={"": 2, "hovered": 6},
                                        text_style=ft.TextStyle(size=20)
                                    ),
                                    icon=ft.icons.LOCAL_HOSPITAL,
                                ),
                                ft.ElevatedButton(
                                    text="Admin",
                                    width=220,
                                    height=40,
                                    style=ft.ButtonStyle(
                                        bgcolor={"": ft.colors.GREEN, "hovered": ft.colors.GREY},
                                        color={"": ft.colors.WHITE, "hovered": ft.colors.WHITE70},
                                        shape=ft.RoundedRectangleBorder(radius=40),
                                        elevation={"": 2, "hovered": 6},
                                        text_style=ft.TextStyle(size=25)
                                    ),
                                    icon=ft.icons.ADMIN_PANEL_SETTINGS
                                ),
                                ft.ElevatedButton(
                                    text="Proveedor",
                                    width=220,
                                    height=40,
                                    style=ft.ButtonStyle(
                                        bgcolor={"": ft.colors.BLUE_ACCENT, "hovered": ft.colors.GREY},
                                        color={"": ft.colors.WHITE, "hovered": ft.colors.WHITE70},
                                        shape=ft.RoundedRectangleBorder(radius=40),
                                        elevation={"": 2, "hovered": 6},
                                        text_style=ft.TextStyle(size=25)
                                    ),
                                    icon=ft.icons.SHOP,
                                ),
                                ft.ElevatedButton(
                                    text="Autoridad",
                                    width=220,
                                    height=40,
                                    style=ft.ButtonStyle(
                                        bgcolor={"": ft.colors.GREEN, "hovered": ft.colors.GREY},
                                        color={"": ft.colors.WHITE, "hovered": ft.colors.WHITE70},
                                        shape=ft.RoundedRectangleBorder(radius=40),
                                        elevation={"": 2, "hovered": 6},
                                        text_style=ft.TextStyle(size=25)
                                    ),
                                    icon=ft.icons.SECURITY
                                ),

                            ],
                        ),
                    ),
                ),
            )
        ])