import collections

def get_empty_problem_tree():

    problem_tree = {"basicIO" : {"value" : 0, "input" : {"value" : 0}, "output" : {"value" : 0}},
        "condition" : {"value" : 0, "if" : {"value" : 0, "ifOnly" : {"value" : 0}, "withElse" : {"value" : 0}}, "switch" : {"value" : 0}},
        "loop" : {"value" : 0, "single" : {"value" : 0, "for" : {"value" : 0}, "while" : {"value" : 0}},
                               "nested" : {"value" : 0, "forOnly" : {"value" : 0}, "whileOnly" : {"value" : 0}, "mixed" : {"value" : 0}}},
        "array" : {"value" : 0, "nonCharArray": {"value" : 0, "singleDim": {"value" : 0}, "multiDim": {"value" : 0}}, "charArray": {"value" : 0, "singleDim": {"value" : 0}, "multiDim": {"value" : 0}}},
        "function" : {"value" : 0, "recursion": {"value" : 0, "procedure": {"value" : 0}, "function": {"value" : 0}}, "notRecursion": {"value" : 0, "procedure": {"value" : 0}, "function": {"value" : 0}}},
        "class" : {"value" : 0, "inheritance": {"value" : 0, "constructor": {"value" : 0}, "noConstructor": {"value" : 0}}, "noInheritance": {"value" : 0, "constructor": {"value" : 0}, "noConstructor": {"value" : 0}}},
        "module" : {"value" : 0, "string": {"value" : 0, "length": {"value" : 0}, "concat": {"value" : 0}, "substr": {"value" : 0}, "replace": {"value" : 0}, "changeType": {"value" : 0}},
                                 "fileIO": {"value" : 0, "open": {"value" : 0}, "close": {"value" : 0}, "write": {"value" : 0}, "read": {"value" : 0}},
                                 "array": {"value" : 0, "length": {"value" : 0}, "concat": {"value" : 0}, "split": {"value" : 0}, "sort": {"value" : 0}, "pop": {"value" : 0}, "push": {"value" : 0}, "find": {"value" : 0}}},
        "maxIfDepth" : {"value" : 0},
        "maxLoopDepth" : {"value" : 0},
        "totalArraySize" : {"value" : 0},
        "maxArrayDim" : {"value" : 0}
       }


    return problem_tree


def get_empty_version_tree():

	version_tree = {"basicIO" : {"value" : 0, "input" : {"value" : 0}, "output" : {"value" : 0}},
        "condition" : {"value" : 0, "if" : {"value" : 0, "ifOnly" : {"value" : 0}, "withElse" : {"value" : 0}}, "switch" : {"value" : 0}},
        "loop" : {"value" : 0, "single" : {"value" : 0, "for" : {"value" : 0}, "while" : {"value" : 0}},
                               "nested" : {"value" : 0, "forOnly" : {"value" : 0}, "whileOnly" : {"value" : 0}, "mixed" : {"value" : 0}}},
        "array" : {"value" : 0, "nonCharArray": {"value" : 0, "singleDim": {"value" : 0}, "multiDim": {"value" : 0}}, "charArray": {"value" : 0, "singleDim": {"value" : 0}, "multiDim": {"value" : 0}}},
        "function" : {"value" : 0, "recursion": {"value" : 0, "procedure": {"value" : 0}, "function": {"value" : 0}}, "notRecursion": {"value" : 0, "procedure": {"value" : 0}, "function": {"value" : 0}}},
        "class" : {"value" : 0, "inheritance": {"value" : 0, "constructor": {"value" : 0}, "noConstructor": {"value" : 0}}, "noInheritance": {"value" : 0, "constructor": {"value" : 0}, "noConstructor": {"value" : 0}}},
        "module" : {"value" : 0, "string": {"value" : 0, "length": {"value" : 0}, "concat": {"value" : 0}, "substr": {"value" : 0}, "replace": {"value" : 0}, "changeType": {"value" : 0}},
                                 "fileIO": {"value" : 0, "open": {"value" : 0}, "close": {"value" : 0}, "write": {"value" : 0}, "read": {"value" : 0}},
                                 "array": {"value" : 0, "length": {"value" : 0}, "concat": {"value" : 0}, "split": {"value" : 0}, "sort": {"value" : 0}, "pop": {"value" : 0}, "push": {"value" : 0}, "find": {"value" : 0}}},
        "maxIfDepth" : {"value" : 0},
        "maxLoopDepth" : {"value" : 0},
        "totalArraySize" : {"value" : 0},
        "maxArrayDim" : {"value" : 0}
       }


	return version_tree


