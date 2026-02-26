from fastapi import Query

def paginate(page: int = Query(1, ge=1), size: int = Query(10, le=100)):
    return {
        "offset": (page - 1) * size,
        "limit": size
    }