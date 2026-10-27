from dataclasses import dataclass
from typing import Iterable

@dataclass
class Source:
    source_id: str
    title: str
    text: str
    url: str = ""

@dataclass
class Claim:
    text: str
    source_id: str
    confidence: float

def extract_claims(sources: Iterable[Source]) -> list[Claim]:
    claims = []
    for source in sources:
        for sentence in source.text.replace("!", ".").replace("?", ".").split("."):
            sentence = sentence.strip()
            if len(sentence.split()) >= 5:
                claims.append(Claim(sentence + ".", source.source_id, 0.75))
    return claims

def build_brief(topic: str, sources: list[Source]) -> dict:
    claims = extract_claims(sources)
    return {"topic": topic, "claims": [c.__dict__ for c in claims], "source_count": len(sources)}
