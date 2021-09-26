from typing import Annotated


class AnnotatedClass:
    def __init__(self, default_value: Annotated[float, "Some default number"]):
        """Constructor"""
        self.default_value = default_value

    def multiply_default_by(self, multiplier: Annotated[float, "The multiplier"]):
        """Multiply default by a multiplier"""
        return self.default_value * multiplier


if __name__ == "__main__":
    annotated_class = AnnotatedClass(33.6)
    print(AnnotatedClass.multiply_default_by.__annotations__)
