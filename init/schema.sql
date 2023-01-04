CREATE DATABASE teste;

CREATE TABLE IF NOT EXISTS `teste`.`purchases` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(255) NOT NULL,
    pvt BOOLEAN NOT NULL,
    incomplete BOOLEAN NOT NULL,
    last_purchase VARCHAR(255) NOT NULL,
    average_purchase_price FLOAT NOT NULL,
    last_purchase_price FLOAT NOT NULL,
    most_frequent_store VARCHAR(255) NOT NULL,
    last_purchase_store VARCHAR(255) NOT NULL
) ENGINE=INNODB;
