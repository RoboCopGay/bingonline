CREATE TABLE Address(
    _id integer primary key not null,
    cep varchar(9) not null,
    number integer not null,
    street text not null,
    neighborhood text not null,
    city text not null,
    country text not null
);
CREATE TABLE User(
    _id integer primary key not null,
    name text not null,
    password text not null,
    email text not null unique,
    phone text unique,
    address integer not null,
    foreign key(address) references Address(_id)
);
CREATE TABLE Wintype(
    _id integer primary key not null,
    name text not null,
    description text not null,
    board text not null
);
CREATE TABLE Reward(
    _id integer primary key not null,
    name text not null,
    description text not null,
    is_money boolean default true,
    win_condiction integer not null,
    foreign key(win_condiction) references Wintype(_id)
);
CREATE TABLE Image(
    _id integer primary key not null,
    src text not null,
    reward integer not null,
    foreign key(reward) references Reward(_id)
);
CREATE TABLE Event(
    _id integer primary key not null,
    name text not null,
    description text not null,
    is_fisic_ball boolean default false,

    address integer not null,
    reward integer not null,
    owner integer not null,
    foreign key(owner) references Owner(_id),
    foreign key(address) references Address(_id),
    foreign key(reward) references Reward(_id));
CREATE TABLE Card(
    _id integer primary key not null,
    board varchar(255) not null unique,

    event integer not null,
    user integer not null,

    foreign key(user) references User(_id),
    foreign key(event) references Event(_id)
);
