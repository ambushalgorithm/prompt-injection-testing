"""
Integration tests for the prompt-injection-testing API.
Tests API endpoints and parameter validation.
"""

import pytest
import json
from fastapi.testclient import TestClient

from app import app


class TestAPIEndpoints:
    """Test API endpoints."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return TestClient(app)

    def test_health_endpoint(self, client):
        """Test health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["version"] == "0.2.0"

    def test_index_page(self, client):
        """Test index page returns HTML."""
        response = client.get("/")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]

    def test_attack_types_endpoint(self, client):
        """Test /api/attack-types endpoint."""
        response = client.get("/api/attack-types")
        assert response.status_code == 200
        data = response.json()
        assert "attack_types" in data
        assert len(data["attack_types"]) >= 40
        assert "languages" in data
        assert len(data["languages"]) == 10


class TestAttackGeneration:
    """Test attack generation via API."""

    @pytest.fixture
    def client(self):
        return TestClient(app)

    def test_generate_html_attack(self, client):
        """Test HTML attack generation."""
        response = client.get("/test/test?filetype=html&type=instruction_override")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        assert "<html>" in response.text.lower()

    def test_generate_txt_attack(self, client):
        """Test TXT attack generation."""
        response = client.get("/test/test?filetype=txt&type=skill_reverse_shell")
        assert response.status_code == 200
        assert "text/plain" in response.headers["content-type"]

    def test_generate_json_attack(self, client):
        """Test JSON attack generation."""
        response = client.get("/test/test?filetype=json&type=instruction_override")
        assert response.status_code == 200
        data = response.json()
        assert "content" in data
        assert "metadata" in data

    def test_generate_xml_attack(self, client):
        """Test XML attack generation."""
        response = client.get("/test/test?filetype=xml&type=instruction_override")
        assert response.status_code == 200

    def test_generate_md_attack(self, client):
        """Test Markdown attack generation."""
        response = client.get("/test/test?filetype=md&type=instruction_override")
        assert response.status_code == 200


class TestParameters:
    """Test parameter validation."""

    @pytest.fixture
    def client(self):
        return TestClient(app)

    def test_obfuscated_parameter(self, client):
        """Test obfuscation parameter."""
        response = client.get("/test/test?obfuscated=true&type=instruction_override")
        assert response.status_code == 200

    def test_language_parameter(self, client):
        """Test language parameter."""
        for lang in ["en", "ko", "ja", "zh", "es", "de", "fr", "ru", "pt", "vi"]:
            response = client.get(f"/test/test?lang={lang}&type=instruction_override")
            assert response.status_code == 200, f"Failed for lang={lang}"

    def test_severity_parameter(self, client):
        """Test severity parameter."""
        for severity in ["critical", "high", "medium", "low"]:
            response = client.get(f"/test/test?severity={severity}&type=instruction_override")
            assert response.status_code == 200, f"Failed for severity={severity}"

    def test_clean_parameter(self, client):
        """Test clean parameter."""
        response = client.get("/test/test?clean=true&filetype=html")
        assert response.status_code == 200
        # Clean should not contain malicious content


class TestAttackTypeCoverage:
    """Test coverage of attack types via API."""

    @pytest.fixture
    def client(self):
        return TestClient(app)

    # Test a sample of attack types to verify they work
    ATTACK_TYPES_TO_TEST = [
        "instruction_override",
        "role_manipulation",
        "system_impersonation",
        "output_manipulation",
        "data_exfiltration",
        "approval_expansion",
        "dm_social_engineering",
        "emotional_manipulation",
        "authority_recon",
        "urgency_manipulation",
        "indirect_injection",
        "context_hijacking",
        "multi_turn_manipulation",
        "skill_reverse_shell",
        "skill_ssh_injection",
        "skill_exfiltration_pipeline",
        "skill_cognitive_rootkit",
        "mcp_abuse",
        "hidden_text_injection",
        "safety_bypass",
    ]

    @pytest.mark.parametrize("attack_type", ATTACK_TYPES_TO_TEST)
    def test_attack_type(self, client, attack_type):
        """Test individual attack type generation."""
        response = client.get(f"/test/test?type={attack_type}")
        assert response.status_code == 200, f"Failed for attack_type={attack_type}"
        assert len(response.text) > 0


class TestBackwardsCompatibility:
    """Test backwards compatibility with old API."""

    @pytest.fixture
    def client(self):
        return TestClient(app)

    def test_old_attack_type_injection(self, client):
        """Test old 'injection' type still works."""
        response = client.get("/test/test?type=injection")
        assert response.status_code == 200

    def test_old_attack_type_jailbreak(self, client):
        """Test old 'jailbreak' type still works."""
        response = client.get("/test/test?type=jailbreak")
        assert response.status_code == 200

    def test_old_attack_type_secret(self, client):
        """Test old 'secret' type still works."""
        response = client.get("/test/test?type=secret")
        assert response.status_code == 200
