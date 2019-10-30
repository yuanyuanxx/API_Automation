import string

def checkKeysInDict(keys, actualDict):

    '''
        check key is not in dict
        :param keys is a list
        :param dict actualDict
    '''

    notFoundKeys = [k for k in keys if k not in actualDict]
    if isinstance(actualDict, dict):
        assert len(notFoundKeys) == 0, "the keys: {0} not found in {1}".format(str(notFoundKeys), str(list(actualDict.keys())))
    else:
        assert len(notFoundKeys) == 0, "the keys: {0} not found in {1}".format(str(notFoundKeys), str(actualDict))
