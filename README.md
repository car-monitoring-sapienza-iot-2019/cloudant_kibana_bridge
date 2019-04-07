# IBM-Cloudant --> Elastic Data Mirroring

This script allows you to send every data insertion in a IBM Cloudant database towards an Elastic database with the usage of server-less IBM Cloud Functions.

## Getting Started

### Requirements

- An account on [IBM Cloud](https://cloud.ibm.com/login) with an instance of a [Cloudant](https://www.ibm.com/cloud/cloudant) database.
- An account on [Elastic](https://www.elastic.co/) with an instance of a database.
- The [IBM CLI](https://cloud.ibm.com/docs/cli?topic=cloud-cli-overview#overview) installed on your machine and configured with your IBM Cloud account.
- Any of the [IBM Cloud Functions](https://www.ibm.com/cloud/functions) supported programming languages (in the example Python is used).

### Usage

- To **create** the binding:

Open **setup.sh** and fill with your instances these lines:
  1. `export CLOUDANT_INSTANCE="YOUR_PACKAGE_NAME"`
  2. `export CLOUDANT_DATABASE="YOUR_DB_NAME"`


Open **process-change.py** and fill these lines with your Elasstic credentials:
  1. `ESUSERNAME = "YOUR_ELASTIC_USERNAME"`
  2. `ESPASSWORD = "YOUR_ELASTIC_PWD"`
  3. `INDEX = "YOUR_INDEX_IN_ELASTIC_DB"`
  4. `HOST = "KIBANA_SERVER_URL"`

Finally run **setup.sh** in a **shell** that has access to **IBM CLI**.

To **remove** the binding, run **clean.sh**
