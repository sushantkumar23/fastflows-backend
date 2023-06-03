create table prompts (
  id uuid primary key,
  user_id uuid references auth.users not null,
  chart_id uuid references charts(id) not null,
  sequence_no integer not null,
  llm_model text not null,
  "text" text not null,
  is_deleted boolean default false not null,
  created_at timestamp with time zone default timezone('utc' :: text, now()) not null,
);