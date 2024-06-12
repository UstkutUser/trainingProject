from typing import Optional


def filter_by_state(
    operations: list, state: Optional[str] = "EXECUTED"
) -> list[dict]:
    """Фильтрует транзакции по состоянию"""
    return [elem for elem in operations if elem["state"] == state]


def filter_by_date(operations: list, ascending: bool = False) -> list:
    """Фильтрует транзакции по дате"""
    return sorted(operations, key=lambda date: date.get("date"), reverse=ascending)
