# Apriori算法实现：挖掘频繁项集和关联规则
from itertools import combinations
from collections import defaultdict

def get_frequent_itemsets(transactions, min_support):
    """
    生成频繁项集
    :param transactions: 交易数据集，列表形式，每项为集合
    :param min_support: 最小支持度阈值
    :return: 频繁项集及其支持度
    """
    # 初始化
    item_counts = defaultdict(int)
    num_transactions = len(transactions)
    frequent_itemsets = []
    
    # 统计单个项的频率（C1）
    for transaction in transactions:
        for item in transaction:
            item_counts[frozenset([item])] += 1
    
    # 筛选频繁1项集（L1）
    frequent_k = {itemset: count/num_transactions for itemset, count in item_counts.items() 
                  if count/num_transactions >= min_support}
    frequent_itemsets.append(frequent_k)
    
    k = 1
    while frequent_k:
        # 生成候选k+1项集（Ck+1）
        candidate_k = generate_candidates(list(frequent_k.keys()), k)
        item_counts = defaultdict(int)
        
        # 统计候选项集频率
        for transaction in transactions:
            for candidate in candidate_k:
                if candidate.issubset(transaction):
                    item_counts[candidate] += 1
        
        # 筛选频繁k+1项集（Lk+1）
        frequent_k = {itemset: count/num_transactions for itemset, count in item_counts.items() 
                      if count/num_transactions >= min_support}
        if frequent_k:
            frequent_itemsets.append(frequent_k)
        k += 1
    
    return frequent_itemsets

def generate_candidates(prev_frequent, k):
    """
    根据k项频繁项集生成k+1项候选项集
    :param prev_frequent: k项频繁项集
    :param k: 当前项集大小
    :return: k+1项候选项集
    """
    candidates = set()
    for itemset1 in prev_frequent:
        for itemset2 in prev_frequent:
            union = itemset1 | itemset2
            if len(union) == k + 1:
                candidates.add(union)
    return candidates

def generate_association_rules(frequent_itemsets, min_confidence):
    """
    生成关联规则
    :param frequent_itemsets: 频繁项集列表
    :param min_confidence: 最小置信度阈值
    :return: 关联规则及其支持度、置信度
    """
    rules = []
    for k_itemsets in frequent_itemsets[1:]:  # 跳过1项集
        for itemset, support in k_itemsets.items():
            for i in range(1, len(itemset)):
                # 生成所有可能的子集作为前件
                for antecedent in combinations(itemset, i):
                    antecedent = frozenset(antecedent)
                    consequent = itemset - antecedent
                    # 计算置信度
                    confidence = support / frequent_itemsets[len(antecedent)-1][antecedent]
                    if confidence >= min_confidence:
                        rules.append({
                            'rule': (antecedent, consequent),
                            'support': support,
                            'confidence': confidence
                        })
    return rules

def main():
    # 示例数据集：超市交易记录
    transactions = [
        {'面包', '牛奶', '鸡蛋'},
        {'面包', '牛奶'},
        {'牛奶', '鸡蛋'},
        {'面包'},
        {'面包', '牛奶', '鸡蛋', '黄油'}
    ]
    
    min_support = 0.4  # 最小支持度
    min_confidence = 0.6  # 最小置信度
    
    # 获取频繁项集
    frequent_itemsets = get_frequent_itemsets(transactions, min_support)
    
    # 打印频繁项集
    print("频繁项集：")
    for i, itemsets in enumerate(frequent_itemsets):
        if itemsets:
            print(f"{i+1}-项集：")
            for itemset, support in itemsets.items():
                print(f"  {set(itemset)}: 支持度 = {support:.2f}")
    
    # 生成关联规则
    rules = generate_association_rules(frequent_itemsets, min_confidence)
    
    # 打印关联规则
    print("\n关联规则：")
    for rule in rules:
        antecedent, consequent = rule['rule']
        print(f"{set(antecedent)} -> {set(consequent)}: "
              f"支持度 = {rule['support']:.2f}, 置信度 = {rule['confidence']:.2f}")

if __name__ == "__main__":
    main()