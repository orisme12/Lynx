import { Client, ClientOptions } from 'packages/postgres@v0.17.0/mod.ts'
import 'packages/dotenv@v3.2.2/load.ts'

const postgres: ClientOptions = {
  user: Deno.env.get('DB_USER'),
  database: Deno.env.get('DB_NAME'),
  hostname: Deno.env.get('DB_HOSTNAME'),
  port: Deno.env.get('DB_PORT'),
  password: Deno.env.get('DB_PASSWORD'),
}

const client = new Client(postgres)
const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms))
let attempts = 0

while (attempts < 5) {
  try {
    console.log('🐳 Connecting to postgres...')
    await client.connect()
    console.log('🚀 Connection succesfuly to postgres')
    break
  } catch (error) {
    console.log('❌ Obtuviste un problema a conectarte a postgres')
    console.log('📕 PROBLEMA: ', (error as Error).message)
    console.log('🐳 Intentando nuevamente, conectando...')
    await sleep(5000)
    attempts++
  }
}

export default client
