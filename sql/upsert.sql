BEGIN;

DELETE FROM public.demo_table t
USING staging_table s
WHERE t.id = s.id;

INSERT INTO public.demo_table
SELECT * FROM staging_table;

END;
