CREATE TABLE items (
    id integer primary key autoincrement not null,
    estimated_time integer not null,
    body text,
    created timestamp default (current_timestamp)
);