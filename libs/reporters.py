from .factories import OutputFileFactory
from .formatters import formatters as F
from etc.contexts import data as D


class FormalReporter:
    
    @staticmethod
    def report(file_type, file_name) -> str:
        creator = OutputFileFactory.create(file_type)
        return creator(file_name, D).output(F)

