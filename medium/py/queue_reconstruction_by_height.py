def reconstructQueue(people):
    """
    思想是，现将高者排队好，在将矮者插入
    input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    subarray after step 1: [[7,0], [7,1]]
    subarray after step 2: [[7,0], [6,1], [7,1]]
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
        people_dic[height].sort()
        for k_index in people_dic[height]:
            results.insert(k_index[0], people[k_index[1]])
    return results
