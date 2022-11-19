class BaseError(Exception):
    message = 'Неизвестная ошибка'


class NotEnoughSpaseError(BaseError):
    message = 'Недостаточно места'


class UnknownProductError(BaseError):
    message = 'Неизвестный товар'


class NotEnoughProductError(BaseError):
    message = 'Недостаточно товара'


class InvalidRequestError(BaseError):
    message = 'Неправильный запрос'

class UnknownStorageError(BaseError):
    message = 'Неизвестный склад'

class TooManyDifferentProductError(BaseError):
    message = 'Слишком много разных товаров'
