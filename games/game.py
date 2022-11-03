
from ui.components.logwindow import LogWindow
from ui.components.UIPlayer import UIPlayer


class Game:

    def __init__(self, log_window: LogWindow) -> None:
        self.players: list[UIPlayer] = []
        self.activeplayers: list[UIPlayer] = []
        self.log_window: LogWindow = log_window
        self.winners: list[UIPlayer] = []
        self.losers: list[UIPlayer] = []
