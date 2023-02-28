from flask import Flask, request, abort
from pathlib import Path
from request_handler import RequestHandler
from request_dataclass import RequestDataclass, RequestSchema


app = Flask(__name__)
DATA_DIR = Path.cwd() / "data"


@app.post("/perform_query")
def perform_query():
    req: RequestDataclass = RequestSchema.load(request.args)

    if None in (req.cmd1, req.value1, req.cmd2, req.value2):
        abort(400, "Incorrect parameters passed")

    if not Path.exists(DATA_DIR / req.file_name):
        abort(400, "File not found")

    try:
        with open(DATA_DIR / req.file_name, "r", encoding="utf-8") as f:
            first_result = getattr(RequestHandler, req.cmd1)(f, req.value1)
            second_result = getattr(RequestHandler, req.cmd2)(first_result, req.value2)
    except (TypeError, ValueError) as e:
        abort(400, e)

    return app.response_class(second_result, content_type="text/plain")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
