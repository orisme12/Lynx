import { Router } from 'packages/oak@v12.6.1/mod.ts'
import adminInfo from '../admin.json' assert { type: 'json' }
import queryToPostgreSQL from './database.ts'
import { User } from 'types/mod.ts'

const router = new Router()

router.prefix('/api')

router.get('/', async (ctx) => {
  const { data } = await queryToPostgreSQL<User[]>('SELECT * FROM users')

  console.log(data)

  ctx.response.body = {
    name: 'Lynx Api',
    version: adminInfo.version,
    api: adminInfo.api,
    description: adminInfo.description,
    authos: adminInfo.authors,
    data,
  }
})

export default router
