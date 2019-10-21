def alienOrder(self, words):
    pre = collections.defaultdict(set)
    suc = collections.defaultdict(set)
    for pair in zip(word, word[1:]):
        for a, b in zip(*pair):
            if a != b:
                suc[a].add(b)
                pre[b].add(a)
    chars = set(''.join(words))
    charToProcess = chars - set(pre)
    order = ''
    while charToProcess:
        ch = charToProcess.pop()
        order += ch
        for b in suc[ch]:
            pre[b].remove(ch)
            if not pre[b]:
                charToProcess.add(b)
    return order if set(order) == chars else []
