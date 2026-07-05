class Solution:
    delim = "⋅"
    def encode(self, strs: List[str]) -> str:
        return self.delim.join(strs) if strs else "⋅⋅"
    def decode(self, s: str) -> List[str]:
        return s.split(self.delim) if s != "⋅⋅" else []