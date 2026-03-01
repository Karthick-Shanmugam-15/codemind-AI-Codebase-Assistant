import hashlib
import string

BASE62 = string.digits + string.ascii_lowercase + string.ascii_uppercase


def _to_base62(number: int) -> str:
    if number == 0:
        return BASE62[0]
    result = []
    while number:
        result.append(BASE62[number % 62])
        number //= 62

    return "".join(reversed(result))


def generate_id(file_path: str, class_name: str, name: str, unit_type: str, parameters: str = "") -> str:
    raw = f"{file_path}_{class_name}_{name}_{unit_type}_{parameters}"
    hash_int = int(hashlib.md5(raw.encode()).hexdigest(), 16)
    short_hash = _to_base62(hash_int)[:8]

    return f"{short_hash}_{class_name}_{name}"