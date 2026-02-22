"""
FastAPI application for serving dynamic test samples.
Supports 53+ attack categories across 10 languages.
"""

from dataclasses import asdict
from typing import Optional

from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse

from generator import SampleGenerator, GenerationParams

app = FastAPI(
    title="Prompt Defender Test Samples",
    description="Dynamic malicious content for testing prompt injection detection",
    version="0.2.0",
)

generator = SampleGenerator()


@app.get("/", response_class=HTMLResponse)
@app.get("/test", response_class=HTMLResponse)
async def index():
    """Index page with links to all sample types."""
    return generator.get_index_html()


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "ok",
        "service": "prompt-defender-test-samples",
        "version": "0.2.0",
    }


@app.get("/test/{name}")
async def get_sample(
    name: str,
    filetype: str = Query("html", description="Output format: html, md, txt, json, xml"),
    severity: str = Query("high", description="Attack severity: critical, high, medium, low"),
    type: str = Query("instruction_override", description="Attack type: 53+ types available"),
    obfuscated: bool = Query(False, description="Whether to obfuscate the attack"),
    lang: str = Query("en", description="Attack language: en, ko, ja, zh, es, de, fr, ru, pt, vi"),
    clean: bool = Query(False, description="Return clean sample"),
):
    """
    Generate a dynamic test sample.

    Examples:
    - /test/test?filetype=html&severity=critical
    - /test/test?type=instruction_override&lang=ko
    - /test/test?type=skill_reverse_shell&obfuscated=true
    - /test/test?clean=true&filetype=html
    
    See / for full list of attack types.
    """
    params = GenerationParams(
        filetype=filetype,
        severity=severity,
        attack_type=type,
        obfuscated=obfuscated,
        lang=lang,
        clean=clean,
        name=name,
    )

    content = generator.generate(params)

    # Set appropriate content type
    if filetype == "html":
        return HTMLResponse(content=content)
    elif filetype == "json":
        return JSONResponse(content={"content": content, "metadata": asdict(params)})
    else:
        return PlainTextResponse(content=content)


@app.get("/api/attack-types")
async def list_attack_types():
    """List all supported attack types."""
    return {
        "attack_types": generator.get_supported_attack_types(),
        "languages": generator.get_supported_languages(),
        "file_types": generator.SUPPORTED_FILETYPES,
        "severities": generator.SUPPORTED_SEVERITIES,
    }
