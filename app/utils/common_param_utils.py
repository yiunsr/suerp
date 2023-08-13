
async def common_paging_param(skip: int = 0, limit: int = 50):
    return {"skip": skip, "limit": limit}

async def common_order_param(sort: str = ""):
    return sort
