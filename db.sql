-- Create database local

CREATE DATABASE commerce;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO users (name, email, password) VALUES ('example', 'example@example.com', 'example123');

CREATE TABLE products();

CREATE TABLE categories();
