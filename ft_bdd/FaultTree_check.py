from .node import And, Or, Not, BasicEvent


def searchRepeatedEvent(event, cache=None):
    #  RepetedEventのBasicEventの集合を返す
    if cache is None:
        cache = set()
    if type(event) == And or type(event) == Or or type(event) == Not:
        p = set()
        for i in event.child:
            p |= searchRepeatedEvent(i, cache)
        return p
    elif type(event) == BasicEvent:
        if event in cache:
            return {event}
        else:
            cache.add(event)
            return set()
    else:
        print("This is not correct")
        return set()


def searchBasicEventcount(event, cache=None):
    #  BasicEventの名前をkeyとしその数を渡す
    if cache is None:
        cache = {}
    if type(event) == And or type(event) == Or or type(event) == Not:
        for i in event.child:
            cache.update(searchBasicEventcount(i, cache))
        return cache
    elif type(event) == BasicEvent:
        if event.name in cache:
            cache[event.name] += 1
            return cache
        else:
            cache[event.name] = 1
            return cache
    else:
        print("This is not correct")
        return cache


def CheckLoop(event, cache=None):
    #   eventより下の木でループがないかを判定し,ループがなかったらTrueを返す。
    if type(event) == And or type(event) == Or or type(event) == Not:
        if cache is None:
            cache = set()
        dic = {}
        cache.add(event)
        for i in event.child:
            if i in cache:
                return False
            dic[i] = cache.copy()
            if not CheckLoop(i, cache=dic[i]):
                return False
        return True
    elif type(event) == BasicEvent:
        return True
    else:
        print("This is not correct")
        return True


def CheckTerminal(event):
    #  最下層の葉にoperatorがついていないかどうか判定
    #  もし全ての葉がbasicEventだったらTrue
    if type(event) == And or type(event) == Or or type(event) == Not:
        if event.child == set():
            return False
        else:
            for i in event.child:
                if not CheckTerminal(i):
                    return False
        return True
    elif type(event) == BasicEvent:
        return True
    else:
        print("This is not correct")
        return True
