"""Data models for the `project` package.

Contains a simple `Customer` dataclass and small helpers for validation
and serialization. Kept minimal so tests are straightforward.
"""
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Customer:
    """A minimal customer record stored in memory.

    Fields:
    - id: int - unique identifier
    - name: str - full name
    - email: Optional[str] - optional email address
    """

    id: int
    name: str
    email: Optional[str] = None

    def to_dict(self) -> dict:
        """Return a dict representation suitable for JSON serialization."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Customer":
        """Create a Customer from a plain mapping.

        Performs minimal validation to ensure `id` and `name` are present.
        """
        if "id" not in data or "name" not in data:
            raise ValueError("Customer data must include 'id' and 'name'")
        return cls(id=int(data["id"]), name=str(data["name"]), email=data.get("email"))
