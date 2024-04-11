
def write(use_cache, sqls, Database, Cache):
    # Implement Write Through strategy

    if use_cache: # Use cache
        i_str = Database.get_idx(DB_TABLE)
        i = int(i_str)
        for sql in sqls:
            sql['id'] = str(i)
            data = json.loads(sql)
            Database,insert(i, sql, DB_TABLE)
            Cache.set(sql['xp'], data)
            Cache.expire(sql['xp'], TTL)
            i += 1
            # idx = Database.get_idx(DB_TABLE)
            # Database.insert(idx, data, DB_TABLE)
            # Cache.setex(str(data['xp']), TTL, sql)
    else: # Do not use cache
        i_str = Database.get_idx(DB_TABLE)
        i = int(i_str)
        for sql in sqls:
            Database.insert(i,sql,DB_TABLE)
            i += 1
            # data = json.loads(sql)
            # idx = Database.get_idx(DB_TABLE)
            # Database.insert(idx, data, DB_TABLE)


def read(use_cache, xps, Database, Cache):
    # Implement Lazy Loading strategy
    result = []

    if use_cache:
        for xp in xps:
            cached_result = Cache.get(xp)
            if cached_result and json.loads(cached_result):
                result.append(json.loads(cached_result))
            else:
                cached_result = Database.query(f"SELECT * FROM mp6 WHERE xp = {xp}")
                if cached_result:
                    if len(cached_result) > 0:
                        result.append(cached_result[0]) # switch from bottom to top
                        dump = json.dumps(cached_result[0])
                        Cache.set(xp, dump)
                        Cache.expire(xp, TTL)
                        

    else:
        for xp in xps:
            cached_result = Database.query(f"SELECT * FROM mp6 WHERE xp = {xp}")
            if cached_result:
                if len(cached_result) > 0:
                    result.append(cached_result[0])
    
    for xp in xps:
        sql = f"SELECT * FROM mp6table WHERE xp={xp}"
        # res =  Database.query(sql)
        # Cache.set(xp,json.dumps(res[0]))
        if use_cache: # Use cache
            res =Cache.get(xp)
            print("valid",res)
            if (res is None or json.loads(res) is None):
                res =  Database.query(sql)
                if res is not None and len(res)>0:
                    print(xp)
                    Cache.set(xp,json.dumps(res[0]))
                    Cache.expire(xp, TTL)
                    result.append(res[0])
            else:
                result.append(json.loads(res))
        else: # Do not use cache
            res =  Database.query(sql)
            if res is not None and len(res)>0:
                result.append(res[0])
        
    return result