/**
 * This project is kept by:
 * - Carlos bonet
 * - Gerzon Rangel
 * - Sebastian Garcia
 * - Santiago Rico
 * Mit License @copyright 2023
 */

import { Application } from 'packages/oak@v12.6.1/mod.ts'
import { oakCors } from 'packages/cors@v1.2.2/mod.ts'
import { PORT } from 'deps/const.ts'
import router from './router.ts'

const app = new Application()

app.use(oakCors())
app.use(router.routes())
app.use(router.allowedMethods())

console.log(`🚀 Server on port: http://localhost:${PORT}/api`)

await app.listen({ port: PORT })
