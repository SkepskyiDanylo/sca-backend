import requests
from rest_framework.exceptions import ValidationError

from sca_backend import settings


def breed_validator(breed) -> bool:
    try:
        response = requests.get(settings.API_URL, timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        raise ValidationError("Error validating breed")
    if not any(
            data.get("name").strip().lower() == breed.strip().lower()
            for data in response.json()
    ):
        return False
    return True
