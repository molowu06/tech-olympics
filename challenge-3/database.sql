-- given the following table definitions, write a query to find the percentage of users who returned to log in within 7 days of their first login
create table logins (
    user_id INT NOT NULL,
    login_date DATE NOT NULL,
    PRIMARY KEY (user_id, login_date)
);

with users_first_login as (
    SELECT user_id, min(login_date) as first_logins, count(*) as total_users
    FROM logins
    GROUP BY user_id
), select_users as (
    select distinct l.user_id, l.first_logins, max(login_date) as recent_login, datediff(day, l.first_logins, max(login_date)) as login_dif, f.total_users
    from logins l join users_first_login f on l.user_id = f.user_id
    where login_dif <= 7
)
select count(*) / total_users from select_users
