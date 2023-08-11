from . import formatters
from libs.output_files import JsonOutputFile, HtmlOutputFile


class OutputFileFactory:
    _creators = {}

    @classmethod
    def register(cls, format_type, creator_cls) -> None:
        cls._creators[format_type] = creator_cls

    @classmethod
    def create(cls, format_type):
        if format_type not in cls._creators:
            raise ValueError(f"Unknown format type: {format_type}")
        return cls._creators[format_type]
  
  
OutputFileFactory.register('json', JsonOutputFile)
OutputFileFactory.register('html', HtmlOutputFile)
