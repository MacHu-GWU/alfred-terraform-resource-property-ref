Terraform Document Quick Search
==============================================================================

.. image:: ./demo.gif

I create an `Alfred Workflow <https://www.alfredapp.com/workflows/>`_ framework called `Full Text Search Anything <https://github.com/MacHu-GWU/afwf_fts_anything-project>`_. You can bring your own json data, define how you gonna index it, then use Alfred Workflow to search it.

You can also download the dataset directly from `Release <https://github.com/MacHu-GWU/alfred-terraform-resource-property-ref/releases>`_


How to Build terraform full text search data
------------------------------------------------------------------------------

**Understand how terraform resource reference document been built**.

Go to https://github.com/hashicorp/terraform-provider-aws, https://github.com/hashicorp/terraform-provider-aws/tree/main/website/docs/r is the original aws resource docs, https://github.com/hashicorp/terraform-provider-aws/tree/main/website/docs/d is the original aws data source docs.

**Build Search Dataset**:

Then we just git clone the document source repo:

.. code-block:: bash

    git clone https://github.com/hashicorp/terraform-provider-aws
    git clone https://github.com/terraform-providers/terraform-provider-azurerm
    git clone https://github.com/hashicorp/terraform-provider-google

And run the python script, alfred full text search dataset is now in ``$HOME/.alfred-fts``

.. code-block:: bash

    python build_data.py
