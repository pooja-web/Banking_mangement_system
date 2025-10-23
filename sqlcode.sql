create database Python_force;
use python_force;

create table bank_accounts(
ID INT auto_increment primary key,
owner_name varchar(25) Not null,
account_number BIGINT unique Not null,
balance float not null default 0);

select * from bank_accounts;
describe bank_accounts;