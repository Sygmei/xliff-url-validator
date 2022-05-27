# coding: utf-8
from __future__ import annotations

import asyncio
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import httpx
from fastapi import FastAPI
from pydantic import BaseModel


async def requests_get_async(url):
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, follow_redirects=True)
            resp.raise_for_status()
            return True
        except:
            return False


def extract_urls_from_xliff(content: str) -> list[str]:
    urls = []
    root = ET.fromstring(content)
    url_pattern = re.compile(r"^\/[^\s]")
    for note in root.iter("{urn:oasis:names:tc:xliff:document:1.2}note"):
        if bool(url_pattern.match(note.text)):
            urls.append(note.text)
    return set(urls)


class XLIFFPayload(BaseModel):
    xliff_content: str


class ValidatedURLs(BaseModel):
    urls: dict[str, bool]


app = FastAPI()


@app.post("/", response_model=ValidatedURLs)
async def validate_urls(payload: XLIFFPayload):
    routes = extract_urls_from_xliff(payload.xliff_content)
    urls = [f"https://stripe.com{route}" for route in routes]
    results = await asyncio.gather(*map(requests_get_async, urls))
    url_results = {url: result for url, result in zip(urls, results)}
    return ValidatedURLs(urls=url_results)
