
## system 사용자 추가

```
INSERT INTO public."user"
(id, status, testmode, ref_id1, ref_id0, name, email, first_name, last_name, display, nickname, avatar, api_key, api_key_last_at, "password", password_last_at, last_join_dt, created_at, updated_at, data_jb, tags_jb)
VALUES(1, '', '', NULL, NULL, 'system', 'system@system.system', 'system', 'system', '', '', '', 'gVG4KDyiYtAB3ISaw2gg', now(), '', now(), NULL, now(), now(), '{}'::jsonb, '[]'::jsonb);

```