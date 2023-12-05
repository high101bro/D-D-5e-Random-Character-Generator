#! /usr/bin/env python3

"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
"""

import re
from pathlib import Path


def find_numbers_and_number_words_in_text(text: str) -> list[int]:
    values = []
    regex = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
    for group in re.findall(regex, text):
        match group:
            case "one":
                values.append(1)
            case "two":
                values.append(2)
            case "three":
                values.append(3)
            case "four":
                values.append(4)
            case "five":
                values.append(5)
            case "six":
                values.append(6)
            case "seven":
                values.append(7)
            case "eight":
                values.append(8)
            case "nine":
                values.append(9)
            case _:
                values.append(int(group))
    return values


def find_numbers_in_text(text: str) -> list[int]:
    return [int(item) for item in re.findall(r"\d", text)]


def find_first_and_last_number_in_text(text: str, text_contains_spelled_words: bool = False) -> tuple[int, int]:
    numbers = find_numbers_and_number_words_in_text(text) if text_contains_spelled_words else find_numbers_in_text(text)
    if len(numbers) == 1:
        return numbers[0], numbers[0]
    return numbers[0], numbers[-1]


def part1(rows: list[str]) -> int:
    return sum(int(str("".join(str(item) for item in find_first_and_last_number_in_text(row)))) for row in rows)


def part2(rows: list[str]) -> int:
    return sum(
        int(
            str(
                "".join(
                    str(item)
                    for item in find_first_and_last_number_in_text(
                        row,
                        text_contains_spelled_words=True,
                    )
                ),
            ),
        )
        for row in rows
    )


if __name__ == "__main__":
    rows = Path("calibration_doc.txt").read_text().split("\n")
    print(part1(rows))
    print(part2(rows))