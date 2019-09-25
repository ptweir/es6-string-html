single_SQL_with_Sign = """
--sql Highlight
select `last_name`, start_day, COUNT(*) AS num_entries
FROM schema_name.table_name
WHERE start_day >= '2019-01-01'
GROUP BY last_name, start_day
ORDER BY num_entries DESC
LIMIT 10;
-- Not Highlight
select column_name from schema_name.table_name;
"""

multi_SQL_with_Sign = '''
--beginsql Highlight
drop TABLE schema_name.table_name;
insert INTO schema_name.table_name(id, grade) VALUES(1, 100);
select `last_name`, start_day FROM schema_name.table_name;
--endsql
-- Not Highlight
drop TABLE schema_name.table_name;
insert INTO schema_name.table_name(id, grade) VALUES(1, 100);
'''

SQL_without_Sign = """
-- Highlight
DROP TABLE schema_name.table_name;
INSERT INTO schema_name.table_name(id, grade) VALUES(1, 100);
SELECT `last_name`, start_day
FROM (SELECT * from schema_name.table_name) tmp;
-- Not Highlight
drop TABLE schema_name.table_name;
insert INTO schema_name.table_name(id, grade) VALUES(1, 100);
select column_name from schema_name.table_name;
"""

# 
# --beginsql
# DROP TABLE schema_name.table_name;
# INSERT INTO schema_name.table_name(id, grade) VALUES(1, 100);
# SELECT `last_name`, start_day
# FROM schema_name.table_name
# ;
# --endsql
#

sql = 'SELECT * FROM schema_name.table_name;'

HTML = """
<!--html-->
<h1>I am a lighlighted html</h1>
hello
<p>world</p>
<!--!html-->
<!--htmlcomment-->
<h1>I am also a lighlighted html</h1>
<!--!htmlcomment-->
<h1>I amd not a lighlighted html</h1>
"""

# ANCHOR variable test
SQL_with_Variable = """
SELECT 
    `name`, birth 
FROM 
    users
WHERE birth > '{date}'
    AND `name` != '{banned}man'
;
""".format(banned='bat', date='2019-09-26')

