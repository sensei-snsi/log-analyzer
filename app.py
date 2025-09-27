from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os, tempfile
from log_analyzer import analyze

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/analyze", methods=["POST"])
def analyze_logs():
    if "file" not in request.files:
        return jsonify({"error": "attach log file as form-data 'file'"}), 400

    f = request.files["file"]
    filename = secure_filename(f.filename or "uploaded.log")
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, filename)
        f.save(path)
        top = int(request.args.get("top", 5))
        report = analyze(path, topn=top)
    return jsonify({"report": report})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
