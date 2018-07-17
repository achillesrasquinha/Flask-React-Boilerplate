class AppError(Exception):
    pass

class KeyError(AppError):
    pass

class ValueError(AppError):
    pass

class NotImplementedError(AppError):
    pass