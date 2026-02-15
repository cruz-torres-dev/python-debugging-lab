import json

class InvalidPayload(ValueError):
    pass

def get_user_id(payload: str) -> int:
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as e:
        raise InvalidPayload("Invalid JSON") from e

    user = data.get("user")
    if not isinstance(user, dict) or "id" not in user:
        raise InvalidPayload("Missing user.id")

    try:
        return int(user["id"])
    except (TypeError, ValueError) as e:
        raise InvalidPayload("user.id must be int") from e

