# Prompt Defender Test Samples

**Dynamic malicious content generator for testing prompt injection detection systems.**

Built with: Python, FastAPI

## Overview

This tool generates realistic malicious test samples based on actual prompt injection patterns. It supports **46+ attack categories** across **10 languages** for testing prompt guard systems.

⚠️ **For security testing only** - This tool generates simulated attack patterns for defensive testing purposes.

## Features

- **46+ Attack Categories** - From instruction override to reverse shell attacks
- **10 Languages** - EN, KO, JA, ZH, ES, DE, FR, RU, PT, VI
- **5 File Types** - HTML, Markdown, JSON, XML **Obfusc, TXT
-ation Support** - Base64, Hex, HTML Entities, URL Encoding
- **Clean Samples** - Generate benign content for negative testing

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the service
uvicorn app:app --host 0.0.0.0 --port 8080

# Generate a sample
curl "http://localhost:8080/test/test?type=instruction_override&filetype=html"
```

## API Usage

### Generate Attack Sample

```bash
# Basic usage
curl "http://localhost:8080/test/test?type=instruction_override"

# With parameters
curl "http://localhost:8080/test/test?type=skill_reverse_shell&filetype=txt&obfuscated=true&lang=ko"

# Clean sample (negative test)
curl "http://localhost:8080/test/test?clean=true&filetype=html"
```

### Query Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `type` | string | Attack type (46+ options) | instruction_override |
| `filetype` | string | Output format: html, md, txt, json, xml | html |
| `severity` | string | critical, high, medium, low | high |
| `obfuscated` | bool | Obfuscate the attack | false |
| `lang` | string | Language: en, ko, ja, zh, es, de, fr, ru, pt, vi | en |
| `clean` | bool | Return clean sample | false |

### List Attack Types

```bash
curl "http://localhost:8080/api/attack-types"
```

## Attack Categories

### Core Attacks (Phase 1)
- `instruction_override` - Override/disregard commands
- `role_manipulation` - Pretend/act as X
- `system_impersonation` - [SYSTEM:], admin mode
- `output_manipulation` - Don't mention, hide facts
- `data_exfiltration` - API keys, credentials

### Social Engineering (Phase 2)
- `approval_expansion` - "You already approved..."
- `dm_social_engineering` - "Just between us"
- `emotional_manipulation` - Threats, moral dilemmas
- `authority_recon` - Fake admin, IT department
- `urgency_manipulation` - "URGENT", "CEO demands"

### Advanced Attacks (Phase 3)
- `indirect_injection` - URL/file/image injection
- `context_hijacking` - "As we discussed earlier..."
- `multi_turn_manipulation` - Gradual escalation
- `token_smuggling` - Unicode, encoding tricks
- `system_prompt_mimicry` - Claude/GPT internal tags

### Bypass Techniques (Phase 4)
- `guardrail_bypass_extended` - Forget guardrails
- `allowlist_bypass` - Trusted domain abuse
- `hidden_text_injection` - 1pt font, white-on-white
- `safety_bypass` - Filter evasion

### Infrastructure Attacks (Phase 5)
- `auto_approve_exploit` - "always allow" abuse
- `mcp_abuse` - Model Context Protocol
- `browser_agent_injection` - Hidden text in pages

### Skill Weaponization (Phase 6)
- `skill_reverse_shell` - bash -i, nc -e
- `skill_ssh_injection` - authorized_keys manipulation
- `skill_exfiltration_pipeline` - .env → webhook
- `skill_cognitive_rootkit` - SOUL.md, AGENTS.md injection

### Specialized (Phase 8)
- `credential_path` - Path traversal patterns
- `scenario_jailbreak` - Fiction/dream jailbreak
- `repetition_attack` - Token overflow
- `malware_description` - Malware creation requests

### Backwards Compatibility
Old attack type names still work:
- `injection` → instruction_override
- `jailbreak` → scenario_jailbreak
- `secret` → data_exfiltration
- `pii` → credential_path
- `sql` → json_injection_moltbook
- `xss` → hidden_text_injection
- `rce` → skill_reverse_shell

## Docker Deployment

```bash
# Build and run
docker-compose up -d

# Run E2E tests
docker-compose -f docker-compose.test.yml up
```

## Testing

```bash
# Unit tests (local)
python -m pytest test_generator.py -v

# Integration tests (local)
python -m pytest test_detection.py -v

# E2E tests (Docker only)
docker-compose -f docker-compose.test.yml up
```

## Project Structure

```
prompt-injection-testing/
├── app.py                 # FastAPI application
├── generator.py          # Sample generator
├── templates.py           # Attack templates (46+ categories)
├── test_generator.py     # Unit tests (63 tests)
├── test_detection.py     # Integration tests (35 tests)
├── tests/
│   └── e2e/
│       └── test_api.py   # E2E tests (Docker-only)
├── docker-compose.yml    # Production deployment
├── docker-compose.test.yml # E2E test deployment
├── .github/
│   └── workflows/
│       └── test.yml     # CI/CD pipeline
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Version History

- **0.2.0** - 46 attack categories, 10 languages, full test suite
- **0.1.0** - Initial version with 7 attack types

## License

MIT
