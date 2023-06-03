create table responses (
  id uuid primary key,
  prompt_id uuid references prompts(id) not null,
  "text" text not null,
  is_deleted boolean default false not null,
  created_at timestamp with time zone default timezone('utc' :: text, now()) not null
);