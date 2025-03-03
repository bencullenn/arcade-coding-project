import pytest
from kv_store.store import Store


@pytest.fixture
def store():
    return Store(str, str)


def test_set_and_get(store):
    store.set("key", "value")
    assert store.get("key") == "value"


def test_delete(store):
    store.set("key", "value")
    store.delete("key")
    assert store.get("key") is None


def test_transaction(store):
    store.begin()
    store.set("key", "value")
    store.commit()
    assert store.get("key") == "value"


def test_rollback(store):
    store.begin()
    store.set("key", "value")
    store.rollback()
    assert store.get("key") is None
