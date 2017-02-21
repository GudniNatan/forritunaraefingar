def dfs(graph, start, threadnumber, inthread, indexes):
    visited, stack, visitedOrder = set(), [start], list()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            indexes[vertex][threadnumber] = (len(visited))
            visited.add(vertex)
            visitedOrder.append(vertex)
            stack.append(graph[vertex])
            inthread[vertex].append(threadnumber)
        elif len(stack) == 0:
            visitedOrder.append(vertex)
    return visitedOrder, inthread, indexes

def createThreads(graph, reverse):
    threads = list()
    indexes = [dict() for x in range(len(graph))]
    inthread = [list() for x in range(len(graph))]
    #index = [-1 for x in range(len(graph))]
    for i in range(len(graph)):
        if reverse[i] == -1:
            thread, inthread, indexes = dfs(graph, i, len(threads), inthread, indexes)
            threads.append(thread)
    """print threads
    print inthread
    print indexes"""
    return threads, inthread, indexes
def main():
    gattafjoldi = int(raw_input())
    gattir = list()
    reverse = [-1 for x in range(gattafjoldi)]
    for i in range(gattafjoldi):
        pointer = int(raw_input()) - 1
        gattir.append(pointer)
        reverse[pointer] = i

    queryamount = int(raw_input())
    tengingar = list()
    asd = set()
    threads, inthread, indexes = createThreads(gattir, reverse)
    """for i in range(gattafjoldi):
        tengingar.append(dfs(gattir, i))"""
    #print tengingar
    for i in range(queryamount):
        query = raw_input().split()
        fra = int(query[0]) - 1
        til = int(query[1]) - 1
        #net = tengingar[fra]
        #frathreads = threads[inthread[fra]]
        frathreads = list()
        for x in range(len(inthread[fra])):
            frathreads.append(threads[inthread[fra][x]])
        #tilthreads = threads[inthread[til]]
        tilthreads = list()
        for x in range(len(inthread[til])):
            tilthreads.append(threads[inthread[til][x]])
        for x in range(len(frathreads)):
            if frathreads[x] in tilthreads:
                combined = frathreads[x]
                threadnumber = x
                threadIndex = inthread[fra][threadnumber]
                #print indexes[fra]
                #print threadIndex
                #print indexes[til]
                if indexes[fra][threadIndex] < indexes[til][threadIndex]:
                    print indexes[til][threadIndex] - indexes[fra][threadIndex]
                    break
        else:
            print -1

        #combined = list(set(frathreads).intersection(tilthreads))
main()