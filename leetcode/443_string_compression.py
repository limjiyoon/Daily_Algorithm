class Solution:
    def compress(self, chars: list[str]) -> int:
        chars.append("")
        prev = chars[0]
        count = 0
        n_chars = len(chars)

        for _ in range(n_chars):
            cur = chars.pop(0)
            if cur == prev:
                count += 1
            elif count == 1:
                chars.append(prev)
                count = 1
                prev = cur
            else:
                chars.append(prev)
                chars.extend(str(count))
                count = 1
                prev = cur
        return len(chars)
