"""Bubble sort implementation.

Provides:
- bubble_sort: returns a new sorted list (doesn't mutate input)
- bubble_sort_in_place: sorts a list in place

Run this file directly to see a small demo.
"""

from __future__ import annotations

from typing import List, Sequence, TypeVar

T = TypeVar("T")


def bubble_sort(values: Sequence[T], *, reverse: bool = False) -> List[T]:
    """Return a sorted copy of `values` using bubble sort.

    Args:
        values: Any finite sequence of comparable items.
        reverse: If True, sort in descending order.

    Returns:
        A new list containing the sorted values.
    """

    arr = list(values)
    bubble_sort_in_place(arr, reverse=reverse)
    return arr


def bubble_sort_in_place(arr: List[T], *, reverse: bool = False) -> None:
    """Sort `arr` in place using an optimized bubble sort."""

    n = len(arr)
    if n < 2:
        return

    def out_of_order(a: T, b: T) -> bool:
        return a < b if reverse else a > b

    for i in range(n - 1):
        swapped = False
        # After each outer iteration, the last i elements are in correct position
        for j in range(0, n - 1 - i):
            if out_of_order(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    data = [5, 1, 4, 2, 8]
    print("original:", data)
    print("sorted:", bubble_sort(data))
    print("sorted desc:", bubble_sort(data, reverse=True))
