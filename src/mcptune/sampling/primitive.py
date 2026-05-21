from .base import ArgumentSampler
import random
import string


class PrimitiveSampler(ArgumentSampler):

    def sample(self, schema: dict):

        t = schema.get("type")

        if t == "string":
            return self._string(schema)

        if t == "integer":
            return random.randint(0, 100)

        if t == "number":
            return random.uniform(0, 100)

        if t == "boolean":
            return random.choice([True, False])

        return None

    def _string(self, schema):
        return "".join(random.choices(string.ascii_lowercase, k=8))