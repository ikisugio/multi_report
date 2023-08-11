from abc import ABC, abstractmethod, ABCMeta


class OutputFile(ABC):
    
    def __init__(self, file_name, data):
        self.file_name = file_name
        self.data = data

    @abstractmethod
    def output(self) -> str:
        pass


class ConcreteOutputFile(OutputFile):
    
    def output(self, formatters, format_type) -> str:
        formatted_data = formatters[format_type](self.data)
        with open(self.file_name, 'w') as f:
            f.write(formatted_data)
        return formatted_data


class JsonOutputFile(ConcreteOutputFile):
    
    def __init__(self, file_name, data):
        super().__init__(file_name, data)
        self.format_type = "json"

    def output(self, formatters) -> str:
        super().output(formatters, self.format_type)


class HtmlOutputFile(ConcreteOutputFile):
    
    def __init__(self, file_name, data):
        super().__init__(file_name, data)
        self.format_type = "html"

    def output(self, formatters) -> str:
        super().output(formatters, self.format_type)
