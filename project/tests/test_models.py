import pytest

from project.models import Customer
from project.app import InMemoryCustomerStore, NotFoundError


def test_customer_to_from_dict():
    data = {"id": "3", "name": "Charlie", "email": "charlie@example.com"}
    c = Customer.from_dict(data)
    assert c.id == 3
    assert c.name == "Charlie"
    assert c.email == "charlie@example.com"
    assert c.to_dict() == {"id": 3, "name": "Charlie", "email": "charlie@example.com"}


def test_customer_from_dict_missing_fields_raises():
    with pytest.raises(ValueError):
        Customer.from_dict({"name": "NoId"})
    with pytest.raises(ValueError):
        Customer.from_dict({"id": 4})


def test_inmemory_store_add_get_list_remove():
    store = InMemoryCustomerStore()
    c1 = Customer(id=10, name="Daisy")
    c2 = Customer(id=20, name="Eve", email="eve@example.com")

    store.add(c1)
    store.add(c2)

    # get
    assert store.get(10).name == "Daisy"
    assert store.get(20).email == "eve@example.com"

    # list
    all_customers = store.list()
    assert len(all_customers) == 2
    ids = {c.id for c in all_customers}
    assert ids == {10, 20}

    # remove
    store.remove(10)
    with pytest.raises(NotFoundError):
        store.get(10)

    # removing non-existent should raise
    with pytest.raises(NotFoundError):
        store.remove(999)


def test_store_add_duplicate_raises():
    store = InMemoryCustomerStore()
    c = Customer(id=1, name="Dup")
    store.add(c)
    with pytest.raises(ValueError):
        store.add(Customer(id=1, name="Dup2"))
