import logging
import re
from pathlib import Path

from utils.logger import setup_logger


def test_setup_logger_returns_logger():
    logger = setup_logger("test_logger_returns_logger")

    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_logger_returns_logger"


def test_logger_has_console_and_file_handlers():
    logger = setup_logger("test_logger_handlers")

    handler_types = {type(handler) for handler in logger.handlers}

    assert logging.StreamHandler in handler_types
    assert logging.FileHandler in handler_types
    assert len(logger.handlers) == 2


def test_setup_logger_does_not_duplicate_handlers():
    logger = setup_logger("test_duplicate_handlers")
    initial_count = len(logger.handlers)

    logger = setup_logger("test_duplicate_handlers")

    assert len(logger.handlers) == initial_count == 2


def test_logger_writes_to_file():
    log_file = Path("brood.log")

    if log_file.exists():
        log_file.unlink()

    logger = setup_logger("test_file_output")
    message = "This is a file logging test."

    logger.info(message)

    assert log_file.exists()

    contents = log_file.read_text(encoding="utf-8")
    assert message in contents


def test_log_format():
    log_file = Path("brood.log")

    if log_file.exists():
        log_file.unlink()

    logger = setup_logger("cipher_engine")
    logger.info("Decryption successful.")

    contents = log_file.read_text(encoding="utf-8").strip()

    pattern = (
        r"^\[\d{2}:\d{2}:\d{2}\] "
        r"\[INFO\] "
        r"\[[^\]]+\]: "
        r"Decryption successful\.$"
    )

    assert re.match(pattern, contents)