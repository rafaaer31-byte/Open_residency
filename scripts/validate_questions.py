#!/usr/bin/env python3
"""Validate question JSON files against schema/question.schema.json.

Usage:
    python scripts/validate_questions.py data/
"""
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    sys.exit("Install dependency: pip install jsonschema")

REQUIRED_TOPICS = {
    "id", "statement", "options", "answer", "topic",
    "source", "license", "review_status",
}

def main(paths):
    schema = json.loads(Path("schema/question.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    errors = 0
    checked = 0
    for p in paths:
        for f in sorted(Path(p).rglob("*.json")):
            checked += 1
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                print(f"INVALID JSON: {f}: {e}")
                errors += 1
                continue
            for err in validator.iter_errors(data):
                print(f"SCHEMA ERROR: {f}: {err.message}")
                errors += 1
            missing = REQUIRED_TOPICS - set(data)
            if missing:
                print(f"MISSING FIELDS: {f}: {sorted(missing)}")
                errors += 1
    print(f"Checked {checked} file(s). {errors} error(s).")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: python scripts/validate_questions.py data/")
    main(sys.argv[1:])
