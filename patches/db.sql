-- Create database local

CREATE DATABASE commerce;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    password VARCHAR(50)
    phone VARCHAR(10),
    role VARCHAR(10)
);

INSERT INTO users (name, email, password) VALUES ('example', 'example@example.com', 'example123');

CREATE TABLE products();

CREATE TABLE categories();

SELECT * FROM users WHERE email LIKE 'al EMAIL DEL USUARIO'
