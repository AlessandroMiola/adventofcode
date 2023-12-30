import os

from collections import Counter

from src.year_2023.day07.part1 import (
    get_hands_to_bids,
    get_sorted_hand_values_by_rank,
    map_hand_to_ladder,
    map_hand_to_values,
    map_values_to_hand,
)
from src.year_2023.utils import read_file


camel_cards_p2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def get_best_in_hand_besides_jolly(hand: str) -> str:
    if hand != "JJJJJ":
        hand_wo_jolly = "".join(card for card in hand if card != "J")
    else:
        hand_wo_jolly = "AAAAA"
    best_hand_values = max(
        Counter(map_hand_to_values(hand_wo_jolly, camel_cards_p2)).most_common(),
        key=lambda x: (x[1], x[0]),
    )[0]
    return map_values_to_hand([best_hand_values], camel_cards_p2)


def replace_jolly_with_best_card(hand: str) -> str:
    return hand.replace("J", get_best_in_hand_besides_jolly(hand))


def get_hands_to_rank(lines: list[str], camel_cards: list[int]) -> dict[str, int]:
    # build ladders based on transformed hand
    # break ties based on original hand
    hands = [k for k, _ in get_hands_to_bids(lines).items()]
    transformed_hands = [replace_jolly_with_best_card(hand) for hand in hands]
    ladders = [map_hand_to_ladder(t_hand) for t_hand in transformed_hands]
    hands_to_values = [map_hand_to_values(hand, camel_cards) for hand in hands]
    sorted_hand_values = get_sorted_hand_values_by_rank(ladders, hands_to_values)
    hand_values_rank = [
        len(lines) - sorted_hand_values.index(value) for value in sorted_hand_values
    ]
    return {
        map_values_to_hand(hand_values, camel_cards): rank
        for (_, hand_values), rank in zip(sorted_hand_values, hand_values_rank)
    }


def get_total_winnings(file_path: str, camel_cards: list[int]) -> int:
    lines = read_file(file_path)
    hands_to_bids = get_hands_to_bids(lines)
    hands_to_rank = get_hands_to_rank(lines, camel_cards)
    return sum((bid * hands_to_rank.get(hand) for hand, bid in hands_to_bids.items()))


if __name__ == "__main__":
    file_name = "input_file.txt"
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "data", file_name)
    print(f"Total winnings are: {get_total_winnings(file_path, camel_cards_p2)}")
