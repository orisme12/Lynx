import { User } from 'types/mod.ts'
import { comparePassword } from '../bcrypt.ts'
import { queryToPostgreSQL } from '../utils.ts'

export const create = async (name: string, email: string, password: string) => {
}

export const findByEmail = async (email: string) => {
  const { data } = await queryToPostgreSQL<User>(
    `SELECT * FROM users WHERE email = $1`,
    [email],
  )

  return data.at(0) || null
}

export const authenticate = async (email: string, password: string) => {
  const user = await findByEmail(email)

  if (!user) {
    console.log('User not found')
    return false
  }
  const isPasswordValid = await comparePassword(password, user.password)

  return isPasswordValid
}
