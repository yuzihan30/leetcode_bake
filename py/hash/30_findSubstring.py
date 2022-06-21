class Solution:
    """
    30. 串联所有单词的子串
    给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。
    """
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 思路：双指针法，参考视频：https://www.bilibili.com/video/BV1Tg4y1z7jR/?spm_id_from=333.788
        # 1. 初始化及特殊处理
        if not s:
            return []
        n = len(s)
        worldCount = len(words)
        if worldCount == 0:
            return []
        wordLen = len(words[0])
        sets = {}
        res = []
        for word in words:
            sets[word] = sets.setdefault(word, 0) + 1
        
        # 2. 遍历
        # 2.1 外层循环只需要移动一个单词的长度，按字母移动
        for i in range(wordLen):
            # total用于记录需要剩余需要匹配的单词个数
            left, total, matchSets = i, worldCount, {}
            # 2.2 内层循环需要以单词为步长移动， 内外层这种移动方式可以避免重复计算
            # 内层循环配合左右指针法
            for j in range(i, n, wordLen):
                sliceWord = s[j: j+wordLen]
                if sliceWord in sets:
                    matchSets[sliceWord] = matchSets.setdefault(sliceWord, 0) + 1
                    total -= 1
                    # 如果匹配字典matchSets中对应的单词数超出了，左指针开始移动
                    while matchSets[sliceWord] > sets[sliceWord]:
                        removeWord = s[left: left+wordLen]
                        matchSets[removeWord] -= 1
                        total += 1
                        left += wordLen
                    if total == 0:
                        res.append(left)
                else: # 容易遗漏， 而且需要修改起始位置为j + wordLen
                    left, total, matchSets = j + wordLen, worldCount, {}

        # 3. 返回结果值
        return res