import os

from collections import Counter

from src.year_2023.utils import read_file


camel_cards_p1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def _map_card_to_value(cards: list[str]) -> dict[str, int]:
    return {card: idx + 2 for idx, card in enumerate(cards)}


def get_hands_to_bids(lines: list[str]) -> dict[str, int]:
    return {line.split()[0]: int(line.split()[1]) for line in lines}


def map_hand_to_values(hand: str, camel_cards: list[str]) -> list[int]:
    card_to_value = _map_card_to_value(camel_cards)
    return [card_to_value[card] for card in hand]


def map_values_to_hand(values: list[int], camel_cards: list[str]) -> str:
    value_to_card = {value: card for card, value in _map_card_to_value(camel_cards).items()}
    return ''.join(value_to_card[value] for value in values)


def map_hand_to_ladder(hand: str) -> list[int]:
    return sorted([v for _, v in Counter(hand).items()], reverse=True)


def _map_ladder_to_rank(ladder: list[int]) -> int:
    match ladder:
        case [5]:
            return 7
        case [4, 1]:
            return 6
        case [3, 2]:
            return 5
        case [3, 1, 1]:
            return 4
        case [2, 2, 1]:
            return 3
        case [2, 1, 1, 1]:
            return 2
        case [1, 1, 1, 1, 1]:
            return 1


def get_sorted_hand_values_by_rank(
    ladders: list[list[int]],
    hands_to_values: list[list[int]]
) -> list[tuple[list[int]]]:
    ladders_and_values = list(zip(ladders, hands_to_values))
    return sorted(
        ladders_and_values,
        key=lambda x: (-_map_ladder_to_rank(x[0]), tuple(-el for el in x[1]))
    )


def get_hands_to_rank(lines: list[str], camel_cards: list[str]) -> dict[str, int]:
    hands = [k for k, _ in get_hands_to_bids(lines).items()]
    ladders = [map_hand_to_ladder(hand) for hand in hands]
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
    print(f"Total winnings are: {get_total_winnings(file_path, camel_cards_p1)}")
