import { Router } from 'packages/oak@v12.6.1/mod.ts'
import adminInfo from '../admin.json' assert { type: 'json' }
import auth from './api/auth.ts'

const router = new Router()

router.prefix('/api')
router.use(auth.routes(), auth.allowedMethods())

router.get('/', (ctx) => {
  ctx.response.body = {
    name: 'Lynx Api',
    version: adminInfo.version,
    api: adminInfo.api,
    description: adminInfo.description,
    authos: adminInfo.authors,
  }
})

export default router
