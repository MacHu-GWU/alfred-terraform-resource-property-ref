I create an Alfred Workflow that allow me to search Terraform AWS Resource and Data Source Reference from anywhere in seconds.

The idea is to use get list of document and url from AWS Docs Github repo on https://www.terraform.io/docs/providers/aws/index.html, extract the data put it in a json file. And then use the full text search framework I created https://github.com/MacHu-GWU/afwf_fts_anything-project to search it in Alfred.


How to Build terraform full text search data
------------------------------------------------------------------------------

Understand how terraform resource reference document been built.

Go to https://github.com/hashicorp/terraform-provider-aws, https://github.com/hashicorp/terraform-provider-aws/tree/main/website/docs/r is the original aws resource docs, https://github.com/hashicorp/terraform-provider-aws/tree/main/website/docs/d is the original aws data source docs.
