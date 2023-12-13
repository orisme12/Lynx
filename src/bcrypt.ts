import * as bcrypt from 'packages/bcrypt@v0.4.1/mod.ts'

const rounds = 10

export const hashPassword = async (password: string): Promise<string> => {
  const salt = await bcrypt.genSalt(rounds)

  const hashedPassword = await bcrypt.hash(password, salt)

  return hashedPassword
}

export const comparePassword = (
  password: string,
  hashedPassword: string,
): Promise<boolean> => {
  return bcrypt.compare(password, hashedPassword)
}
