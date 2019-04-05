
# Insert here the package name which you want to connect the action to
# You can view all your packages, actions, triggers typing the command:
# ibmcloud fn list
export CLOUDANT_INSTANCE="YOUR_PACKAGE_NAME"
# Insert here the name of the database to connect to the trigger
export CLOUDANT_DATABASE="YOUR_DB_NAME"

# Create a trigger that's activated each time the database is updated
ibmcloud wsk trigger create data-inserted-trigger \
  --feed ${CLOUDANT_INSTANCE}/changes \
  --param dbname ${CLOUDANT_DATABASE}

# Create the action to be triggered with the specified script
ibmcloud wsk action create process-change process-change.py

# Chain previous cerated action with cloudant "read" built-in action in a sequence
ibmcloud wsk action create process-change-cloudant-sequence \
  --sequence ${CLOUDANT_INSTANCE}/read,process-change

# Map a sequence of actions with the trigger
ibmcloud wsk rule create log-change-rule data-inserted-trigger process-change-cloudant-sequence

# To show logs in terminal
ibmcloud wsk activation poll
