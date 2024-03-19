-- 16-no_link.sql
SELECT score, IF EXISTS name
from second_table
ORDER By score DESC;