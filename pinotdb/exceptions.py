class Error(Exception):
    pass


class Warning(Exception):
    pass


class InterfaceError(Error):
    pass


class NotFoundError(Error):
    pass


class ServerError(Error):
    pass


class ServiceUnavailableError(Error):
    pass


class DatabaseError(Error):
    pass


class InternalError(DatabaseError):
    pass


class OperationalError(DatabaseError):
    pass


class ProgrammingError(DatabaseError):
    pass


class IntegrityError(DatabaseError):
    pass


class DataError(DatabaseError):
    pass


class NotSupportedError(DatabaseError):
    pass


class QueryTimeoutError(DatabaseError):
    pass


class MalformedQueryResponseError(DatabaseError):
    pass