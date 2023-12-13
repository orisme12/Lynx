import { AsyncResult } from 'types/mod.ts'
import db from './database.ts'

const queryToPostgreSQL = <T>(
  query: string,
  values?: unknown[],
): Promise<AsyncResult<T>> => {
  return new Promise((resolve, reject) => {
    try {
      db.queryObject(query, values)
        .then((res) => {
          const asyncResult: AsyncResult<T> = {
            data: res.rows as T[],
            count: res.rowCount,
            description: res.rowDescription,
          }
          resolve(asyncResult)
        })
        .catch((err) => reject(err))
    } catch (error) {
      reject((error as Error).message)
    }
  })
}

export { queryToPostgreSQL }
