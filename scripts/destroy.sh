ENV=${1:-dev}
CURRENT=$(pwd)

# delete
sam delete --config-env $ENV

cd $CURRENT