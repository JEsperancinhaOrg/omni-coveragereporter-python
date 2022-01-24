from enum import Enum


class Language(Enum):
    JAVA = 1
    KOTLIN = 2
    SCALA = 3
    PYTHON = 4
    JAVA_SCRIPT = 5

    def capitalized(self):
        name = self.name
        return "".join(list(map(lambda t: t.capitalize(), name.split("_"))))


def convert_coverage(data, report=None):
    return None
