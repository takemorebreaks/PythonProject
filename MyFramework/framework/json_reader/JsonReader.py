import json, os

class JsonReader:
    @staticmethod
    def read_json(file_path):
        if not file_path:
            raise ValueError("File path cannot be null or empty.")
        if not file_path.lower().endswith(".json"):
            raise ValueError("Invalid file type. Expected a .json file.")

        # Go up TWO levels: from framework/json_reader/JsonReader.py → MyFramework/
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        full_path = os.path.join(project_root, file_path)

        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File not found: {full_path}")

        with open(full_path, "r", encoding="utf-8") as f:
            return json.load(f)
