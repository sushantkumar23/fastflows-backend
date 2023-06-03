create table charts (
  id uuid primary key,
  "name" text,
  "type" text not null,
  user_id uuid references auth.users not null,
  is_deleted boolean default false not null,
  created_at timestamp with time zone default timezone('utc' :: text, now()) not null
);