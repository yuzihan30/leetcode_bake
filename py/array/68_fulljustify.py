
class Solution:
    """
    68. 文本左右对齐
给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
文本的最后一行应为左对齐，且单词之间不插入额外的空格。
注意:
单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
    """
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 思路：按行处理，line和count记录每行的字符串和每行的单词字符数，最后一行特殊处理；
        # count+对应行的单词数量的空格数+新词长度 小于 maxWidth， 则将新词填充到该行；
        # 否则重置line和count， 并将该行的前count-1个单词的尾部依次填充空格

        # 1. 初始化及特殊处理
        line, count = [], 0
        res = []
        n = len(words)

        # 2. 遍历处理每个单词
        for i in range(n):
            # 2.1 处理行
            if count + len(line) + len(words[i]) > maxWidth:
                for j in range(maxWidth - count):
                    # 关键点：最后一个单词前的每个单词后面依次添加空格
                    # 易错点：len(line)可能为1, 也就是该行只有一个单词的情况
                    # line[j % (len(line) - 1)] += ' '
                    line[j % max(len(line) - 1, 1)] += ' '
                res.append(''.join(line))
                line, count = [], 0
            # 易漏点
            line.append(words[i])
            count += len(words[i])
        # 3. 处理最后一行，最后一次没有填满的line自动成为最后一行
        # 最后一行左对齐, 最后一个单词前的每个单词后面添加一个空格
        res.append(' '.join(line).ljust(maxWidth))
        
        # 或者
        # last = ' '.join(line)
        # total = len(last)
        # for k in range(maxWidth - total):
        #     last += ' '
        # res.append(last)

        # 4. 返回结果值
        return res
