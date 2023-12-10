/**
 * This project is kept by:
 * - Carlos bonet
 * - Gerzon Rangel
 * - Sebastian Garcia
 * - Santiago Rico
 * Mit License @copyright 2023
 */

import fastify from './fastify.ts'
import { PORT } from 'deps/const.ts'
import { auth_routes } from './route_auth.ts'

import { Client } from 'packages/postgres@v0.17.0/mod.ts'

const postgres = new Client({
  user: 'postgres',
  database: 'lynx',
  hostname: 'localhost',
  port: 5432,
})

await postgres.connect()

console.log('Coneccion succesfuly to postgres 🚀')

await postgres.end()

fastify.get('/', (_request, reply) => {
  reply.send({
    message: 'Hola Api Lynx',
    data: [
      { name: 'title' },
    ],
  })
})

auth_routes.forEach((route_login) => {
  fastify.route(route_login)
})

await fastify.listen({ port: PORT })
fastify.log.info(`Server running... 🚀`)
