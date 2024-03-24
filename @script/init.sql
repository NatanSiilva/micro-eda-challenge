CREATE TABLE IF NOT EXISTS balances (
    id VARCHAR(255) PRIMARY KEY,
    account_id VARCHAR(255),
    balance INT,
    created_at DATE,
    updated_at DATE
);


DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS clients;

CREATE TABLE IF NOT EXISTS clients (
    id VARCHAR(255),
    name VARCHAR(255),
    email VARCHAR(255),
    created_at DATE
);

CREATE TABLE IF NOT EXISTS accounts (
    id VARCHAR(255),
    client_id VARCHAR(255),
    balance INT,
    created_at DATE
);

CREATE TABLE IF NOT EXISTS transactions (
    id VARCHAR(255),
    account_id_from VARCHAR(255),
    account_id_to VARCHAR(255),
    amount INT,
    created_at DATE
);

INSERT INTO clients (id, name, email, created_at) VALUES ('323ae4f9-4e7b-490a-92e5-d1dcb27cac07', 'John Doe', 'johndoe@example.com', '2023-10-06');
INSERT INTO clients (id, name, email, created_at) VALUES ('f46bb0a4-403a-466e-8ec1-8c2e3502d38c', 'Jane Doe', 'janedoe@example.com', '2023-10-06');

INSERT INTO accounts (id, client_id, balance, created_at) VALUES ('9a9d550f-c475-4bad-a034-cfd3dbdb6813', '323ae4f9-4e7b-490a-92e5-d1dcb27cac07', 27000, '2023-10-06');
INSERT INTO accounts (id, client_id, balance, created_at) VALUES ('092ce768-68e5-448f-8747-b0b149b01131', 'f46bb0a4-403a-466e-8ec1-8c2e3502d38c', 10, '2023-10-06');
