def string_similarity(str1, str2, boost=False):
    '''
    Based on the Levenshtein distance algorithm
    '''
    str1 = str1.lower()
    str2 = str2.lower()
    len1 = len(str1)
    len2 = len(str2)
    # Initializing matrix
    matrix = []
    for row in xrange(len1 + 1):
        matrix.append([])
        for _ in xrange(len2 + 1):
            matrix[row].append(0)
    for i in xrange(0, len1 + 1):
        matrix[i][0] = i
    for i in xrange(0, len2 + 1):
        matrix[0][i] = i
    # Running algorithm
    for row in xrange(1, len1 + 1):
        for col in xrange(1, len2 + 1):
            if str1[row - 1] == str2[col - 1]:
                # No operation
                matrix[row][col] = matrix[row - 1][col - 1]
            else:
                matrix[row][col] = min(
                    # Deletion
                    matrix[row - 1][col] + 1,
                    # Insertion
                    matrix[row][col - 1] + 1,
                    # Substitution
                    matrix[row - 1][col - 1] + 1)
    # Calculate normalized or boosted similarity
    normalized = 1 - matrix[len1][len2] / float(max(len1, len2))
    if boost and (len1 >= 3 or len2 >= 3):
        words1 = set([word for word in str1.split() if len(word) >= 3])
        words2 = set([word for word in str2.split() if len(word) >= 3])
        same_count = len(words1 & words2)
        normalized *= (1 + 0.5 * same_count)
    return normalized
