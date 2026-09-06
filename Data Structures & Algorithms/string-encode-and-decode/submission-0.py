import json

class Solution:

    def encode(self, strs: List[str]) -> str:
        return f"({json.dumps(strs)})"

    def decode(self, s: str) -> List[str]:
        
        return json.loads(s[1:-1])