def day1_1():
    with open('inputs/day1.txt') as f:
        left = []
        right = []
        distances = []
        for line in f:
            split_line = line.split("   ")
            left.append(int(split_line[0]))
            right.append(int(split_line[1]))

        left.sort()
        right.sort()

        for i in range(len(left)):
            distances.append(abs(left[i] - right[i]))

    return sum(distances)


def day1_2():
    with open('inputs/day1.txt') as f:
        left = []
        right = []
        counts = {}
        similarities = []

        for line in f:
            split_line = line.split("   ")
            left.append(split_line[0])
            right.append(split_line[1])

        left.sort()
        right.sort()

        for i in range(len(left)):
            counts[left[i]] = 0

        for i in range(len(right)):
            if right[i].strip() in counts:
                counts[right[i].strip()] += 1

        for key in left:
            if key in counts:
                score = int(key) * counts[key]
                similarities.append(score)
    return sum(similarities)


if __name__ == '__main__':
    print(day1_1())
    print(day1_2())
