



def solution(F, S, G, U, D):

    visited = []
    loc = []
    que = []



    for i in range(F+1):
        visited.append(0)
        loc.append(-1)

    que.append(S)
    loc[S] = 0
    count = 0

    while que:

        if G==S:

            print(0)
            return



        if loc[G] != -1:
            print(loc[G])
            #print(loc[:F+1])
            return

        #print(loc[:20])
        count+=1
        num = que.pop(0)

        up_loc = num+U
        down_loc = num-D

        if up_loc <= F and loc[up_loc] == -1:
            loc[up_loc] = loc[num] + 1
            que.append(up_loc)

        if down_loc > 0 and loc[down_loc] == -1:
            loc[down_loc] = loc[num] + 1
            que.append(down_loc)

    print('use the stairs')
    return

F, S, G, U, D = map(int, input().split())
solution(F, S, G, U, D)
