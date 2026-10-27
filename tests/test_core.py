from research_assistant.core import Source, build_brief
def test_brief_has_citations():
    result = build_brief("x", [Source("S1", "t", "This sentence contains enough words for extraction.")])
    assert result["claims"][0]["source_id"] == "S1"
