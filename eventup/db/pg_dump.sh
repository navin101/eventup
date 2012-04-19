source cred.sh

pg_dump $DB -U $USER --data-only > dump3.sql 
