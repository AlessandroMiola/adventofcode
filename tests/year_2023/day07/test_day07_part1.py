import os

import pytest

from src.year_2023.day07.part1 import (
    camel_cards_p1,
    get_hands_to_bids,
    get_hands_to_rank,
    get_sorted_hand_values_by_rank,
    get_total_winnings,
    map_hand_to_ladder,
    map_hand_to_values,
    map_values_to_hand,
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
    ["test_input_hand_and_bid", "test_hand", "test_bid"],
    [
        (["32T3K 765"], "32T3K", 765),
        (["T55J5 684"], "T55J5", 684),
        (["KK677 28"], "KK677", 28),
        (["KTJJT 220"], "KTJJT", 220),
        (["QQQJA 483"], "QQQJA", 483),
    ],
)
def test_get_hands_to_bids(test_input_hand_and_bid, test_hand, test_bid):
    assert [k for k, _ in get_hands_to_bids(test_input_hand_and_bid).items()][0] == test_hand
    assert [v for _, v in get_hands_to_bids(test_input_hand_and_bid).items()][0] == test_bid


@pytest.mark.parametrize(
    ["test_hand", "test_values"],
    [
        ("32T3K", [3, 2, 10, 3, 13]),
        ("T55J5", [10, 5, 5, 11, 5]),
        ("KK677", [13, 13, 6, 7, 7]),
        ("KTJJT", [13, 10, 11, 11, 10]),
        ("QQQJA", [12, 12, 12, 11, 14]),
    ],
)
def test_map_hand_to_values(test_hand, test_values):
    assert map_hand_to_values(test_hand, camel_cards_p1) == test_values


@pytest.mark.parametrize(
    ["test_values", "test_hand"],
    [
        ([3, 2, 10, 3, 13], "32T3K"),
        ([10, 5, 5, 11, 5], "T55J5"),
        ([13, 13, 6, 7, 7], "KK677"),
        ([13, 10, 11, 11, 10], "KTJJT"),
        ([12, 12, 12, 11, 14], "QQQJA"),
    ],
)
def test_map_values_to_hand(test_hand, test_values):
    assert map_values_to_hand(test_values, camel_cards_p1) == test_hand


@pytest.mark.parametrize(
    ["test_hand", "test_ladder"],
    [
        ("32T3K", [2, 1, 1, 1]),
        ("T55J5", [3, 1, 1]),
        ("KK677", [2, 2, 1]),
        ("KTJJT", [2, 2, 1]),
        ("QQQJA", [3, 1, 1]),
    ],
)
def test_map_hand_to_ladder(test_hand, test_ladder):
    assert map_hand_to_ladder(test_hand) == test_ladder


def test_get_sorted_hand_values_by_rank():
    test_ladders = [
        [2, 1, 1, 1],
        [3, 1, 1],
        [2, 2, 1],
        [2, 2, 1],
        [3, 1, 1],
        [5],
        [1, 1, 1, 1, 1],
        [3, 2],
    ]
    test_values = [
        [3, 2, 10, 3, 13],
        [10, 5, 5, 12, 5],
        [13, 13, 6, 7, 7],
        [13, 10, 12, 12, 10],
        [11, 11, 11, 12, 14],
        [5, 5, 5, 5, 5],
        [2, 3, 5, 10, 11],
        [12, 12, 7, 7, 12],
    ]
    test_results = [
        ([5], [5, 5, 5, 5, 5]),
        ([3, 2], [12, 12, 7, 7, 12]),
        ([3, 1, 1], [11, 11, 11, 12, 14]),
        ([3, 1, 1], [10, 5, 5, 12, 5]),
        ([2, 2, 1], [13, 13, 6, 7, 7]),
        ([2, 2, 1], [13, 10, 12, 12, 10]),
        ([2, 1, 1, 1], [3, 2, 10, 3, 13]),
        ([1, 1, 1, 1, 1], [2, 3, 5, 10, 11]),
    ]
    assert get_sorted_hand_values_by_rank(test_ladders, test_values) == test_results


@pytest.mark.parametrize(
    ["test_hand", "test_rank"],
    [
        ("32T3K", 1),
        ("T55J5", 4),
        ("KK677", 3),
        ("KTJJT", 2),
        ("QQQJA", 5),
    ],
)
def test_get_hands_to_rank(mock_file_data, test_hand, test_rank):
    lines = read_file(mock_file_data)
    hands_to_rank = get_hands_to_rank(lines, camel_cards_p1)
    assert hands_to_rank.get(test_hand) == test_rank


def test_get_total_winnings(mock_file_data):
    assert get_total_winnings(mock_file_data, camel_cards_p1) == 6440
