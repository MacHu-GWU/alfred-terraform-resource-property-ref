I create an Alfred Workflow that allow me to search Terraform AWS Resource and Data Source Reference from anywhere in seconds.

The idea is to use get list of document and url from AWS Docs Github repo on https://www.terraform.io/docs/providers/aws/index.html, extract the data put it in a json file. And then use the full text search framework I created https://github.com/MacHu-GWU/afwf_fts_anything-project to search it in Alfred.
