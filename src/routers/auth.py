from fastapi import APIRouter

router = APIRouter(tags=['Authentication'])


@router.post('/login')
async def router_login():
    return 'login'


@router.post('/register')
async def router_register():
    return 'register'
