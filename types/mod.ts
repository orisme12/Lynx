import { RowDescription } from 'packages/postgres@v0.17.0/query/query.ts'

export type AsyncResult<T> = {
  data: T[]
  count: number | undefined
  description: RowDescription | undefined
}

export type User = {
  id: number
  name: string
  email: string
  password: string
}