def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
        	new_key = new_key[:-6]
        	items.append((new_key, v))
    return dict(items)

def get_problem_tree():

    problem_tree = {"basicIO" : {"value" : 200, "input" : {"value" : 100}, "output" : {"value" : 100}},
        "condition" : {"value" : 3, "if" : {"value" : 3, "ifOnly" : {"value" : 3}, "withElse" : {"value" : 0}}, "switch" : {"value" : 0}},
        "loop" : {"value" : 98, "single" : {"value" : 3, "for" : {"value" : 3}, "while" : {"value" : 0}},
                               "nested" : {"value" : 95, "forOnly" : {"value" : 95}, "whileOnly" : {"value" : 0}, "mixed" : {"value" : 0}}},
        "array" : {"value" : 3, "nonCharArray": {"value" : 3, "singleDim": {"value" : 3}, "multiDim": {"value" : 0}}, "charArray": {"value" : 0, "singleDim": {"value" : 0}, "multiDim": {"value" : 0}}},
        "function" : {"value" : 0, "recursion": {"value" : 0, "procedure": {"value" : 0}, "function": {"value" : 0}}, "notRecursion": {"value" : 0, "procedure": {"value" : 0}, "function": {"value" : 0}}},
        "class" : {"value" : 0, "inheritance": {"value" : 0, "constructor": {"value" : 0}, "noConstructor": {"value" : 0}}, "noInheritance": {"value" : 0, "constructor": {"value" : 0}, "noConstructor": {"value" : 0}}},
        "module" : {"value" : 0, "string": {"value" : 0, "length": {"value" : 0}, "concat": {"value" : 0}, "substr": {"value" : 0}, "replace": {"value" : 0}, "changeType": {"value" : 0}},
                                 "fileIO": {"value" : 0, "open": {"value" : 0}, "close": {"value" : 0}, "write": {"value" : 0}, "read": {"value" : 0}},
                                 "array": {"value" : 0, "length": {"value" : 0}, "concat": {"value" : 0}, "split": {"value" : 0}, "sort": {"value" : 0}, "pop": {"value" : 0}, "push": {"value" : 0}, "find": {"value" : 0}}},
        "maxIfDepth" : {"value" : 0},
        "maxLoopDepth" : {"value" : 2},
        "totalArraySize" : {"value" : 0},
        "maxArrayDim" : {"value" : 0}
       }

    return problem_tree

def get_version_tree():

	version_tree = {"basicIO" : {"value" : 2, "input" : {"value" : 1}, "output" : {"value" : 1}},
        "condition" : {"value" : 1, "if" : {"value" : 1, "ifOnly" : {"value" : 1}, "withElse" : {"value" : 0}}, "switch" : {"value" : 0}},
        "loop" : {"value" : 0, "single" : {"value" : 0, "for" : {"value" : 0}, "while" : {"value" : 0}},
                               "nested" : {"value" : 0, "forOnly" : {"value" : 0}, "whileOnly" : {"value" : 0}, "mixed" : {"value" : 0}}},
        "array" : {"value" : 0, "nonCharArray": {"value" : 0, "singleDim": {"value" : 0}, "multiDim": {"value" : 0}}, "charArray": {"value" : 0, "singleDim": {"value" : 0}, "multiDim": {"value" : 0}}},
        "function" : {"value" : 0, "recursion": {"value" : 0, "procedure": {"value" : 0}, "function": {"value" : 0}}, "notRecursion": {"value" : 0, "procedure": {"value" : 0}, "function": {"value" : 0}}},
        "class" : {"value" : 0, "inheritance": {"value" : 0, "constructor": {"value" : 0}, "noConstructor": {"value" : 0}}, "noInheritance": {"value" : 0, "constructor": {"value" : 0}, "noConstructor": {"value" : 0}}},
        "module" : {"value" : 0, "string": {"value" : 0, "length": {"value" : 0}, "concat": {"value" : 0}, "substr": {"value" : 0}, "replace": {"value" : 0}, "changeType": {"value" : 0}},
                                 "fileIO": {"value" : 0, "open": {"value" : 0}, "close": {"value" : 0}, "write": {"value" : 0}, "read": {"value" : 0}},
                                 "array": {"value" : 0, "length": {"value" : 0}, "concat": {"value" : 0}, "split": {"value" : 0}, "sort": {"value" : 0}, "pop": {"value" : 0}, "push": {"value" : 0}, "find": {"value" : 0}}},
        "maxIfDepth" : {"value" : 1},
        "maxLoopDepth" : {"value" : 0},
        "totalArraySize" : {"value" : 0},
        "maxArrayDim" : {"value" : 0}
       }

	return version_tree


