class GNUHealthError(Exception):
    """
    Base GNU Health exception
    """


class GNUHealthTypeError(GNUHealthError):
    """
    Exception raised when there is a type mismatch
    """

    def __init__(self, adapter, model, msg=None):
        if msg is None:
            msg = "{0} adapter cannot process this {1} model".format(adapter, model)
        super(GNUHealthTypeError, self).__init__(msg)


class GNUHealthImportError(GNUHealthError):
    """
    Exception raised when error importing data from model
    """

    def __init__(self, attribute, msg=None):
        if msg is None:
            msg = "Error importing {0} data from the model".format(attribute)
        super(GNUHealthImportError, self).__init__(msg)


__all__ = ["GNUHealthError", "GNUHealthTypeError", "GNUHealthImportError"]
