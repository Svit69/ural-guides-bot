from src.route_navigation.next_post_resolver import NextPostResolver


def test_resolves_next_post_after_fourth_post() -> None:
    resolver = NextPostResolver()

    assert resolver.resolve_next_post(4) == 5


def test_resolves_next_post_after_fifth_post() -> None:
    resolver = NextPostResolver()

    assert resolver.resolve_next_post(5) == 6


def test_resolves_next_post_after_sixth_post() -> None:
    resolver = NextPostResolver()

    assert resolver.resolve_next_post(6) == 7


def test_resolves_next_post_after_seventh_post() -> None:
    resolver = NextPostResolver()

    assert resolver.resolve_next_post(7) == 8


def test_resolves_next_post_after_eighth_post() -> None:
    resolver = NextPostResolver()

    assert resolver.resolve_next_post(8) == 9


def test_resolves_next_post_after_ninth_post() -> None:
    resolver = NextPostResolver()

    assert resolver.resolve_next_post(9) == 10


def test_resolves_next_post_after_tenth_post() -> None:
    resolver = NextPostResolver()

    assert resolver.resolve_next_post(10) == 11


def test_resolves_final_post_after_eleventh_post() -> None:
    resolver = NextPostResolver()

    assert resolver.resolve_next_post(11) == 12
