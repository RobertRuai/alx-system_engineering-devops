-- Create a MySQL user named replica_user on web-01

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'pass';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
