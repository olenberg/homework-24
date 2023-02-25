from flask import Flask, request, abort
from pathlib import Path
from request_handler import RequestHandler


app = Flask(__name__)
DATA_DIR = Path.cwd() / "data"
cmd_to_func = {
    "filter": RequestHandler.filter,
    "sort": RequestHandler.sort,
    "map": RequestHandler.map,
    "limit": RequestHandler.limit,
    "unique": RequestHandler.unique
}

@app.post("/perform_query")
def perform_query():
    file_name = request.args.get("file_name")
    cmd1 = request.args.get("cmd1")
    value1 = request.args.get("value1")
    cmd2 = request.args.get("cmd2")
    value2 = request.args.get("value2")

    if None in (cmd1, value1, cmd2, value2):
        abort(400, "Incorrect parameters passed")

    if not Path.exists(DATA_DIR / file_name):
        abort(400, "File not found")

    try:
        with open(DATA_DIR / file_name, "r", encoding="utf-8") as f:
            first_result = cmd_to_func[cmd1](f, value1)
            second_result = cmd_to_func[cmd2](first_result, value2)
    except (TypeError, ValueError) as e:
        abort(400, e)

    return app.response_class(second_result, content_type="text/plain")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
