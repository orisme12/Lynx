import jwt from 'npm:jsonwebtoken'
import { load } from 'deps/lib.ts'

const env = await load()

const jwtSecret = env['JWT_SECRET']

export const generateToken = (userId: string) => {
  return jwt.sign({ userId }, jwtSecret, {
    expiresIn: '1h',
  })
}

export const verifyToken = (token: string) => {
  return jwt.verify(token, jwtSecret)
}
