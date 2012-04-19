source cred.sh

echo "password for dropdb"
dropdb -U $USER $DB

echo "password for createdb"
createdb -U $USER $DB

echo "re-creating schema"
python ../manage.py syncdb --settings=settings

# echo "repopulate db"
# psql -U $USER $DB< dumps/dump3.sql


