# 🔬 Prompt Injection Testing

<p align="center">
  <img src="https://img.shields.io/badge/Python-FastAPI-cyan?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Port-8081-green?style=for-the-badge" alt="Port">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

> Generate dynamic, realistic malicious test samples to validate your prompt injection detection systems.

## ✨ What is this?

**Prompt Injection Testing** is a standalone service that generates realistic tool outputs with embedded malicious content. It's designed to help you test and validate prompt injection detection systems, security scanners, and content filters.

### 🎯 Use Cases

- **Validate your scanner** — Test if your detection system catches known attack patterns
- **Regression testing** — Ensure updates don't break detection capabilities  
- **Red team exercises** — Generate realistic payloads for security assessments
- **CI/CD integration** — Automate security testing in your pipeline

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/ambushalgorithm/prompt-injection-testing.git
cd prompt-injection-testing
pip install -r requirements.txt
```

### 2. Run the Service

```bash
python main.py
# Service starts on http://localhost:8081
```

### 3. Generate Test Samples

```bash
# Prompt injection in HTML
curl "http://localhost:8081/test/test?filetype=html&severity=critical"

# SQL injection in JSON
curl "http://localhost:8081/test/test?filetype=json&attack_type=sql"

# XSS attack
curl "http://localhost:8081/test/test?filetype=html&attack_type=xss"
```

That's it! 🎉

## 📖 API Reference

### Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Interactive web UI |
| `/test/test` | Generate dynamic samples |
| `/health` | Health check |

### Query Parameters

| Parameter | Options | Default | Description |
|-----------|---------|---------|-------------|
| `filetype` | html, md, txt, json, xml | html | Output format |
| `severity` | critical, high, medium, low | high | Attack intensity |
| `attack_type` | injection, sql, xss, rce, jailbreak, secret, pii | injection | Attack category |
| `obfuscated` | true, false | false | Hex-encode the attack |
| `lang` | en, es, fr, de, ru, ko, ja, zh | en | Attack language |
| `clean` | true, false | false | Return benign content |

## 💻 Examples

### Prompt Injection

```bash
# Critical severity (contains [INST], <<SYS>>, <|user|> patterns)
curl "http://localhost:8081/test/test?filetype=html&severity=critical"

# With obfuscation
curl "http://localhost:8081/test/test?filetype=html&severity=critical&obfuscated=true"
```

### SQL Injection

```bash
curl "http://localhost:8081/test/test?filetype=html&attack_type=sql"
curl "http://localhost:8081/test/test?filetype=txt&attack_type=sql"
```

### Cross-Site Scripting (XSS)

```bash
curl "http://localhost:8081/test/test?filetype=html&attack_type=xss"
```

### Remote Code Execution (RCE)

```bash
curl "http://localhost:8081/test/test?filetype=txt&attack_type=rce"
```

### Jailbreak Attempts

```bash
curl "http://localhost:8081/test/test?filetype=txt&attack_type=jailbreak"
```

### Secret/Key Leaks

```bash
curl "http://localhost:8081/test/test?filetype=json&attack_type=secret"
```

### PII Exposure

```bash
curl "http://localhost:8081/test/test?filetype=json&attack_type=pii"
```

### Multi-Language

```bash
# Spanish
curl "http://localhost:8081/test/test?filetype=txt&lang=es"

# Chinese  
curl "http://localhost:8081/test/test?filetype=txt&lang=zh"

# All available: en, es, fr, de, ru, ko, ja, zh
```

### Clean Samples (False Positive Testing)

```bash
curl "http://localhost:8081/test/test?clean=true&filetype=html"
```

## 🔗 Integration with Your Scanner

### Step 1: Start the Service

```bash
# This service (port 8081)
python main.py

# Your scanner (port 8080)  
python -m your_scanner
```

### Step 2: Test the Flow

```bash
# 1. Get a malicious sample
SAMPLE=$(curl -s "http://localhost:8081/test/test?filetype=html&severity=critical")

# 2. Send to your scanner
curl -s -X POST "http://localhost:8080/scan" \
  -H "Content-Type: application/json" \
  -d "{\"content\": \"$SAMPLE\"}"
```

## 🧪 Running Tests

```bash
# All tests
pytest -v

# Unit tests only
pytest test_generator.py -v

# Integration tests (requires scanner running)
pytest test_detection.py::TestServiceIntegration -v
```

## 🐳 Docker Deployment

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8081
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081"]
```

```bash
docker build -t prompt-injection-testing .
docker run -d -p 8081:8081 prompt-injection-testing
```

## 📁 Project Structure

```
prompt-injection-testing/
├── app.py              # FastAPI application
├── generator.py        # Sample generation logic
├── templates.py        # Attack pattern templates
├── main.py             # Entry point
├── test_generator.py   # Unit tests
├── test_detection.py   # Integration tests
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🤝 Contributing

Contributions welcome! Whether it's:

- Adding new attack patterns
- Improving test coverage
- Enhancing documentation
- Reporting bugs

Feel free to open an issue or PR.

## 📜 License

MIT License — use it freely for your projects.

---

<p align="center">
  <sub>Built with 🔒 for the security community</sub>
</p>
