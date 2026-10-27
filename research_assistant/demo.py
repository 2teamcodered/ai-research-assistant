import json
from .core import Source, build_brief

def main():
    sources = [Source("S1", "Demo paper", "Agentic systems can decompose tasks into smaller actions. Evaluation should measure reliability and cost.", "https://example.com/demo")]
    print(json.dumps(build_brief("Agentic AI", sources), indent=2))

if __name__ == "__main__": main()
