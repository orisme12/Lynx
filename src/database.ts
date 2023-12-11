import { Client, ClientOptions } from 'packages/postgres@v0.17.0/mod.ts'
import { load } from 'https://deno.land/std@0.208.0/dotenv/mod.ts'

const env = await load()

const postgres: ClientOptions = {
  user: env['DB_USER'],
  database: env['DB_NAME'],
  hostname: env['DB_HOSTNAME'],
  port: env['DB_PORT'],
  password: env['DB_PASSWORD'],
}

const client = new Client(postgres)

try {
  console.log('🐳 Connecting to postgres...')
  await client.connect()
  console.log('🚀 Connection succesfuly to postgres')
} catch (error) {
  console.log('❌ Obtuviste un problema a conectarte a postgres')
  console.log('📕 PROBLEMA: ', (error as Error).message)
}
