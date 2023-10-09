
async def common_paging_param(page: int=1, limit: int = 50):
    skip = (page - 1) * limit
    return {"skip": skip, "limit": limit}

async def common_order_param(sort: str = ""):
    return sort
