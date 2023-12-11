import router from '../router.ts'

router.post('/login', (ctx) => {
  ctx.response.body = 'Log In...'
})

router.post('/register', (ctx) => {
  ctx.response.body = 'Create account'
})
