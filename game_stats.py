class GameStats:
    """Track stats for Alien Invasion."""

    def __init__(self, ai_game):
        """Initilize stats."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.settings.ship_limit