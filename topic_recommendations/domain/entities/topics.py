from dataclasses import dataclass


@dataclass
class Topic:
    id: int
    content: str
    user_id: int
