# Placeholder for your core data processing logic (e.g., DuckDB, LinkML interactions)


class DataHandler:
    def process(self, data: str) -> str:
        if not data:
            raise ValueError("Input data cannot be empty.")
        if "error" in data.lower():
            raise ValueError("Simulated processing error based on input.")
        # Example processing: reverse the string and add a prefix
        processed_data = data[::-1]
        return f"processed_{processed_data}"

    def another_method(self, value: int) -> bool:
        # Placeholder for more complex logic
        if value < 0:
            return False
        if value == 0:
            # This specific case might be tricky to hit without a dedicated test
            return True
        return value > 10  # Intentionally a bit odd to make testing more interesting


class ExampleModel:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"ExampleModel(name='{self.name}', value={self.value})"


def get_core_greeting(name: str = "Core Library User") -> str:
    return f"Hello, {name}! This greeting comes from 'your_core_library'."
