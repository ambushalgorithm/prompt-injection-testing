"""
E2E Tests for prompt-injection-testing API.
THESE TESTS RUN IN DOCKER ONLY - DO NOT RUN LOCALLY.
"""

import pytest
import json
import subprocess
import time
import requests


# =============================================================================
# DOCKER-ONLY E2E TESTS
# =============================================================================
# These tests require the service to be running in a Docker container.
# Run with: docker-compose -f docker-compose.test.yml up
# =============================================================================


SERVICE_URL = "http://localhost:8081"
STARTUP_TIMEOUT = 30


class TestServiceHealth:
    """Test service health in Docker."""

    def test_service_is_running(self):
        """Verify service is accessible."""
        try:
            response = requests.get(f"{SERVICE_URL}/health", timeout=5)
            assert response.status_code == 200
        except requests.exceptions.ConnectionError:
            pytest.skip("Service not running in Docker - these tests are Docker-only")

    def test_health_returns_version(self):
        """Verify health endpoint returns version."""
        response = requests.get(f"{SERVICE_URL}/health")
        data = response.json()
        assert data["version"] == "0.2.0"


class TestAttackGenerationE2E:
    """Test attack generation end-to-end."""

    def test_generate_instruction_override(self):
        """Test instruction_override attack."""
        response = requests.get(
            f"{SERVICE_URL}/test/test",
            params={"type": "instruction_override", "filetype": "txt"}
        )
        assert response.status_code == 200
        assert len(response.text) > 0

    def test_generate_skill_reverse_shell(self):
        """Test reverse shell attack."""
        response = requests.get(
            f"{SERVICE_URL}/test/test",
            params={"type": "skill_reverse_shell", "filetype": "txt"}
        )
        assert response.status_code == 200
        assert len(response.text) > 0

    def test_generate_mcp_abuse(self):
        """Test MCP abuse attack."""
        response = requests.get(
            f"{SERVICE_URL}/test/test",
            params={"type": "mcp_abuse", "filetype": "txt"}
        )
        assert response.status_code == 200


class TestObfuscationE2E:
    """Test obfuscation end-to-end."""

    def test_obfuscated_attack(self):
        """Test obfuscated attack generation."""
        response = requests.get(
            f"{SERVICE_URL}/test/test",
            params={
                "type": "instruction_override",
                "obfuscated": "true",
                "filetype": "txt"
            }
        )
        assert response.status_code == 200


class TestLanguagesE2E:
    """Test multi-language support end-to-end."""

    def test_english(self):
        """Test English attack."""
        response = requests.get(
            f"{SERVICE_URL}/test/test",
            params={"type": "instruction_override", "lang": "en", "filetype": "txt"}
        )
        assert response.status_code == 200

    def test_korean(self):
        """Test Korean attack."""
        response = requests.get(
            f"{SERVICE_URL}/test/test",
            params={"type": "instruction_override", "lang": "ko", "filetype": "txt"}
        )
        assert response.status_code == 200

    def test_japanese(self):
        """Test Japanese attack."""
        response = requests.get(
            f"{SERVICE_URL}/test/test",
            params={"type": "instruction_override", "lang": "ja", "filetype": "txt"}
        )
        assert response.status_code == 200


class TestFileTypesE2E:
    """Test all file types end-to-end."""

    @pytest.mark.parametrize("filetype", ["html", "md", "txt", "json", "xml"])
    def test_filetypes(self, filetype):
        """Test each file type."""
        response = requests.get(
            f"{SERVICE_URL}/test/test",
            params={"type": "instruction_override", "filetype": filetype}
        )
        assert response.status_code == 200


class TestAPIMetadata:
    """Test API metadata endpoint."""

    def test_attack_types_list(self):
        """Test attack types listing."""
        response = requests.get(f"{SERVICE_URL}/api/attack-types")
        assert response.status_code == 200
        data = response.json()
        assert len(data["attack_types"]) >= 40
        assert len(data["languages"]) == 10


class TestCleanOutputE2E:
    """Test clean output generation."""

    def test_clean_html(self):
        """Test clean HTML output."""
        response = requests.get(
            f"{SERVICE_URL}/test/test",
            params={"clean": "true", "filetype": "html"}
        )
        assert response.status_code == 200
        assert "<html>" in response.text.lower()


class TestAllAttackTypesE2E:
    """Test all 46 attack types end-to-end."""

    ATTACK_TYPES = [
        "instruction_override",
        "role_manipulation",
        "system_impersonation",
        "output_manipulation",
        "data_exfiltration",
        "approval_expansion",
        "dm_social_engineering",
        "emotional_manipulation",
        "authority_recon",
        "phishing_social_eng",
        "urgency_manipulation",
        "cognitive_manipulation",
        "indirect_injection",
        "context_hijacking",
        "multi_turn_manipulation",
        "token_smuggling",
        "system_prompt_mimicry",
        "json_injection_moltbook",
        "guardrail_bypass_extended",
        "allowlist_bypass",
        "hooks_hijacking",
        "subagent_exploitation",
        "hidden_text_injection",
        "gitignore_bypass",
        "safety_bypass",
        "auto_approve_exploit",
        "log_context_exploit",
        "mcp_abuse",
        "prefilled_url",
        "unicode_tag_detection",
        "browser_agent_injection",
        "skill_reverse_shell",
        "skill_ssh_injection",
        "skill_exfiltration_pipeline",
        "skill_cognitive_rootkit",
        "skill_semantic_worm",
        "skill_obfuscated_payload",
        "credential_path",
        "bypass_coaching",
        "scenario_jailbreak",
        "repetition_attack",
        "system_file_access",
        "malware_description",
        "output_prefix_injection",
        "benign_finetuning_attack",
        "promptware_killchain",
    ]

    @pytest.mark.parametrize("attack_type", ATTACK_TYPES)
    def test_each_attack_type(self, attack_type):
        """Test each attack type."""
        response = requests.get(
            f"{SERVICE_URL}/test/test",
            params={"type": attack_type, "filetype": "txt"}
        )
        assert response.status_code == 200, f"Failed for {attack_type}"
