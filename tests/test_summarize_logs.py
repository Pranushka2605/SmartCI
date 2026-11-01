from scripts.summarize_logs import summarize_logs
from pathlib import Path
from pathlib import Path
from scripts.summarize_logs import summarize_logs


def test_log_summary_generation(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    log_file = tmp_path / "build.log"
    log_file.write_text(
        "2 tests passed, 1 failed",
        encoding="utf-8"
    )

    summarize_logs(str(log_file))

    prompt_file = tmp_path / "llm_prompt.txt"

    assert prompt_file.exists()
    assert "2 tests passed, 1 failed" in prompt_file.read_text(
        encoding="utf-8"
    )


def test_missing_log_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    summarize_logs("missing.log")

    prompt_file = tmp_path / "llm_prompt.txt"

    assert prompt_file.exists()
    assert "No build log available" in prompt_file.read_text(
        encoding="utf-8"
    )