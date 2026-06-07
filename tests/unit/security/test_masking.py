from raztint.security.masking import DEFAULT_RULES, MaskRule, redact


class TestRedact:
    def test_github_token(self) -> None:
        token = "ghp_" + "a" * 20
        assert redact(f"key={token}") == "key=ghp_****"

    def test_openai_key(self) -> None:
        key = "sk-" + "A" * 48
        assert redact(key) == "sk-****"

    def test_jwt(self) -> None:
        jwt = "eyJabc.def.ghi"
        assert redact(jwt) == "[JWT:REDACTED]"

    def test_bearer_token(self) -> None:
        assert redact("Bearer secret123") == "Bearer [REDACTED]"

    def test_url_credentials(self) -> None:
        url = "https://user:pass@example.com"
        assert redact(url) == "https://user:****@example.com"

    def test_credit_card(self) -> None:
        assert redact("4111 1111 1111 1111") == "4111-****-****-1111"

    def test_generic_secret(self) -> None:
        assert redact("password=supersecret") == "password=****"

    def test_custom_rules(self) -> None:
        rules = [MaskRule(r"SECRET-\d+", "custom", "SECRET-***")]
        assert redact("SECRET-12345", rules=rules) == "SECRET-***"

    def test_default_rules_count(self) -> None:
        assert len(DEFAULT_RULES) == 8
