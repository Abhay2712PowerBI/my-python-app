"""Small demo application module for the `project` package.

Implements a tiny in-memory repository for `Customer` objects and a
simple CLI demo when run as a script.
"""
from typing import Dict, List, Optional
from .models import Customer


class NotFoundError(Exception):
    pass


class InMemoryCustomerStore:
    """Simple in-memory store for Customer objects."""

    def __init__(self) -> None:
        self._data: Dict[int, Customer] = {}

    def add(self, customer: Customer) -> None:
        if customer.id in self._data:
            raise ValueError(f"Customer with id {customer.id} already exists")
        self._data[customer.id] = customer

    def get(self, customer_id: int) -> Customer:
        try:
            return self._data[customer_id]
        except KeyError:
            raise NotFoundError(f"Customer {customer_id} not found")

    def list(self) -> List[Customer]:
        return list(self._data.values())

    def remove(self, customer_id: int) -> None:
        if customer_id not in self._data:
            raise NotFoundError(f"Customer {customer_id} not found")
        del self._data[customer_id]


# Package-level default store (convenience)
_store = InMemoryCustomerStore()


def create_customer(id: int, name: str, email: Optional[str] = None) -> Customer:
    c = Customer(id=id, name=name, email=email)
    _store.add(c)
    return c


def get_customer(id: int) -> Customer:
    return _store.get(id)


def list_customers() -> List[Customer]:
    return _store.list()


def remove_customer(id: int) -> None:
    _store.remove(id)


def _demo() -> None:
    """Run a quick demo when executed as a script."""
    print("Demo: creating customers...")
    create_customer(1, "Alice Example", "alice@example.com")
    create_customer(2, "Bob Example")
    for c in list_customers():
        print(c.to_dict())


if __name__ == "__main__":
    _demo()
