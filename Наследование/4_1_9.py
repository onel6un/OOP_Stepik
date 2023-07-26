class Validator:
    def _is_valid(self, data):
        return True

    def __call__(self, data):
        return self._is_valid(data)


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if isinstance(data, int) and self.min_value <= data <= self.max_value:
            return True
        raise ValueError('данные не прошли валидацию')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if isinstance(data, float) and self.min_value <= data <= self.max_value:
            return True
        raise ValueError('данные не прошли валидацию')
