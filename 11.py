from typing import List
from collections import deque
import tqdm
import re


class Monkey:
    def __init__(self, monkey_nr, items, operation, test, test_true, test_false):
        self.monkey_nr = int(monkey_nr)
        self.items = deque([int(i) for i in items.split(", ")])
        self.operation = operation
        self.test = int(test)
        self.test_true = int(test_true)
        self.test_false = int(test_false)
        self.inspected = 0

    def __str__(self):
        return f"Monkey: {self.monkey_nr}, items: {self.items}"

    def inspect_items(self, div):
        while len(self.items) != 0:
            self.inspected += 1
            old = self.items.popleft()
            new = eval(self.operation)
            new = (new // div) % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
            if new % self.test == 0:
                yield self.test_true, new
            else:
                yield self.test_false, new

    def add_item(self, item):
        self.items.appendleft(item)


def parse_input(d):
    monkey_information = re.findall("""Monkey (\d):
  Starting items: (.+)
  Operation: new = (.+)
  Test: divisible by (.+)
    If true: throw to monkey (\d)
    If false: throw to monkey (\d)""", d)
    return monkey_information


def run_monkeys(n, div):
    for _ in range(n):
        for i in range(len(monkeys)):
            for to, item in monkeys[i].inspect_items(div=div):
                monkeys[to].add_item(item)

    inspected = []
    for nr, monkey in monkeys.items():
        inspected.append(monkey.inspected)

    inspected = sorted(inspected)
    return inspected[-1] * inspected[-2]


with open('inputs/11.txt') as f:
    monkey_data = parse_input(f.read())
    monkeys = {int(i[0]): Monkey(*i) for i in monkey_data}

    print(f"Part 1: {run_monkeys(20, 3)}")
    print(f"Part 2: {run_monkeys(10_000, 1)}")
