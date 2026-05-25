from card import Card

class Hand:
    """The hand in a poker game."""

    max_hand_size = 5
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        """Initialize Hand."""
        self.cards_in_hand: list[Card] = []

    def can_add_card(self, card: Card) -> bool:
        """
        Check for card validity.

        Can only add card if:
        - A card with the same suit and value is already not being held.
        - The player is holding less than five cards
        - The card has both a valid value and a valid suite.
        """
        if len(self.cards_in_hand) >= Hand.max_hand_size:
            return False
        if not card.is_valid():
            return False
        return card in self.cards_in_hand

    def add_card(self, card: Card):
        """
        Add a card to hand.

        Before adding a card, you would have to check if it can be added.
        """
        if self.can_add_card(card):
            self.cards_in_hand.append(card)

    def can_remove_card(self, card: Card):
        """
        Check if a card can be removed from hand.

        The only consideration should be that the card is already being held.
        """
        return card in self.cards_in_hand

    def remove_card(self, card: Card):
        """
        Remove a card from hand.

        Before removing the card, you would have to check if it can be removed.
        """
        if self.can_remove_card(card):
            self.cards_in_hand.remove(card)

    def get_cards(self):
        """Return a list of cards as objects."""
        return self.cards_in_hand[:]

    def is_straight(self):
        """
        Determine if the hand is a straight.

        A straight hand will have all cards in the order of value.
        Sorting will help you here as the order will vary.

        Examples:
        4 5 6 7 8
        K J 10 Q A

        For the sake of simplicity - A 2 3 4 5 will not be tested.
        You can always consider A to be the highest ranked card.
        """
        self.cards_in_hand.sort()
        previous_card = None
        for current_card in self.cards_in_hand:
            if previous_card is None:
                previous_card = current_card
                continue
            if (previous_card + 1).value != current_card.value:
                return False
            previous_card = current_card
        return True


    def is_flush(self):
        """
        Determine if the hand is a flush.

        In a flush hand all cards are the same suit. Their number value is not important here.
        """
        raise NotImplementedError

    def is_straight_flush(self):
        """
        Determine if the hand is a straight flush.

        Such a hand is both straight and flush at the same time.

        """
        raise NotImplementedError

    def is_full_house(self):
        """
        Determine if the hand is a full house.

        A house will have three cards of one value, and two cards of a second value.
        For example:
        2 2 2 6 6
        K J K J K
        """
        raise NotImplementedError

    def is_four_of_a_kind(self):
        """
        Determine if there are four cards of the same value in hand.

        For example:
        2 2 K 2 2
        9 4 4 4 4

        """
        raise NotImplementedError

    def is_three_of_a_kind(self):
        """
        Determine if there are three cards of the same value in hand.

        For Example:
        Q 4 Q Q 7
        5 5 1 5 2

        """
        raise NotImplementedError

    def is_pair(self):
        """
        Determine if there are two kinds of the same value in hand.

        For example:
        5 A 2 K A
        8 7 6 6 5

        """
        raise NotImplementedError

    def get_hand_type(self):
        """
        Return a string representation of the hand.

        Return None (or nothing), if there are less than five cards in hand.

        "straight flush" - Both a straight and a flush
        "flush" - The cards are all of the same suit
        "straight" - The cards can be ordered
        "full house" - Three cards are of the same value while the other two also share a value.
        "four of a kind" - Four cards are of the same value
        "three of a kind" - Three cards are of the same value
        "pair" - Two cards are of the same value
        "high card" - None of the above

        """
        if self.is_straight():
            return

    def __repr__(self):
        """
        Return a string representation of the hand.

        I got a {type} with cards: {card list}
        I got a straight with cards: 2 of diamonds, 4 of spades, 5 of clubs, 3 of diamonds, 6 of hearts

        If a hand type cannot be yet determined, return a list of cards as so:

        I'm holding {cards}
        I'm holding 2 of diamonds, 4 of spades.

        Order of the cards is not important.
        """
        raise NotImplementedError