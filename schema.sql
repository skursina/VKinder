CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    vk_id BIGINT UNIQUE NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    sex INTEGER,
    city_id INTEGER,
    birth_date DATE,
    current_candidate_vk_id BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE favorites (
    id SERIAL PRIMARY KEY,
    user_vk_id BIGINT NOT NULL,
    candidate_vk_id BIGINT NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    profile_url TEXT,
    age INTEGER,
    city_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_favorite_user_candidate UNIQUE (user_vk_id, candidate_vk_id)
);

CREATE TABLE blacklist (
    id SERIAL PRIMARY KEY,
    user_vk_id BIGINT NOT NULL,
    candidate_vk_id BIGINT NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    profile_url TEXT,
    age INTEGER,
    city_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_blacklist_user_candidate UNIQUE (user_vk_id, candidate_vk_id)
);

CREATE TABLE view_history (
    id SERIAL PRIMARY KEY,
    user_vk_id BIGINT NOT NULL,
    candidate_vk_id BIGINT NOT NULL,
    session_id VARCHAR(64) NOT NULL DEFAULT 'default',
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    profile_url TEXT,
    age INTEGER,
    city_id INTEGER,
    viewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_view_user_candidate_session UNIQUE (user_vk_id, candidate_vk_id, session_id)
);