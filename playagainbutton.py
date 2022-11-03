from button import Button


class PlayAgainButton(Button):

    def __init__(self, name: str = "Button", fill: tuple = ..., text_size: int = 40, center=...) -> None:
        super().__init__(name, fill, text_size, center)

    def handle_click(self, play_again: bool) -> bool:

        play_again = True

        return play_again
