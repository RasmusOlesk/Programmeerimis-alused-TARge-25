class Card:
    """A card in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, value: str, suit: str):
        """Initialze Card."""
        self.suit = suit
        self.value = value

    def __repr__(self):
        """
        Return a string representation of the card.

        "{value} of {suit}"
        "2 of hearts" or "Q of spades"

        """
        return f"{self.value} of {self.suit}"

    def __eq__(self, other, /):
        if isinstance(other, Card):
            return self.value == other.value and self.suit == other.suit
        return False

    def __lt__(self, other):
        """return true if other.value is less then self.value."""
        return isinstance(other, Card) and self.value < other.value

    def __add__(self, offset):
        """Add an interger to card.

        returns: new card with value offset by integer
        """
        if isinstance(offset, int):
            new_card_value_index = Card.values.index(self.value) + offset
            if len(Card.values) > new_card_value_index >= 0:
                return Card(Card.values[new_card.value_index], self.suit)
        return Card("", "")

    def is_valid(self):
        """Validate the card. Must be possible suit and value"""
        return self.value in card.values and self.suit in Card.suits