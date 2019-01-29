

# 2.1 查询所有期
def check_get_read_period(params=None, status_exp=0):
    uri = "v1/admin/read/period"
    resp_act = apiReqWs.send_soa_request_for_read(uri, "GET", params=params, status_exp=status_exp)

    if status_exp == 0:
        cb.checkKeysInDict(['currentPage', 'currentSize', 'items', 'pageSize', 'totalCount'], resp_act)
        cb.checkResultIsNotNone(resp_act['totalCount'])

        # 返回items个数
        item_count = len(resp_act['items'])it push --set-upstream origin master

        # 未传入参数
        if params is None:
            cb.checkEqual(resp_act['currentPage'], 1)
            cb.checkEqual(resp_act['pageSize'], 20)
            assert item_count <= 20, 'item数量应<=pageSize：20， 实际返回数量：%s' % item_count
        # 传入参数
        else:
            cb.checkEqual(resp_act['currentPage'], params['pageIndex'])
            cb.checkEqual(resp_act['pageSize'], params['pageSize'])
            assert item_count <= params['pageSize'], \
                'item数量应<=pageSize：%s， 实际返回数量：%s' % (params['pageSize'], item_count)

        # 返回值items数量和currentSize一致
        cb.checkEqual(item_count, resp_act['currentSize'])

        # 没有重复的数据
        cb.checkListHasDuplicateItem(resp_act['items'])

        # 比较item
        for item in resp_act['items']:
            cb.checkKeysInDict(['category', 'periodId', 'periodName', 'periodStatus'], item)
            cb.checkResultIsNotNone(item['periodId'])
            cb.checkResultIsNotNone(item['periodName'])
            cb.checkResultIsNotNone(item['periodStatus'])

        return resp_act['items']
