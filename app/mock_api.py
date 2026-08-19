import json
from pathlib import Path

def main():
    request_path = Path("data/agent_request.json")
    response_path = Path("data/agent_response.json")

    request = json.loads(
        request_path.read_text(encoding="utf-8")
    )

    response = {
        "is_commitment": True,
        "title": "Entregar informe de Ingeniería de Software",
        "category": "academic",
        "responsible": "user",
        "due_date": "2026-08-21",
        "due_time": "23:59",
        "priority": "high",
        "status": "pending",
        "needs_approval": False
    }

    response_path.write_text(
        json.dumps(response, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print("Respuesta mock generada")


if __name__ == "__main__":
    main()