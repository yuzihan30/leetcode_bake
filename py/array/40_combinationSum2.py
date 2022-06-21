class Solution:
    """
    40. 组合总和 II
    给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。 
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 思路：递归、回溯加剪枝，和39题的区别是，candidates有重复元素，且组合里单个元素的数目不能多于
        # candidates中对应单个元素的个数，也就是说组合里元素必须是candidates出现过的
        # 1. 初始化及特殊处理
        res = []
        sorted_candidates = sorted(candidates)
        count = len(sorted_candidates)

        # 2. 定义回溯方法, start是为了排除掉重复组合
        def back_track(start: int, path: List[int]):
            sum = 0
            for num in path:
                sum += num
            # 2.1 递归终止条件
            if sum > target:
                return
            if sum == target:
                # res.append(path)
                # 易错点：注意添加的是path的拷贝，而非path，否则res中添加的path最终结果指向同一个path
                res.append(path.copy()) 
                return 
            i = start
            # for i in range(start, count):
            while i < count:
                path.append(sorted_candidates[i])
                back_track(i + 1, path)  # 与39题的区别1，从i + 1开始
                path.pop()
                # i += 1
                # 与39题的区别2，如果当前值与前一个值相同，就跳过，避免重复组合
                while i < count-1 and sorted_candidates[i+1] == sorted_candidates[i]:
                    i += 1
                # 外层while循环的前进条件
                i += 1
                
        
        # 3. 调用回溯方法
        back_track(0, [])
        
        # 4. 返回结果值
        return res        
