
---- creat_et 
-- select EXTRACT(EPOCH FROM TIMESTAMP '2090-01-01T00:00:00')
-- 3786912000
CREATE OR REPLACE FUNCTION now_ets() RETURNS integer AS $$ 
    select cast(extract(epoch from current_timestamp) as integer) - 3786912000
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION ts2ets(in ts timestamptz) RETURNS integer AS $$ 
    select cast(extract(epoch from ts) as integer) - 3786912000
$$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION ets2ts(in ts integer) RETURNS timestamptz AS $$ 
	select to_timestamp ((ts + 3786912000)::integer)
$$ LANGUAGE SQL;

-- example
select ts2ets(to_timestamp(1654567890))
