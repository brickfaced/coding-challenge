def left_join(ht1, ht2):
    for LL in ht2.buckets:
        # import pdb; pdb.set_trace()
        if LL.head:
            if ht1.get(list(LL.head.val.keys())[0]) != 'Key Not Found':
                ht1.set(list(LL.head.val.keys())[0], list(LL.head.val.values())[0])
            else:
                ht1.set(list(LL.head.val.keys())[0], list(LL.head.val.values())[0])
                ht1.set(list(LL.head.val.keys())[0], None)

    for LL in ht1.buckets:
        if LL.head:
            if len(ht1.get(list(LL.head.val.keys())[0])) < 2:
                ht1.set(list(LL.head.val.keys())[0], None)

    return ht1
