
drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  name string not null,
  FOREIGN KEY(type) REFERENCES types(id),
  library string null,
  from_bus string not null,
  to_bus string not null,
  length int not null,
  ampacity real not null
);

drop table if exists types;
create table types (
  id integer primary key autoincrement,
  type string not null,
  icon string not null  
);

