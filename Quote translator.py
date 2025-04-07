import flet as ft

def main(page: ft.Page):
    page.title = "I agree but pear pizza is worse"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "adaptative" 


    og = "なんてこった、ゼリーだんごは恐ろしい。"
    sauce = "Fujiwara no Mokou from Touhou 8 Imperishable night which you should totally try today-"
    trans = {
        "J (original)": og,
        "EN": "God, Jelly donuts are so scary.",
        "ES": "Dios, Las donas rellenas de gelatina son tan aterradoras.",
        "D": "el diablo manito aleja eso donu relleno de mi cara eso e del diablo muchachoeldiablomfmfmfmfmffmmfmf *empieza a rapear*",
        "B": 'Oh, good heavens, Thy doughnuts, filled to the brim with mermelade jelly are horrifying. *takes a sip of tea*',
        "JU": "what am I doing here"
    }

    dizplay = ft.Text(
        og,
        size=20,
        weight=ft.FontWeight.W_500,
        selectable=True
    )
    
    radio_thing = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="J", label="japanEZ"),
            ft.Radio(value="EN", label="englICH"),
            ft.Radio(value="ES", label="Espa;ol I mean español"),
            ft.Radio(value="D", label="Dominicano (what)"),
            ft.Radio(value="B", label="british"),
            ft.Radio(value="JU", label= "Junko from touhou 15 which you should NOT pla")
        ]),
        value="J",
        on_change=lambda e: update(e.control.value)
    )
    
    def update(lang):
        dizplay.value = trans[lang]
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("Hello how are you :)", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Yo so like do whatev u want idk I'm too busy dying I mean sleepin rn lol", size=12, weight=ft.FontWeight.BOLD),
                ft.Divider(height=10), #btw teach these are hella cool I found bout em here https://flet.dev/docs/controls/divider/
                ft.Image(              #idk how I didn't knew about these before they're so cool!!!!
                    src="https://i.imgur.com/nQHR4cQ.png", 
                    width=150,
                    height=150,
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Text(sauce, italic=True),
                ft.Divider(height=20),
                ft.Container(
                    content=dizplay,
                    padding=20,
                    border_radius=10,
                    width=400,
                ),
                ft.Divider(height=20),
                ft.Text("zelect a language or smth idk", weight=ft.FontWeight.BOLD),
                radio_thing,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main, assets_dir="assets")