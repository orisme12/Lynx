FROM denoland/deno:1.38.5

EXPOSE 1993

WORKDIR /app

USER deno

COPY . .

RUN deno cache src/main.ts

CMD ["run", "-A", "src/main.ts"]