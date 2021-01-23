-- Create custom types
CREATE TYPE Role AS ENUM ('ADMIN', 'USER');

-- Create tables
CREATE TABLE IF NOT EXISTS users (
  id                  BIGSERIAL PRIMARY KEY,
  username            VARCHAR NOT NULL UNIQUE,
  password            VARCHAR NOT NULL,
  name                VARCHAR NOT NULL,
  email               VARCHAR NOT NULL,
  -- team_id             VARCHAR,
  challenge_id        VARCHAR,
  points              INTEGER NOT NULL default 0,
  role                Role NOT NULL
);

CREATE TABLE IF NOT EXISTS teams (
  id                  BIGSERIAL PRIMARY KEY,
  -- team_id             VARCHAR NOT NULL UNIQUE,
  name                VARCHAR NOT NULL UNIQUE,
  points              INTEGER NOT NULL default 0
);

CREATE TABLE IF NOT EXISTS challenges (
  id              BIGSERIAL PRIMARY KEY,
  challenge_id    VARCHAR NOT NULL UNIQUE,
  name            VARCHAR NOT NULL,
  status          VARCHAR NOT NULL,
  leader          VARCHAR NOT NULL,
  start_date      BIGINT      NOT NULL,
  end_date        BIGINT      NOT NULL
);

CREATE TABLE IF NOT EXISTS tasks (
  id              BIGSERIAL  PRIMARY KEY,
  task_id         VARCHAR NOT NULL UNIQUE,
  challenge_id    VARCHAR NOT NULL,
  name            VARCHAR NOT NULL,
  owner           VARCHAR NOT NULL,
  status          VARCHAR NOT NULL,
  points          INTEGER NOT NULL default 0
);