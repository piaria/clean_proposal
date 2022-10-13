def validate_message_creation(*, text: str, user_id: int):
    # raise if fails
    assert user_id
    assert len(text) > 10