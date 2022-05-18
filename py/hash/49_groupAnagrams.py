'''
Author: yuzihan yuzihanyuzihan@163.com
Date: 2022-05-18 19:41:45
LastEditors: yuzihan yuzihanyuzihan@163.com
LastEditTime: 2022-05-18 19:44:51
FilePath: /leetcode_bake/py/hash/49_group.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    """
    49. 字母异位词分组
    给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
anagrams 英[ˈænəgræmz] 美[ˈænəˌgræmz]n.相同字母异序词
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 思路：根据特征分类的问题一般要用到hash数据结构
        # 1. 初始化及特殊处理
        if not strs:
            return []
        n = len(strs)
        if n == 1 and not strs[0]:
            return [[""]]
        group_dict = {}

        # 2. 遍历处理
        for item in strs:
            # (group_dict[sorted(item)] or group_dict[sorted(item)] = []).append(item)
            # python中字符串需要转为数组后排序, item.split()不行
            # sorted_item = ''.join(sorted(item.split()))
            sorted_item = ''.join(sorted(list(item)))
            # print(sorted_item)
            if sorted_item not in group_dict:
                group_dict[sorted_item] = []
            group_dict[sorted_item].append(item)

        # 3. 返回结果值
        # Python3 字典 values() 方法返回一个视图对象，需要通过list转为列表
        return list(group_dict.values())
        
