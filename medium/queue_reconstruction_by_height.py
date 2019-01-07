def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    people_dic = {}
    heights = []
    results = []
    for i in range(len(people)):
        if people[i][0] not in people_dic:
            people_dic[people[i][0]] = [(people[i][1], i)]
            heights.append(people[i][0])
        else:
            people_dic[people[i][0]].append((people[i][1], i))
    heights.sort()
    for height in heights[::-1]:
        print(height)
        print(people_dic[height])
        people_dic[height].sort()
        for k_index in people_dic[height]:
            results.insert(k_index[0], people[k_index[1]])
    return results