
from ui.components.buttons.button import Button
from games.game import Game


class WarButton(Button):

    def __init__(self, name: str = "Button", fill: tuple = ..., text_size: int = 40, center=...) -> None:
        super().__init__(name, fill, text_size, center)

    def handle_click(self, game: Game) -> None:

        match game.state:
            case "Draw":
                game.update_state("Battle")
            case "Battle":
                game.battle(game.players)
                game.update_state("Collect")
            case "Collect":
                game.collect()
                game.update_state("Draw")
