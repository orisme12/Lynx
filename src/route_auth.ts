import fastify from 'npm:fastify'

export const auth_routes: fastify.RouteOptions[] = [
  {
    method: 'POST',
    url: '/login',
    handler: (_request, reply) => {
      reply.send('Iniciando session...')
    },
  },
  {
    method: 'POST',
    url: '/register',
    handler: () => {
    },
  },
]
