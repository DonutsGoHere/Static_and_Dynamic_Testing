import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardGame = CardGame()
        self.card = Card("spades", 1)
        self.card1 = Card("diamonds", 6)
        self.card2 = Card("hearts", 3)
        self.card3 = Card("club", 8)
        self.cards = [self.card, self.card1, self.card2, self.card3]

    def test_check_for_ace(self):
        self.assertEqual(True, self.cardGame.check_for_ace(self.card))

    def test_highest_card(self):
        self.assertEqual(self.card1, self.cardGame.highest_card(self.card1, self.card2))
    
    def test_get_cards_total(self):
        self.assertEqual("You have a total of18", self.cardGame.cards_total(self.cards))
