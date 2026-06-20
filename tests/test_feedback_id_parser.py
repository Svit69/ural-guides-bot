from src.admin.feedback_id_parser import FeedbackIdParser


def test_parses_comma_separated_feedback_ids() -> None:
    assert FeedbackIdParser().parse_ids("3, 7,3") == [3, 7]


def test_rejects_invalid_feedback_ids() -> None:
    assert FeedbackIdParser().parse_ids("3, abc") == []
    assert FeedbackIdParser().parse_ids(None) == []
