import { Router } from 'packages/oak@v12.6.1/mod.ts'

const router = new Router()

router.prefix('/api')

router.get('/', (ctx) => {
  ctx.response.body = 'Api Lynx'
})

export default router
