import logging
import random
from typing import Any
from typing import Dict
from typing import List

# Import from the installed package name, not the src directory
from your_core_library.data_handler import get_core_greeting

# Configure basic logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_data() -> List[Dict[str, Any]]:
    """Simulates extracting raw data."""
    logging.info("Starting data extraction...")
    # In a real scenario, this could read from a DB, API, file, etc.
    raw_data = [
        {
            "id": i,
            "value": random.randint(1, 100),
            "category": random.choice(["A", "B", "C"]),
        }
        for i in range(1, 11)
    ]
    logging.info(f"Extracted {len(raw_data)} raw records.")
    return raw_data


def transform_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Simulates transforming the data."""
    logging.info("Starting data transformation...")
    transformed = []
    # Example: Filter records with value > 50 and add a derived field using the core library
    core_lib_msg = get_core_greeting()  # Get message from core library
    for record in data:
        if record.get("value", 0) > 50:
            record["status"] = "processed"
            record["core_message"] = core_lib_msg  # Add info from core lib
            record["value_category"] = f"{record['value']}-{record['category']}"
            transformed.append(record)
    logging.info(f"Transformed data resulted in {len(transformed)} records.")
    return transformed


def load_data(data: List[Dict[str, Any]]):
    """Simulates loading the transformed data."""
    logging.info("Starting data loading...")
    # In a real scenario, this could write to a DB, file, API, etc.
    if not data:
        logging.warning("No data to load.")
        return

    print("--- Processed Data ---")
    for record in data:
        print(record)
    print("---------------------")
    logging.info(f"Successfully loaded {len(data)} records.")


def main():
    """Main function to run the ETL pipeline."""
    logging.info("ETL Pipeline Started.")
    raw = extract_data()
    transformed = transform_data(raw)
    load_data(transformed)
    logging.info("ETL Pipeline Finished.")


if __name__ == "__main__":
    main()
