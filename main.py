import flet as ft


def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()


    new_task = ft.TextField(hint_text="O que precisa ser feito?")
    page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked))
    page.add(ft.Checkbox(label="Teste"))
    page.add(ft.TextButton(text='ok'))

ft.app(target=main)