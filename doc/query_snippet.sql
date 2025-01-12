
-- @block
SELECT  ('{"a": 123456789012345678901234567890}'::jsonb -> 'a')::numeric(32);


-- @block  쿼리 확인
select version();

