import json
from etc.templates import html_template


formatters = {
    "json": lambda data: json.dumps(data, indent=4),
    "html": lambda data: html_template(data),
}
