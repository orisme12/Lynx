import { User } from 'types/mod.ts'
import { comparePassword, hashPassword } from '../bcrypt.ts'
import { queryToPostgreSQL } from '../utils.ts'

export const create = async (name: string, email: string, password: string) => {
  // logic for resgiter
  if (name && email && password) {
    try {
      const existuser = await findByEmail(email)
      if (existuser === null) {
        const passwordbcrypt = await hashPassword(password)
        await queryToPostgreSQL(
          'INSERT INTO users (name, email, password) VALUES ($1,$2,$3)',
          [name, email, passwordbcrypt],
        )
        return { success: true, message: 'Usuario registrado exitosamente.' }
      } else {
        return { success: false, message: 'El email ya esta en uso.' }
      }
    } catch {
      return {
        success: false,
        message: 'Error al interactuar con la base de datos',
      }
    }
  } else {
    return { success: false, message: 'Al menos uno de los datos está vacíos' }
  }
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
