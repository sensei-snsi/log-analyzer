import os, tempfile
from log_analyzer import analyze

SAMPLE_APACHE = '203.0.113.5 - - [25/Sep/2025:10:15:32 +0000] "GET /api HTTP/1.1" 500 123\n'
SIMPLE_ERR = '2025-09-25T10:15:32Z ERROR 192.0.2.7 - failed duration_ms=842\n'
SIMPLE_OK = '2025-09-25T10:15:40Z INFO 192.0.2.7 - ok\n'

def write_log(text):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".log")
    tmp.write(text.encode("utf-8"))
    tmp.close()
    return tmp.name

def test_analyze_counts_and_slow_lines():
    path = write_log(SAMPLE_APACHE + SIMPLE_ERR + SIMPLE_OK)
    try:
        report = analyze(path, topn=5)
        assert "Total lines: 3" in report
        assert "By level:" in report and "ERROR=" in report and "INFO=" in report
        assert "HTTP statuses:" in report and "500=" in report
        assert "Slow lines" in report and "842 ms" in report
    finally:
        os.unlink(path)
