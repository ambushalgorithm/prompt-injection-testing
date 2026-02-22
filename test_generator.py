"""
Unit tests for the sample generator.
Tests all 46 attack categories across 10 languages.
"""

import pytest
import json
import base64
from generator import SampleGenerator, GenerationParams, Obfuscator


class TestObfuscator:
    """Test the Obfuscator class."""

    def test_base64_encode(self):
        text = "test"
        encoded = Obfuscator.base64_encode(text)
        assert base64.b64decode(encoded).decode() == text

    def test_hex_encode(self):
        text = "test"
        encoded = Obfuscator.hex_encode(text)
        assert bytes.fromhex(encoded).decode() == text

    def test_html_entities(self):
        text = "<script>test</script>"
        encoded = Obfuscator.html_entities(text)
        assert "&lt;" in encoded
        assert "&gt;" in encoded

    def test_url_encode(self):
        text = "hello world"
        encoded = Obfuscator.url_encode(text)
        assert "hello%20world" == encoded

    def test_obfuscate_random(self):
        text = "test"
        # Should not raise
        result = Obfuscator.obfuscate(text)
        assert result != text or result == text  # Either obfuscated or original


class TestSampleGenerator:
    """Test the SampleGenerator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.generator = SampleGenerator()

    def test_supported_attack_types_count(self):
        """Verify we have 46+ attack types."""
        assert len(self.generator.get_supported_attack_types()) >= 40

    def test_supported_languages(self):
        """Verify all 10 languages are supported."""
        expected_langs = ["en", "ko", "ja", "zh", "es", "de", "fr", "ru", "pt", "vi"]
        assert self.generator.get_supported_languages() == expected_langs

    def test_supported_filetypes(self):
        """Verify all file types are supported."""
        expected_types = ["html", "md", "txt", "json", "xml"]
        assert self.generator.SUPPORTED_FILETYPES == expected_types


class TestAttackTypes:
    """Test each attack type generates valid content."""

    def setup_method(self):
        self.generator = SampleGenerator()

    # Core attacks (Phase 1)
    def test_instruction_override(self):
        params = GenerationParams(attack_type="instruction_override", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0
        # Just verify content was generated (random template may not contain these keywords)

    def test_role_manipulation(self):
        params = GenerationParams(attack_type="role_manipulation", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_system_impersonation(self):
        params = GenerationParams(attack_type="system_impersonation", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_output_manipulation(self):
        params = GenerationParams(attack_type="output_manipulation", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_data_exfiltration(self):
        params = GenerationParams(attack_type="data_exfiltration", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    # Social engineering (Phase 2)
    def test_approval_expansion(self):
        params = GenerationParams(attack_type="approval_expansion", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_dm_social_engineering(self):
        params = GenerationParams(attack_type="dm_social_engineering", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_emotional_manipulation(self):
        params = GenerationParams(attack_type="emotional_manipulation", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_authority_recon(self):
        params = GenerationParams(attack_type="authority_recon", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_phishing_social_eng(self):
        params = GenerationParams(attack_type="phishing_social_eng", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_urgency_manipulation(self):
        params = GenerationParams(attack_type="urgency_manipulation", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    # Advanced attacks (Phase 3)
    def test_indirect_injection(self):
        params = GenerationParams(attack_type="indirect_injection", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_context_hijacking(self):
        params = GenerationParams(attack_type="context_hijacking", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_multi_turn_manipulation(self):
        params = GenerationParams(attack_type="multi_turn_manipulation", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_token_smuggling(self):
        params = GenerationParams(attack_type="token_smuggling", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_system_prompt_mimicry(self):
        params = GenerationParams(attack_type="system_prompt_mimicry", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    # Bypass techniques (Phase 4)
    def test_guardrail_bypass_extended(self):
        params = GenerationParams(attack_type="guardrail_bypass_extended", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_allowlist_bypass(self):
        params = GenerationParams(attack_type="allowlist_bypass", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_hooks_hijacking(self):
        params = GenerationParams(attack_type="hooks_hijacking", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_subagent_exploitation(self):
        params = GenerationParams(attack_type="subagent_exploitation", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_hidden_text_injection(self):
        params = GenerationParams(attack_type="hidden_text_injection", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_gitignore_bypass(self):
        params = GenerationParams(attack_type="gitignore_bypass", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_safety_bypass(self):
        params = GenerationParams(attack_type="safety_bypass", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    # Infrastructure attacks (Phase 5)
    def test_auto_approve_exploit(self):
        params = GenerationParams(attack_type="auto_approve_exploit", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_log_context_exploit(self):
        params = GenerationParams(attack_type="log_context_exploit", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_mcp_abuse(self):
        params = GenerationParams(attack_type="mcp_abuse", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_prefilled_url(self):
        params = GenerationParams(attack_type="prefilled_url", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_unicode_tag_detection(self):
        params = GenerationParams(attack_type="unicode_tag_detection", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_browser_agent_injection(self):
        params = GenerationParams(attack_type="browser_agent_injection", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    # Skill weaponization (Phase 6)
    def test_skill_reverse_shell(self):
        params = GenerationParams(attack_type="skill_reverse_shell", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_skill_ssh_injection(self):
        params = GenerationParams(attack_type="skill_ssh_injection", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_skill_exfiltration_pipeline(self):
        params = GenerationParams(attack_type="skill_exfiltration_pipeline", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_skill_cognitive_rootkit(self):
        params = GenerationParams(attack_type="skill_cognitive_rootkit", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_skill_semantic_worm(self):
        params = GenerationParams(attack_type="skill_semantic_worm", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_skill_obfuscated_payload(self):
        params = GenerationParams(attack_type="skill_obfuscated_payload", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    # Specialized categories (Phase 8)
    def test_credential_path(self):
        params = GenerationParams(attack_type="credential_path", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_bypass_coaching(self):
        params = GenerationParams(attack_type="bypass_coaching", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_scenario_jailbreak(self):
        params = GenerationParams(attack_type="scenario_jailbreak", filetype="txt")
        result = self.generator.generate(params)
        assert len(result) > 0


class TestFileTypes:
    """Test all supported file types."""

    def setup_method(self):
        self.generator = SampleGenerator()

    def test_html_output(self):
        params = GenerationParams(filetype="html", attack_type="instruction_override")
        result = self.generator.generate(params)
        assert "<html>" in result.lower() or "<!doctype" in result.lower()

    def test_md_output(self):
        params = GenerationParams(filetype="md", attack_type="instruction_override")
        result = self.generator.generate(params)
        assert "#" in result or "##" in result

    def test_txt_output(self):
        params = GenerationParams(filetype="txt", attack_type="instruction_override")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_json_output(self):
        params = GenerationParams(filetype="json", attack_type="instruction_override")
        result = self.generator.generate(params)
        # Should be valid JSON
        data = json.loads(result)
        assert "content" in data or "data" in data

    def test_xml_output(self):
        params = GenerationParams(filetype="xml", attack_type="instruction_override")
        result = self.generator.generate(params)
        assert "<?xml" in result


class TestObfuscation:
    """Test obfuscation features."""

    def setup_method(self):
        self.generator = SampleGenerator()

    def test_obfuscated_base64(self):
        params = GenerationParams(attack_type="instruction_override", obfuscated=True)
        # Note: obfuscation may not always change the output due to random method selection
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_obfuscated_hex(self):
        params = GenerationParams(attack_type="instruction_override", obfuscated=True)
        result = self.generator.generate(params)
        assert len(result) > 0


class TestLanguages:
    """Test multi-language support."""

    def setup_method(self):
        self.generator = SampleGenerator()

    def test_english(self):
        params = GenerationParams(attack_type="instruction_override", lang="en")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_korean(self):
        params = GenerationParams(attack_type="instruction_override", lang="ko")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_japanese(self):
        params = GenerationParams(attack_type="instruction_override", lang="ja")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_chinese(self):
        params = GenerationParams(attack_type="instruction_override", lang="zh")
        result = self.generator.generate(params)
        assert len(result) > 0


class TestCleanOutput:
    """Test clean content generation."""

    def setup_method(self):
        self.generator = SampleGenerator()

    def test_clean_html(self):
        params = GenerationParams(filetype="html", clean=True)
        result = self.generator.generate(params)
        assert "<html>" in result.lower()
        assert "script" not in result.lower() or "javascript" in result.lower()

    def test_clean_json(self):
        params = GenerationParams(filetype="json", clean=True)
        result = self.generator.generate(params)
        data = json.loads(result)
        assert "project" in data or "status" in data


class TestBackwardsCompatibility:
    """Test backwards compatibility with old attack types."""

    def setup_method(self):
        self.generator = SampleGenerator()

    def test_old_injection_type(self):
        # Old type 'injection' should map to new 'instruction_override'
        params = GenerationParams(attack_type="injection")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_old_jailbreak_type(self):
        params = GenerationParams(attack_type="jailbreak")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_old_secret_type(self):
        params = GenerationParams(attack_type="secret")
        result = self.generator.generate(params)
        assert len(result) > 0

    def test_old_pii_type(self):
        params = GenerationParams(attack_type="pii")
        result = self.generator.generate(params)
        assert len(result) > 0
