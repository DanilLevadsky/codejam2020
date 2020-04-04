def main():
    T = int(input()) # number of tests
    for x in range(1, T + 1):
        
        impossible = False
        activities = int(input())
        array = []
        
        for i in range(activities):
            array.append([int(s) for s in input().split()]) # time of activity
            array[i].append(i) # index of activity
        
        array.sort(key=SortByTheFirstElement)

        # in this array will be indicies of activities, made by Jamie or Cameron
        jamies_activities = []
        camerons_activities = []
        c = j = 0
        for a in range(activities):
            if array[a][0] >= c:
                camerons_activities.append(array[a][2])
                c = array[a][1]
            else:
                if array[a][0] >= j:
                    jamies_activities.append(array[a][2])   
                    j = array[a][1]
                else:
                    impossible = True
                    break

        if impossible:
            print("Case #{}: {}".format(x, "IMPOSSIBLE"))
        else:
            order = [' '] * activities
            for a in jamies_activities:
                order[a] = 'J'
            for a in camerons_activities:
                order[a] = 'C'
            print("Case #{}: {}".format(x, ''.join(order)))  


SortByTheFirstElement = lambda x: x[0]

if __name__ == '__main__':
    main()
