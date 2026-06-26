import string
import pytest

from utils.text_cleaner import filterText, clean_input_text


# ---------- filterText ----------

@pytest.mark.parametrize(
    "text, criteria, expected",
    [
        ("", string.punctuation, ""),
        ("abcdef", "", "abcdef"),
        ("!!!!!!", string.punctuation, ""),
        ("abc123", "123", "abc"),
        ("banana", "an", "b"),
        ("AaAa", "A", "aa"),
        ("   hello   ", " ", "hello"),
        ("\tHello\n", "\t\n", "Hello"),
        ("a,b.c!d?", string.punctuation, "abcd"),
    ],
)
def test_filter_text_edge_cases(text, criteria, expected):
    assert filterText(text, criteria) == expected


def test_filter_text_removes_every_occurrence():
    text = "aaaaaaaaaa"
    assert filterText(text, "a") == ""


def test_filter_text_unicode():
    text = "héllo, 世界!"
    expected = "héllo 世界"
    assert filterText(text, string.punctuation) == expected


# ---------- clean_input_text ----------

@pytest.mark.parametrize(
    "raw, expected",
    [
        ("", ""),
        ("HELLO", "hello"),
        ("1234567890", ""),
        ("!!!", ""),
        ("JUMP", "ivmp"),
        ("JuJuJu", "iviviv"),
        ("jJjJ", "iiii"),
        ("uUuU", "vvvv"),
        ("Julius", "ivlivs"),
        ("The quick brown fox jumps over 13 dogs.",
         "the qvick brown fox ivmps over  dogs"),
        ("Room #42!", "room "),
    ],
)
def test_clean_input_text_cases(raw, expected):
    assert clean_input_text(raw) == expected


def test_clean_input_text_removes_all_punctuation():
    text = string.punctuation * 5
    assert clean_input_text(text) == ""


def test_clean_input_text_only_j_and_u():
    text = "juJUjU"
    assert clean_input_text(text) == "iviviv"


def test_clean_input_text_large_input():
    text = ("Ju!123 " * 10000)
    expected = ("iv " * 10000)
    assert clean_input_text(text) == expected


def test_clean_input_text_idempotent():
    """
    Running the function twice should produce the same output.
    """
    text = "JuLiUs!!123"
    once = clean_input_text(text)
    twice = clean_input_text(once)

    assert once == twice


def test_clean_input_text_contains_no_digits():
    result = clean_input_text("abc123xyz456")
    assert not any(c.isdigit() for c in result)


def test_clean_input_text_contains_no_punctuation():
    result = clean_input_text("Hello!!! How, are: you?")
    assert all(c not in string.punctuation for c in result)


def test_clean_input_text_contains_no_j_or_u():
    result = clean_input_text("Jumping Julius under umbrellas")
    assert "j" not in result
    assert "u" not in result


def test_clean_input_text_preserves_spaces():
    text = "Hello,    World!   123"
    assert clean_input_text(text) == "hello    world   "