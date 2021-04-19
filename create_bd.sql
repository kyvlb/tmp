create table cafe
(
    chat_id   bigint            not null
        constraint users_pk
            primary key,
    cafe_name    text,
    address_name text,
    referral     integer,
    id           serial            not null,
    balance      integer default 0 not null
    menu_URL     URL
);

create table review
(
    chat_id   bigint            not null
        constraint users_pk
            primary key,
    all_review  text,
    id          serial            not null,
    menu_URL    URL
);

alter table cafe
    owner to postgres;

create unique index users_id_uindex
    on users (id);