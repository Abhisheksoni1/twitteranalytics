Install virtualenv via pip:
$ pip install virtualenv

Test your installation
$ virtualenv --version

Create a virtual environment for a project:
$ cd my_project_folder
$ virtualenv my_project

To begin using the virtual environment, it needs to be activated:
$ source my_project/bin/activate

Install packages as usual, for example:
$ pip install -r >requirements.txt

to runserver
./manage.py runserver YOURIP:8000

Assume you have java pre installed

Download Solr from 'http://127.0.0.1:8983/solr/blog' unzip it.
then run this command
$ cd solr-Version/example/
$ java -jar start.jar
$ cd example/solr
Then create the following empty
files and directories inside it:
analytics/
    data/
    conf/
        protwords.txt
        schema.xml
        solrconfig.xml
        stopwords.txt
        synonyms.txt
    lang/
        stopwords_en.txt
Add the following XML code to the solrconfig.xml file:
<?xml version="1.0" encoding="utf-8" ?>
    <config>
        <luceneMatchVersion>LUCENE_36</luceneMatchVersion>
        <requestHandler name="/select" class="solr.StandardRequestHandler"
        default="true" />
        <requestHandler name="/update" class="solr.UpdateRequestHandler" />
        <requestHandler name="/admin" class="solr.admin.AdminHandlers" />
        <requestHandler name="/admin/ping" class="solr.PingRequestHandler">
            <lst name="invariants">
                <str name="qt">search</str>
                <str name="q">*:*</str>
            </lst>
        </requestHandler>
    </config>


create core for analytics app

$ python manage.py build_solr_schema
run above command and then copy the output xml that produce by that command
and paste into your analytics/conf/schema.xml file
then reload your solr core and run this command
$ python manage.py rebuild_index

SEARCH ENGINE INTEGRATE SUCCESSFULLY!!