broker_uri = ''


def set_broker_uri(uri: str) -> None:
    global broker_uri
    broker_uri = uri


def get_broker_uri() -> str:
    return broker_uri
