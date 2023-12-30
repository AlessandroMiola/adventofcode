import os

import pytest

from src.year_2023.day07.part2 import (
    camel_cards_p2,
    get_best_in_hand_besides_jolly,
    get_hands_to_rank,
    get_total_winnings,
    replace_jolly_with_best_card,
)
from src.year_2023.utils import read_file


@pytest.fixture
def mock_file_data(tmp_path):
    test_file_path = os.path.join(tmp_path, "test_file.txt")
    test_input = "32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483"
    with open(test_file_path, "w") as file:
        file.write(test_input)
    return test_file_path


@pytest.mark.parametrize(
    ["test_hand", "test_best_card_in_hand"],
    [
        ("32T3K", "3"),
        ("T55J5", "5"),
        ("KK677", "K"),
        ("KTJJT", "T"),
        ("QQQJA", "Q"),
        ("JJJJJ", "A"),
    ],
)
def test_get_best_card_in_hand(test_hand, test_best_card_in_hand):
    assert get_best_in_hand_besides_jolly(test_hand) == test_best_card_in_hand


@pytest.mark.parametrize(
    ["test_original_hand", "test_transformed_hand"],
    [
        ("32T3K", "32T3K"),
        ("T55J5", "T5555"),
        ("KK677", "KK677"),
        ("KTJJT", "KTTTT"),
        ("QQQJA", "QQQQA"),
        ("JJJJJ", "AAAAA"),
    ],
)
def test_replace_jolly_with_best_card(test_original_hand, test_transformed_hand):
    assert replace_jolly_with_best_card(test_original_hand) == test_transformed_hand


@pytest.mark.parametrize(
    ["test_hand", "test_rank"],
    [
        ("32T3K", 1),
        ("T55J5", 3),
        ("KK677", 2),
        ("KTJJT", 5),
        ("QQQJA", 4),
    ],
)
def test_get_hands_to_rank(mock_file_data, test_hand, test_rank):
    lines = read_file(mock_file_data)
    hands_to_rank = get_hands_to_rank(lines, camel_cards_p2)
    assert hands_to_rank.get(test_hand) == test_rank


def test_get_total_winnings(mock_file_data):
    assert get_total_winnings(mock_file_data, camel_cards_p2) == 5905
